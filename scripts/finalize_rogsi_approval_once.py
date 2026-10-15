import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "RogSi"
NAME = "Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept"

candidate = Path("refinement/decklists/RogSi_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/RogSi_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/RogSi_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/RogSi_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md")
gate_path = Path("refinement/verification/rogsi_2026-10-15/gate_output/RogSi_2026-10-15_Complete_Gate.json")
approval_record = Path("refinement/approvals/RogSi_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"RogSi candidate SHA mismatch: {actual_sha}")

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
    raise SystemExit(f"RogSi candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 100:
    raise SystemExit(f"RogSi candidate must contain 100 distinct names; found {len(set(names))}")
if lines[:2] != [
    "1x Rograkh, Son of Rohgahh [Commander]",
    "1x Silas Renn, Seeker Adept [Commander]",
]:
    raise SystemExit("RogSi commander lines mismatch")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY — NOT APPROVED / NOT LOCKED" not in verification:
    raise SystemExit("RogSi verification is not bound to approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("RogSi verification lacks zero-new-material-improvement closure")
if "Power Bracket 5 — cEDH" not in verification:
    raise SystemExit("RogSi natural power ceiling gate missing")
if "Project exceptions: **none**" not in verification:
    raise SystemExit("RogSi project-exception gate missing")

 audit = audit_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in audit or "98/98" not in audit or "91 KEEP / 7 CUT" not in audit:
    raise SystemExit("RogSi whole-list audit incomplete or SHA-mismatched")

decision = decision_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in decision or "ZERO NEW MATERIAL IMPROVEMENTS" not in decision:
    raise SystemExit("RogSi decision closeout incomplete or SHA-mismatched")

gate = json.loads(gate_path.read_text(encoding="utf-8"))
if gate.get("deck_sha256") != EXPECTED_SHA or gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
    raise SystemExit("RogSi complete gate is not clean APPROVAL_READY for approved SHA")
if gate.get("count") != 100 or gate.get("distinct_names") != 100:
    raise SystemExit("RogSi complete gate structural result mismatch")
if gate.get("commander_color_identity") != ["B", "R", "U"]:
    raise SystemExit("RogSi complete gate color-identity mismatch")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved RogSi artifact SHA mismatch")

approval_record.parent.mkdir(parents=True, exist_ok=True)
approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready RogSi candidate after authoritative FINAL baseline reconciliation, mandatory 98-slot whole-list audit for the partner-commanders configuration, classic turbo-naus/Breach versus artifact-Monolith branch review, candidate exhaustion, adversarial red-team review, current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact 100-card verification, singleton compliance, and U/B/R partner color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 100 distinct names, two commanders, 24 lands, no repeated names, and no project legality exception. Natural ceiling: Power Bracket 5 — cEDH. Archidekt tags: Turbo Naus / Underworld Breach / Fast Mana.\n\n"
    "This approval freezes `refinement/decklists/RogSi_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
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
        "- Exact approved artifact: `refinement/decklists/RogSi_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory partner-deck whole-list audit + targeted approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Saruman, the White Hand (index 47 / deck 48 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing RogSi approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory partner-deck whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 98-slot whole-list audit, classic turbo-naus/Breach versus artifact-Monolith branch review, candidate exhaustion, adversarial red-team review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton compliance, and U/B/R partner color-identity verification.",
    "whole_list_audit_artifact": "refinement/verification/RogSi_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/RogSi_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/rogsi_2026-10-15/gate_output/RogSi_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/RogSi_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/RogSi_Approved_2026-10-15.txt"
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound RogSi candidate verified at 100 cards / 100 distinct names with two commanders and U/B/R partner color identity.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — classic RogSi turbo-naus / Underworld Breach / fast-mana identity finalized at Power Bracket 5 — cEDH; Rograkh is the zero-mana resource engine and Silas the U/B partner plus secondary artifact-recursion axis.",
    "high_impact_candidate_triage_complete": "PASS — classic turbo versus artifact-Monolith branch review, current tournament-core comparison, candidate exhaustion, and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 98/98 noncommander slots adjudicated at 91 KEEP / 7 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Rograkh commander-resource interactions; Silas recursion timing; Vexing Bauble symmetry; Hexing Squelcher interaction; Samut split second; Final Fortune/Warrior's Oath delayed-loss triggers; Demonic Counsel delirium; Mnemonic Betrayal; Underworld Breach/LED/Brain Freeze and Grinding Station lines; Tainted Pact singleton integrity reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 100 distinct names / 24 lands / two commanders / no repeats; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound RogSi candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 100 distinct names, 24 lands, two commanders, no repeats; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 5 — cEDH. Tags: Turbo Naus / Underworld Breach / Fast Mana. 98-slot audit: 91 KEEP / 7 CUT. Classic turbo-naus/Breach versus artifact-Monolith branch review, current tournament-core comparison, candidate exhaustion, mana/flex red team, and zero-new-material-improvement closure PASS. Next unlocked: Saruman, the White Hand (index 47 / deck 48 of 62)."
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("RogSi tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("RogSi approval finalized.")
