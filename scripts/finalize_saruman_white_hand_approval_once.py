import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
DECK_ID = "Saruman__the_White_Hand"
NAME = "Saruman, the White Hand"

candidate = Path("refinement/decklists/Saruman_the_White_Hand_Approval_Ready_2026-10-15.txt")
approved = Path("refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt")
audit_path = Path("refinement/verification/Saruman_the_White_Hand_Whole_List_Audit_2026-10-15.md")
verification_path = Path("refinement/verification/Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md")
decision_path = Path("refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md")
gate_path = Path("refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_2026-10-15_Complete_Gate.json")
approval_record = Path("refinement/approvals/Saruman_the_White_Hand_Approved_2026-10-15.md")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Saruman candidate SHA mismatch: {actual_sha}")

lines = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
if not lines or lines[0] != "1x Saruman, the White Hand [Commander]":
    raise SystemExit("Saruman commander-first line mismatch")

card_total = 0
names = []
for line in lines:
    qty_text, name = line.split("x ", 1)
    qty = int(qty_text)
    card_total += qty
    clean_name = name.replace(" [Commander]", "")
    names.extend([clean_name] * qty)
if card_total != 100:
    raise SystemExit(f"Saruman candidate must contain 100 cards; found {card_total}")
if len(set(names)) != 97:
    raise SystemExit(f"Saruman candidate must contain 97 distinct names; found {len(set(names))}")

from collections import Counter
counts = Counter(names)
repeats = {k: v for k, v in counts.items() if v > 1}
expected_repeats = {"Island": 2, "Mountain": 2, "Swamp": 2}
if repeats != expected_repeats:
    raise SystemExit(f"Unexpected repeated names: {repeats}")

verification = verification_path.read_text(encoding="utf-8")
required_verification_bits = [
    EXPECTED_SHA,
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    "99/99 noncommander copies adjudicated; 86 KEEP / 13 CUT",
    "ZERO NEW MATERIAL IMPROVEMENTS",
    "Power Bracket 4 — Optimized",
    "Project exceptions: **none**",
    "Functional land-capable slots: **35**",
]
for bit in required_verification_bits:
    if bit not in verification:
        raise SystemExit(f"Saruman verification missing required evidence: {bit}")

audit = audit_path.read_text(encoding="utf-8")
for bit in [EXPECTED_SHA, "99/99", "86 KEEP / 13 CUT", "35 functional land-capable slots"]:
    if bit not in audit:
        raise SystemExit(f"Saruman whole-list audit incomplete or SHA-mismatched: {bit}")

decision = decision_path.read_text(encoding="utf-8")
for bit in [EXPECTED_SHA, "ZERO NEW MATERIAL IMPROVEMENTS", "Power Bracket 4 — Optimized"]:
    if bit not in decision:
        raise SystemExit(f"Saruman decision closeout incomplete or SHA-mismatched: {bit}")

gate = json.loads(gate_path.read_text(encoding="utf-8"))
if gate.get("deck_sha256") != EXPECTED_SHA:
    raise SystemExit("Saruman complete gate SHA mismatch")
if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
    raise SystemExit("Saruman complete gate is not clean APPROVAL_READY")
if gate.get("count") != 100 or gate.get("distinct_names") != 97:
    raise SystemExit("Saruman complete gate structural result mismatch")
if gate.get("commander_color_identity") != ["B", "R", "U"]:
    raise SystemExit("Saruman complete gate color-identity mismatch")
if gate.get("project_exceptions"):
    raise SystemExit("Unexpected Saruman project exception")
if gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS":
    raise SystemExit("Saruman rules/legality gate not PASS")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Saruman artifact SHA mismatch")

approval_record.parent.mkdir(parents=True, exist_ok=True)
approval_record.write_text(
    f"# {NAME} — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{EXPECTED_SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready Saruman candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, high-mana-value/low-actual-cost commander-first review, candidate exhaustion, adversarial red-team review, mana-base/MDFC review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton compliance, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 97 distinct names, 31 front-face lands plus 4 land-capable MDFCs for 35 functional land-capable slots, and only Island x2 / Mountain x2 / Swamp x2 repeat. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Spellslinger / Amass / Orc Army.\n\n"
    "This approval freezes `refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
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
        "- Exact approved artifact: `refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification**\n"
        "- Next unlocked deck in tracker order: **Sauron, Lord of the Rings (index 48 / deck 49 of 62)**.\n"
    )
decision_path.write_text(decision, encoding="utf-8")

state = json.loads(state_path.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("Wrong current refinement cycle")
existing = state.setdefault("decks", {}).get(DECK_ID)
if existing and existing.get("approved_list_sha256") not in (None, EXPECTED_SHA):
    raise SystemExit("Conflicting existing Saruman approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": EXPECTED_SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Saruman, the White Hand approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, high-mana-value/low-actual-cost commander-first review, candidate exhaustion, adversarial red-team review, mana-base/MDFC review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton compliance, and U/B/R color-identity verification.",
    "whole_list_audit_artifact": "refinement/verification/Saruman_the_White_Hand_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Saruman_the_White_Hand_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt"
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
    "fresh_oracle_identity_check": "PASS — exact SHA-bound Saruman candidate verified at 100 cards / 97 distinct names within U/B/R; only Island x2, Mountain x2, and Swamp x2 repeat.",
    "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
    "commander_blueprint_complete": "PASS — high-MV/discounted-spell Saruman spellslinger / amass / Orc Army blueprint finalized at Power Bracket 4 — Optimized; deck exploits mana value rather than generic storm/combo homogenization.",
    "high_impact_candidate_triage_complete": "PASS — high-MV/low-actual-cost review, current-card challenger pass, Army-finisher review, mana-base/MDFC red team, candidate exhaustion, and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 86 KEEP / 13 CUT; exact candidate explicitly approved 2026-10-15.",
    "combo_rules_interactions_verified": "PASS — Saruman mana-value triggers under cost reduction/alternate costs; X spells; Soul's Fire/Chandra's Ignition sequencing; Harmonic Prodigy/Wizard's Staff/Veyran trigger multiplication; Mauhúr replacement; The Great Goblin/All Will Be One; Widespread Brutality; Fall of Cair Andros; Mizzix's Mastery; Summons of Saruman; MDFCs; The Black Gate reviewed.",
    "consistency_test_complete": "PASS — approved artifact 100 cards / 97 distinct names / 31 front-face lands + 4 MDFCs = 35 functional land-capable slots; only Island x2, Mountain x2, Swamp x2 repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Saruman, the White Hand candidate approved and locked. Canonical hash: {EXPECTED_SHA}. 100 cards, 97 distinct names, 31 front-face lands + 4 MDFCs = 35 functional land-capable slots; only Island x2, Mountain x2, Swamp x2 repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Spellslinger / Amass / Orc Army. 99-slot audit: 86 KEEP / 13 CUT. High-MV/low-actual-cost review, Army-finisher review, mana-base/MDFC red team, candidate exhaustion, and zero-new-material-improvement closure PASS. Next unlocked: Sauron, Lord of the Rings (index 48 / deck 49 of 62)."
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Saruman tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
assert hashlib.sha256(approved.read_bytes()).hexdigest() == EXPECTED_SHA
print("Saruman, the White Hand approval finalized.")
