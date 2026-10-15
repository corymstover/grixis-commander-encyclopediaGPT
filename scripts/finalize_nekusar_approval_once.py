import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Nekusar__the_Mindrazer"

candidate = Path("refinement/decklists/Nekusar_the_Mindrazer_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Nekusar_the_Mindrazer_Candidate_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Nekusar_the_Mindrazer_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Nekusar candidate SHA mismatch: {actual_sha}")

lines = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
card_total = 0
names = []
for line in lines:
    qty_text, name = line.split("x ", 1)
    qty = int(qty_text)
    card_total += qty
    clean_name = name.replace(" [Commander]", "")
    names.extend([clean_name] * qty)
if card_total != 100:
    raise SystemExit(f"Nekusar candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 97:
    raise SystemExit(f"Nekusar candidate must contain 97 distinct names; found {len(set(names))}")
if lines[0] != "1x Nekusar, the Mindrazer [Commander]":
    raise SystemExit("Nekusar commander line mismatch")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Nekusar verification is not bound to the approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Nekusar verification lacks zero-new-material-improvement closure")
if "Power Bracket 4 — Optimized" not in verification:
    raise SystemExit("Nekusar natural power ceiling gate is missing")

audit = audit_path.read_text(encoding="utf-8")
if "99/99" not in audit or "82 KEEP / 17 CUT" not in audit:
    raise SystemExit("Nekusar mandatory whole-list audit is incomplete")
if EXPECTED_SHA not in audit:
    raise SystemExit("Nekusar audit SHA mismatch")

decision = decision_path.read_text(encoding="utf-8")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision:
    raise SystemExit("Nekusar decision closeout lacks candidate-exhaustion closure")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Nekusar artifact SHA mismatch")

approval_record.write_text(
    "# Nekusar, the Mindrazer — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound Nekusar, the Mindrazer approval-ready candidate after authoritative FINAL baseline reconciliation, the mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/trigger-arithmetic review, Ghyrson/Solphim red-team correction, mana-base red team, zero-new-material-improvement closure, exact 100-card verification, singleton/color-identity verification, and current Commander legality checkpoint all passed.\n\n"
    "Approved structure: 100 cards, 97 distinct names, 35 lands; only Island x2, Mountain x2, and Swamp x2 repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Wheels / Draw Punishment / Group Slug.\n\n"
    "This approval freezes `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt` as the current-cycle canonical Nekusar list.\n",
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
        "- Exact approved artifact: `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Nicol Bolas (index 40 / deck 41 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Nekusar approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Nekusar, the Mindrazer approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/trigger-arithmetic red-team, Ghyrson/Solphim correction, mana-base red-team, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/verification/Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Nekusar_the_Mindrazer_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Nekusar_the_Mindrazer_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — current-cycle Nekusar approval-ready verification completed 2026-10-15; exact SHA-bound candidate verified at 100 cards / 97 distinct names within U/B/R color identity; only Island x2, Mountain x2, and Swamp x2 repeat.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Nekusar candidate checked against current official Commander legality on 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint completed 2026-10-15; no unexpected banned card and no project exception required.",
    "commander_blueprint_complete": "PASS — commander-first wheels / draw-punishment / group-slug blueprint finalized at Power Bracket 4 — Optimized; Nekusar is the primary forced-draw damage engine and the refined package multiplies his triggers and increases controllable wheel density.",
    "high_impact_candidate_triage_complete": "PASS — project top-100 candidates, historical Krang proposal, current optimized Nekusar evidence, 2026 Nekusar-specific research, trigger multipliers, wheels, draw punishers, alternate kills, interaction, sweepers, and mana-base challengers exhausted; final serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — all 99 baseline noncommander slots adjudicated at 82 KEEP / 17 CUT; exact 17-cut / 17-add SHA-bound candidate explicitly approved by user on 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Wizard's Staff/Harmonic Prodigy/Krang additive trigger arithmetic; Krang scope; Ghyrson/Solphim exact-1 anti-synergy correction; Curiosity with Nekusar and Niv-Mizzet; Winds of Change; Molten Psyche; Toxic Deluge; Mikokoro; and mana-base interactions reviewed.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 97 distinct names / 35 lands; only Island x2, Mountain x2, and Swamp x2 repeat; singleton, U/B/R color identity, and candidate/approved byte-match SHA checks PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, natural-ceiling, and strategic verification passed; no unsupported gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Nekusar, the Mindrazer approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 97 distinct names, 35 lands; only Island x2, Mountain x2, and Swamp x2 repeat; singleton PASS; U/B/R identity PASS; current Oracle/rules/trigger-arithmetic review PASS; current official Commander legality checkpoint PASS; no project exceptions. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Wheels / Draw Punishment / Group Slug. Mandatory 99-slot audit completed at 82 KEEP / 17 CUT. Candidate exhaustion, adversarial red-team, commander-necessity verification, Ghyrson/Solphim correction, mana-base red team, zero-new-material-improvement closure, and exact structural verification all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Nicol Bolas (index 40 / deck 41 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Nekusar tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Nekusar, the Mindrazer approval finalized.")