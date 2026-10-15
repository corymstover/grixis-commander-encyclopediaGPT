#!/usr/bin/env python3
import csv, hashlib, io, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = "d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e"
DECK_ID = "Tetsuo__Imperial_Champion"
CYCLE = "global-restart-2026-10-13"
DATE = "2026-10-15"
C = ROOT / "refinement/decklists/Tetsuo_Imperial_Champion_Approval_Ready_2026-10-15.txt"
A = ROOT / "refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt"
V = ROOT / "refinement/verification/Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md"
W = ROOT / "refinement/verification/Tetsuo_Imperial_Champion_Whole_List_Audit_2026-10-15.md"
D = ROOT / "refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md"
G = ROOT / "refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_2026-10-15_Complete_Gate.json"
R = ROOT / "refinement/approvals/Tetsuo_Imperial_Champion_Approved_2026-10-15.md"
S = ROOT / "state/current_deck_overrides.json"
T = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"

raw = C.read_bytes()
if hashlib.sha256(raw).hexdigest() != SHA:
    raise SystemExit("Tetsuo Imperial Champion candidate SHA mismatch")
text = raw.decode("utf-8-sig")
if not text.startswith("1x Tetsuo, Imperial Champion [Commander]\n"):
    raise SystemExit("commander-first line mismatch")
qty = 0
names = []
for line in [x for x in text.splitlines() if x.strip()]:
    q, n = line.split("x ", 1)
    q = int(q)
    qty += q
    names += [n.replace(" [Commander]", "")] * q
if qty != 100 or len(set(names)) != 91:
    raise SystemExit(f"structure mismatch: {qty} cards / {len(set(names))} distinct")
repeats = {n:q for n,q in Counter(names).items() if q > 1}
if repeats != {"Island":5,"Mountain":4,"Swamp":3}:
    raise SystemExit(f"repeat mismatch: {repeats}")

verify = V.read_text(encoding="utf-8")
for bit in [SHA,"APPROVAL_READY — NOT APPROVED / NOT LOCKED","99/99 noncommander copies adjudicated; 87 KEEP / 12 CUT","ZERO NEW MATERIAL IMPROVEMENTS","Power Bracket 4 — Optimized","Project exceptions: **none**","Lands: **35**","Force of Will blue-pitch pool: **22 other blue nonland cards**"]:
    if bit not in verify:
        raise SystemExit(f"verification evidence mismatch: {bit}")

audit = W.read_text(encoding="utf-8")
for bit in [SHA,"99/99 noncommander copies adjudicated: 87 KEEP / 12 CUT","Candidate remains **35 lands**","ZERO NEW MATERIAL IMPROVEMENTS"]:
    if bit not in audit:
        raise SystemExit(f"whole-list audit mismatch: {bit}")

dec = D.read_text(encoding="utf-8")
for bit in [SHA,"ZERO NEW MATERIAL IMPROVEMENTS","Power Bracket 4 — Optimized","Savage Beating","World at War","Oathkeeper, Takeno's Daisho"]:
    if bit not in dec:
        raise SystemExit(f"decision closeout mismatch: {bit}")

gate = json.loads(G.read_text(encoding="utf-8"))
if (gate.get("deck_sha256") != SHA or gate.get("overall_result") != "APPROVAL_READY" or gate.get("errors") or gate.get("count") != 100 or gate.get("distinct_names") != 91 or gate.get("commander_color_identity") != ["B","R","U"] or gate.get("project_exceptions") or gate.get("rules_gate") != "PASS" or gate.get("official_legality_gate") != "PASS"):
    raise SystemExit("complete gate mismatch")

A.write_bytes(raw)
if hashlib.sha256(A.read_bytes()).hexdigest() != SHA:
    raise SystemExit("approved artifact SHA mismatch")

R.parent.mkdir(parents=True, exist_ok=True)
R.write_text(
    f"# Tetsuo, Imperial Champion — Current-Cycle Approval Record\n\nDate: {DATE}  \nCycle: `{CYCLE}`\n\nStatus: **APPROVED / LOCKED**\n\nCanonical approved SHA-256: `{SHA}`\n\n"
    "The user explicitly approved the exact SHA-bound approval-ready Tetsuo, Imperial Champion candidate after authoritative frozen-baseline reconciliation, mandatory 99-slot whole-list audit, commander-first Equipment/free-cast/extra-combat review, candidate exhaustion, adversarial red-team review, mana-base review, targeted current Oracle refresh, rules-interaction verification, current official Commander legality verification, exact structural verification, singleton verification, and U/B/R color-identity verification all passed.\n\n"
    "Approved structure: 100 cards, 91 distinct names, 35 lands; Island x5, Mountain x4, and Swamp x3 are the only repeats. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Equipment / Free-Cast Spells / Extra Combats.\n\n"
    "This approval freezes `refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt` as the current-cycle canonical list.\n",
    encoding="utf-8",
)

