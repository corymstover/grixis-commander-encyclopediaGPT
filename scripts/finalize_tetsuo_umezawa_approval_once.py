#!/usr/bin/env python3
import csv, hashlib, io, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = "14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6"
DECK_ID = "Tetsuo_Umezawa"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
C = ROOT / "refinement/decklists/Tetsuo_Umezawa_Approval_Ready_2026-10-15.txt"
A = ROOT / "refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt"
V = ROOT / "refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md"
W = ROOT / "refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md"
D = ROOT / "refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md"
G = ROOT / "refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_2026-10-15_Complete_Gate.json"
R = ROOT / "refinement/approvals/Tetsuo_Umezawa_Approved_2026-10-15.md"
S = ROOT / "state/current_deck_overrides.json"
T = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"

raw = C.read_bytes()
if hashlib.sha256(raw).hexdigest() != SHA:
    raise SystemExit("Tetsuo Umezawa candidate SHA mismatch")
text = raw.decode("utf-8-sig")
if not text.startswith("1x Tetsuo Umezawa [Commander]\n"):
    raise SystemExit("Tetsuo Umezawa commander-first line mismatch")
qty = 0
names = []
for line in [x for x in text.splitlines() if x.strip()]:
    q, n = line.split("x ", 1)
    q = int(q)
    qty += q
    names += [n.replace(" [Commander]", "")] * q
if qty != 100 or len(set(names)) != 87:
    raise SystemExit(f"Tetsuo structure mismatch: {qty} cards / {len(set(names))} distinct")
repeats = {n: q for n, q in Counter(names).items() if q > 1}
if repeats != {"Island": 5, "Mountain": 5, "Swamp": 6}:
    raise SystemExit(f"Unexpected Tetsuo repeats: {repeats}")

verify = V.read_text(encoding="utf-8")
for bit in [
    SHA,
    "APPROVAL_READY — NOT APPROVED / NOT LOCKED",
    "99/99 noncommander copies adjudicated; 85 KEEP / 14 CUT",
    "ZERO NEW MATERIAL IMPROVEMENTS",
    "Power Bracket 4 — Optimized",
    "Project exceptions: **none**",
    "Front-face lands: **35**",
    "Land-capable MDFCs: **1**",
    "Functional land-capable slots: **36**",
    "Force of Will blue-pitch pool: **25 other blue nonland cards**",
]:
    if bit not in verify:
        raise SystemExit(f"Tetsuo verification evidence mismatch: {bit}")

audit = W.read_text(encoding="utf-8")
for bit in [SHA, "99/99 noncommander copies adjudicated: 85 KEEP / 14 CUT", "35 front-face lands + 1 land-capable MDFC", "ZERO NEW MATERIAL IMPROVEMENTS"]:
    if bit not in audit:
        raise SystemExit(f"Tetsuo whole-list audit mismatch: {bit}")

dec = D.read_text(encoding="utf-8")
for bit in [SHA, "ZERO NEW MATERIAL IMPROVEMENTS", "Power Bracket 4 — Optimized", "Sting, the Glinting Dagger", "Sink into Stupor // Soporific Springs"]:
    if bit not in dec:
        raise SystemExit(f"Tetsuo decision closeout mismatch: {bit}")

gate = json.loads(G.read_text(encoding="utf-8"))
if (
    gate.get("deck_sha256") != SHA
    or gate.get("overall_result") != "APPROVAL_READY"
    or gate.get("errors")
    or gate.get("count") != 100
    or gate.get("distinct_names") != 87
    or gate.get("commander_color_identity") != ["B", "R", "U"]
    or gate.get("project_exceptions")
    or gate.get("rules_gate") != "PASS"
    or gate.get("official_legality_gate") != "PASS"
):
    raise SystemExit("Tetsuo complete gate mismatch")

A.write_bytes(raw)
if hashlib.sha256(A.read_bytes()).hexdigest() != SHA:
    raise SystemExit("Tetsuo approved artifact SHA mismatch")

R.parent.mkdir(parents=True, exist_ok=True)
R.write_text(
    f"# Tetsuo Umezawa — Current-Cycle Approval Record\n\n"
    f"Date: {DATE}  \nCycle: `{CYCLE}`\n\n"
    "Status: **APPROVED / LOCKED**\n\n"
    f"Canonical approved SHA-256: `{SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready Tetsuo Umezawa candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, commander-first tap/untap and forced-combat review, candidate exhaustion, adversarial red-team review, mana-base and functional-land review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton verification, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 87 distinct names, 35 front-face lands plus one land-capable MDFC for 36 functional land-capable slots; Island x5, Mountain x5, and Swamp x6 are the only repeats. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Tap/Untap / Forced Combat / Activated Abilities.\n\n"
    "This approval freezes `refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
    encoding="utf-8",
)

