import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Marchesa__Dealer_of_Death"

candidate = Path("refinement/decklists/Marchesa_Dealer_of_Death_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt")
audit_path = Path("refinement/decisions/Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv")
verification_path = Path("refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Marchesa_Dealer_of_Death_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Marchesa candidate SHA mismatch: {actual_sha}")

if not approved.exists() or approved.read_bytes() != raw:
    raise SystemExit("Approved Marchesa artifact is missing or not byte-identical to candidate")
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Marchesa artifact SHA mismatch")

with audit_path.open("r", encoding="utf-8", newline="") as fh:
    audit_rows = list(csv.DictReader(fh))
if len(audit_rows) != 99:
    raise SystemExit(f"Marchesa whole-list audit must contain 99 noncommander rows; found {len(audit_rows)}")
if len({row.get("card", "") for row in audit_rows}) != 99:
    raise SystemExit("Marchesa whole-list audit contains duplicate or blank card rows")
if any(row.get("decision") not in {"KEEP", "CUT"} for row in audit_rows):
    raise SystemExit("Marchesa whole-list audit contains unresolved decisions")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Marchesa approval-ready verification is not bound to the approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Marchesa verification lacks zero-new-material-improvement closure")

if not decision_path.exists() or "APPROVED / LOCKED" not in decision_path.read_text(encoding="utf-8"):
    raise SystemExit("Marchesa decision closeout does not record explicit approval")
if not approval_record.exists() or EXPECTED_SHA not in approval_record.read_text(encoding="utf-8"):
    raise SystemExit("Marchesa approval record missing or SHA mismatch")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Marchesa approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Marchesa, Dealer of Death approval candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, contemporary cEDH ceiling review, candidate exhaustion, adversarial red-team review, zero-new-material-improvement closure, relevant Oracle/rules/combo verification, current official Commander legality checkpoint, singleton/color-identity verification, and exact 100-card structural verification.",
    "whole_list_audit_artifact": "refinement/decisions/Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Marchesa_Dealer_of_Death_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — current-cycle Marchesa approval-ready verification completed 2026-10-15; exact SHA-bound candidate verified at 100 cards / 100 distinct names within B/R/U color identity with no unresolved identity issue.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Marchesa candidate checked against current official Commander legality on 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander banned-list checkpoint completed 2026-10-15; no candidate card unexpectedly banned and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first crimes / control / storm cEDH blueprint completed; Marchesa is the primary selection/graveyard engine and targeted interaction/repeatable abilities supply crime density.",
    "high_impact_candidate_triage_complete": "PASS — project top-100 candidates, current competitive Marchesa configurations, repeatable crime engines, interaction replacements, mana-base challengers, and generic cEDH staples exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — all 99 baseline noncommander slots adjudicated; exact 48-cut / 48-add rebuild and SHA-bound candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — relevant Marchesa crime targeting, Aphetto Alchemist + Hawkeye's Bow, Spatial Binding, Hex Parasite X=0 targeting, Spellskite targeting, Tezzeret/Displacer Kitten, Urborg/Hammerheim/Talon Gates utility crimes, Lapis Lazuli Talisman + Bender's Waterskin, Tainted Pact + Thassa's Oracle, and Breach/LED/Brain Freeze interactions reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 100 distinct names / 29 lands; singleton and B/R/U color-identity checks PASS; approved artifact is byte-identical to SHA-bound candidate.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, tournament-ceiling, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Marchesa, Dealer of Death approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 100 distinct names, 29 lands; B/R/U identity PASS; relevant rules/combo review PASS; current official Commander legality checkpoint PASS; no project exceptions. Natural ceiling: Power Bracket 5 — cEDH. Archidekt tags: Crimes / Control / Storm. Current cycle uses a 48-card rebuild from the frozen FINAL baseline, matching the selected 2026-10-11 Takeda Ryuhei tournament-winning configuration while preserving Marchesa as the primary crime-selection/graveyard engine. Mandatory 99-slot audit, candidate exhaustion, adversarial red-team, zero-new-material-improvement closure, Oracle/rules/legality checks, singleton/color identity, and exact 100-card verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Marchesa, the Black Rose (index 34 / deck 35 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Marchesa tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Marchesa, Dealer of Death approval finalized.")
