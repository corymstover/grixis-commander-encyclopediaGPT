import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Obeka__Brute_Chronologist"
NAME = "Obeka, Brute Chronologist"

candidate = Path("refinement/decklists/Obeka_Brute_Chronologist_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Obeka_Brute_Chronologist_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Obeka_Brute_Chronologist_Candidate_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Obeka_Brute_Chronologist_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Obeka candidate SHA mismatch: {actual_sha}")

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
    raise SystemExit(f"Obeka candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 100:
    raise SystemExit(f"Obeka candidate must contain 100 distinct names; found {len(set(names))}")
if lines[0] != "1x Obeka, Brute Chronologist [Commander]":
    raise SystemExit("Obeka commander line mismatch")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Obeka verification is not bound to approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Obeka verification lacks zero-new-material-improvement closure")
if "Bracket 4" not in verification:
    raise SystemExit("Obeka natural power ceiling gate missing")

audit = audit_path.read_text(encoding="utf-8")
if "99/99" not in audit or "80 KEEP / 19 CUT" not in audit or EXPECTED_SHA not in audit:
    raise SystemExit("Obeka whole-list audit incomplete or SHA-mismatched")

decision = decision_path.read_text(encoding="utf-8")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or EXPECTED_SHA not in decision:
    raise SystemExit("Obeka decision closeout incomplete or SHA-mismatched")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Obeka artifact SHA mismatch")

approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial end-the-turn/rules review, mana-base red team, zero-new-material-improvement closure, exact 100-card verification, singleton/color-identity verification, and current Commander legality checkpoint all passed.\n\n"
    "Approved structure: 100 cards, 100 distinct names, 34 lands, no repeated names. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Extra Turns / Delayed Triggers / Clones.\n\n"
    "This approval freezes `refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
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
        "- Exact approved artifact: `refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Obeka, Splitter of Seconds (index 44 / deck 45 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Obeka approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Obeka, Brute Chronologist approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/end-the-turn/rules review, mana-base red team, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality checkpoint.",
    "whole_list_audit_artifact": "refinement/verification/Obeka_Brute_Chronologist_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md",
    "decision_closeout_artifact": "refinement/decisions/Obeka_Brute_Chronologist_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Obeka_Brute_Chronologist_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt",
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Obeka candidate verified at 100 cards / 100 distinct names within U/B/R; no repeated names.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — end-the-turn / delayed-trigger / temporary-value blueprint finalized at Power Bracket 4 — Optimized; Obeka is the primary liability-erasure engine.",
    "high_impact_candidate_triage_complete": "PASS — candidate exhaustion and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 80 KEEP / 19 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — active-player choice; next-end-step sequencing; Isochron Scepter/Final Fortune; Identity Thief; Come Back Wrong; Reflection; Hate Mirage; Apprentice Necromancer; Venser; Hellkite Courser; activation infrastructure reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 100 distinct names / 34 lands; no repeats; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Obeka, Brute Chronologist candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 100 distinct names, 34 lands; no repeats; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Extra Turns / Delayed Triggers / Clones. 99-slot audit: 80 KEEP / 19 CUT. End-the-turn sequencing, Hellkite red-team reversal, candidate exhaustion, mana-base red team, and zero-new-material-improvement closure PASS. Next unlocked: Obeka, Splitter of Seconds (index 44 / deck 45 of 62).",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Obeka tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Obeka, Brute Chronologist approval finalized.")
