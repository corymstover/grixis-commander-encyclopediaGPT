from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
CANDIDATE = ROOT / "refinement/decklists/Wick_the_Whorled_Mind_Approval_Candidate_2026-10-15.txt"
APPROVED = ROOT / "refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt"
APPROVAL_RECORD = ROOT / "refinement/approvals/Wick_the_Whorled_Mind_Approved_2026-10-15.md"

EXPECTED_SHA = "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98"
DECK_KEY = "Wick__the_Whorled_Mind"
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
    "approval_basis": "Explicit user approval of the exact SHA-bound Wick, the Whorled Mind approval-ready candidate after authoritative FINAL2 baseline reconciliation, mandatory 99-slot whole-list audit, commander-first Rat/Snail-counter/combo review, candidate exhaustion, adversarial Oracle/rules/combo and mana-base red-team, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality verification.",
    "whole_list_audit_artifact": "refinement/decisions/Wick_the_Whorled_Mind_Whole_List_Audit_2026-10-15.csv",
    "verification_artifact": "refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Wick_the_Whorled_Mind_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt",
}
STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with TRACKER.open("r", encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fieldnames = reader.fieldnames
    rows = list(reader)
if not fieldnames:
    raise SystemExit("Tracker has no header")
found = False
for row in rows:
    if row["deck_id"] == DECK_KEY:
        found = True
        row["baseline_status"] = "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged."
        row["fresh_oracle_identity_check"] = "PASS — current-cycle Oracle/color-identity verification completed for the exact SHA-bound Wick candidate; U/B/R identity PASS with zero unresolved candidate issues."
        row["fresh_official_legality_check"] = "PASS — exact SHA-bound Wick candidate verified against current official Commander legality on 2026-10-15; no project exception required."
        row["official_named_ban_list_checkpoint"] = "PASS — current official Commander legality/banned-list checkpoint complete; no unexpected banned cards and no project exception required."
        row["commander_blueprint_complete"] = "PASS — commander-first Rats / Snail Counters / Combo blueprint finalized at Power Bracket 4 — Optimized."
        row["high_impact_candidate_triage_complete"] = "PASS — project top-100 candidates plus meaningful outside-ranked challengers exhausted; final serious adversarial pass produced ZERO NEW MATERIAL IMPROVEMENTS."
        row["swap_decision_ledger_complete"] = "PASS — 99/99 noncommander copies adjudicated at 76 KEEP / 23 CUT; exact 23-cut / 23-add SHA-bound candidate explicitly approved by user on 2026-10-15."
        row["combo_rules_interactions_verified"] = "PASS — Wick damage-source/infect interaction, Arcane Adaptation/Leyline/Maskwood Rat-Snail loops, Marrow-Gnawer/Intruder Alarm, The Ozolith, Bulk Up, Blade of the Bloodchief, Song of Totentanz and relevant sacrifice-outlet lines reviewed."
        row["consistency_test_complete"] = "PASS — exact approved artifact verified at 100 cards / 99 distinct names / 36 land-capable slots; only Island x2 repeats; singleton and U/B/R color identity PASS."
        row["multiplayer_test_complete_or_reason_not_applicable"] = "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling and strategic verification passed; no unsupported gameplay win-rate claim is made."
        row["final_gate_passed"] = "YES"
        row["final_list_hash"] = EXPECTED_SHA
        row["user_approval_date"] = DATE
        row["refinement_status"] = "APPROVED / LOCKED — current global-restart-2026-10-13 cycle"
        row["notes"] = "CURRENT-CYCLE RECONCILIATION 2026-10-15: exact SHA-bound Wick, the Whorled Mind approval candidate explicitly approved and locked. Canonical hash: " + EXPECTED_SHA + ". Final candidate: 100 cards, 99 distinct names, 36 land-capable slots; only Island x2 repeats; singleton PASS; U/B/R identity PASS; rules/combo PASS; current official Commander legality PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Rats / Snail Counters / Combo. Mandatory 99-slot audit completed at 76 KEEP / 23 CUT. Candidate exhaustion, commander-necessity/differentiation, adversarial red-team, zero-new-material-improvement closure and exact structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Zevlor, Elturel Exile (index 61 / deck 62 of 62)."
if not found:
    raise SystemExit("Wick tracker row not found")
with TRACKER.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)

APPROVAL_RECORD.parent.mkdir(parents=True, exist_ok=True)
APPROVAL_RECORD.write_text(f"# Wick, the Whorled Mind — APPROVED / LOCKED — 2026-10-15\n\n- Cycle: `global-restart-2026-10-13`\n- Tracker position: index 60 / deck 61 of 62\n- Approval status: **APPROVED**\n- Lock status: **LOCKED**\n- Final gate passed: **true**\n- User approval date: **2026-10-15**\n- Quality gate: `{QUALITY_GATE}`\n- Canonical SHA-256: `{EXPECTED_SHA}`\n- Approved list: `refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt`\n\nThe approved artifact is byte-identical to the SHA-bound approval candidate. Structural closeout: 100 cards, 99 distinct names, 36 land-capable slots, only Island x2 repeated, singleton PASS, U/B/R color identity PASS, relevant rules/combo PASS, current official Commander legality PASS, no project exception required, mandatory 99-slot audit PASS at 76 KEEP / 23 CUT, candidate exhaustion PASS, adversarial red-team PASS, and zero-new-material-improvement closure PASS.\n\nNext unlocked deck: **Zevlor, Elturel Exile — deck 62 of 62**.\n", encoding="utf-8")
if hashlib.sha256(APPROVED.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved artifact changed during finalization")
print(f"APPROVED_LOCKED {DECK_KEY} {EXPECTED_SHA}")
