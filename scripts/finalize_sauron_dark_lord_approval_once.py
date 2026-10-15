import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

EXPECTED_SHA = "fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Sauron__the_Dark_Lord"
NAME = "Sauron, the Dark Lord"

candidate = Path("refinement/decklists/Sauron_the_Dark_Lord_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Sauron_the_Dark_Lord_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md")
gate_path = Path("refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_2026-10-15_Complete_Gate.json")
approval_record = Path("refinement/approvals/Sauron_the_Dark_Lord_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Sauron the Dark Lord candidate SHA mismatch: {actual_sha}")

lines = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
if not lines or lines[0] != "1x Sauron, the Dark Lord [Commander]":
    raise SystemExit("Sauron the Dark Lord commander-first line mismatch")

card_total = 0
names = []
for line in lines:
    qty_text, name = line.split("x ", 1)
    qty = int(qty_text)
    card_total += qty
    clean_name = name.replace(" [Commander]", "")
    names.extend([clean_name] * qty)
if card_total != 100:
    raise SystemExit(f"Candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 91:
    raise SystemExit(f"Candidate must contain 91 distinct names; found {len(set(names))}")

counts = Counter(names)
repeats = {k: v for k, v in counts.items() if v > 1}
expected_repeats = {"Nazgûl": 7, "Swamp": 3, "Mountain": 2}
if repeats != expected_repeats:
    raise SystemExit(f"Unexpected repeated names: {repeats}")

verification = verification_path.read_text(encoding="utf-8")
for bit in [
    EXPECTED_SHA,
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    "99/99 noncommander copies adjudicated; 91 KEEP / 8 CUT",
    "ZERO NEW MATERIAL IMPROVEMENTS",
    "Power Bracket 4 — Optimized",
    "Project exceptions: **none**",
    "Lands: **34**",
]:
    if bit not in verification:
        raise SystemExit(f"Verification missing required evidence: {bit}")

audit = audit_path.read_text(encoding="utf-8")
for bit in [EXPECTED_SHA, "99/99", "91 KEEP / 8 CUT", "34 lands"]:
    if bit not in audit:
        raise SystemExit(f"Whole-list audit incomplete or SHA-mismatched: {bit}")

decision = decision_path.read_text(encoding="utf-8")
for bit in [EXPECTED_SHA, "ZERO NEW MATERIAL IMPROVEMENTS", "Power Bracket 4 — Optimized"]:
    if bit not in decision:
        raise SystemExit(f"Decision closeout incomplete or SHA-mismatched: {bit}")

gate = json.loads(gate_path.read_text(encoding="utf-8"))
if gate.get("deck_sha256") != EXPECTED_SHA:
    raise SystemExit("Complete gate SHA mismatch")
if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
    raise SystemExit("Complete gate is not clean APPROVAL_READY")
if gate.get("count") != 100 or gate.get("distinct_names") != 91:
    raise SystemExit("Complete gate structural result mismatch")
if gate.get("commander_color_identity") != ["B", "R", "U"]:
    raise SystemExit("Complete gate color-identity mismatch")
if gate.get("project_exceptions"):
    raise SystemExit("Unexpected project exception")
if gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS":
    raise SystemExit("Rules/legality gate not PASS")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved artifact SHA mismatch")

approval_record.parent.mkdir(parents=True, exist_ok=True)
approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready Sauron, the Dark Lord candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first Army/Ring/Wraith review, candidate exhaustion, adversarial red-team review, mana-base review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, Nazgûl deck-construction verification, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 91 distinct names, 34 lands, with Nazgûl x7 permitted by its own deck-construction text, plus Swamp x3 and Mountain x2 as the only other repeats. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Amass Orcs / Ring Temptation / Wraiths.\n\n"
    "This approval freezes `refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
    encoding="utf-8",
)

if "Status: working decision closeout; not user approval" in decision:
    decision = decision.replace(
        "Status: working decision closeout; not user approval",
        "Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",
        1,
    )
if "## Approval closeout" not in decision:
    decision += (
        "\n## Approval closeout\n\n"
        f"- Explicit user approval received: **{DATE}**\n"
        f"- Canonical approved SHA-256: `{EXPECTED_SHA}`\n"
        "- Exact approved artifact: `refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Sedris, the Traitor King (index 50 / deck 51 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Sauron the Dark Lord approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Sauron, the Dark Lord approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first Army/Ring/Wraith review, candidate exhaustion, adversarial red-team review, mana-base review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, Nazgûl deck-construction verification, and U/B/R color-identity verification.",
    "whole_list_audit_artifact": "refinement/verification/Sauron_the_Dark_Lord_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Sauron_the_Dark_Lord_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt"
}
state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

raw_lines = tracker_path.read_text(encoding="utf-8").splitlines()
header = next(csv.reader([raw_lines[0]]))
idx = {name: i for i, name in enumerate(header)}

def update_line(line, updates):
    row = next(csv.reader([line]))
    if len(row) < len(header):
        row += [""] * (len(header) - len(row))
    for key, value in updates.items():
        row[idx[key]] = value
    out = io.StringIO()
    csv.writer(out, lineterminator="").writerow(row)
    return out.getvalue()

updates = {
    "baseline_status": "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.",
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Sauron, the Dark Lord candidate verified at 100 cards / 91 distinct names within U/B/R; Nazgûl x7, Swamp x3, Mountain x2 are the only repeats.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — Sauron Army/Ring/Wraith blueprint finalized at Power Bracket 4 — Optimized; opponent-spell amass, Army combat damage, Ring temptation, and Nazgûl/Wraith growth remain primary identity.",
    "high_impact_candidate_triage_complete": "PASS — Great Goblin/Roaming Throne/Minas Morgul branch review, current-card challenger pass, fast-mana/protection review, mana-base red team, Ring/Nazgûl preservation, candidate exhaustion, and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 91 KEEP / 8 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Sauron ward and opponent-spell amass; Army combat-to-Ring loop; Nazgûl construction/triggers; Mauhúr replacement; The Great Goblin; Great Goblin, Foul-Hearted; Minas Morgul Army-Wraith bridge; Roaming Throne Avatar/Wraith modes; Force of Will pitch pool; Wonder/Anger; Widespread Brutality reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 91 distinct names / 34 lands; Nazgûl x7 permitted by card text plus Swamp x3 and Mountain x2 only other repeats; singleton/deck-construction, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Sauron, the Dark Lord candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 91 distinct names, 34 lands; Nazgûl x7 permitted by card-specific deck-construction text plus Swamp x3 and Mountain x2 only other repeats; singleton/deck-construction/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Amass Orcs / Ring Temptation / Wraiths. 99-slot audit: 91 KEEP / 8 CUT. Great Goblin/Roaming Throne/Minas Morgul review, mana-base red team, Ring/Nazgûl preservation, candidate exhaustion, and zero-new-material-improvement closure PASS. Next unlocked: Sedris, the Traitor King (index 50 / deck 51 of 62)."
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Sauron the Dark Lord tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Sauron, the Dark Lord approval finalized.")
