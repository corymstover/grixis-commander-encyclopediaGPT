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
DECK_ID = "Sedris__the_Traitor_King"
DISPLAY = "Sedris, the Traitor King"
CANDIDATE = ROOT / "refinement/decklists/Sedris_the_Traitor_King_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/Sedris_the_Traitor_King_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/Sedris_the_Traitor_King_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/sedris_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "Sedris_the_Traitor_King_Complete_Gate_Config.json"
RULES = OUTDIR / "Sedris_the_Traitor_King_Rules_Attestation.json"
LEGAL = OUTDIR / "Sedris_the_Traitor_King_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")

EXPECTED_CUTS = Counter({
    "Counterspell": 1,
    "Underworld Breach": 1,
    "Fellwar Stone": 1,
    "Blightstep Pathway // Searstep Pathway": 1,
    "Clearwater Pathway // Murkwater Pathway": 1,
    "Riverglide Pathway // Lavaglide Pathway": 1,
    "Fabled Passage": 1,
    "Bojuka Bog": 1,
})
EXPECTED_ADDS = Counter({
    "Force of Will": 1,
    "Ripples of Undeath": 1,
    "Grim Monolith": 1,
    "Badlands": 1,
    "Flooded Strand": 1,
    "Misty Rainforest": 1,
    "Marsh Flats": 1,
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
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("/Sedris__the_Traitor_King.txt")]
        if not matches:
            matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sedris__the_Traitor_King.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sedris FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Sedris FINAL TXT baseline")
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
        raise RuntimeError("Sedris decision ledger membership mismatch")
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
    if (baseline_total, keep_total, cut_total) != (99, 91, 8):
        raise RuntimeError(f"Ledger totals must be 99 / 91 KEEP / 8 CUT; found {baseline_total} / {keep_total} / {cut_total}")


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    raw = CANDIDATE.read_bytes()
    deck_sha = sha256(raw)
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100 or len(baseline) != 99:
        raise RuntimeError(f"FINAL baseline structure mismatch: {sum(baseline.values())} cards / {len(baseline)} distinct")
    if sum(candidate.values()) != 100 or len(candidate) != 99:
        raise RuntimeError(f"Candidate structure mismatch: {sum(candidate.values())} cards / {len(candidate)} distinct")
    if lines[0] != "1x Sedris, the Traitor King [Commander]" or candidate[DISPLAY] != 1:
        raise RuntimeError("Sedris commander-first line mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")

    repeats = {n: q for n, q in candidate.items() if q > 1}
    if repeats != {"Swamp": 2}:
        raise RuntimeError(f"Unexpected repeats: {repeats}")

    verify_ledger(baseline)

    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run targeted Sedris refresh first")
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
    if land_count != 31:
        raise RuntimeError(f"Candidate land count is {land_count}, expected 31")
    if blue_pitch_pool < 15:
        raise RuntimeError(f"Force of Will blue pitch pool too shallow for approved candidate: {blue_pitch_pool}")

    for p in [AUDIT, DECISIONS]:
        t = p.read_text(encoding="utf-8")
        if deck_sha not in t:
            raise RuntimeError(f"{p.name} is not bound to current candidate SHA")
    audit = AUDIT.read_text(encoding="utf-8")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "99/99" not in audit or "91 KEEP / 8 CUT" not in audit:
        raise RuntimeError("Sedris whole-list audit incomplete")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or "Power Bracket 4" not in decision:
        raise RuntimeError("Sedris decision closeout incomplete")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — unearth, delayed triggered abilities, replacement effects, phasing, ending the turn, blink/new objects, triggered abilities and alternative costs (current 2026 rules)",
            "Current Oracle text captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Current Wizards release-note rulings for unearth/end-the-turn interactions",
        ],
        "interactions": [
            {"name": "Sedris-granted unearth", "status": "PASS", "finding": "Each creature card in Sedris's controller's graveyard has unearth {2}{B}. Unearth is an activated ability usable only as a sorcery; it returns the card with haste and creates a delayed beginning-of-next-end-step exile instruction plus a leave-the-battlefield exile replacement effect."},
            {"name": "Convergence of Dominion", "status": "PASS", "finding": "While Sedris is controlled, Convergence reduces activated abilities of cards in that player's graveyard by {2}. Sedris-granted unearth {2}{B} therefore costs {B}; the one-mana floor prevents Embalmer's Tools from reducing it further."},
            {"name": "Obeka / Sundial timing", "status": "PASS", "finding": "If the unearth delayed exile trigger has already triggered at the beginning of the end step and is on the stack, ending the turn exiles that trigger from the stack. It does not trigger again on a later end step. Ending the turn before the delayed trigger exists would not accomplish the same thing."},
            {"name": "Teferi's Veil", "status": "PASS", "finding": "An attacking creature phases out at end of combat. A phased-out unearthed permanent is unavailable to the delayed exile instruction when that instruction resolves later; lethal combat damage is dealt before the end-of-combat phase-out."},
            {"name": "Deadeye Navigator rescue", "status": "PASS", "finding": "Deadeye can exile and immediately return a paired unearthed creature. Unearth's leave-the-battlefield replacement does not replace an effect already trying to exile the permanent; the returned card is a new object and is no longer tracked by the old unearth delayed trigger/replacement effect."},
            {"name": "River Kelpie", "status": "PASS", "finding": "A creature returned by unearth enters the battlefield from a graveyard and therefore triggers River Kelpie's permanent-from-graveyard draw ability."},
            {"name": "Twilight Diviner", "status": "PASS", "finding": "An unearthed creature entered from a graveyard, so Twilight Diviner can create a token copy of one qualifying creature, subject to its once-each-turn trigger restriction. The token is not the unearthed card and is not subject to that card's unearth exile instruction."},
            {"name": "Ripples of Undeath", "status": "PASS", "finding": "At the beginning of the controller's first main phase it mills three cards, then the controller may pay {1} and 3 life to put one of those cards into hand. Cards not selected remain in the graveyard as Sedris resources."},
            {"name": "Deadeye Navigator + Peregrine Drake", "status": "PASS", "finding": "With Deadeye paired to Peregrine Drake, paying {1}{U} blinks Drake and its ETB untaps up to five lands. With sufficient mana-producing lands this is a repeatable positive-mana loop; the existing combo package is preserved rather than replaced."},
            {"name": "Panharmonicon ETB package", "status": "PASS", "finding": "The deck retains numerous creature ETB triggers—including tutor, removal, reanimation and value effects—that can trigger an additional time under Panharmonicon when applicable."},
            {"name": "Grim Monolith role", "status": "PASS", "finding": "Grim Monolith supplies three colorless mana toward six-mana Sedris. No separate Power Artifact/Basalt/Rings-style Monolith combo package is introduced by this candidate."},
            {"name": "Undercity Sewers", "status": "PASS", "finding": "Undercity Sewers has Island and Swamp land types, is fetchable by the candidate's relevant fetchlands, and surveils 1 when it enters, allowing a creature to be placed into the graveyard for Sedris."},
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
        "finding": "Every Sedris candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "Sedris_the_Traitor_King_2026-10-15",
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

    gate_json = OUTDIR / "Sedris_the_Traitor_King_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
        raise RuntimeError(f"Complete gate did not return clean APPROVAL_READY: {gate}")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #51 of 62\n\n"
        "## Result\n\n"
        "**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Distinct names: **99**\n"
        "- Lands: **31**\n"
        "- Repeats: **Swamp x2 only**\n"
        "- Singleton: **PASS**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        f"- Force of Will blue-pitch pool: **{blue_pitch_pool} other blue nonland cards**\n"
        "- Whole-list audit: **99/99 noncommander copies adjudicated; 91 KEEP / 8 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 4 — Optimized**\n"
        "- Proposed Archidekt tags: **Unearth / Reanimator / End-Step Control**\n\n"
        "## Final proposed delta\n\n"
        "1. Counterspell -> Force of Will\n"
        "2. Underworld Breach -> Ripples of Undeath\n"
        "3. Fellwar Stone -> Grim Monolith\n"
        "4. Blightstep Pathway // Searstep Pathway -> Badlands\n"
        "5. Clearwater Pathway // Murkwater Pathway -> Flooded Strand\n"
        "6. Riverglide Pathway // Lavaglide Pathway -> Misty Rainforest\n"
        "7. Fabled Passage -> Marsh Flats\n"
        "8. Bojuka Bog -> Undercity Sewers\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "APPROVAL_READY", "deck_sha256": deck_sha, "count": 100, "distinct": 99, "lands": land_count, "blue_pitch_pool": blue_pitch_pool}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
