#!/usr/bin/env python3
import csv, hashlib, io, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHA="72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58"
DECK_ID="Sol_kanar_the_Tainted"
CYCLE="global-restart-2026-10-13"
DATE="2026-10-15"
C=ROOT/"refinement/decklists/Solkanar_the_Tainted_Approval_Ready_2026-10-15.txt"
A=ROOT/"refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt"
V=ROOT/"refinement/verification/Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md"
D=ROOT/"refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md"
G=ROOT/"refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_2026-10-15_Complete_Gate.json"
R=ROOT/"refinement/approvals/Solkanar_the_Tainted_Approved_2026-10-15.md"
S=ROOT/"state/current_deck_overrides.json"
T=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
raw=C.read_bytes()
if hashlib.sha256(raw).hexdigest()!=SHA: raise SystemExit("candidate SHA mismatch")
text=raw.decode("utf-8-sig")
if not text.startswith("1x Sol'Kanar the Tainted [Commander]\n"): raise SystemExit("commander mismatch")
qty=0; names=[]
for line in [x for x in text.splitlines() if x.strip()]:
    q,n=line.split("x ",1); q=int(q); qty+=q; names += [n.replace(" [Commander]","")]*q
if qty!=100 or len(set(names))!=93: raise SystemExit("structure mismatch")
if {n:names.count(n) for n in set(names) if names.count(n)>1}!={"Island":3,"Mountain":3,"Swamp":4}: raise SystemExit("repeat mismatch")
verify=V.read_text()
for x in [SHA,"APPROVAL_READY — NOT APPROVED / NOT LOCKED","86 KEEP / 13 CUT","Power Bracket 4 — Optimized","Project exceptions: **none**"]:
    if x not in verify: raise SystemExit("verification evidence mismatch")
gate=json.loads(G.read_text())
if gate.get("deck_sha256")!=SHA or gate.get("overall_result")!="APPROVAL_READY" or gate.get("errors") or gate.get("count")!=100 or gate.get("distinct_names")!=93 or gate.get("commander_color_identity")!=["B","R","U"] or gate.get("project_exceptions") or gate.get("rules_gate")!="PASS" or gate.get("official_legality_gate")!="PASS": raise SystemExit("gate mismatch")
A.write_bytes(raw)
R.parent.mkdir(parents=True,exist_ok=True)
R.write_text(f"# Sol'Kanar the Tainted — Current-Cycle Approval Record\n\nDate: {DATE}  \nCycle: `{CYCLE}`\n\nStatus: **APPROVED / LOCKED**\n\nCanonical approved SHA-256: `{SHA}`\n\nApproved structure: 100 cards, 93 distinct names, 35 lands; Island x3, Mountain x3, and Swamp x4 are the only repeats. No project legality exception is required. Natural ceiling: Power Bracket 4 — Optimized. Archidekt tags: Donate / Blink / Giftable Curses.\n\nThis approval freezes `refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt` as the current-cycle canonical list.\n")
dec=D.read_text()
dec=dec.replace("Status: working decision closeout; not user approval","Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",1)
if "## Approval closeout" not in dec: dec+=f"\n## Approval closeout\n\n- Explicit user approval received: **{DATE}**\n- Canonical approved SHA-256: `{SHA}`\n- Current-cycle state: **APPROVED / LOCKED**\n- Next unlocked: **Tetsuo Umezawa (index 53 / deck 54 of 62)**.\n"
D.write_text(dec)
state=json.loads(S.read_text())
if state.get("cycle_id")!=CYCLE: raise SystemExit("wrong cycle")
old=state.setdefault("decks",{}).get(DECK_ID)
if old and old.get("approved_list_sha256") not in (None,SHA): raise SystemExit("conflicting hash")
state["decks"][DECK_ID]={"approval_status":"APPROVED","lock_status":"LOCKED","final_gate_passed":True,"user_approval_date":DATE,"current_stage":"LOCKED","approved_list_sha256":SHA,"quality_gate_version":"Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification","approval_basis":"Explicit user approval of exact SHA-bound approval-ready candidate after complete current-cycle verification.","verification_artifact":"refinement/verification/Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md","complete_gate_artifact":"refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_2026-10-15_Complete_Gate.json","decision_closeout_artifact":"refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md","approval_record_artifact":"refinement/approvals/Solkanar_the_Tainted_Approved_2026-10-15.md","approved_list_artifact":"refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt"}
S.write_text(json.dumps(state,indent=2)+"\n")
lines=T.read_text().splitlines(); hdr=next(csv.reader([lines[0]])); ix={v:i for i,v in enumerate(hdr)}
for i in range(1,len(lines)):
    row=next(csv.reader([lines[i]])); row += [""]*(len(hdr)-len(row))
    if row[ix["deck_id"]]==DECK_ID:
        vals={"baseline_status":"CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.","final_gate_passed":"YES","final_list_hash":SHA,"user_approval_date":DATE,"refinement_status":f"APPROVED / LOCKED — current {CYCLE} cycle","notes":f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Sol'Kanar the Tainted candidate approved and locked. Canonical hash: {SHA}. 100 cards / 93 distinct / 35 lands; legality/rules/identity PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Donate / Blink / Giftable Curses. 99-slot audit: 86 KEEP / 13 CUT. Next unlocked: Tetsuo Umezawa (index 53 / deck 54 of 62)."}
        for k,v in vals.items(): row[ix[k]]=v
        out=io.StringIO(); csv.writer(out,lineterminator="").writerow(row); lines[i]=out.getvalue(); break
else: raise SystemExit("tracker row missing")
T.write_text("\n".join(lines)+"\n")
r=json.loads(S.read_text())["decks"][DECK_ID]
assert r["approval_status"]=="APPROVED" and r["lock_status"]=="LOCKED" and r["approved_list_sha256"]==SHA
assert hashlib.sha256(A.read_bytes()).hexdigest()==SHA
print("Sol'Kanar the Tainted approval finalized")
