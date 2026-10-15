import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Missy"

candidate = Path("refinement/decklists/Missy_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Missy_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Missy_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Missy_Candidate_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Missy_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Missy candidate SHA mismatch: {actual_sha}")

verification = verification_path.read_text(encoding="utf-8")
for required in (EXPECTED_SHA, "APPROVAL_READY", "ZERO NEW MATERIAL IMPROVEMENTS", "100", "Singleton compliance: **PASS**"):
    if required not in verification:
        raise SystemExit(f"Missy verification missing required marker: {required}")

audit = audit_path.read_text(encoding="utf-8")
for required in ("99/99", "83 KEEP / 16 CUT"):
    if required not in audit:
        raise SystemExit(f"Missy whole-list audit missing required marker: {required}")

# Freeze exact approval-ready bytes as the canonical approved artifact.
approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Missy artifact SHA mismatch")

# Convert the working decision record into an explicit approval closeout without changing its decisions.
decision = decision_path.read_text(encoding="utf-8")
decision = decision.replace("Status: working decision closeout; not user approval", "Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15")
if "## Approval closeout" not in decision:
    decision += f"\n## Approval closeout\n\n- Explicit user approval received: **{DATE}**\n- Canonical approved SHA-256: `{EXPECTED_SHA}`\n- Exact approved artifact: `refinement/decklists/Missy_Approved_2026-10-15.txt`\n- Current-cycle state: **APPROVED / LOCKED**\n- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit**\n- Next unlocked deck in tracker order: **Nathan Drake, Treasure Hunter (index 38 / deck 39 of 62)**.\n"
decision_path.write_text(decision, encoding="utf-8")

approval_record.parent.mkdir(parents=True, exist_ok=True)
approval_record.write_text(
    "# Missy — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready Missy candidate after the mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/combo review, mana/curve review, zero-new-material-improvement closure, exact 100-card verification, singleton/color-identity verification, and current Commander legality checkpoint all passed.\n\n"
    "Approved structure: 100 cards, 97 distinct names, 35 lands; only Island x2 and Swamp x3 repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Cybermen / Morph / Aristocrats.\n\n"
    "This approval freezes `refinement/decklists/Missy_Approved_2026-10-15.txt` as the current-cycle canonical Missy list.\n",
    encoding="utf-8",
)

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Missy approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit",
    "approval_basis": "Explicit user approval of the exact SHA-bound Missy approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/combo red-team, mana/curve red-team, zero-new-material-improvement closure, exact 100-card structural verification, singleton/color-identity verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/verification/Missy_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Missy_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Missy_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Missy_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — current-cycle Missy approval-ready verification completed 2026-10-15; exact SHA-bound candidate verified at 100 cards / 97 distinct names within U/B/R color identity; only Island x2 and Swamp x3 repeat.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Missy candidate checked against current official Commander legality on 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint completed 2026-10-15; no unexpected banned card and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first Cyberman / morph / aristocrats blueprint completed at Power Bracket 4 — Optimized; Missy is the recursion, theft/conversion, face-down, and villainous-choice engine.",
    "high_impact_candidate_triage_complete": "PASS — project top-100 candidates, current Missy evidence, free reveal-morph loops, sacrifice outlets, face-down engines, Cyberman payoffs, mana-base challengers, and generic Grixis alternatives exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — all 99 baseline noncommander slots adjudicated at 83 KEEP / 16 CUT; exact 16-cut / 16-add SHA-bound candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Missy face-down return rules; Ruthless Ripper, Dragon's Eye Savants, and Horde Ambusher sacrifice loops; Ixidron anti-synergy correction; The Valeyard villainous-choice multiplication; Ugin's Mastery face-down cast interaction; Panoptic Projektor limitations/payoffs; Cybership Cyberman theft; and relevant sacrifice-outlet lines reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 97 distinct names / 35 lands; only Island x2 and Swamp x3 repeat; singleton, U/B/R color identity, and candidate/approved byte-match SHA checks PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Missy approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 97 distinct names, 35 lands; only Island x2 and Swamp x3 repeat; singleton PASS; U/B/R identity PASS; current Oracle/rules/combo review PASS; current official Commander legality checkpoint PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Cybermen / Morph / Aristocrats. Mandatory 99-slot audit completed at 83 KEEP / 16 CUT. Candidate exhaustion, adversarial red-team, commander-native recursion/combo verification, zero-new-material-improvement closure, and exact structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Nathan Drake, Treasure Hunter (index 38 / deck 39 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Missy tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["final_gate_passed"] is True
assert reread["current_stage"] == "LOCKED"
assert reread["quality_gate_version"] == "Deck Quality Gates v3 + mandatory whole-list audit"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Missy approval finalized.")
