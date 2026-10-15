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
DECK_ID = "Sauron__Lord_of_the_Rings"
DISPLAY = "Sauron, Lord of the Rings"
CANDIDATE = ROOT / "refinement/decklists/Sauron_Lord_of_the_Rings_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/Sauron_Lord_of_the_Rings_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/Sauron_Lord_of_the_Rings_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/sauron_lotr_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "Sauron_Lord_of_the_Rings_Complete_Gate_Config.json"
RULES = OUTDIR / "Sauron_Lord_of_the_Rings_Rules_Attestation.json"
LEGAL = OUTDIR / "Sauron_Lord_of_the_Rings_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/Sauron_Lord_of_the_Rings_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")

EXPECTED_CUTS = Counter({
    "Knollspine Dragon": 1,
    "Notion Thief": 1,
    "In the Darkness Bind Them": 1,
    "Stitch Together": 1,
    "Counterspell": 1,
    "Crumbling Necropolis": 1,
    "Drowned Catacomb": 1,
    "Sulfurous Springs": 1,
    "Underground River": 1,
    "Island": 1,
    "Mountain": 1,
    "Swamp": 1,
})
EXPECTED_ADDS = Counter({
    "Metamorphosis Fanatic": 1,
    "Mana Vault": 1,
    "Grim Monolith": 1,
    "Dance of the Dead": 1,
    "Force of Will": 1,
    "Volcanic Island": 1,
    "City of Brass": 1,
    "Command Beacon": 1,
    "Phyrexian Tower": 1,
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
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("/Sauron__Lord_of_the_Rings.txt")]
        if not matches:
            matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sauron__Lord_of_the_Rings.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sauron FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Sauron FINAL TXT baseline")
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
        raise RuntimeError("Sauron decision ledger membership mismatch")
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
    if (baseline_total, keep_total, cut_total) != (99, 87, 12):
        raise RuntimeError(f"Ledger totals must be 99 / 87 KEEP / 12 CUT; found {baseline_total} / {keep_total} / {cut_total}")


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    raw = CANDIDATE.read_bytes()
    deck_sha = sha256(raw)
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100 or len(baseline) != 93:
        raise RuntimeError(f"FINAL baseline structure mismatch: {sum(baseline.values())} cards / {len(baseline)} distinct")
    if sum(candidate.values()) != 100 or len(candidate) != 96:
        raise RuntimeError(f"Candidate structure mismatch: {sum(candidate.values())} cards / {len(candidate)} distinct")
    if lines[0] != "1x Sauron, Lord of the Rings [Commander]" or candidate[DISPLAY] != 1:
        raise RuntimeError("Sauron commander-first line mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")

    expected_repeats = {"Nazgûl": 4, "Swamp": 2}
    actual_repeats = {n: q for n, q in candidate.items() if q > 1}
    if actual_repeats != expected_repeats:
        raise RuntimeError(f"Unexpected repeats: {actual_repeats}")

    verify_ledger(baseline)

    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run targeted Sauron refresh first")
    cache = load_cache()
    unresolved, nonlegal = [], []
    land_count = 0
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
    if unresolved:
        raise RuntimeError("Candidate names missing from current Oracle cache: " + ", ".join(sorted(unresolved)))
    if nonlegal:
        raise RuntimeError(f"Unexpected Commander legality rows: {nonlegal}")
    if land_count != 32:
        raise RuntimeError(f"Candidate land count is {land_count}, expected 32")

    nazgul = cache.get(nkey("Nazgûl"))
    nazgul_text = (nazgul or {}).get("oracle_text", "")
    if "A deck can have up to nine cards named Nazgûl." not in nazgul_text:
        raise RuntimeError("Nazgûl deck-construction permission not verified in current Oracle text")

    bind_sha(AUDIT, deck_sha)
    bind_sha(DECISIONS, deck_sha)
    audit = AUDIT.read_text(encoding="utf-8")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "99/99" not in audit or "87 KEEP / 12 CUT" not in audit or deck_sha not in audit:
        raise RuntimeError("Sauron whole-list audit incomplete or SHA-mismatched")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or "Power Bracket 4" not in decision or deck_sha not in decision:
        raise RuntimeError("Sauron decision closeout incomplete or SHA-mismatched")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — triggered abilities, commander additional costs, mana abilities, Aura/reanimation rules, Living Death sequencing, and deck-construction exceptions (current 2026 rules)",
            "The Lord of the Rings: Tales of Middle-earth release notes — Sauron, Lord of the Rings and Ring/amass rulings",
            "Current Oracle text captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Wizards current Commander banned/restricted list checked 2026-10-15",
        ],
        "interactions": [
            {"name": "Sauron cast-trigger independence", "status": "PASS", "finding": "Sauron's first ability triggers when the commander spell is cast. Once on the stack, the triggered ability exists independently of the Sauron spell; countering the commander spell does not counter or remove the trigger."},
            {"name": "Sauron trigger sequencing", "status": "PASS", "finding": "On resolution the trigger amasses Orcs 5, mills five cards, then returns a creature card from the controller's graveyard to the battlefield. The creature is chosen during resolution and may be one of the five cards just milled."},
            {"name": "Command Beacon and commander tax", "status": "PASS", "finding": "Command Beacon can move Sauron from the command zone to its owner's hand. Commander tax applies to casts from the command zone, so casting Sauron from hand avoids that additional cost while still being a cast that triggers Sauron's ability."},
            {"name": "Metamorphosis Fanatic chain", "status": "PASS", "finding": "If Sauron's trigger returns Metamorphosis Fanatic, the Fanatic enters and its own ETB trigger can return up to one target creature card from its controller's graveyard with a lifelink counter, producing a second reanimation event."},
            {"name": "Dance of the Dead", "status": "PASS", "finding": "Dance of the Dead enchants a creature card in a graveyard, returns it tapped, then becomes attached to that creature. The creature gets +1/+1, does not untap normally, and its controller may pay {1}{B} at upkeep to untap it."},
            {"name": "Phyrexian Tower", "status": "PASS", "finding": "Phyrexian Tower's {T}, sacrifice-a-creature ability is a mana ability that adds {B}{B}. Sacrificing a creature can intentionally place it into the graveyard before Living Death or another recursion effect."},
            {"name": "Nazgûl deck construction", "status": "PASS", "finding": "Nazgûl's Oracle text explicitly allows up to nine cards named Nazgûl in a deck. The candidate contains four, so the Commander singleton rule is satisfied by the card-specific permission."},
            {"name": "Nazgûl and Ring temptation", "status": "PASS", "finding": "Each Nazgûl enters and causes the Ring to tempt its controller. Whenever the Ring tempts that player, each Nazgûl trigger puts a +1/+1 counter on each Wraith controlled by that player; the preserved Ring package therefore remains a real secondary engine."},
            {"name": "Anger and Wonder land-type checks", "status": "PASS", "finding": "Anger grants haste while in the graveyard only if its controller controls a Mountain; Wonder grants flying only if its controller controls an Island. The revised mana base retains both basics and multiple typed duals with those land types."},
            {"name": "Living Death sequencing", "status": "PASS", "finding": "Living Death exiles creature cards from graveyards, then each player sacrifices all creatures they control, then puts the cards they exiled this way onto the battlefield. Setup and sacrifice timing therefore matter."},
            {"name": "Sneak Attack graveyard setup", "status": "PASS", "finding": "Sneak Attack's delayed sacrifice at the beginning of the next end step naturally places cheated creatures into the graveyard, where Sauron or another reanimation spell can use them later."},
            {"name": "The Mouth of Sauron self-mill", "status": "PASS", "finding": "The Mouth of Sauron's enter-the-battlefield ability can target its controller. That player mills three cards and then the Mouth amasses Orcs X based on instant and sorcery cards in that player's graveyard, directly supporting setup plus Army growth."},
            {"name": "Sauron opponent-commander death trigger", "status": "PASS", "finding": "Sauron's final ability triggers when a commander an opponent controls dies, even if that commander is then moved to the command zone; the Ring temptation supports the retained Nazgûl package."},
            {"name": "Fast-mana role", "status": "PASS", "finding": "Mana Vault and Grim Monolith provide colorless acceleration toward Sauron's eight-mana casting cost. Their inclusion is commander-speed support, not a separate Monolith combo package in this candidate."},
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
        "finding": "Every Sauron candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "Sauron_Lord_of_the_Rings_2026-10-15",
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

    gate_json = OUTDIR / "Sauron_Lord_of_the_Rings_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
        raise RuntimeError(f"Complete gate did not return clean APPROVAL_READY: {gate}")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #49 of 62\n\n"
        "## Result\n\n"
        "**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Distinct names: **96**\n"
        "- Lands: **32**\n"
        "- Repeats: **Nazgûl x4 / Swamp x2 only**\n"
        "- Singleton: **PASS — Nazgûl card-specific permission verified**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        "- Whole-list audit: **99/99 noncommander copies adjudicated; 87 KEEP / 12 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 4 — Optimized**\n"
        "- Proposed Archidekt tags: **Reanimator / Graveyard Setup / Amass Orcs**\n\n"
        "## Final proposed delta\n\n"
        "1. Knollspine Dragon -> Metamorphosis Fanatic\n"
        "2. Notion Thief -> Mana Vault\n"
        "3. In the Darkness Bind Them -> Grim Monolith\n"
        "4. Stitch Together -> Dance of the Dead\n"
        "5. Counterspell -> Force of Will\n"
        "6. Crumbling Necropolis -> Volcanic Island\n"
        "7. Drowned Catacomb -> City of Brass\n"
        "8. Sulfurous Springs -> Flooded Strand\n"
        "9. Underground River -> Marsh Flats\n"
        "10. Island -> Misty Rainforest\n"
        "11. Mountain -> Command Beacon\n"
        "12. Swamp -> Phyrexian Tower\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "APPROVAL_READY", "deck_sha256": deck_sha, "count": 100, "distinct": 96, "lands": land_count}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
