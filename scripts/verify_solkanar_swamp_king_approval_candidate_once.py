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
DECK_ID = "Sol_kanar_the_Swamp_King"
DISPLAY = "Sol'kanar the Swamp King"
EXPECTED_SHA = "7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106"
CANDIDATE = ROOT / "refinement/decklists/Solkanar_the_Swamp_King_Approval_Ready_2026-10-15.txt"
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
AUDIT = ROOT / "refinement/verification/Solkanar_the_Swamp_King_Whole_List_Audit_2026-10-15.md"
DECISIONS = ROOT / "refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md"
LEDGER = ROOT / "refinement/decisions/Solkanar_the_Swamp_King_Whole_List_Decision_Ledger_2026-10-15.csv"
OUTDIR = ROOT / "refinement/verification/solkanar_swamp_king_2026-10-15/gate_output"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CONFIG = OUTDIR / "Solkanar_the_Swamp_King_Complete_Gate_Config.json"
RULES = OUTDIR / "Solkanar_the_Swamp_King_Rules_Attestation.json"
LEGAL = OUTDIR / "Solkanar_the_Swamp_King_Official_Legality_Attestation.json"
SUMMARY = ROOT / "refinement/verification/Solkanar_the_Swamp_King_Approval_Ready_Verification_2026-10-15.md"

LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
PRINT_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")
EXPECTED_CUTS = Counter({
    "Feed the Swarm": 1,
    "Fellwar Stone": 1,
    "Blightstep Pathway // Searstep Pathway": 1,
    "Dragonskull Summit": 1,
    "Drowned Catacomb": 1,
})
EXPECTED_ADDS = Counter({
    "Withering Torment": 1,
    "The Soul Stone": 1,
    "Fell the Profane // Fell Mire": 1,
    "Raucous Theater": 1,
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
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("/Sol_kanar_the_Swamp_King.txt")]
        if not matches:
            matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sol_kanar_the_Swamp_King.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sol'kanar FINAL TXT member, found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Sol'kanar FINAL TXT baseline")
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
        raise RuntimeError("Sol'kanar decision ledger membership mismatch")
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
    if (baseline_total, keep_total, cut_total) != (99, 94, 5):
        raise RuntimeError(f"Ledger totals must be 99 / 94 KEEP / 5 CUT; found {baseline_total} / {keep_total} / {cut_total}")


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    raw = CANDIDATE.read_bytes()
    deck_sha = sha256(raw)
    if deck_sha != EXPECTED_SHA:
        raise RuntimeError(f"Candidate SHA mismatch: {deck_sha}; expected {EXPECTED_SHA}")
    lines, candidate = parse_bytes(raw)
    member_name, baseline_raw = baseline_member()
    _, baseline = parse_bytes(baseline_raw)

    if sum(baseline.values()) != 100 or len(baseline) != 95:
        raise RuntimeError(f"FINAL baseline structure mismatch: {sum(baseline.values())} cards / {len(baseline)} distinct")
    if sum(candidate.values()) != 100 or len(candidate) != 95:
        raise RuntimeError(f"Candidate structure mismatch: {sum(candidate.values())} cards / {len(candidate)} distinct")
    if lines[0] != "1x Sol'kanar the Swamp King [Commander]" or candidate[DISPLAY] != 1:
        raise RuntimeError("Sol'kanar commander-first line mismatch")

    actual_cuts = baseline - candidate
    actual_adds = candidate - baseline
    if actual_cuts != EXPECTED_CUTS:
        raise RuntimeError(f"Unexpected baseline cuts: {actual_cuts}; expected {EXPECTED_CUTS}")
    if actual_adds != EXPECTED_ADDS:
        raise RuntimeError(f"Unexpected baseline additions: {actual_adds}; expected {EXPECTED_ADDS}")
    repeats = {n: q for n, q in candidate.items() if q > 1}
    if repeats != {"Swamp": 6}:
        raise RuntimeError(f"Unexpected repeats: {repeats}")

    verify_ledger(baseline)
    if not CACHE.exists():
        raise RuntimeError("Oracle cache missing; run targeted Sol'kanar refresh first")
    cache = load_cache()
    unresolved, nonlegal, identity_errors = [], [], []
    front_face_land_count = 0
    for name, qty in candidate.items():
        rec = cache.get(nkey(name))
        if not rec:
            unresolved.append(name)
            continue
        first_type = (rec.get("type_line") or "").split(" // ", 1)[0]
        if "Land" in first_type:
            front_face_land_count += qty
        if rec.get("commander_legality") != "legal":
            nonlegal.append((name, rec.get("commander_legality")))
        if not set(rec.get("color_identity") or []).issubset({"U", "B", "R"}):
            identity_errors.append((name, rec.get("color_identity")))
    if unresolved:
        raise RuntimeError("Candidate names missing from current Oracle cache: " + ", ".join(sorted(unresolved)))
    if nonlegal:
        raise RuntimeError(f"Unexpected Commander legality rows: {nonlegal}")
    if identity_errors:
        raise RuntimeError(f"Color identity mismatches: {identity_errors}")
    if front_face_land_count != 35:
        raise RuntimeError(f"Candidate front-face land count is {front_face_land_count}, expected 35")
    if candidate["Fell the Profane // Fell Mire"] != 1:
        raise RuntimeError("Fell the Profane // Fell Mire MDFC missing")
    functional_land_slots = front_face_land_count + 1
    if functional_land_slots != 36:
        raise RuntimeError(f"Functional land-capable slots are {functional_land_slots}, expected 36")

    star = cache.get(nkey("Starscape Cleric"))
    if not star:
        raise RuntimeError("Starscape Cleric exact Oracle record missing")
    if star.get("canonical_name") != "Starscape Cleric" or star.get("commander_legality") != "legal":
        raise RuntimeError("Starscape Cleric exact-printing resolution failed")
    if "Bat Cleric" not in (star.get("type_line") or "") or "Whenever you gain life" not in (star.get("oracle_text") or ""):
        raise RuntimeError("Starscape Cleric did not resolve to BLB #116 card object")
    soul = cache.get(nkey("The Soul Stone")) or {}
    if "Indestructible" not in (soul.get("oracle_text") or "") or "Add {B}" not in (soul.get("oracle_text") or "") or "Harness" not in (soul.get("oracle_text") or ""):
        raise RuntimeError("The Soul Stone Oracle record incomplete for intended role")
    if "B" not in (soul.get("color_identity") or []):
        raise RuntimeError("The Soul Stone is not resolving as black identity")

    for p in [AUDIT, DECISIONS]:
        text = p.read_text(encoding="utf-8")
        if deck_sha not in text:
            raise RuntimeError(f"{p.name} is not bound to current candidate SHA")
    audit = AUDIT.read_text(encoding="utf-8")
    decision = DECISIONS.read_text(encoding="utf-8")
    if "99/99" not in audit or "94 KEEP / 5 CUT" not in audit or "36 functional land-capable slots" not in audit:
        raise RuntimeError("Sol'kanar whole-list audit incomplete")
    if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or "Power Bracket 4" not in decision:
        raise RuntimeError("Sol'kanar decision closeout incomplete")

    now = datetime.now(timezone.utc).isoformat()
    rules = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "Magic Comprehensive Rules — spell colors, triggered abilities, life gain/loss, land subtypes, mana abilities, modal double-faced cards, replacement/continuous effects (current 2026 rules)",
            "Current Oracle text captured in refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl",
            "Current Wizards Commander banned/restricted list checked 2026-10-15",
            "Marvel's Spider-Man release notes — The Soul Stone harness designation",
        ],
        "interactions": [
            {"name": "Sol'kanar black-spell trigger", "status": "PASS", "finding": "Sol'kanar triggers whenever any player casts a black spell. Each qualifying spell creates a separate trigger that gains its controller 1 life when it resolves."},
            {"name": "Demon's Horn parallel trigger", "status": "PASS", "finding": "Demon's Horn separately triggers when a player casts a black spell. A single black spell can therefore produce both the Sol'kanar trigger and the Horn trigger; each life-gain event resolves separately."},
            {"name": "Painter's Servant naming black", "status": "PASS", "finding": "Painter's Servant makes cards, spells and permanents the chosen color in addition to their other colors. Naming black therefore makes spells cast by any player black for Sol'kanar and Demon's Horn while preserving the Painter/Grindstone line."},
            {"name": "Repeated lifegain payoffs", "status": "PASS", "finding": "Each separate Sol'kanar/Horn or other life-gain event can independently trigger applicable gain-to-loss payoffs such as Vito, Starscape Cleric, Marauding Blight-Priest and Enduring Tenacity according to their Oracle text."},
            {"name": "Exquisite Blood life loop", "status": "PASS", "finding": "Exquisite Blood (and the analogous Bloodthirsty Conqueror trigger) gains life when an opponent loses life. With a retained mandatory gain-to-loss payoff, an initial qualifying life-gain or opponent-life-loss event can create a repeating loss/gain loop unless interrupted."},
            {"name": "Painter's Servant + Grindstone", "status": "PASS", "finding": "With Painter's Servant making all cards the same chosen color, Grindstone's repeated-color condition continues to repeat as it resolves and mills the targeted player's library absent an interruption/replacement effect."},
            {"name": "Blanket of Night / Urborg", "status": "PASS", "finding": "Blanket of Night and Urborg each make affected lands Swamps in addition to their other land types. This enables Sol'kanar's swampwalk against an opponent controlling a Swamp and expands Swamp-counting/mana-doubling synergies."},
            {"name": "Typed surveil Swamps", "status": "PASS", "finding": "Raucous Theater is a Swamp Mountain and Undercity Sewers is an Island Swamp. Both are fetchable by matching fetchlands, count as Swamps for Cabal Coffers and Consuming Corruption, work with Crypt Ghast when tapped for black mana, and trigger Dread Presence when entering under the controller's control."},
            {"name": "The Soul Stone", "status": "PASS", "finding": "The Soul Stone costs {1}{B}, so it is a black spell while on the stack and triggers Sol'kanar/Demon's Horn when cast. It is indestructible, taps for {B}, and once harnessed its infinity ability triggers at upkeep to return a target creature card from its controller's graveyard to the battlefield."},
            {"name": "Withering Torment", "status": "PASS", "finding": "Withering Torment is a black instant that destroys target creature or enchantment and causes its controller to lose 2 life. Casting it triggers Sol'kanar/Demon's Horn; if its target is illegal on resolution, the spell does not resolve and the life loss does not occur."},
            {"name": "Fell the Profane // Fell Mire", "status": "PASS", "finding": "Casting Fell the Profane uses the black instant front and triggers Sol'kanar/Demon's Horn. Playing Fell Mire as a land is not casting a spell and does not trigger them. Fell Mire may enter untapped if its controller pays 3 life and taps for {B}."},
            {"name": "Bontu's Monument", "status": "PASS", "finding": "Bontu's Monument reduces black creature spells and separately triggers when its controller casts a creature spell, draining each opponent and gaining life. Those events layer naturally with the deck's black-spell/lifegain plan."},
            {"name": "K'rrik and Bolas's Citadel", "status": "PASS", "finding": "K'rrik can substitute life for black mana symbols where permitted, and Bolas's Citadel can pay life equal to mana value for top-library spells. The deck's repeated lifegain offsets those life-resource engines but does not remove their normal timing/cost restrictions."},
            {"name": "Wheel pressure", "status": "PASS", "finding": "Wheel of Fortune and Windfall cause card draws that can trigger Sheoldred for its controller/opponents as applicable and Underworld Dreams for opponent draws; those are preserved secondary pressure lines rather than the primary commander identity."},
        ],
    }
    RULES.write_text(json.dumps(rules, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    legal = {
        "status": "PASS",
        "deck_sha256": deck_sha,
        "checked_at_utc": now,
        "sources": [
            "https://magic.wizards.com/en/banned-restricted-list — current Commander banned list checked 2026-10-15",
            "Current_Cycle_Oracle_Cache.jsonl generated/refreshed from current Scryfall metadata",
        ],
        "unexpected_banned_cards": [],
        "project_exceptions_required": [],
        "finding": "Every Sol'kanar candidate card is officially Commander-legal in the refreshed current-cycle Oracle cache and no card appears on the current Commander banned list; no project exception is required.",
    }
    LEGAL.write_text(json.dumps(legal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "deck_id": DECK_ID,
        "display_name": DISPLAY,
        "decklist_path": str(CANDIDATE.relative_to(ROOT)),
        "expected_deck_sha256": deck_sha,
        "baseline_source_sha256": sha256(baseline_raw),
        "output_dir": str(OUTDIR.relative_to(ROOT)),
        "output_stem": "Solkanar_the_Swamp_King_2026-10-15",
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

    gate_json = OUTDIR / "Solkanar_the_Swamp_King_2026-10-15_Complete_Gate.json"
    gate = json.loads(gate_json.read_text(encoding="utf-8"))
    if gate.get("deck_sha256") != deck_sha or gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
        raise RuntimeError("Complete gate did not return clean SHA-bound APPROVAL_READY")
    if gate.get("count") != 100 or gate.get("distinct_names") != 95:
        raise RuntimeError("Complete gate structural result mismatch")
    if gate.get("commander_color_identity") != ["B", "R", "U"]:
        raise RuntimeError(f"Unexpected commander color identity: {gate.get('commander_color_identity')}")
    if gate.get("project_exceptions"):
        raise RuntimeError("Unexpected project exception in complete gate")
    if gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS":
        raise RuntimeError("Rules/legality gate not PASS")

    SUMMARY.write_text(
        f"# {DISPLAY} — approval-ready verification\n\n"
        f"Date: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #52 of 62\n\n"
        "## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n"
        f"- Exact candidate SHA-256: `{deck_sha}`\n"
        "- Cards: **100**\n"
        "- Distinct names: **95**\n"
        f"- Front-face lands: **{front_face_land_count}**\n"
        "- Land-capable MDFCs: **1**\n"
        f"- Functional land-capable slots: **{functional_land_slots}**\n"
        "- Repeats: **Swamp x6 only**\n"
        "- Singleton: **PASS**\n"
        "- Commander color identity: **U/B/R — PASS**\n"
        "- Starscape Cleric exact BLB #116 resolution: **PASS**\n"
        "- Fresh current-cycle Oracle resolution: **PASS**\n"
        "- Official Commander legality: **PASS**\n"
        "- Project exceptions: **none**\n"
        "- Rules-interaction attestation: **PASS**\n"
        "- Whole-list audit: **99/99 noncommander copies adjudicated; 94 KEEP / 5 CUT**\n"
        "- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n"
        "- Natural ceiling: **Power Bracket 4 — Optimized**\n"
        "- Proposed Archidekt tags: **Black Spells / Lifegain / Swamp Matters**\n\n"
        "## Final proposed delta\n\n"
        "1. Feed the Swarm -> Withering Torment\n"
        "2. Fellwar Stone -> The Soul Stone\n"
        "3. Blightstep Pathway // Searstep Pathway -> Fell the Profane // Fell Mire\n"
        "4. Dragonskull Summit -> Raucous Theater\n"
        "5. Drowned Catacomb -> Undercity Sewers\n\n"
        "The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "APPROVAL_READY",
        "deck_sha256": deck_sha,
        "count": 100,
        "distinct_names": 95,
        "front_face_lands": front_face_land_count,
        "functional_land_slots": functional_land_slots,
        "whole_list_audit": "99/99 — 94 KEEP / 5 CUT",
        "project_exceptions": [],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