dec = dec.replace("Status: working decision closeout; not user approval","Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",1)
if "## Approval closeout" not in dec:
    dec += (f"\n## Approval closeout\n\n- Explicit user approval received: **{DATE}**\n- Canonical approved SHA-256: `{SHA}`\n- Exact approved artifact: `refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt`\n- Current-cycle state: **APPROVED / LOCKED**\n- Next unlocked: **The Madcap Jester (index 55 / deck 56 of 62)**.\n")
D.write_text(dec, encoding="utf-8")

state = json.loads(S.read_text(encoding="utf-8"))
if state.get("cycle_id") != CYCLE:
    raise SystemExit("wrong current refinement cycle")
old = state.setdefault("decks",{}).get(DECK_ID)
if old and old.get("approved_list_sha256") not in (None,SHA):
    raise SystemExit("conflicting existing approved hash")
state["decks"][DECK_ID] = {
    "approval_status":"APPROVED","lock_status":"LOCKED","final_gate_passed":True,"user_approval_date":DATE,"current_stage":"LOCKED","approved_list_sha256":SHA,
    "quality_gate_version":"Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification",
    "approval_basis":"Explicit user approval of the exact SHA-bound Tetsuo, Imperial Champion approval-ready candidate after complete current-cycle verification.",
    "whole_list_audit_artifact":"refinement/verification/Tetsuo_Imperial_Champion_Whole_List_Audit_2026-10-15.md",
    "verification_artifact":"refinement/verification/Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md",
    "complete_gate_artifact":"refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_2026-10-15_Complete_Gate.json",
    "decision_closeout_artifact":"refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md",
    "approval_record_artifact":"refinement/approvals/Tetsuo_Imperial_Champion_Approved_2026-10-15.md",
    "approved_list_artifact":"refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt"
}
S.write_text(json.dumps(state,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

lines = T.read_text(encoding="utf-8").splitlines()
hdr = next(csv.reader([lines[0]])); ix = {v:i for i,v in enumerate(hdr)}
for i in range(1,len(lines)):
    row = next(csv.reader([lines[i]])); row += [""]*(len(hdr)-len(row))
    if row[ix["deck_id"]] == DECK_ID:
        vals = {
            "baseline_status":"CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.",
            "fresh_oracle_identity_check":"PASS — exact SHA-bound Tetsuo, Imperial Champion candidate verified at 100 cards / 91 distinct names within U/B/R; only Island x5, Mountain x4, and Swamp x3 repeat.",
            "fresh_official_legality_check":"PASS — current official Commander legality checked 2026-10-15; no project exception required.",
            "official_named_ban_list_checkpoint":"PASS — no unexpected Commander-banned card; no project exception required.",
            "commander_blueprint_complete":"PASS — Equipment / free-cast spells / extra-combats blueprint finalized at Power Bracket 4 — Optimized.",
            "high_impact_candidate_triage_complete":"PASS — Equipment suite, free-cast targets, extra-combat timing, protection, mana base, candidate exhaustion and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
            "swap_decision_ledger_complete":"PASS — 99/99 noncommander copies adjudicated at 87 KEEP / 12 CUT; exact candidate explicitly approved 2026-10-15.",
            "combo_rules_interactions_verified":"PASS — Tetsuo intervening equipped condition, no-mana-cost spell casting, Savage Beating/World at War combat timing, Oathkeeper Samurai clause, Equipment MV ceiling and retained extra-combat engines reviewed.",
            "consistency_test_complete":"PASS — approved artifact 100 cards / 91 distinct names / 35 lands; only Island x5, Mountain x4, Swamp x3 repeat; singleton, U/B/R identity and candidate/approved SHA match PASS.",
            "multiplayer_test_complete_or_reason_not_applicable":"NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
            "final_gate_passed":"YES","final_list_hash":SHA,"user_approval_date":DATE,"refinement_status":f"APPROVED / LOCKED — current {CYCLE} cycle",
            "notes":f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Tetsuo, Imperial Champion candidate approved and locked. Canonical hash: {SHA}. 100 cards, 91 distinct names, 35 lands; only Island x5, Mountain x4, Swamp x3 repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Equipment / Free-Cast Spells / Extra Combats. 99-slot audit: 87 KEEP / 12 CUT. Candidate exhaustion and zero-new-material-improvement closure PASS. Next unlocked: The Madcap Jester (index 55 / deck 56 of 62)."
        }
        for k,v in vals.items(): row[ix[k]] = v
        out = io.StringIO(); csv.writer(out,lineterminator="").writerow(row); lines[i] = out.getvalue(); break
else:
    raise SystemExit("tracker row missing")
T.write_text("\n".join(lines)+"\n",encoding="utf-8")

reread = json.loads(S.read_text(encoding="utf-8"))["decks"][DECK_ID]
assert reread["approval_status"] == "APPROVED" and reread["lock_status"] == "LOCKED" and reread["approved_list_sha256"] == SHA
assert hashlib.sha256(A.read_bytes()).hexdigest() == SHA
print("Tetsuo Imperial Champion approval finalized")
