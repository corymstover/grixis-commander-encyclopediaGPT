from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
CANDIDATE = ROOT / "refinement/decklists/Tresserhorn_s_Lord_Returned_Approval_Candidate_2026-10-15.txt"
APPROVED = ROOT / "refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt"
APPROVAL_RECORD = ROOT / "refinement/approvals/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md"

EXPECTED_SHA = "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8"
DECK_KEY = "Tresserhorn_s_Lord__Returned"
DATE = "2026-10-15"
QUALITY_GATE = "Deck Quality Gates v3 + mandatory whole-list audit"

candidate_bytes = CANDIDATE.read_bytes()
actual_sha = hashlib.sha256(candidate_bytes).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Candidate SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")

# Freeze the exact approved bytes.
APPROVED.write_bytes(candidate_bytes)

state = json.loads(STATE.read_text(encoding="utf-8"))
if state.get("cycle_id") != "global-restart-2026-10-13":
    raise SystemExit(f"Unexpected cycle_id: {state.get('cycle_id')}")

state.setdefault("decks", {})[DECK_KEY] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": QUALITY_GATE,
    "approval_basis": (
        "Explicit user approval of the exact SHA-bound Tresserhorn's Lord, Returned approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity and encyclopedia-differentiation review, adversarial Oracle/rules/combo and mana-base red-team, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, current official Commander legality verification, and correction of the obsolete future-release exception following official 2026-08-03 Commander legality."
    ),
    "whole_list_audit_artifact": "refinement/decisions/Tresserhorn_s_Lord_Returned_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt",
}
STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with TRACKER.open("r", encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fieldnames = reader.fieldnames
    if not fieldnames:
        raise SystemExit("Tracker has no header")
    rows = list(reader)

found_tresserhorn = False
found_thraximundar = False
for row in rows:
    if row["deck_id"] == DECK_KEY:
        found_tresserhorn = True
        row["baseline_status"] = "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged."
        row["fresh_oracle_identity_check"] = "PASS — current-cycle Oracle/color-identity verification completed for the exact SHA-bound Tresserhorn's Lord, Returned candidate; U/B/R identity PASS with zero unresolved candidate issues."
        row["fresh_official_legality_check"] = "PASS — exact SHA-bound candidate verified against current official Commander legality on 2026-10-15; prior future-release exception is obsolete because Wizards made Mystery Booster Commander Edition collector numbers 1–60 Commander-legal on 2026-08-03."
        row["official_named_ban_list_checkpoint"] = "PASS — current official Commander legality/banned-list checkpoint complete; no unexpected banned cards and no project exception required."
        row["commander_blueprint_complete"] = "PASS — commander-first Aristocrats / Sacrifice / Tokens blueprint finalized at Power Bracket 4 — Optimized; Returned intentionally exploits rather than suppresses its three-creature ETB sacrifice requirement."
        row["high_impact_candidate_triage_complete"] = "PASS — project top-100 candidates plus meaningful outside-ranked challengers exhausted; final serious adversarial pass produced ZERO NEW MATERIAL IMPROVEMENTS."
        row["swap_decision_ledger_complete"] = "PASS — 99/99 noncommander copies adjudicated at 80 KEEP / 19 CUT; exact 19-cut / 19-add SHA-bound candidate explicitly approved by user on 2026-10-15."
        row["combo_rules_interactions_verified"] = "PASS — Tresserhorn ETB sacrifice triggers, Gravecrawler/Phyrexian Altar, Gravecrawler/Pitiless Plunderer, Warren Soultrader life-neutralization requirement, Locust God loop, Plumb the Forbidden draw arithmetic, Blasphemous Edict simultaneous sacrifices, Infantry Shield, Wand of Orcus, Nightscape Familiar, Not of This World and My Precious interactions reviewed."
        row["consistency_test_complete"] = "PASS — exact approved artifact verified at 100 cards / 93 distinct names / 34 land-capable slots; only Island x3, Mountain x3 and Swamp x4 repeat; singleton and U/B/R color identity PASS."
        row["multiplayer_test_complete_or_reason_not_applicable"] = "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling and strategic verification passed; no unsupported gameplay win-rate claim is made."
        row["final_gate_passed"] = "YES"
        row["final_list_hash"] = EXPECTED_SHA
        row["user_approval_date"] = DATE
        row["refinement_status"] = "APPROVED / LOCKED — current global-restart-2026-10-13 cycle"
        row["notes"] = (
            "CURRENT-CYCLE RECONCILIATION 2026-10-15: exact SHA-bound Tresserhorn's Lord, Returned approval candidate explicitly approved and locked. Canonical hash: "
            + EXPECTED_SHA
            + ". Final candidate: 100 cards, 93 distinct names, 34 land-capable slots; only Island x3, Mountain x3 and Swamp x4 repeat; singleton PASS; U/B/R identity PASS; rules/combo PASS; current official Commander legality PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Aristocrats / Sacrifice / Tokens. Mandatory 99-slot audit completed at 80 KEEP / 19 CUT. Candidate exhaustion, commander-necessity/differentiation, adversarial red-team, zero-new-material-improvement closure and exact structural verification all PASS. The former future-release exception is obsolete following official Mystery Booster Commander Edition legality on 2026-08-03. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Wick, the Whorled Mind (index 60 / deck 61 of 62)."
        )

    # Repair the stale tracker status discovered during recovery; state JSON was already authoritative.
    if row["deck_id"] == "Thraximundar":
        found_thraximundar = True
        thrax = state["decks"].get("Thraximundar")
        if not thrax or thrax.get("approval_status") != "APPROVED" or thrax.get("lock_status") != "LOCKED":
            raise SystemExit("Authoritative Thraximundar state is not APPROVED/LOCKED")
        row["baseline_status"] = "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged."
        row["final_gate_passed"] = "YES"
        row["final_list_hash"] = thrax["approved_list_sha256"]
        row["user_approval_date"] = thrax["user_approval_date"]
        row["refinement_status"] = "APPROVED / LOCKED — current global-restart-2026-10-13 cycle"
        marker = "CURRENT-CYCLE RECONCILIATION 2026-10-15: authoritative state/current_deck_overrides.json records Thraximundar APPROVED and LOCKED"
        if marker not in (row.get("notes") or ""):
            row["notes"] = (row.get("notes") or "").rstrip() + (" " if row.get("notes") else "") + marker + f" with canonical SHA-256 {thrax['approved_list_sha256']}. Tracker stale unlocked status corrected; approved decklist unchanged."

if not found_tresserhorn:
    raise SystemExit("Tresserhorn tracker row not found")
if not found_thraximundar:
    raise SystemExit("Thraximundar tracker row not found")

with TRACKER.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

approval_record = f"""# Tresserhorn's Lord, Returned — APPROVED / LOCKED — 2026-10-15

- Cycle: `global-restart-2026-10-13`
- Tracker position: index 59 / deck 60 of 62
- Approval status: **APPROVED**
- Lock status: **LOCKED**
- Final gate passed: **true**
- User approval date: **2026-10-15**
- Quality gate: `{QUALITY_GATE}`
- Canonical SHA-256: `{EXPECTED_SHA}`
- Approved list: `refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt`
- Whole-list audit: `refinement/decisions/Tresserhorn_s_Lord_Returned_Whole_List_Audit_2026-10-15.csv`
- Candidate decisions: `refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md`
- Verification: `refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`

The approved artifact is byte-identical to the SHA-bound approval candidate. Structural closeout: 100 cards, 93 distinct names, 34 land-capable slots, only basic-land repetitions, singleton PASS, U/B/R color identity PASS, relevant rules/combo PASS, current official Commander legality PASS, no project exception required, mandatory 99-slot audit PASS at 80 KEEP / 19 CUT, candidate exhaustion PASS, adversarial red-team PASS, and zero-new-material-improvement closure PASS.

The prior future-release exception for this commander is historical only: current official Mystery Booster Commander Edition legality applies.

Next unlocked deck in authoritative tracker order: **Wick, the Whorled Mind — deck 61 of 62**.
"""
APPROVAL_RECORD.parent.mkdir(parents=True, exist_ok=True)
APPROVAL_RECORD.write_text(approval_record, encoding="utf-8")

# Final local invariants.
if hashlib.sha256(APPROVED.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved artifact changed during finalization")

print(f"APPROVED_LOCKED {DECK_KEY} {EXPECTED_SHA}")
