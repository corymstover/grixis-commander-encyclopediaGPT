import csv
import hashlib
import io
import json
from pathlib import Path

EXPECTED_SHA = "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-14"
DECK_ID = "Goro_Goro_and_Satoru"

candidate = Path("refinement/decklists/Goro_Goro_and_Satoru_Approval_Candidate_2026-10-14.txt")
approved = Path("refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt")
gate_path = Path("refinement/verification/goro_goro_and_satoru_2026-10-14/gate_output/Goro_Goro_and_Satoru_2026-10-14_Complete_Gate.json")
state_path = Path("state/current_deck_overrides.json")
tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")
approval_record = Path("refinement/approvals/Goro_Goro_and_Satoru_Approved_2026-10-14.md")

raw = candidate.read_bytes()
actual_sha = hashlib.sha256(raw).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"Goro-Goro and Satoru candidate SHA mismatch: {actual_sha}")

gate = json.loads(gate_path.read_text(encoding="utf-8"))
if gate.get("deck_sha256") != EXPECTED_SHA:
    raise SystemExit("Complete gate is not bound to the approved Goro-Goro and Satoru SHA")
if gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors"):
    raise SystemExit("Goro-Goro and Satoru complete gate is not clean APPROVAL_READY")
if gate.get("count") != 100 or gate.get("distinct_names") != 99:
    raise SystemExit("Goro-Goro and Satoru structural gate no longer reports 100 cards / 99 distinct names")
if sorted(gate.get("commander_color_identity", [])) != ["B", "R", "U"]:
    raise SystemExit("Goro-Goro and Satoru color identity gate mismatch")
if gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS":
    raise SystemExit("Goro-Goro and Satoru rules or legality gate is not PASS")
if gate.get("project_exceptions"):
    raise SystemExit("Unexpected Goro-Goro and Satoru project exception")

approved.write_bytes(raw)
if hashlib.sha256(approved.read_bytes()).hexdigest() != EXPECTED_SHA:
    raise SystemExit("Approved Goro-Goro and Satoru artifact failed byte-match check")

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
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + Complete Approval Gate v1",
    "approval_basis": "Explicit user approval of the exact SHA-bound Goro-Goro and Satoru approval candidate after mandatory 99-slot whole-list audit, candidate exhaustion, adversarial second-pass review, zero-new-material-improvement closure, fresh Oracle/color-identity verification, current official Commander legality verification, independent rules verification, and complete fail-closed gate APPROVAL_READY with zero errors.",
    "complete_gate_artifact": "refinement/verification/goro_goro_and_satoru_2026-10-14/gate_output/Goro_Goro_and_Satoru_2026-10-14_Complete_Gate.json",
    "whole_list_audit_artifact": "refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md",
    "approval_record_artifact": "refinement/approvals/Goro_Goro_and_Satoru_Approved_2026-10-14.md",
    "approved_list_artifact": "refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt",
}
state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

