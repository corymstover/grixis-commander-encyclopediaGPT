import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

EXPECTED_SHA = "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Sedris__the_Traitor_King"
NAME = "Sedris, the Traitor King"

candidate = Path("refinement/decklists/Sedris_the_Traitor_King_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Sedris_the_Traitor_King_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md")
gate_path = Path("refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_2026-10-15_Complete_Gate.json")
approval_record = Path("refinement/approvals/Sedris_the_Traitor_King_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Sedris candidate SHA mismatch: {actual_sha}")

lines = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
if not lines or lines[0] != "1x Sedris, the Traitor King [Commander]":
    raise SystemExit("Sedris commander-first line mismatch")

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
if len(set(names)) != 99:
    raise SystemExit(f"Candidate must contain 99 distinct names; found {len(set(names))}")

counts = Counter(names)
repeats = {k: v for k, v in counts.items() if v > 1}
if repeats != {"Swamp": 2}:
    raise SystemExit(f"Unexpected repeated names: {repeats}")

verification = verification_path.read_text(encoding="utf-8")
for bit in [
    EXPECTED_SHA,
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    "99/99 noncommander copies adjudicated; 91 KEEP / 8 CUT",
    "ZERO NEW MATERIAL IMPROVEMENTS",
    "Power Bracket 4 — Optimized",
    "Project exceptions: **none**",
    "Lands: **31**",
]:
    if bit not in verification:
        raise SystemExit(f"Verification missing required evidence: {bit}")

audit = audit_path.read_text(encoding="utf-8")
for bit in [EXPECTED_SHA, "99/99", "91 KEEP / 8 CUT", "31 lands"]:
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
if gate.get("count") != 100 or gate.get("distinct_names") != 99:
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
    "The user explicitly approved the exact SHA-bound approval-ready Sedris candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first unearth/reanimator review, candidate exhaustion, adversarial red-team review, graveyard-resource and mana-base review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton verification, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 99 distinct names, 31 lands, with Swamp x2 as the only repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Unearth / Reanimator / End-Step Control.\n\n"
    "This approval freezes `refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
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
        "- Exact approved artifact: `refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Sol'kanar the Swamp King (index 51 / deck 52 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Sedris approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Sedris, the Traitor King approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first unearth/reanimator review, candidate exhaustion, adversarial red-team review, graveyard-resource and mana-base review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton verification, and U/B/R color-identity verification.",
    "whole_list_audit_artifact": "refinement/verification/Sedris_the_Traitor_King_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Sedris_the_Traitor_King_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt"
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Sedris candidate verified at 100 cards / 99 distinct names within U/B/R; Swamp x2 is the only repeat.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — Sedris unearth / reanimator / end-step-control blueprint finalized at Power Bracket 4 — Optimized; commander-granted unearth and graveyard-to-battlefield ETB value remain primary identity.",
    "high_impact_candidate_triage_complete": "PASS — graveyard setup, rescue-density, fast-mana/protection, current-card challenger, mana-base, and generic-combo red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 91 KEEP / 8 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Sedris-granted unearth; Convergence one-mana floor; Obeka/Sundial timing; Teferi's Veil phasing; Deadeye rescue; River Kelpie; Twilight Diviner; Ripples of Undeath; Deadeye + Peregrine Drake; Panharmonicon; Grim Monolith role; Undercity Sewers reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 99 distinct names / 31 lands; Swamp x2 only repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Sedris, the Traitor King candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 99 distinct names, 31 lands; Swamp x2 only repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Unearth / Reanimator / End-Step Control. 99-slot audit: 91 KEEP / 8 CUT. Graveyard-resource review, rescue-density check, mana-base red team, candidate exhaustion, and zero-new-material-improvement closure PASS. Next unlocked: Sol'kanar the Swamp King (index 51 / deck 52 of 62)."
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Sedris tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Sedris, the Traitor King approval finalized.")
