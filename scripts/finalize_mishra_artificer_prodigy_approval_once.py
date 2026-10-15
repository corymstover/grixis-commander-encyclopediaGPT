import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Mishra__Artificer_Prodigy"

candidate = Path("refinement/decklists/Mishra_Artificer_Prodigy_Approval_Candidate_2026-10-15.txt")
approved = Path("refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt")
audit_path = Path("refinement/decisions/Mishra_Artificer_Prodigy_Whole_List_Audit_2026-10-15.csv")
verification_path = Path("refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Mishra_Artificer_Prodigy_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Mishra candidate SHA mismatch: {actual_sha}")

if not approved.exists() or approved.read_bytes() != raw:
    raise SystemExit("Approved Mishra artifact is missing or not byte-identical to candidate")
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Mishra artifact SHA mismatch")

with audit_path.open("r", encoding="utf-8", newline="") as fh:
    audit_rows = list(csv.DictReader(fh))
if len(audit_rows) != 99:
    raise SystemExit(f"Mishra whole-list audit must contain 99 noncommander rows; found {len(audit_rows)}")
if len({row.get("card_name", "") for row in audit_rows}) != 99:
    raise SystemExit("Mishra whole-list audit contains duplicate or blank card rows")
if any(row.get("decision") not in {"KEEP", "CUT"} for row in audit_rows):
    raise SystemExit("Mishra whole-list audit contains unresolved decisions")
if sum(row.get("decision") == "KEEP" for row in audit_rows) != 87 or sum(row.get("decision") == "CUT" for row in audit_rows) != 12:
    raise SystemExit("Mishra whole-list audit does not reconcile to 87 KEEP / 12 CUT")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Mishra approval-ready verification is not bound to the approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Mishra verification lacks zero-new-material-improvement closure")
if "100 cards" not in verification or "100" not in verification:
    raise SystemExit("Mishra verification lacks structural closeout")

if not decision_path.exists() or "APPROVED / LOCKED" not in decision_path.read_text(encoding="utf-8"):
    raise SystemExit("Mishra decision closeout does not record explicit approval")
if not approval_record.exists() or EXPECTED_SHA not in approval_record.read_text(encoding="utf-8"):
    raise SystemExit("Mishra approval record missing or SHA mismatch")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Mishra approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Mishra, Artificer Prodigy approval candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-identity review, adversarial rules/combo red-team, mana-base red-team, zero-new-material-improvement closure, exact structural verification, current Oracle/rules verification, singleton/color-identity verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/decisions/Mishra_Artificer_Prodigy_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Mishra_Artificer_Prodigy_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — current-cycle Mishra, Artificer Prodigy approval-ready verification completed 2026-10-15; exact SHA-bound candidate verified at 100 cards / 100 distinct names within U/B/R color identity.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Mishra candidate checked against current official Commander legality on 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint completed 2026-10-15; no unexpected banned card and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first artifact-spell parity-breaking stax-combo blueprint finalized at Power Bracket 5 — fringe cEDH; Mishra converts symmetrical counter/redirect effects into one-sided artifact deployment engines.",
    "high_impact_candidate_triage_complete": "PASS — project candidates, current optimized/cEDH Mishra evidence, parity-breaking counter engines, artifact tutors, stack interaction, fast mana, draw engines, mana-base challengers, and generic cEDH alternatives exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — all 99 baseline noncommander slots adjudicated at 87 KEEP / 12 CUT; exact 12-cut / 12-add SHA-bound candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Mishra cast-trigger timing with Blood Funnel, Nether Void, Nullstone Gargoyle, Chalice of the Void, Void Mirror, Vexing Bauble, Planar Chaos, and Possibility Storm verified; Uthros Research Craft station/draw interaction and retained Mystic Forge/Top/Aetherflux, Citadel/Top/Aetherflux, KCI recursion, Karn/Lattice, and Lattice/Vandalblast packages reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 100 distinct names / 29 lands; singleton, U/B/R color identity, and candidate/approved byte-match SHA checks PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Mishra, Artificer Prodigy approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 100 distinct names, 29 lands; singleton PASS; U/B/R identity PASS; current Oracle/rules/combo review PASS; current official Commander legality checkpoint PASS; no project exceptions. Natural ceiling: Power Bracket 5 — cEDH (fringe / commander-centric artifact stax-combo). Archidekt tags: Artifacts / Stax / Combo. Mandatory 99-slot audit completed at 87 KEEP / 12 CUT. Candidate exhaustion, adversarial red-team, parity-breaking rules verification, zero-new-material-improvement closure, and exact structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Mishra, Eminent One (index 36 / deck 37 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Mishra tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Mishra, Artificer Prodigy approval finalized.")
