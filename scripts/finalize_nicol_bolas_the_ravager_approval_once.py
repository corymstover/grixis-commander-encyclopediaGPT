import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Nicol_Bolas__the_Ravager"
NAME = "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"

candidate = Path("refinement/decklists/Nicol_Bolas_the_Ravager_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Nicol_Bolas_the_Ravager_Candidate_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Nicol_Bolas_the_Ravager_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Ravager candidate SHA mismatch: {actual_sha}")

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
    raise SystemExit(f"Ravager candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 98:
    raise SystemExit(f"Ravager candidate must contain 98 distinct names; found {len(set(names))}")
if lines[0] != "1x Nicol Bolas, the Ravager // Nicol Bolas, the Arisen [Commander]":
    raise SystemExit("Ravager commander line mismatch")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Ravager verification is not bound to the approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Ravager verification lacks zero-new-material-improvement closure")
if "Power Bracket 4" not in verification:
    raise SystemExit("Ravager natural power ceiling gate is missing")

audit = audit_path.read_text(encoding="utf-8")
if "99/99" not in audit or "83 KEEP / 16 CUT" not in audit or EXPECTED_SHA not in audit:
    raise SystemExit("Ravager mandatory whole-list audit is incomplete or SHA-mismatched")

decision = decision_path.read_text(encoding="utf-8")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or EXPECTED_SHA not in decision:
    raise SystemExit("Ravager decision closeout is incomplete or SHA-mismatched")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Ravager artifact SHA mismatch")

approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/combo review, mana-base red team, encyclopedia-differentiation review, zero-new-material-improvement closure, exact 100-card verification, singleton/color-identity verification, and current Commander legality checkpoint all passed.\n\n"
    "Approved structure: 100 cards, 98 distinct names, 34 lands; only Island x2 and Swamp x2 repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Superfriends / Transform / Proliferate.\n\n"
    "This approval freezes `refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
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
        "- Exact approved artifact: `refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Norman Osborn // Green Goblin (index 42 / deck 43 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Ravager approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Nicol Bolas, the Ravager // Nicol Bolas, the Arisen approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules/combo red-team, mana-base red-team, encyclopedia-differentiation review, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/verification/Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Nicol_Bolas_the_Ravager_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Nicol_Bolas_the_Ravager_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Ravager candidate verified at 100 cards / 98 distinct names within U/B/R; only Island x2 and Swamp x2 repeat.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — Ravager ETB discard / transform / Superfriends / proliferate blueprint finalized at Power Bracket 4 — Optimized; deck intentionally differentiated from original Nicol Bolas.",
    "high_impact_candidate_triage_complete": "PASS — candidate exhaustion and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 83 KEEP / 16 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Training Grounds transform reduction; Displacer Kitten DFC reset; Deliver Unto Evil Bolas condition; Rowan's Talent/Rings loyalty copies; Chain Veil/Rings/Teferi engine; Sanctum Lurker; proliferate interactions reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 98 distinct names / 34 lands; only Island x2 and Swamp x2 repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Nicol Bolas, the Ravager // Nicol Bolas, the Arisen candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 98 distinct names, 34 lands; Island x2 and Swamp x2 only repeats; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Superfriends / Transform / Proliferate. 99-slot audit: 83 KEEP / 16 CUT. Candidate exhaustion, rules/combo red-team, adjacent-deck differentiation, and zero-new-material-improvement closure PASS. Next unlocked: Norman Osborn // Green Goblin (index 42 / deck 43 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Ravager tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Nicol Bolas, the Ravager approval finalized.")
