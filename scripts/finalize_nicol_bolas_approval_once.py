import csv, hashlib, io, json
from pathlib import Path

SHA="e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617"
CYCLE="global-restart-2026-10-13"
DATE="2026-10-15"
DECK="Nicol_Bolas"
C=Path("refinement/decklists/Nicol_Bolas_Approval_Ready_2026-10-15.txt")
A=Path("refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt")
AUD=Path("refinement/verification/Nicol_Bolas_Whole_List_Audit_2026-10-15.md")
VER=Path("refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md")
DEC=Path("refinement/decisions/Nicol_Bolas_Candidate_Decisions_2026-10-15.md")
REC=Path("refinement/approvals/Nicol_Bolas_Approved_2026-10-15.md")
STATE=Path("state/current_deck_overrides.json")
TRACK=Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")

raw=C.read_bytes()
if hashlib.sha256(raw).hexdigest()!=SHA: raise SystemExit("candidate SHA mismatch")
lines=[x.strip() for x in raw.decode().splitlines() if x.strip()]
count=0; names=[]
for line in lines:
    q,n=line.split("x ",1); q=int(q); count+=q; names += [n.replace(" [Commander]","")]*q
if count!=100 or len(set(names))!=99 or lines[0]!="1x Nicol Bolas [Commander]": raise SystemExit("structural mismatch")
if names.count("Island")!=2 or any(names.count(n)!=1 for n in set(names) if n!="Island"): raise SystemExit("singleton mismatch")
ver=VER.read_text()
aud=AUD.read_text()
dec=DEC.read_text()
for needle in (SHA,"APPROVAL_READY","Lands: **37**","ZERO NEW MATERIAL IMPROVEMENTS"):
    if needle not in ver: raise SystemExit(f"verification missing {needle}")
for needle in (SHA,"99/99","70 KEEP / 29 CUT"):
    if needle not in aud: raise SystemExit(f"audit missing {needle}")
if "ZERO NEW MATERIAL IMPROVEMENTS" not in dec: raise SystemExit("decision closeout incomplete")

A.write_bytes(raw)
if hashlib.sha256(A.read_bytes()).hexdigest()!=SHA: raise SystemExit("approved artifact mismatch")
REC.write_text(f'''# Nicol Bolas — Current-Cycle Approval Record

Date: {DATE}  
Cycle: `{CYCLE}`

Status: **APPROVED / LOCKED**

Canonical approved SHA-256: `{SHA}`

The user explicitly approved the exact SHA-bound Nicol Bolas approval-ready candidate after authoritative FINAL baseline reconciliation, mandatory 99-slot whole-list audit, candidate exhaustion, commander-necessity review, adversarial Oracle/rules and commander-source-damage review, mana-base and acceleration red team, encyclopedia differentiation review, zero-new-material-improvement closure, exact structural verification, singleton/color-identity verification, and current official Commander legality verification.

Approved structure: 100 cards, 99 distinct names, 37 lands; Island x2 is the only repeated name. No project exception is required. Power Bracket 4 — Optimized. Archidekt tags: Discard / Commander Damage / Control.
''')

if "Status: working decision closeout; not user approval" in dec:
    dec=dec.replace("Status: working decision closeout; not user approval","Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15",1)
if "## Approval closeout" not in dec:
    dec += f'''\n## Approval closeout\n\n- Explicit user approval received: **{DATE}**\n- Canonical approved SHA-256: `{SHA}`\n- Exact approved artifact: `refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt`\n- Current-cycle state: **APPROVED / LOCKED**\n- Next unlocked deck: **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen (#42)**.\n'''
DEC.write_text(dec)

state=json.loads(STATE.read_text())
if state.get("cycle_id")!=CYCLE: raise SystemExit("wrong cycle")
old=state.setdefault("decks",{}).get(DECK)
if old and old.get("approved_list_sha256") not in (None,SHA): raise SystemExit("conflicting approved hash")
state["decks"][DECK]={
 "approval_status":"APPROVED","lock_status":"LOCKED","final_gate_passed":True,
 "user_approval_date":DATE,"current_stage":"LOCKED","approved_list_sha256":SHA,
 "quality_gate_version":"Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification",
 "approval_basis":"Explicit user approval of exact SHA-bound Nicol Bolas candidate after full current-cycle gates passed.",
 "whole_list_audit_artifact":str(AUD),"verification_artifact":str(VER),
 "decision_closeout_artifact":str(DEC),"approval_record_artifact":str(REC),"approved_list_artifact":str(A)}
STATE.write_text(json.dumps(state,indent=2,ensure_ascii=False)+"\n")

rawlines=TRACK.read_text().splitlines(); header=next(csv.reader([rawlines[0]])); idx={n:i for i,n in enumerate(header)}
updates={
 "baseline_status":"CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.",
 "fresh_oracle_identity_check":"PASS — exact SHA-bound Nicol Bolas candidate verified at 100 cards / 99 distinct names within U/B/R; Island x2 only repeat.",
 "fresh_official_legality_check":"PASS — current official Commander legality checked 2026-10-15; no project exception required.",
 "official_named_ban_list_checkpoint":"PASS — no unexpected Commander-banned card; no project exception required.",
 "commander_blueprint_complete":"PASS — original Elder Dragon discard / commander-damage / control blueprint; Nicol himself is the damage-to-full-hand-discard engine; Power Bracket 4 — Optimized.",
 "high_impact_candidate_triage_complete":"PASS — candidate exhaustion and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.",
 "swap_decision_ledger_complete":"PASS — 99/99 noncommander copies adjudicated at 70 KEEP / 29 CUT; exact candidate explicitly approved 2026-10-15.",
 "combo_rules_interactions_verified":"PASS — any-damage discard scope; Ingris; Kediss; Dragon Tempest; Chandra's Ignition; Pain for All; pinger equipment/aura; Tinybones/Tergrid; Assault/Sword interactions reviewed.",
 "consistency_test_complete":"PASS — approved artifact 100 cards / 99 distinct names / 37 lands; Island x2 only repeat; singleton, U/B/R identity, candidate/approved SHA match PASS.",
 "multiplayer_test_complete_or_reason_not_applicable":"NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.",
 "final_gate_passed":"YES","final_list_hash":SHA,"user_approval_date":DATE,
 "refinement_status":f"APPROVED / LOCKED — current {CYCLE} cycle",
 "notes":f"CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound Nicol Bolas candidate approved and locked. Canonical hash: {SHA}. 100 cards, 99 distinct names, 37 lands; Island x2 only repeat; singleton/U-B-R/legality PASS; no project exceptions. Power Bracket 4 — Optimized. Tags: Discard / Commander Damage / Control. 99-slot audit: 70 KEEP / 29 CUT. Candidate exhaustion and zero-new-material-improvement closure PASS. Next unlocked: Nicol Bolas, the Ravager // Nicol Bolas, the Arisen (index 41 / deck 42 of 62)."}
found=False
for i in range(1,len(rawlines)):
    row=next(csv.reader([rawlines[i]])); row += [""]*(len(header)-len(row))
    if row[idx["deck_id"]]==DECK:
        for k,v in updates.items(): row[idx[k]]=v
        out=io.StringIO(); csv.writer(out,lineterminator="").writerow(row); rawlines[i]=out.getvalue(); found=True; break
if not found: raise SystemExit("tracker row missing")
TRACK.write_text("\n".join(rawlines)+"\n")
check=json.loads(STATE.read_text())["decks"][DECK]
assert check["approval_status"]=="APPROVED" and check["lock_status"]=="LOCKED" and check["approved_list_sha256"]==SHA
print("Nicol Bolas approval finalized")