dec = dec.replace(
    "Status: working decision closeout; not user approval",
    "Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",
    1,
)
if "## Approval closeout" not in dec:
    dec += (
        "\n## Approval closeout\n\n"
        f"- Explicit user approval received: **{DATE}**\n"
        f"- Canonical approved SHA-256: `{SHA}`\n"
        "- Exact approved artifact: `refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt`\n"
        "- Current-cycle state: **APPROVED / LOCKED**\n"
        "- Next unlocked: **Tetsuo, Imperial Champion (index 54 / deck 55 of 62)**.\n"
    )
D.write_text(dec, encoding="utf-8")

state = json.loads(S.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("wrong current refinement cycle")
old = state.setdefault("decks", {}).get(DECK_ID)
if old and old.get("approved_list_sha256") not in (None, SHA):
    raise SystemExit("conflicting existing Tetsuo approved hash")
state["decks"][DECK_ID] = {
    "approval_status": "APPROVED",
    "lock_status": "LOCKED",
    "final_gate_passed": True,
    "user_approval_date": DATE,
    "current_stage": "LOCKED",
    "approved_list_sha256": SHA,
    "quality_gate_version": "Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis": "Explicit user approval of the exact SHA-bound Tetsuo Umezawa approval-ready candidate after complete current-cycle verification.",
    "whole_list_audit_artifact": "refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md",
    "verification_artifact": "refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact": "refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact": "refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact": "refinement/approvals/Tetsuo_Umezawa_Approved_2026-10-15.md",
    "approved_list_artifact": "refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt",
}
S.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = T.read_text(encoding="utf-8").splitlines()
hdr = next(csv.reader([lines[0]]))
ix = {v: i for i, v in enumerate(hdr)}
for i in range(1, len(lines)):
    row = next(csv.reader([lines[i]]))
    row += [""] * (len(hdr) - len(row))
    if row[ix["deck_id"]] == DECK_ID:
        vals = {
            "baseline_status": "CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.",
            "fresh_oracle_identity_check": "PASS — exact SHA-bound Tetsuo Umezawa candidate verified at 100 cards / 87 distinct names within U/B/R; only Island x5, Mountain x5, and Swamp x6 repeat.",
            "fresh_official_legality_check": "PASS — current official Commander legality checked 2026-10-15; no project exception required.",
            "official_named_ban_list_checkpoint": "PASS — no unexpected Commander-banned card; no project exception required.",
            "commander_blueprint_complete": "PASS — Tetsuo tap/untap / forced-combat / activated-ability blueprint finalized at Power Bracket 4 — Optimized.",
            "high_impact_candidate_triage_complete": "PASS — tap-target, untap, forced-combat, protection, mana-base/MDFC, late Sting challenger, candidate exhaustion, and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
            "swap_decision_ledger_complete": "PASS — 99/99 noncommander copies adjudicated at 85 KEEP / 14 CUT; exact candidate explicitly approved 2026-10-15.",
            "combo_rules_interactions_verified": "PASS — Tetsuo tapped-or-blocking targeting, activated-ability copying, repeated untaps, Sting combat untaps, Patriar's Seal, Puppeteer, Flood, Blustersquall, Retreat to Coralhelm, Aura targeting restriction, and MDFC structure reviewed.",
            "consistency_test_complete": "PASS — approved artifact 100 cards / 87 distinct names / 35 front-face lands + 1 MDFC = 36 functional land-capable slots; only Island x5, Mountain x5, Swamp x6 repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
            "multiplayer_test_complete_or_reason_not_applicable": "NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
            "final_gate_passed": "YES",
            "final_list_hash": SHA,
            "user_approval_date": DATE,
            "refinement_status": f"APPROVED / LOCKED — current {CYCLE} cycle",
            "notes": f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Tetsuo Umezawa candidate approved and locked. Canonical hash: {SHA}. 100 cards, 87 distinct names, 35 front-face lands plus Sink into Stupor // Soporific Springs = 36 functional land-capable slots; only Island x5, Mountain x5, Swamp x6 repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Tap/Untap / Forced Combat / Activated Abilities. 99-slot audit: 85 KEEP / 14 CUT. Candidate exhaustion and zero-new-material-improvement closure PASS. Next unlocked: Tetsuo, Imperial Champion (index 54 / deck 55 of 62).",
        }
        for k, v in vals.items():
            row[ix[k]] = v
        out = io.StringIO()
        csv.writer(out, lineterminator="").writerow(row)
        lines[i] = out.getvalue()
        break
else:
    raise SystemExit("Tetsuo tracker row missing")
T.write_text("\n".join(lines) + "\n", encoding="utf-8")

reread = json.loads(S.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED"
assert reread["lock_status"] == "LOCKED"
assert reread["approved_list_sha256"] == SHA
assert hashlib.sha256(A.read_bytes()).hexdigest() == SHA
print("Tetsuo Umezawa approval finalized")
