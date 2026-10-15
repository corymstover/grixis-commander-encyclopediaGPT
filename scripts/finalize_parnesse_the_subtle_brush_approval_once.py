import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

EXPECTED_SHA = "8ff8c101d98e7de997c1de29973db2dd6a51ffdd7b44e4f34145bb1abf2d9e7c"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Parnesse__the_Subtle_Brush"
NAME = "Parnesse, the Subtle Brush"

candidate = Path("refinement/decklists/Parnesse_the_Subtle_Brush_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Parnesse_the_Subtle_Brush_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md")
complete_gate_path = Path("refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_2026-10-15_Complete_Gate.json")
decision_path = Path("refinement/decisions/Parnesse_the_Subtle_Brush_Candidate_Decisions_2026-10-15.md")
approval_record = Path("refinement/approvals/Parnesse_the_Subtle_Brush_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Parnesse candidate SHA mismatch: {actual_sha}")

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
    raise SystemExit(f"Parnesse candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 96:
    raise SystemExit(f"Parnesse candidate must contain 96 distinct names; found {len(set(names))}")
if lines[0] != "1x Parnesse, the Subtle Brush [Commander]":
    raise SystemExit("Parnesse commander line mismatch")

counts = Counter(names)
repeats = {name: qty for name, qty in counts.items() if qty > 1}
expected_repeats = {"Island": 2, "Mountain": 3, "Swamp": 2}
if repeats != expected_repeats:
    raise SystemExit(f"Unexpected Parnesse repeated names: {repeats}")

verification = verification_path.read_text(encoding="utf-8")
if EXPECTED_SHA not in verification or "APPROVAL_READY" not in verification:
    raise SystemExit("Parnesse verification is not bound to approved SHA")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in verification:
    raise SystemExit("Parnesse verification lacks zero-new-material-improvement closure")
if "Power Bracket 4" not in verification:
    raise SystemExit("Parnesse natural power ceiling gate missing")
if "Project exceptions: **none**" not in verification:
    raise SystemExit("Parnesse project-exception gate missing")

audit = audit_path.read_text(encoding="utf-8")
if "99/99" not in audit or "89 KEEP / 10 CUT" not in audit or EXPECTED_SHA not in audit:
    raise SystemExit("Parnesse whole-list audit incomplete or SHA-mismatched")

decision = decision_path.read_text(encoding="utf-8")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in decision or EXPECTED_SHA not in decision:
    raise SystemExit("Parnesse decision closeout incomplete or SHA-mismatched")

complete_gate = json.loads(complete_gate_path.read_text(encoding="utf-8"))
if complete_gate.get("deck_sha256") != EXPECTED_SHA:
    raise SystemExit("Parnesse complete-gate SHA mismatch")
if complete_gate.get("overall_result") != "APPROVAL_READY":
    raise SystemExit("Parnesse complete gate is not APPROVAL_READY")
if complete_gate.get("rules_gate") != "PASS" or complete_gate.get("official_legality_gate") != "PASS":
    raise SystemExit("Parnesse rules or legality gate not PASS")
if complete_gate.get("errors"):
    raise SystemExit(f"Parnesse complete gate contains errors: {complete_gate['errors']}")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Parnesse artifact SHA mismatch")

approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first review, candidate exhaustion, adversarial red-team review, mana-base review, zero-new-material-improvement closure, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact 100-card verification, singleton compliance, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 96 distinct names, 35 lands; only Island x2, Mountain x3, and Swamp x2 repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Spell Copy / Politics / Spellslinger.\n\n"
    "This approval freezes `refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
    encoding="utf-8",
)

if "Status: working decision closeout; not user approval" in decision:
    decision = decision.replace(
        "Status: working decision closeout; not user approval",
        "Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",
        1,
    )
if "**Decision result: PASS — complete Oracle/legality/rules gate and explicit user approval are still required.**" in decision:
    decision = decision.replace(
        "**Decision result: PASS — complete Oracle/legality/rules gate and explicit user approval are still required.**",
        "**Decision closeout: PASS — complete Oracle/legality/rules gate passed and explicit user approval was received 2026-10-15.**",
        1,
    )
if "## Approval closeout" not in decision:
    decision += (
        "\n## Approval closeout\n\n"
        f"- Explicit user approval received: **{DATE}**\n"
        f"- Canonical approved SHA-256: `{EXPECTED_SHA}`\n"
        "- Exact approved artifact: `refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept (index 46 / deck 47 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Parnesse approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Parnesse, the Subtle Brush approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first review, candidate exhaustion, adversarial red-team review, mana-base review, zero-new-material-improvement closure, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton compliance, and U/B/R color-identity verification.",
    "whole_list_audit_artifact": "refinement/verification/Parnesse_the_Subtle_Brush_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/Parnesse_the_Subtle_Brush_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Parnesse_the_Subtle_Brush_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt"
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Parnesse candidate verified at 100 cards / 96 distinct names within U/B/R; only Island x2, Mountain x3, and Swamp x2 repeat.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — spell-copy politics / copy-trigger / spellslinger blueprint finalized at Power Bracket 4 — Optimized; Parnesse remains the political copy engine rather than a generic Grixis storm shell.",
    "high_impact_candidate_triage_complete": "PASS — current Parnesse evidence, inherited top-100 research, recent cards, stale-membership blind spots, candidate exhaustion, and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 89 KEEP / 10 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — spell copies vs copied cards/cast copies; Tempt with Mayhem; Wizard's Staff/Harmonic Prodigy/Veyran trigger multiplication; Twinning Staff; Prismari storm copies; Sunken Palace delayed spell copy; Replication Technique/demonstrate reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 96 distinct names / 35 lands; only Island x2, Mountain x3, and Swamp x2 repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Parnesse, the Subtle Brush candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 96 distinct names, 35 lands; only Island x2, Mountain x3, and Swamp x2 repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Spell Copy / Politics / Spellslinger. 99-slot audit: 89 KEEP / 10 CUT. Spell-copy-vs-card-copy rules review, Tempt with Mayhem political-copy upgrade, Sunken Palace interaction, mana-base red team, candidate exhaustion, and zero-new-material-improvement closure PASS. Next unlocked: Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept (index 46 / deck 47 of 62)."
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Parnesse tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Parnesse, the Subtle Brush approval finalized.")
