import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-14"
DECK_ID = "Mairsil__the_Pretender"

approved = Path("refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt")
verification = Path("refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = approved.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Mairsil approved-list SHA mismatch: {actual_sha}")
lines = [line for line in raw.decode("utf-8").splitlines() if line.strip()]
if len(lines) != 100 or len(set(lines)) != 100:
    raise SystemExit("Mairsil approved artifact is not 100 unique source lines")
if lines[0] != "1x Mairsil, the Pretender [Commander]":
    raise SystemExit("Mairsil commander line mismatch")

verify_text = verification.read_text(encoding="utf-8")
for token in [
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    "Whole-list audit complete: PASS",
    "Candidate exhaustion: PASS",
    "Red-team pass: PASS",
    "Zero-new-material-improvement closure: PASS",
    "Official Commander legality: PASS",
    EXPECTED_SHA,
]:
    if token not in verify_text:
        raise SystemExit(f"Mairsil verification missing required token: {token}")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
state.setdefault("decks", {})[DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit",
    "approval_basis": "Explicit user approval of the exact SHA-bound Mairsil, the Pretender approval candidate after authoritative baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, adversarial red-team review, correction retaining Rings of Brighthearth over Reanimate, zero-new-material-improvement closure, Oracle/rules verification, current official Commander legality verification, singleton/color-identity verification, and exact 100-card structural verification.",
    "whole_list_audit_artifact": "refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv",
    "verification_artifact": "refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md",
    "decision_closeout_artifact": "refinement/decisions/Mairsil_the_Pretender_Current_Cycle_Decisions_2026-10-14.md",
    "approval_record_artifact": "refinement/approvals/Mairsil_the_Pretender_Approved_2026-10-14.md",
    "approved_list_artifact": "refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt",
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
    "commander_blueprint_complete": "PASS — current-cycle commander-first cage / activated-ability blueprint and mandatory 99-slot whole-list audit completed 2026-10-14.",
    "high_impact_candidate_triage_complete": "PASS — project top-100 candidates, stale-audit alternatives, current commander evidence, blink/copy engines, activated-ability payloads, mana-base alternatives, and adversarial challengers exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — exact six-swap SHA-bound Mairsil approval candidate explicitly approved by user on 2026-10-14.",
    "combo_rules_interactions_verified": "PASS — Mairsil cage ETBs, Pack Rat self-copy, Rings copied activations, blink/new-object behavior, Spark Double copy behavior, Asmodeus static-vs-activated distinction, Marvin static-vs-activated distinction, Quicksilver Elemental engines, and Mirror-Mad danger reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 100 distinct names / 32 lands; singleton compliance and commander-first strategic coherence verified.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Mairsil, the Pretender approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 100 distinct names, 32 lands; B/R/U identity PASS; current official Commander legality PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Approved changes: Puppet Strings -> Pack Rat; Underworld Breach -> Faithless Looting; Animate Dead -> Essence Flux; Mirror-Mad Phantasm -> Displacer Kitten; Reanimate -> Spark Double; Fabled Passage -> Minamo, School at Water's Edge. Mandatory whole-list audit, candidate exhaustion, adversarial red-team review, zero-new-material-improvement closure, and structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Marchesa, Dealer of Death.",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Mairsil tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["final_gate_passed"] is True
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert reread["quality_gate_version"] == "Deck Quality Gates v3 + mandatory whole-list audit"
print("Mairsil, the Pretender approval finalized.")
