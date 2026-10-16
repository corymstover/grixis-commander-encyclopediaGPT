from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
CANDIDATE = ROOT / "refinement/decklists/Zevlor_Elturel_Exile_Approval_Candidate_2026-10-15.txt"
APPROVED = ROOT / "refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt"
APPROVAL_RECORD = ROOT / "refinement/approvals/Zevlor_Elturel_Exile_Approved_2026-10-15.md"

EXPECTED_SHA = "d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9"
DECK_KEY = "Zevlor__Elturel_Exile"
DATE = "2026-10-15"
QUALITY_GATE = "Deck Quality Gates v3 + mandatory whole-list audit"

candidate_bytes = CANDIDATE.read_bytes()
actual_sha = hashlib.sha256(candidate_bytes).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Candidate SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")

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
        "Explicit user approval of the exact SHA-bound Zevlor, Elturel Exile approval-ready candidate after authoritative FINAL2 baseline reconciliation, mandatory 99-slot whole-list audit, commander-first targeted-spell/copy/theft-control review, correction to Zevlor's current Oracle single-target restriction, activation/untap sequencing verification, candidate exhaustion, adversarial Oracle/rules/combo and mana-base red-team, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality verification."
    ),
    "whole_list_audit_artifact": "refinement/decisions/Zevlor_Elturel_Exile_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Zevlor_Elturel_Exile_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt",
}
STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with TRACKER.open("r", encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fieldnames = reader.fieldnames
    if not fieldnames:
        raise SystemExit("Tracker has no header")
    rows = list(reader)

found = False
for row in rows:
    if row["deck_id"] != DECK_KEY:
        continue
    found = True
    row["baseline_status"] = "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged."
    row["fresh_oracle_identity_check"] = "PASS — current-cycle Oracle/color-identity verification completed for the exact SHA-bound Zevlor, Elturel Exile candidate; U/B/R identity PASS with zero unresolved candidate issues."
    row["fresh_official_legality_check"] = "PASS — exact SHA-bound Zevlor candidate verified against current official Commander legality on 2026-10-15; no project exception required."
    row["official_named_ban_list_checkpoint"] = "PASS — current official Commander legality/banned-list checkpoint complete; no unexpected banned cards and no project exception required."
    row["commander_blueprint_complete"] = "PASS — commander-first Targeted Spells / Spell Copy / Theft-Control blueprint finalized at Power Bracket 4 — Optimized, centered on Zevlor's single-target opponent/permanent restriction and repeatable activation infrastructure."
    row["high_impact_candidate_triage_complete"] = "PASS — project top-100 candidates plus meaningful outside-ranked challengers exhausted; final adversarial pass incorporated Pemmin's Aura and completed the usable fetchland suite, then produced ZERO NEW MATERIAL IMPROVEMENTS."
    row["swap_decision_ledger_complete"] = "PASS — 99/99 noncommander copies adjudicated at 78 KEEP / 21 CUT; exact 21-cut / 21-add SHA-bound candidate explicitly approved by user on 2026-10-15."
    row["combo_rules_interactions_verified"] = "PASS — Zevlor's corrected 'targets only a single opponent or a single permanent an opponent controls' Oracle restriction, copied delayed triggers, Illusionist's Bracers, Training Grounds, Omen Hawker, Patriar's Seal, Minamo, Pemmin's Aura, Twinning Staff, Cruel Ultimatum, Great Intelligence's Plan, Portent, Acquire, River's Rebuke, Jeska's Will, Rakdos Charm, Cyclonic Rift overload, modes, X values and copied-spell not-cast behavior reviewed."
    row["consistency_test_complete"] = "PASS — exact approved artifact verified at 100 cards / 97 distinct names / 34 lands; only Island x2, Mountain x2 and Swamp x2 repeat; singleton, U/B/R identity and candidate/approved SHA match PASS."
    row["multiplayer_test_complete_or_reason_not_applicable"] = "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling and strategic verification passed; no unsupported gameplay win-rate claim is made."
    row["final_gate_passed"] = "YES"
    row["final_list_hash"] = EXPECTED_SHA
    row["user_approval_date"] = DATE
    row["refinement_status"] = "APPROVED / LOCKED — current global-restart-2026-10-13 cycle"
    row["notes"] = (
        "CURRENT-CYCLE RECONCILIATION 2026-10-15: exact SHA-bound Zevlor, Elturel Exile approval candidate explicitly approved and locked. Canonical hash: "
        + EXPECTED_SHA
        + ". Final candidate: 100 cards, 97 distinct names, 34 lands; only Island x2, Mountain x2 and Swamp x2 repeat; singleton PASS; U/B/R identity PASS; rules/combo PASS; current official Commander legality PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Targeted Spells / Spell Copy / Theft-Control. Mandatory 99-slot audit completed at 78 KEEP / 21 CUT. Candidate exhaustion, commander-necessity/differentiation, adversarial Oracle/rules/combo and mana-base red-team, and zero-new-material-improvement closure all PASS. Frozen source exports remain historical baseline evidence. This is deck 62 of 62; the global-restart-2026-10-13 refinement cycle is complete."
    )

if not found:
    raise SystemExit("Zevlor tracker row not found")

with TRACKER.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

approval_record = f"""# Zevlor, Elturel Exile — APPROVED / LOCKED — 2026-10-15

- Cycle: `global-restart-2026-10-13`
- Tracker position: index 61 / deck 62 of 62
- Approval status: **APPROVED**
- Lock status: **LOCKED**
- Final gate passed: **true**
- User approval date: **2026-10-15**
- Quality gate: `{QUALITY_GATE}`
- Canonical SHA-256: `{EXPECTED_SHA}`
- Approved list: `refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt`
- Whole-list audit: `refinement/decisions/Zevlor_Elturel_Exile_Whole_List_Audit_2026-10-15.csv`
- Candidate decisions: `refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md`
- Verification: `refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`

The approved artifact is byte-identical to the SHA-bound approval candidate. Structural closeout: 100 cards, 97 distinct names, 34 lands, only basic-land repetitions, singleton PASS, U/B/R color identity PASS, relevant rules/combo PASS, current official Commander legality PASS, no project exception required, mandatory 99-slot audit PASS at 78 KEEP / 21 CUT, candidate exhaustion PASS, adversarial red-team PASS, and zero-new-material-improvement closure PASS.

This approval completes the `global-restart-2026-10-13` refinement cycle at **62/62 APPROVED / LOCKED**.
"""
APPROVAL_RECORD.parent.mkdir(parents=True, exist_ok=True)
APPROVAL_RECORD.write_text(approval_record, encoding="utf-8")

if hashlib.sha256(APPROVED.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved artifact changed during finalization")

locked_count = sum(
    1
    for d in state.get("decks", {}).values()
    if d.get("approval_status") == "APPROVED" and d.get("lock_status") == "LOCKED"
)
if locked_count != 62:
    raise SystemExit(f"Expected 62 locked decks after Zevlor approval, found {locked_count}")

print(f"APPROVED_LOCKED {DECK_KEY} {EXPECTED_SHA} LOCKED_COUNT={locked_count}")
