import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Marchesa__the_Black_Rose"

candidate = Path("refinement/decklists/Marchesa_the_Black_Rose_Approval_Candidate_2026-10-15.txt")
approved = Path("refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt")
audit_path = Path("refinement/decisions/Marchesa_the_Black_Rose_Whole_List_Audit_2026-10-15.csv")
verification_path = Path("refinement/verification/Marchesa_the_Black_Rose_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Marchesa_the_Black_Rose_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Marchesa the Black Rose candidate SHA mismatch: {actual_sha}")

if not approved.exists() or approved.read_bytes() != raw:
    raise SystemExit("Approved Marchesa the Black Rose artifact is missing or not byte-identical to candidate")
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Marchesa the Black Rose artifact SHA mismatch")

with audit_path.open("r", encoding="utf-8", newline="") as fh:
    audit_rows = list(csv.DictReader(fh))
if len(audit_rows) != 99:
    raise SystemExit(f"Marchesa the Black Rose whole-list audit must contain 99 noncommander rows; found {len(audit_rows)}")
if any(row.get("decision") not in {"KEEP", "CUT"} for row in audit_rows):
    raise SystemExit("Marchesa the Black Rose whole-list audit contains unresolved decisions")
if sum(row.get("decision") == "KEEP" for row in audit_rows) != 78:
    raise SystemExit("Marchesa the Black Rose KEEP count mismatch")
if sum(row.get("decision") == "CUT" for row in audit_rows) != 21:
    raise SystemExit("Marchesa the Black Rose CUT count mismatch")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Marchesa the Black Rose verification is not bound to the approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Marchesa the Black Rose verification lacks zero-new-material-improvement closure")
if "Total cards including commander: **100**" not in verification:
    raise SystemExit("Marchesa the Black Rose verification does not confirm 100 cards")

if not decision_path.exists() or "APPROVED / LOCKED" not in decision_path.read_text(encoding="utf-8"):
    raise SystemExit("Marchesa the Black Rose decision closeout does not record explicit approval")
if not approval_record.exists() or EXPECTED_SHA not in approval_record.read_text(encoding="utf-8"):
    raise SystemExit("Marchesa the Black Rose approval record missing or SHA mismatch")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Marchesa the Black Rose approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Marchesa, the Black Rose approval candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, adversarial red-team review, zero-new-material-improvement closure, structural verification, singleton/color-identity verification, current Oracle/rules/combo verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/decisions/Marchesa_the_Black_Rose_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Marchesa_the_Black_Rose_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Marchesa_the_Black_Rose_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — current-cycle Marchesa, the Black Rose approval-ready verification completed 2026-10-15; exact SHA-bound candidate verified at 100 cards / 98 distinct names within U/B/R color identity; only Island x2 and Swamp x2 repeat.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Marchesa, the Black Rose candidate checked against current official Commander legality on 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint completed 2026-10-15; no unexpected banned card and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first +1/+1-counter / sacrifice / death-ETB recursion engine finalized at Power Bracket 4 — Optimized; compact persist and Marchesa-native loops retained without generic Grixis homogenization.",
    "high_impact_candidate_triage_complete": "PASS — project candidates, current optimized Marchesa evidence, persist/counter engines, sacrifice outlets, draw engines, interaction, tutors, mana-base challengers, and final red-team corrections exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — all 99 baseline noncommander slots adjudicated at 78 KEEP / 21 CUT; exact 21-cut / 21-add SHA-bound candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Marchesa delayed end-step return timing, persist counter cancellation, Gev + Murderous Redcap, Spark Double + Murderous Redcap + Ashnod's Altar, Sage of Fables persist loops, Mikaeus + Yawgmoth + Gray Merchant package, Agatha's Soul Cauldron limits, Satoru noncast-entry draw, and Twilight Diviner graveyard-return interaction reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 34 lands / 98 distinct names; only basic lands repeat; singleton, U/B/R color identity, and candidate/approved byte-match SHA checks PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Marchesa, the Black Rose approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 34 lands, 98 distinct names; only Island x2 and Swamp x2 repeat; singleton PASS; U/B/R identity PASS; current Oracle/rules/combo review PASS; current official Commander legality checkpoint PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: +1/+1 Counters / Aristocrats / Combo. Mandatory 99-slot audit completed at 78 KEEP / 21 CUT. Candidate exhaustion, adversarial red-team, Gray Merchant/Ozolith retention correction, zero-new-material-improvement closure, and exact structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Mishra, Artificer Prodigy (index 35 / deck 36 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Marchesa the Black Rose tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Marchesa, the Black Rose approval finalized.")
