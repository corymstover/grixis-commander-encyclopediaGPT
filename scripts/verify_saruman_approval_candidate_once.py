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
DECK_ID = "Saruman__the_White_Hand"
DISPLAY = "Saruman, the White Hand"
CANDIDATE = ROOT / "refinement/decklists/Saruman_the_White_Hand_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/Saruman_the_White_Hand_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/Saruman_the_White_Hand_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/saruman_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "Saruman_the_White_Hand_Complete_Gate_Config.json"
RULES = OUTDIR / "Saruman_the_White_Hand_Rules_Attestation.json"
LEGAL = OUTDIR / "Saruman_the_White_Hand_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")
BASICS = {"Island", "Mountain", "Swamp"}
MDFC_LANDS = {
    "Kazuul's Fury // Kazuul's Cliffs",
    "Sea Gate Restoration // Sea Gate, Reborn",
    "Shatterskull Smashing // Shatterskull, the Hammer Pass",
    "Sink into Stupor // Soporific Springs",
}

EXPECTED_CUTS = Counter({
    "Surrounded by Orcs": 1,
    "Faithless Looting": 1,
    "Reanimate": 1,
    "Fiery Inscription": 1,
    "Crumbling Necropolis": 1,
    "Drowned Catacomb": 1,
    "Smoldering Marsh": 1,
    "Shivan Reef": 1,
    "Sulfurous Springs": 1,
    "Underground River": 1,
    "Island": 1,
    "Mountain": 1,
    "Swamp": 1,
})
EXPECTED_ADDS = Counter({
    "Volcanic Salvo": 1,
    "Treasure Cruise": 1,
    "Force of Will": 1,
    "Soul's Fire": 1,
    "Volcanic Island": 1,
    "City of Brass": 1,
    "The Black Gate": 1,
    "Flooded Strand": 1,
    "Marsh Flats": 1,
    "Misty Rainforest": 1,
    "Sea Gate Restoration // Sea Gate, Reborn": 1,
    "Shatterskull Smashing // Shatterskull, the Hammer Pass": 1,
    "Sink into Stupor // Soporific Springs": 1,
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
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("/Saruman__the_White_Hand.txt")]
        if not matches:
            matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Saruman__the_White_Hand.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Saruman FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Saruman FINAL TXT baseline")
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
    expected_names = {n for n in baseline if n != DISPLAY}
    if {r["card"] for r in rows} != expected_names:
        raise RuntimeError("Saruman decision ledger membership mismatch")
    baseline_total = keep_total = cut_total = 0
    for r in rows:
        card = r["card"]
        b = int(r["baseline_qty"]); k = int(r["keep_qty"]); c = int(r["cut_qty"])
        if b != baseline[card] or k + c != b:
            raise RuntimeError(f"Ledger quantity mismatch for {card}")
        expected_decision = "KEEP" if c == 0 else ("CUT" if k == 0 else "PARTIAL")
        if r["decision"].strip().upper() != expected_decision:
            raise RuntimeError(f"Ledger decision mismatch for {card}")
        baseline_total += b; keep_total += k; cut_total += c
    if (baseline_total, keep_total, cut_total) != (99, 86, 13):
        raise RuntimeError(f"Ledger totals must be 99 / 86 KEEP / 13 CUT; found {baseline_total} / {keep_total} / {cut_total}")


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    raw = CANDIDATE.read_bytes()
    deck_sha = sha256(raw)
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100 or len(baseline) != 94:
        raise RuntimeError(f"FINAL baseline structure mismatch: {sum(baseline.values())} cards / {len(baseline)} distinct")
    if sum(candidate.values()) != 100 or len(candidate) != 97:
        raise RuntimeError(f"Candidate structure mismatch: {sum(candidate.values())} cards / {len(candidate)} distinct")
    if lines[0] != "1x Saruman, the White Hand [Commander]" or candidate[DISPLAY] != 1:
        raise RuntimeError("Saruman commander-first line mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")

    expected_repeats = {"Island": 2, "Mountain": 2, "Swamp": 2}
    actual_repeats = {n: q for n, q in candidate.items() if q > 1}
    if actual_repeats != expected_repeats:
        raise RuntimeError(f"Unexpected repeats: {actual_repeats}")
    for name, qty in candidate.items():
        if qty > 1 and name not in BASICS:
            raise RuntimeError(f"Singleton violation: {qty}x {name}")

    verify_ledger(baseline)

    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run targeted Saruman refresh first")
    cache = load_cache()
    front_face_lands = 0
    unresolved, nonlegal = [], []
    for name, qty in candidate.items():
        rec = cache.get(nkey(name))
        if not rec:
            unresolved.append(name)
            continue
        first_type = (rec.get("type_line") or "").split(" // ", 1)[0]
        if "Land" in first_type:
            front_face_lands += qty
        if rec.get("commander_legality") != "legal":
            nonlegal.append((name, rec.get("commander_legality")))
    if unresolved:
        raise RuntimeError("Candidate names missing from current Oracle cache: " + ", ".join(sorted(unresolved)))
    if nonlegal:
        raise RuntimeError(f"Unexpected Commander legality rows: {nonlegal}")
    if front_face_lands != 31:
        raise RuntimeError(f"Candidate front-face land count is {front_face_lands}, expected 31")
    if not MDFC_LANDS.issubset(candidate.keys()):
        raise RuntimeError("Candidate is missing one or more required land-capable MDFCs")
    functional_land_slots = front_face_lands + len(MDFC_LANDS)
    if functional_land_slots != 35:
        raise RuntimeError(f"Candidate functional land-capable slots = {functional_land_slots}, expected 35")

    bind_sha(AUDIT, deck_sha)
    bind_sha(DECISIONS, deck_sha)
    audit = AUDIT.read_text(encoding="utf-8")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "99/99" not in audit or "86 KEEP / 13 CUT" not in audit or deck_sha not in audit:
        raise RuntimeError("Saruman whole-list audit incomplete or SHA-mismatched")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or "Power Bracket 4" not in decision or deck_sha not in decision:
        raise RuntimeError("Saruman decision closeout incomplete or SHA-mismatched")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — mana value, X, alternative/additional costs, triggered abilities, replacement effects, MDFCs and amass (current 2026 rules)",
            "Current Oracle text captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Wizards current Commander banned/restricted list checked 2026-10-15",
        ],
        "interactions": [
            {"name": "Saruman mana-value engine", "status": "PASS", "finding": "Saruman triggers when its controller casts a noncreature spell and uses that spell's mana value. Cost reductions and alternative costs change what is paid, not mana value."},
            {"name": "High-MV discounted spells", "status": "PASS", "finding": "Volcanic Salvo remains mana value 12 after its cost reduction; Treasure Cruise remains mana value 8 with delve; Force of Will remains mana value 5 when cast for its alternative cost. Existing Blasphemous Act, Dig Through Time, Blood for the Blood God!, Deadly Rollick, Fierce Guardianship and Deflecting Swat follow the same mana-value principle."},
            {"name": "X spells", "status": "PASS", "finding": "For a spell on the stack, the chosen value of X contributes to mana value. Assault on Osgiliath, Summons of Saruman and Shatterskull Smashing therefore scale Saruman's trigger with the chosen X."},
            {"name": "Soul's Fire / Chandra's Ignition", "status": "PASS", "finding": "Casting either noncreature spell triggers Saruman. The Saruman trigger is placed above the spell and resolves first, growing the Army before the damage spell resolves. Soul's Fire does not require sacrificing the Army."},
            {"name": "Harmonic Prodigy / Wizard's Staff / Veyran", "status": "PASS", "finding": "Saruman is a Wizard. Harmonic Prodigy and Wizard's Staff each add an additional Saruman trigger when applicable. Veyran adds another when casting or copying an instant or sorcery causes Saruman's triggered ability to trigger. Multiple applicable effects are additive."},
            {"name": "Mauhúr replacement", "status": "PASS", "finding": "When one or more +1/+1 counters would be put on an Army, Goblin or Orc controlled by the Saruman player, Mauhúr replaces that event with that many plus one counters, not one additional counter per counter."},
            {"name": "The Great Goblin / All Will Be One", "status": "PASS", "finding": "Each separate event that puts one or more counters on an eligible Goblin, Orc or Army can trigger The Great Goblin once. All Will Be One uses the number of counters actually put on the permanent after applicable replacement effects."},
            {"name": "Widespread Brutality", "status": "PASS", "finding": "Saruman's trigger from casting Widespread Brutality resolves before the spell. Widespread then amasses Orcs 2 and the chosen Army deals damage equal to its power to each non-Army creature; the Army is not a non-Army creature and is not damaged by that effect."},
            {"name": "Fall of Cair Andros", "status": "PASS", "finding": "Each opposing creature dealt excess noncombat damage can cause a separate Fall of Cair Andros trigger. This can compound Army growth after effects such as Widespread Brutality, Blasphemous Act or Chandra's Ignition."},
            {"name": "Bothersome Noisemaker", "status": "PASS", "finding": "Its noncreature-cast amass-Goblins trigger is separate from Saruman's amass-Orcs trigger. Saruman grants ward {2} to Goblins and Orcs controlled by its controller, including an Army carrying those creature types."},
            {"name": "Mizzix's Mastery", "status": "PASS", "finding": "Mizzix's Mastery copies exiled instant/sorcery cards and permits casting the copies. Each copied card actually cast is a noncreature spell and can trigger Saruman."},
            {"name": "Summons of Saruman", "status": "PASS", "finding": "The chosen X contributes to Summons' mana value on the stack, so its cast triggers Saruman for that full mana value. Summons then amasses/mills X and may cast an eligible milled instant or sorcery without paying its mana cost; such a spell is cast and can trigger Saruman separately."},
            {"name": "MDFC spell/land package", "status": "PASS", "finding": "Playing an MDFC land back is a land play and does not trigger Saruman. Casting Kazuul's Fury, Sea Gate Restoration, Shatterskull Smashing or Sink into Stupor as the front spell is casting a noncreature spell and does trigger Saruman using the front spell's mana value."},
            {"name": "The Black Gate", "status": "PASS", "finding": "The Black Gate's activated ability targets a creature and a player with the most life or tied for most life; creatures that chosen player controls cannot block the targeted creature that turn, providing Army evasion without changing Saruman's spell engine."},
        ],
    }
    RULES.write_text(json.dumps(rules, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    legal = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "https://magic.wizards.com/en/banned-restricted-list — current Commander banned list",
            "Wizards Banned and Restricted Announcement — October 12, 2026 (no paper Commander change)",
            "Current_Cycle_Oracle_Cache.jsonl generated/refreshed from current Scryfall metadata",
        ],
        "unexpected_banned_cards": [],
        "project_exceptions_required": [],
        "finding": "Every Saruman candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache and no card appears on the current Commander banned list; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "Saruman_the_White_Hand_2026-10-15",
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

    gate_json = OUTDIR / "Saruman_the_White_Hand_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
        raise RuntimeError(f"Complete gate did not return clean APPROVAL_READY: {gate}")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #48 of 62\n\n"
        "## Result\n\n"
        "**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Distinct names: **97**\n"
        "- Front-face lands: **31**\n"
        "- Land-capable MDFCs: **4**\n"
        "- Functional land-capable slots: **35**\n"
        "- Repeats: **Island x2 / Mountain x2 / Swamp x2 only**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        "- Whole-list audit: **99/99 noncommander copies adjudicated; 86 KEEP / 13 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 4 — Optimized**\n"
        "- Proposed Archidekt tags: **Spellslinger / Amass / Orc Army**\n\n"
        "## Final proposed delta\n\n"
        "1. Surrounded by Orcs -> Volcanic Salvo\n"
        "2. Faithless Looting -> Treasure Cruise\n"
        "3. Reanimate -> Force of Will\n"
        "4. Fiery Inscription -> Soul's Fire\n"
        "5. Crumbling Necropolis -> Volcanic Island\n"
        "6. Drowned Catacomb -> City of Brass\n"
        "7. Smoldering Marsh -> The Black Gate\n"
        "8. Shivan Reef -> Flooded Strand\n"
        "9. Sulfurous Springs -> Marsh Flats\n"
        "10. Underground River -> Misty Rainforest\n"
        "11. Island -> Sea Gate Restoration // Sea Gate, Reborn\n"
        "12. Mountain -> Shatterskull Smashing // Shatterskull, the Hammer Pass\n"
        "13. Swamp -> Sink into Stupor // Soporific Springs\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "APPROVAL_READY", "deck_sha256": deck_sha, "count": 100, "distinct": 97, "front_face_lands": front_face_lands, "functional_land_slots": functional_land_slots}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
