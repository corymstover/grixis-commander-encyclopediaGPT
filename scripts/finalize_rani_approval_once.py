import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "The_Rani"

candidate = Path("refinement/decklists/The_Rani_Approval_Candidate_2026-10-15.txt")
approved = Path("refinement/decklists/The_Rani_Approved_2026-10-15.txt")
verification = Path("refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md")
approval_record = Path("refinement/approvals/The_Rani_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"The Rani candidate SHA mismatch: {actual_sha}")
if not approved.exists() or approved.read_bytes() != raw:
    raise SystemExit("Approved The Rani artifact is missing or does not byte-match candidate")

verification_text = verification.read_text(encoding="utf-8")
required = [
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    EXPECTED_SHA,
    "Cards: **100**",
    "Distinct names: **94**",
    "Singleton: **PASS**",
    "Commander color identity: **U/B/R — PASS**",
    "Official Commander legality: **PASS**",
    "Project exceptions: **none**",
    "Rules-interaction attestation: **PASS**",
    "91 KEEP / 8 CUT",
    "ZERO NEW MATERIAL IMPROVEMENTS",
]
missing = [x for x in required if x not in verification_text]
if missing:
    raise SystemExit(f"The Rani verification artifact missing gate evidence: {missing}")

approval_text = approval_record.read_text(encoding="utf-8")
if "APPROVED / LOCKED" not in approval_text or EXPECTED_SHA not in approval_text:
    raise SystemExit("The Rani approval record is not bound to the approved SHA")

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
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound The Rani approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first goad/Clue/forced-combat review, candidate exhaustion, adversarial red-team review, mana-base review, fresh Oracle/color-identity verification, current official Commander legality verification, rules-interaction verification, exact structural verification, singleton verification, and zero-new-material-improvement closure.",
    "verification_artifact": "refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/The_Rani_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/The_Rani_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — fresh current-cycle Oracle resolution completed for the exact SHA-bound The Rani candidate; U/B/R identity PASS with zero unresolved candidate issues.",
    "fresh_official_legality_check": "PASS — exact SHA-bound The Rani candidate verified against current official Commander legality; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint complete; no unexpected banned cards and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first Goad / Clues / Forced Combat blueprint and mandatory 99-slot whole-list audit completed 2026-10-15.",
    "high_impact_candidate_triage_complete": "PASS — project rankings, commander-specific goad/Clue engines, protection, mana-base challengers, candidate exhaustion and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — exact SHA-bound eight-swap The Rani approval candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Rani Mark/goad/investigate engine, Thassa/Displacer Kitten blink, Baeloth/Mark power threshold, Impetus package, Academy Manufactor/Erdwal Illuminator token replacement, Time Sieve artifact conversion, and relevant protection interactions reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 94 distinct names / 33 lands; only basic lands repeat; candidate and approved artifact byte-match SHA.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, and strategic verification passed; no gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound The Rani approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 94 distinct names, 33 lands; singleton PASS with basic lands only repeated; B/R/U identity PASS; rules PASS; current official Commander legality PASS; no project exceptions; 99/99 noncommander slots adjudicated; 91 KEEP / 8 CUT; candidate exhaustion returned ZERO NEW MATERIAL IMPROVEMENTS. Natural ceiling: Bracket 4 — Optimized. Archidekt tags: Goad / Clues / Forced Combat. Next deck after this approval was The Valeyard, now separately approved and locked; current next unlocked deck is Thraximundar.",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("The Rani tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
print("The Rani approval state and tracker row reconciled.")
