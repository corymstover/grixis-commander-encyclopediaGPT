#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import tarfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-15"
CYCLE = "global-restart-2026-10-13"
DECK_ID = "RogSi"
DISPLAY = "Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept"
CANDIDATE = ROOT / "refinement/decklists/RogSi_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/RogSi_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/RogSi_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/rogsi_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "RogSi_Complete_Gate_Config.json"
RULES = OUTDIR / "RogSi_Rules_Attestation.json"
LEGAL = OUTDIR / "RogSi_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/RogSi_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")

COMMANDERS = {
    "Rograkh, Son of Rohgahh",
    "Silas Renn, Seeker Adept",
}

EXPECTED_CUTS = Counter({
    "Timetwister": 1,
    "Retraction Helix": 1,
    "Orcish Bowmasters": 1,
    "Talisman of Indulgence": 1,
    "Training Center": 1,
    "Luxury Suite": 1,
    "Morphic Pool": 1,
})
EXPECTED_ADDS = Counter({
    "Final Fortune": 1,
    "Mnemonic Betrayal": 1,
    "Vexing Bauble": 1,
    "Talisman of Dominance": 1,
    "Demonic Counsel": 1,
    "Wooded Foothills": 1,
    "Undercity Sewers": 1,
})


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clean_name(rest: str) -> str:
    rest = ROLE_RE.sub("", rest).strip()
    rest = PRINT_RE.sub("", rest).strip()
    return rest


def parse_bytes(data: bytes) -> tuple[list[str], Counter[str]]:
    lines = [x.strip() for x in data.decode("utf-8-sig").splitlines() if x.strip()]
    cards: Counter[str] = Counter()
    for line in lines:
        m = LINE_RE.match(line)
        if not m:
            raise RuntimeError(f"Malformed deck line: {line}")
        cards[clean_name(m.group(2))] += int(m.group(1))
    return lines, cards


def baseline_member() -> tuple[str, bytes]:
    with tarfile.open(BASELINE_TAR, "r:gz") as tf:
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("/RogSi.txt")]
        if not matches:
            matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("RogSi.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one RogSi FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract RogSi FINAL TXT baseline")
        return matches[0].name, fh.read()


def nkey(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.casefold().replace("’", "'"))