approval_record.parent.mkdir(parents=True, exist_ok=True)
approval_record.write_text("\n".join([
    "# Goro-Goro and Satoru — APPROVED / LOCKED",
    "",
    f"Cycle: `{CYCLE}`  ",
    f"Approval date: {DATE}  ",
    f"Approved SHA-256: `{EXPECTED_SHA}`  ",
    "Power Bracket: **4 — Optimized**  ",
    "Archidekt tags: **Ninjutsu / Dragon Tokens / Extra Combats**",
    "",
    "## Approval basis",
    "",
    "The user explicitly approved the exact SHA-bound approval candidate after the complete fail-closed gate returned `APPROVAL_READY` with zero errors.",
    "",
    "Verification state:",
    "- 100 cards",
    "- 99 distinct names; only basic Island repeats (2 copies)",
    "- Commander color identity: B/R/U",
    "- Rules gate: PASS",
    "- Official Commander legality gate: PASS",
    "- Project exceptions: none",
    "- Fresh Oracle cache: PASS",
    "- Mandatory whole-list audit: complete",
    "- Candidate exhaustion / adversarial second-pass review: complete",
    "- Zero-new-material-improvement closure: complete",
    "",
    "Approved swaps:",
    "1. Reinforced Ronin -> Phoenix Chick",
    "2. Rising of the Day -> Samut, Hazoret's Champion",
    "3. Feed the Swarm -> Withering Torment",
    "4. Combat Research -> Waterbender Ascension",
    "5. Impact Tremors -> Raphael, the Nightwatcher",
    "6. Kaito, Dancing Shadow -> Fire Navy Trebuchet",
    "",
    "Canonical approved artifact: `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt`",
    "",
    "Complete gate artifact: `refinement/verification/goro_goro_and_satoru_2026-10-14/gate_output/Goro_Goro_and_Satoru_2026-10-14_Complete_Gate.json`",
    "",
    "This deck is now locked. Do not revise, reopen, or replace it unless the user explicitly requests that action.",
]) + "\n", encoding="utf-8")

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
    "fresh_oracle_identity_check": "PASS — fresh current-cycle Oracle cache generated 2026-10-14; exact SHA-bound Goro-Goro and Satoru candidate verified at 100 cards / 99 distinct names within B/R/U color identity with zero unresolved metadata.",
    "fresh_official_legality_check": "PASS — exact SHA-bound Goro-Goro and Satoru candidate verified against current official Commander legality on 2026-10-14; no project exception required.",
    "official_named_ban_list_checkpoint": "PASS — current official Commander legality checkpoint completed 2026-10-14; no unexpected banned cards and no project exception required.",
    "commander_blueprint_complete": "PASS — current-cycle commander-first fresh-entry / ninjutsu / Dragon-token blueprint and mandatory 99-slot whole-list audit completed 2026-10-14.",
    "high_impact_candidate_triage_complete": "PASS — project top-100 candidates, current commander evidence, 2026 challengers, retained Ninja package, mana-base challengers, and adversarial alternatives exhausted; second serious pass produced ZERO NEW MATERIAL IMPROVEMENTS.",
    "swap_decision_ledger_complete": "PASS — exact six-swap SHA-bound Goro-Goro and Satoru approval candidate explicitly approved by user on 2026-10-14.",
    "combo_rules_interactions_verified": "PASS — SHA-bound rules attestation covers fresh-entry timing, Phoenix Chick recursion, Breath of Fury with continuous haste, Samut haste function, Raphael sneak/double-strike timing, Fire Navy Trebuchet fresh attacking tokens, Dragon Tempest/Terror triggers, and extra-combat sequencing.",
    "consistency_test_complete": "PASS — exact approved artifact verified at 100 cards / 99 distinct names / 33 lands; only basic Island repeats; candidate and approved artifact byte-match SHA.",
    "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — commander-first structural, rules, legality, and strategic verification passed; no gameplay win-rate claim is made.",
    "final_gate_passed": "YES",
    "final_list_hash": EXPECTED_SHA,
    "user_approval_date": DATE,
    "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
    "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Goro-Goro and Satoru approval candidate explicitly approved and locked. Canonical hash: {EXPECTED_SHA}. Final candidate: 100 cards, 99 distinct names, 33 lands; only Island repeats; B/R/U identity PASS; rules PASS; current official Commander legality PASS; no project exceptions; complete gate errors 0. Natural ceiling: Bracket 4 — Optimized. Commander-first Ninjutsu / Dragon Tokens / Extra Combats identity preserved. Approved swaps: Reinforced Ronin -> Phoenix Chick; Rising of the Day -> Samut, Hazoret's Champion; Feed the Swarm -> Withering Torment; Combat Research -> Waterbender Ascension; Impact Tremors -> Raphael, the Nightwatcher; Kaito, Dancing Shadow -> Fire Navy Trebuchet. Mandatory 99-slot whole-list audit, candidate exhaustion, adversarial second-pass review, zero-new-material-improvement closure, fresh Oracle/rules/legality checks, and complete fail-closed gate all PASS. Frozen source exports remain historical baseline evidence. Next unlocked deck in tracker order: Gwendlyn Di Corci.",
}

found = False
for n in range(1, len(raw_lines)):
    row = next(csv.reader([raw_lines[n]]))
    if len(row) > idx["deck_id"] and row[idx["deck_id"]] == DECK_ID:
        raw_lines[n] = update_line(raw_lines[n], updates)
        found = True
        break
if not found:
    raise SystemExit("Goro-Goro and Satoru tracker row missing")
tracker_path.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

reread = json.loads(state_path.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == EXPECTED_SHA
print("Goro-Goro and Satoru approval finalized.")
