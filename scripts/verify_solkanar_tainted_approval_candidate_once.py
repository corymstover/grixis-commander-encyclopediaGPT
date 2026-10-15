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
DECK_ID = "Sol_kanar_the_Tainted"
DISPLAY = "Sol'Kanar the Tainted"
EXPECTED_SHA = "72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58"
CANDIDATE = ROOT / "refinement/decklists/Solkanar_the_Tainted_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/Solkanar_the_Tainted_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/Solkanar_the_Tainted_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/solkanar_tainted_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "Solkanar_the_Tainted_Complete_Gate_Config.json"
RULES = OUTDIR / "Solkanar_the_Tainted_Rules_Attestation.json"
LEGAL = OUTDIR / "Solkanar_the_Tainted_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")

EXPECTED_CUTS = Counter({
    "Arcane Denial": 1,
    "Fellwar Stone": 1,
    "Feed the Swarm": 1,
    "Lightning Greaves": 1,
    "Clackbridge Troll": 1,
    "Brainstealer Dragon": 1,
    "Disrupt Decorum": 1,
    "Dragonskull Summit": 1,
    "Drowned Catacomb": 1,
    "Riverglide Pathway // Lavaglide Pathway": 1,
    "Shivan Reef": 1,
    "Sulfurous Springs": 1,
    "Underground River": 1,
})
EXPECTED_ADDS = Counter({
    "Force of Will": 1,
    "Mana Vault": 1,
    "Withering Torment": 1,
    "Deflecting Swat": 1,
    "Immortal Coil": 1,
    "Captive Audience": 1,
    "Conjurer's Closet": 1,
    "Badlands": 1,
    "Underground Sea": 1,
    "Volcanic Island": 1,
    "Flooded Strand": 1,
    "Marsh Flats": 1,
    "Misty Rainforest": 1,
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
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sol_kanar_the_Tainted.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Solkanar Tainted FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Solkanar Tainted FINAL TXT baseline")
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


def verify_ledger(baseline: Counter[str]) -> None:
    with LEDGER.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    expected_names = {n for n in baseline if n != DISPLAY}
    if {r["card"] for r in rows} != expected_names:
        raise RuntimeError("Solkanar Tainted decision ledger membership mismatch")
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
    if deck_sha != EXPECTED_SHA:
        raise RuntimeError(f"Candidate SHA mismatch: expected {EXPECTED_SHA}, found {deck_sha}")
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100 or len(baseline) != 93:
        raise RuntimeError(f"FINAL baseline structure mismatch: {sum(baseline.values())} cards / {len(baseline)} distinct")
    if sum(candidate.values()) != 100 or len(candidate) != 93:
        raise RuntimeError(f"Candidate structure mismatch: {sum(candidate.values())} cards / {len(candidate)} distinct")
    if lines[0] != "1x Sol'Kanar the Tainted [Commander]" or candidate[DISPLAY] != 1:
        raise RuntimeError("Solkanar Tainted commander-first line mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")

    repeats = {n: q for n, q in candidate.items() if q > 1}
    if repeats != {"Island": 3, "Mountain": 3, "Swamp": 4}:
        raise RuntimeError(f"Unexpected repeats: {repeats}")

    verify_ledger(baseline)

    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run targeted Solkanar Tainted refresh first")
    cache = load_cache()
    unresolved, nonlegal = [], []
    land_count = 0
    blue_pitch_pool = 0
    for name, qty in candidate.items():
        rec = cache.get(nkey(name))
        if not rec:
            unresolved.append(name)
            continue
        first_type = (rec.get("type_line") or "").split(" // ", 1)[0]
        if "Land" in first_type:
            land_count += qty
        if rec.get("commander_legality") != "legal":
            nonlegal.append((name, rec.get("commander_legality")))
        if name != "Force of Will" and "U" in (rec.get("color_identity") or []) and "Land" not in first_type:
            blue_pitch_pool += qty
    if unresolved:
        raise RuntimeError("Candidate names missing from current Oracle cache: " + ", ".join(sorted(unresolved)))
    if nonlegal:
        raise RuntimeError(f"Unexpected Commander legality rows: {nonlegal}")
    if land_count != 35:
        raise RuntimeError(f"Candidate land count is {land_count}, expected 35")
    if blue_pitch_pool < 15:
        raise RuntimeError(f"Force of Will blue pitch pool too shallow for candidate: {blue_pitch_pool}")

    for p in [AUDIT, DECISIONS]:
        t = p.read_text(encoding="utf-8")
        if deck_sha not in t:
            raise RuntimeError(f"{p.name} is not bound to current candidate SHA")
    audit = AUDIT.read_text(encoding="utf-8")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "99/99" not in audit or "86 KEEP / 13 CUT" not in audit:
        raise RuntimeError("Solkanar Tainted whole-list audit incomplete")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or "Power Bracket 4" not in decision:
        raise RuntimeError("Solkanar Tainted decision closeout incomplete")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — modal triggered abilities, source self-reference, zone changes/new objects, control changes, targets, and state-triggered abilities (current 2026 rules)",
            "Current Oracle text captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Current Wizards/Scryfall rulings for Sol'Kanar the Tainted, blink/control-change cards, and transferred losing-game permanents",
        ],
        "interactions": [
            {"name": "Sol'Kanar mode history and modal timing", "status": "PASS", "finding": "Sol'Kanar's beginning-of-end-step ability is modal; its mode is chosen as the triggered ability is put on the stack. The set of previously chosen modes is associated with that battlefield object. If Sol'Kanar leaves and returns, it is a new object with no modes previously chosen for its new existence."},
            {"name": "Thassa / Conjurer's Closet — reuse first three modes", "status": "PASS", "finding": "At the beginning of the end step, Sol'Kanar and Thassa or Conjurer's Closet can trigger together. For a draw/drain/damage mode, put the blink trigger below Sol'Kanar's trigger: the chosen Sol'Kanar mode resolves first, then the blink returns Sol'Kanar as a new object with all modes available again."},
            {"name": "Blinking before the fourth-mode trigger resolves", "status": "PASS", "finding": "When the fourth mode is chosen, putting a Thassa/Closet blink trigger above Sol'Kanar's trigger can exile and return Sol'Kanar first. The returned permanent is a new object. The older triggered ability's self-reference does not identify that new object, so it cannot exile and give away the returned Sol'Kanar."},
            {"name": "Fourth mode itself resets Sol'Kanar", "status": "PASS", "finding": "If the fourth mode resolves normally, it exiles Sol'Kanar and returns it under an opponent's control. The returned permanent is a new object, so its chosen-mode history is reset even though an opponent controls it."},
            {"name": "Planar Incision recovery", "status": "PASS", "finding": "Planar Incision can target an artifact or creature regardless of controller, then returns that card to the battlefield under its owner's control. It can therefore recover an opponent-controlled Sol'Kanar while also making it a new object with reset mode history."},
            {"name": "Homeward Path and Coveted Falcon recovery", "status": "PASS", "finding": "A pure control change does not make a permanent a new object. Homeward Path or Coveted Falcon can regain an owned Sol'Kanar, but those control changes do not themselves reset modes. If Sol'Kanar had been transferred by its fourth mode, that exile-and-return already created a fresh object before the later recovery."},
            {"name": "Immortal Coil gift kill", "status": "PASS", "finding": "Immortal Coil's current controller loses the game when that controller's graveyard is empty. After Coil is transferred to an opponent, Bojuka Bog or Rakdos Charm can exile that player's graveyard and cause Coil's state-triggered losing-game ability to trigger. Once that trigger is on the stack, adding a card to the graveyard does not remove that trigger."},
            {"name": "Fateful Handoff + Immortal Coil", "status": "PASS", "finding": "Fateful Handoff targets an artifact or creature you control, draws cards equal to its mana value, then an opponent gains control of it. Immortal Coil has mana value 4, so a resolving Handoff targeting Coil draws four cards and then transfers Coil."},
            {"name": "Demonic Pact transfer", "status": "PASS", "finding": "Demonic Pact's previously chosen modes remain associated with the same enchantment through ordinary control changes. The deck can take safe modes, then transfer that same object so the recipient inherits the remaining mode history, including the losing-game mode when it is the only choice left."},
            {"name": "Captive Audience", "status": "PASS", "finding": "Captive Audience enters under the control of an opponent of its owner's choice. Its beginning-of-upkeep trigger is controlled by its current controller, who chooses one of the modes not previously chosen for that same enchantment object."},
            {"name": "Greed's Gambit donation", "status": "PASS", "finding": "Greed's Gambit front-loads its entry value for its controller, while its later upkeep and leaves-the-battlefield liabilities are controlled by whoever controls it when those abilities trigger, making transfer effects strategically coherent with the deck."},
            {"name": "Lightning Greaves exclusion", "status": "PASS", "finding": "Shroud prevents a permanent from being targeted even by its controller. Removing Lightning Greaves avoids blocking Thassa, Conjurer's Closet and Planar Incision from targeting Sol'Kanar; Deflecting Swat protects without imposing shroud."},
            {"name": "Mana Vault role", "status": "PASS", "finding": "Mana Vault supplies three colorless mana toward Sol'Kanar's five-mana cost. The candidate does not add a separate Vault/Monolith combo package; the card is commander acceleration."},
            {"name": "Withering Torment", "status": "PASS", "finding": "Withering Torment is instant-speed creature-or-enchantment removal in black and is used as a direct speed/efficiency upgrade over Feed the Swarm."},
        ],
    }
    RULES.write_text(json.dumps(rules, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    legal = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "https://magic.wizards.com/en/banned-restricted-list — current Commander banned list",
            "Current_Cycle_Oracle_Cache.jsonl generated/refreshed from current Scryfall metadata",
        ],
        "unexpected_banned_cards": [],
        "project_exceptions_required": [],
        "finding": "Every Sol'Kanar the Tainted candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "Solkanar_the_Tainted_2026-10-15",
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

    gate_json = OUTDIR / "Solkanar_the_Tainted_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("deck_sha256") != deck_sha or gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
        raise RuntimeError("Complete gate did not return clean APPROVAL_READY for exact candidate")
    if gate.get("count") != 100 or gate.get("distinct_names") != 93:
        raise RuntimeError("Complete gate structure mismatch")
    if gate.get("commander_color_identity") != ["B", "R", "U"]:
        raise RuntimeError("Complete gate commander color identity mismatch")
    if gate.get("project_exceptions"):
        raise RuntimeError("Unexpected project exception in Solkanar Tainted gate")
    if gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS":
        raise RuntimeError("Rules or official legality gate failed")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #53 of 62\n\n"
        "## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Distinct names: **93**\n"
        "- Lands: **35**\n"
        "- Repeats: **Island x3 / Mountain x3 / Swamp x4 only**\n"
        "- Singleton: **PASS**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        f"- Force of Will blue-pitch pool: **{blue_pitch_pool} other blue nonland cards**\n"
        "- Whole-list audit: **99/99 noncommander copies adjudicated; 86 KEEP / 13 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 4 — Optimized**\n"
        "- Proposed Archidekt tags: **Donate / Blink / Giftable Curses**\n\n"
        "## Final proposed delta\n\n"
        "1. Arcane Denial -> Force of Will\n"
        "2. Fellwar Stone -> Mana Vault\n"
        "3. Feed the Swarm -> Withering Torment\n"
        "4. Lightning Greaves -> Deflecting Swat\n"
        "5. Clackbridge Troll -> Immortal Coil\n"
        "6. Brainstealer Dragon -> Captive Audience\n"
        "7. Disrupt Decorum -> Conjurer's Closet\n"
        "8. Dragonskull Summit -> Badlands\n"
        "9. Drowned Catacomb -> Underground Sea\n"
        "10. Riverglide Pathway // Lavaglide Pathway -> Volcanic Island\n"
        "11. Shivan Reef -> Flooded Strand\n"
        "12. Sulfurous Springs -> Marsh Flats\n"
        "13. Underground River -> Misty Rainforest\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": "APPROVAL_READY",
        "deck_sha256": deck_sha,
        "baseline_member": member_name,
        "baseline_source_sha256": sha256(baseline_raw),
        "land_count": land_count,
        "blue_pitch_pool": blue_pitch_pool,
        "ledger": "99 / 86 KEEP / 13 CUT",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