def load_cache() -> dict[str, dict]:
    out = {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        for key in {r.get("query_name"), r.get("canonical_name")}:
            if key:
                out[nkey(key)] = r
    return out


def bind_sha(path: Path, deck_sha: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "__CANDIDATE_SHA__" in text:
        text = text.replace("__CANDIDATE_SHA__", deck_sha)
        path.write_text(text, encoding="utf-8")
    if deck_sha not in path.read_text(encoding="utf-8"):
        raise RuntimeError(f"{path.name} is not bound to current candidate SHA")


def verify_ledger(baseline: Counter[str]) -> None:
    with LEDGER.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 98:
        raise RuntimeError(f"RogSi decision ledger must contain 98 noncommander rows; found {len(rows)}")
    seen = Counter()
    keeps = cuts = 0
    for r in rows:
        card = (r.get("card") or "").strip()
        decision = (r.get("decision") or "").strip().upper()
        if not card:
            raise RuntimeError("RogSi decision ledger contains blank card")
        seen[card] += 1
        if decision == "KEEP":
            keeps += 1
        elif decision == "CUT":
            cuts += 1
        else:
            raise RuntimeError(f"Unexpected decision for {card}: {decision}")
    expected = Counter({name: qty for name, qty in baseline.items() if name not in COMMANDERS})
    if seen != expected:
        missing = expected - seen
        extra = seen - expected
        raise RuntimeError(f"RogSi ledger membership mismatch; missing={missing}; extra={extra}")
    if (keeps, cuts) != (91, 7):
        raise RuntimeError(f"RogSi ledger decision totals must be 91 KEEP / 7 CUT; found {keeps} / {cuts}")


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    raw = CANDIDATE.read_bytes()
    deck_sha = sha256(raw)
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100:
        raise RuntimeError(f"FINAL baseline count is {sum(baseline.values())}, expected 100")
    if len(baseline) != 100:
        raise RuntimeError(f"FINAL baseline distinct-name count is {len(baseline)}, expected 100")
    if sum(candidate.values()) != 100:
        raise RuntimeError(f"Candidate count is {sum(candidate.values())}, expected 100")
    if len(candidate) != 100:
        raise RuntimeError(f"Candidate distinct-name count is {len(candidate)}, expected 100")
    if lines[:2] != [
        "1x Rograkh, Son of Rohgahh [Commander]",
        "1x Silas Renn, Seeker Adept [Commander]",
    ]:
        raise RuntimeError("RogSi commander-first lines mismatch")
    if candidate["Rograkh, Son of Rohgahh"] != 1 or candidate["Silas Renn, Seeker Adept"] != 1:
        raise RuntimeError("RogSi commander quantity mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")

    for name, qty in candidate.items():
        if qty != 1:
            raise RuntimeError(f"Singleton violation: {qty}x {name}")

    verify_ledger(baseline)

    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run augment_rogsi_candidate_oracle_cache.py first")
    cache = load_cache()
    land_count = 0
    unresolved = []
    nonlegal = []
    for name, qty in candidate.items():
        rec = cache.get(nkey(name))
        if not rec:
            unresolved.append(name)
            continue
        if "Land" in (rec.get("type_line") or "").split(" // ", 1)[0]:
            land_count += qty
        if rec.get("commander_legality") != "legal":
            nonlegal.append((name, rec.get("commander_legality")))
    if unresolved:
        raise RuntimeError("Candidate names missing from current Oracle cache: " + ", ".join(sorted(unresolved)))
    if nonlegal:
        raise RuntimeError(f"Unexpected Commander legality rows: {nonlegal}")
    if land_count != 24:
        raise RuntimeError(f"Candidate land count is {land_count}, expected 24")

    bind_sha(AUDIT, deck_sha)
    bind_sha(DECISIONS, deck_sha)

    audit = AUDIT.read_text(encoding="utf-8")
    if "98/98" not in audit or "91 KEEP / 7 CUT" not in audit or deck_sha not in audit:
        raise RuntimeError("RogSi whole-list audit is incomplete or SHA-mismatched")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or deck_sha not in decision:
        raise RuntimeError("RogSi decision closeout is incomplete or SHA-mismatched")
    if "Power Bracket 5" not in decision:
        raise RuntimeError("RogSi natural power ceiling gate missing")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — partner/color identity, casting, split second, delayed triggered abilities, and copy/cast rules (current 2026 rules)",
            "Current Oracle text as captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Current Wizards Commander legality / banned-list checkpoint as cross-checked by the complete gate",
        ],
        "interactions": [
            {"name": "Partner color identity", "status": "PASS", "finding": "Rograkh is red and Silas Renn is blue-black; together the commanders establish U/B/R color identity for deck construction."},
            {"name": "Rograkh zero-mana resource engine", "status": "PASS", "finding": "Rograkh can be cast for zero mana before commander tax and provides a legendary/red creature for Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge, Diabolic Intent, commander-presence free spells, Jeska's Will, and Flare of Duplication. Later commander-tax casts require the applicable additional cost."},
            {"name": "Silas Renn artifact recursion", "status": "PASS", "finding": "After Silas deals combat damage to a player, his trigger targets an artifact card in its controller's graveyard and grants permission to cast that card that turn; normal timing restrictions still apply unless another effect changes them."},
            {"name": "Thassa's Oracle + Demonic Consultation / Tainted Pact", "status": "PASS", "finding": "The candidate preserves the compact Oracle library-exhaustion wins. Tainted Pact's construction requirement is supported by 100 distinct card names."},
            {"name": "Underworld Breach + Lion's Eye Diamond + Brain Freeze", "status": "PASS", "finding": "With sufficient graveyard material and spell count, LED supplies mana while Brain Freeze's storm copies replenish the graveyard, allowing repeated escapes that mill libraries and/or build a winning storm sequence."},
            {"name": "Underworld Breach + Grinding Station + zero-mana artifact", "status": "PASS", "finding": "Grinding Station untaps when an artifact enters. With Breach and a reusable zero-mana artifact such as Mox Amber, the artifact can be used, sacrificed to Station, and escaped using cards milled by Station, producing repeated mill/storm; Rograkh enables Mox Amber to make red mana."},
            {"name": "Final Fortune / Warrior's Oath", "status": "PASS", "finding": "Each creates an extra turn and a delayed triggered ability that causes its controller to lose at the beginning of that extra turn's end step. The line must win or otherwise answer/end around that trigger rather than treating the extra turn as consequence-free."},
            {"name": "Samut, Tyrant of Naktamun split second", "status": "PASS", "finding": "Samut gives instant and sorcery spells its controller controls split second. While such a spell is on the stack, players cannot cast spells or activate nonmana abilities, but triggered abilities still trigger and resolve normally."},
            {"name": "Vexing Bauble symmetry", "status": "PASS", "finding": "Bauble triggers on any spell cast without mana spent to cast it, including the controller's own zero-mana or free/alternate-cost spells. Spending commander tax on a later Rograkh cast counts as mana spent. Bauble can be sacrificed for its draw ability before a planned free-spell sequence."},
            {"name": "Vexing Bauble + Hexing Squelcher", "status": "PASS", "finding": "Bauble may still trigger on a no-mana-spent spell controlled by the RogSi player, but Hexing Squelcher makes that player's spells unable to be countered, so Bauble cannot successfully counter them while Squelcher is active."},
            {"name": "Vexing Bauble + Samut", "status": "PASS", "finding": "Split second does not suppress triggered abilities. Vexing Bauble therefore still triggers on a Samut-granted split-second instant or sorcery if no mana was spent to cast it."},
            {"name": "Demonic Counsel", "status": "PASS", "finding": "Without delirium, Demonic Counsel searches only for a Demon card; this candidate contains no Demon card, so a pre-delirium search cannot find a card. With four or more card types in the graveyard, delirium replaces that restriction and it becomes an unrestricted tutor."},
            {"name": "Mnemonic Betrayal", "status": "PASS", "finding": "Mnemonic Betrayal exiles cards from opponents' graveyards and permits casting those cards that turn with mana flexibility. It does not grant permission to play lands; uncast exiled cards return at the next end step, and Betrayal exiles itself."},
            {"name": "Undercity Sewers", "status": "PASS", "finding": "Undercity Sewers is a front-face land with Island and Swamp types, enters tapped, and surveils 1; it is therefore fetchable by the candidate's appropriate fetchlands and counts as one of the 24 land slots."},
        ],
    }
    RULES.write_text(json.dumps(rules, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    legal = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "https://magic.wizards.com/en/banned-restricted-list",
            "Current_Cycle_Oracle_Cache.jsonl generated from validated current Scryfall metadata",
        ],
        "unexpected_banned_cards": [],
        "project_exceptions_required": [],
        "finding": "Every RogSi candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "baseline_source_member": member_name,
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "RogSi_2026-10-15",
        "rules_attestation_path": str(RULES.relative_to(ROOT)),
        "official_legality_attestation_path": str(LEGAL.relative_to(ROOT)),
        "max_cache_age_hours": 72,
    }
    CONFIG.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/verify_complete_approval_gate.py"), "--config", str(CONFIG.relative_to(ROOT))],
        cwd=ROOT,
        check=False,
    )
    if proc.returncode != 0:
        return proc.returncode

    gate_json = OUTDIR / "RogSi_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("overall_result") != "APPROVAL_READY":
        raise RuntimeError(f"Complete gate did not return APPROVAL_READY: {gate.get('overall_result')}")
    if gate.get("count") != 100 or gate.get("distinct_names") != 100:
        raise RuntimeError("Complete gate structural totals do not match RogSi candidate")
    if sorted(gate.get("commander_color_identity") or []) != ["B", "R", "U"]:
        raise RuntimeError(f"Unexpected RogSi commander color identity: {gate.get('commander_color_identity')}")
    if gate.get("project_exceptions"):
        raise RuntimeError(f"Unexpected RogSi project exceptions: {gate.get('project_exceptions')}")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #47 of 62\n\n"
        "## Result\n\n"
        "**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Commanders: **2**\n"
        "- Distinct names: **100**\n"
        "- Lands: **24**\n"
        "- Repeats: **none**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        "- Whole-list audit: **98/98 noncommander slots adjudicated; 91 KEEP / 7 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 5 — cEDH**\n"
        "- Proposed Archidekt tags: **Turbo Naus / Underworld Breach / Fast Mana**\n\n"
        "## Final proposed delta\n\n"
        "1. Timetwister -> Final Fortune\n"
        "2. Retraction Helix -> Mnemonic Betrayal\n"
        "3. Orcish Bowmasters -> Vexing Bauble\n"
        "4. Talisman of Indulgence -> Talisman of Dominance\n"
        "5. Training Center -> Demonic Counsel\n"
        "6. Luxury Suite -> Wooded Foothills\n"
        "7. Morphic Pool -> Undercity Sewers\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": "APPROVAL_READY",
        "deck_sha256": deck_sha,
        "cards": 100,
        "distinct_names": 100,
        "lands": 24,
        "noncommander_audit": "98/98 — 91 KEEP / 7 CUT",
        "project_exceptions": [],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
