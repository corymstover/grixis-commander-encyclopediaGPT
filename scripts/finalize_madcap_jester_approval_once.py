#!/usr/bin/env python3
import csv, hashlib, io, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHA='caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7'
DECK_ID='The_Madcap_Jester'
CYCLE='global-restart-2026-10-13'
DATE='2026-10-15'
C=ROOT/'refinement/decklists/The_Madcap_Jester_Approval_Ready_2026-10-15.txt'
A=ROOT/'refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt'
V=ROOT/'refinement/verification/The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md'
W=ROOT/'refinement/verification/The_Madcap_Jester_Whole_List_Audit_2026-10-15.md'
D=ROOT/'refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md'
G=ROOT/'refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_2026-10-15_Complete_Gate.json'
R=ROOT/'refinement/approvals/The_Madcap_Jester_Approved_2026-10-15.md'
S=ROOT/'state/current_deck_overrides.json'
T=ROOT/'refinement/Deck_Refinement_Tracker_2026-10-12.csv'
raw=C.read_bytes()
if hashlib.sha256(raw).hexdigest()!=SHA: raise SystemExit('Madcap candidate SHA mismatch')
text=raw.decode('utf-8-sig')
if not text.startswith('1x The Madcap Jester [Commander]\n'): raise SystemExit('commander-first line mismatch')
qty=0; names=[]
for line in [x for x in text.splitlines() if x.strip()]:
    q,n=line.split('x ',1); q=int(q); qty+=q; names += [n.replace(' [Commander]','')]*q
if qty!=100 or len(set(names))!=100: raise SystemExit(f'structure mismatch {qty}/{len(set(names))}')
verify=V.read_text(encoding='utf-8')
for bit in [SHA,'APPROVAL_READY — NOT APPROVED / NOT LOCKED','99/99 noncommander copies adjudicated; 94 KEEP / 5 CUT','ZERO NEW MATERIAL IMPROVEMENTS','Power Bracket 5 — cEDH',"The Madcap Jester / Dragon's Smile"]:
    if bit not in verify: raise SystemExit(f'verification mismatch: {bit}')
dec=D.read_text(encoding='utf-8')
for bit in [SHA,'ZERO NEW MATERIAL IMPROVEMENTS','Power Bracket 5 — cEDH','Ashiok, Nightmare Weaver','Dauthi Voidwalker','Demonic Consultation','Tainted Pact','Lightning Greaves']:
    if bit not in dec: raise SystemExit(f'decision mismatch: {bit}')
gate=json.loads(G.read_text(encoding='utf-8'))
if gate.get('deck_sha256')!=SHA or gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('count')!=100 or gate.get('distinct_names')!=100 or gate.get('commander_color_identity')!=['B','R','U'] or gate.get('rules_gate')!='PASS' or gate.get('official_legality_gate')!='PASS': raise SystemExit('complete gate mismatch')
ex={x.get('card') for x in gate.get('project_exceptions') or []}
if ex!={'The Madcap Jester',"Dragon's Smile"}: raise SystemExit(f'exception mismatch {ex}')
A.write_bytes(raw)
if hashlib.sha256(A.read_bytes()).hexdigest()!=SHA: raise SystemExit('approved artifact SHA mismatch')
R.parent.mkdir(parents=True,exist_ok=True)
R.write_text(f'''# The Madcap Jester — Current-Cycle Approval Record\n\nDate: {DATE}  \nCycle: `{CYCLE}`\n\nStatus: **APPROVED / LOCKED**\n\nCanonical approved SHA-256: `{SHA}`\n\nThe user explicitly approved the exact SHA-bound approval-ready The Madcap Jester candidate after frozen-baseline reconciliation, mandatory 99-slot whole-list audit, commander-first exile-theft and cEDH-ceiling review, candidate exhaustion, adversarial red-team review, targeted current Oracle refresh, rules-interaction verification, exact structural verification, singleton verification, and U/B/R color-identity verification all passed.\n\nApproved structure: 100 cards, 100 distinct names, 34 lands, no repeats. Natural ceiling: Power Bracket 5 — cEDH. Archidekt tags: Exile Theft / Library Control / Grixis Combo.\n\nProject-exception distinction: The Madcap Jester and Dragon's Smile are retained under the registered future-release exceptions. On 2026-10-15 they are **not yet officially Commander-legal**; the verified gate records the prospective legality date as 2026-11-13. All 98 ordinary cards passed current official Commander legality.\n\nThis approval freezes `refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt` as the current-cycle canonical list.\n''',encoding='utf-8')
dec=dec.replace('Status: working decision closeout; not user approval','Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15',1)
if '## Approval closeout' not in dec:
    dec += f'''\n## Approval closeout\n\n- Explicit user approval received: **{DATE}**\n- Canonical approved SHA-256: `{SHA}`\n- Exact approved artifact: `refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt`\n- Current-cycle state: **APPROVED / LOCKED**\n- Project exceptions preserved: The Madcap Jester / Dragon's Smile future-release treatment; not represented as officially legal before release.\n- Next unlocked: **The Rani (index 56 / deck 57 of 62)**.\n'''
D.write_text(dec,encoding='utf-8')
state=json.loads(S.read_text(encoding='utf-8'))
if state.get('cycle_id')!=CYCLE: raise SystemExit('wrong cycle')
old=state.setdefault('decks',{}).get(DECK_ID)
if old and old.get('approved_list_sha256') not in (None,SHA): raise SystemExit('conflicting approved hash')
state['decks'][DECK_ID]={
 'approval_status':'APPROVED','lock_status':'LOCKED','final_gate_passed':True,'user_approval_date':DATE,'current_stage':'LOCKED','approved_list_sha256':SHA,
 'quality_gate_version':'Deck Quality Gates v3 + mandatory whole-list audit + targeted approval-ready verification',
 'approval_basis':'Explicit user approval of the exact SHA-bound Madcap Jester approval-ready candidate after complete current-cycle verification; registered future-release exceptions preserved and distinguished from official legality.',
 'whole_list_audit_artifact':'refinement/verification/The_Madcap_Jester_Whole_List_Audit_2026-10-15.md','verification_artifact':'refinement/verification/The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md','complete_gate_artifact':'refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_2026-10-15_Complete_Gate.json','decision_closeout_artifact':'refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md','approval_record_artifact':'refinement/approvals/The_Madcap_Jester_Approved_2026-10-15.md','approved_list_artifact':'refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt'}
S.write_text(json.dumps(state,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lines=T.read_text(encoding='utf-8').splitlines(); hdr=next(csv.reader([lines[0]])); ix={v:i for i,v in enumerate(hdr)}
for i in range(1,len(lines)):
    row=next(csv.reader([lines[i]])); row += ['']*(len(hdr)-len(row))
    if row[ix['deck_id']]==DECK_ID:
        vals={
          'baseline_status':'CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.',
          'fresh_oracle_identity_check':'PASS — exact SHA-bound Madcap Jester candidate verified at 100 cards / 100 distinct names within U/B/R; future-release commander and Dragon\'s Smile handled through registered project exceptions.',
          'fresh_official_legality_check':'PASS WITH PROJECT EXCEPTIONS — all 98 ordinary cards currently Commander-legal; The Madcap Jester and Dragon\'s Smile are future-release exceptions and not represented as officially legal on 2026-10-15.',
          'official_named_ban_list_checkpoint':'PASS / PROJECT EXCEPTION — no unexpected Commander-banned card; two registered future-release exceptions only.',
          'commander_blueprint_complete':'PASS — exile theft / library control / cast-from-exile cEDH blueprint finalized at Power Bracket 5 — cEDH.',
          'high_impact_candidate_triage_complete':'PASS — exile-engine, cEDH-ceiling, protection, combo, mana, challenger and adversarial red-team completed; ZERO NEW MATERIAL IMPROVEMENTS.',
          'swap_decision_ledger_complete':'PASS — 99/99 noncommander copies adjudicated at 94 KEEP / 5 CUT; exact candidate explicitly approved 2026-10-15.',
          'combo_rules_interactions_verified':'PASS — Jester library-exile permissions, Ashiok Weaver, Dauthi replacement effects, Jester\'s Scepter face-down exile, Lightning Greaves, Oracle/Consultation, Oracle/Tainted Pact, Breach/LED/Brain Freeze and Dragon\'s Smile alternative-cost interaction reviewed.',
          'consistency_test_complete':'PASS — approved artifact 100 cards / 100 distinct names / 34 lands / no repeats; singleton, U/B/R identity and candidate/approved SHA match PASS.',
          'multiplayer_test_complete_or_reason_not_applicable':'NOT APPLICABLE AS A FINALIZATION GATE — structural/rules/legality/strategy verified; no unsupported gameplay win-rate claim.',
          'final_gate_passed':'YES','final_list_hash':SHA,'user_approval_date':DATE,'refinement_status':f'APPROVED / LOCKED — current {CYCLE} cycle',
          'notes':f'CURRENT-CYCLE RECONCILIATION {DATE}: exact SHA-bound The Madcap Jester candidate approved and locked. Canonical hash: {SHA}. 100 cards, 100 distinct names, 34 lands, singleton/U-B-R PASS. Whole-list audit 94 KEEP / 5 CUT. Power Bracket 5 — cEDH. Tags: Exile Theft / Library Control / Grixis Combo. The Madcap Jester and Dragon\'s Smile remain registered future-release project exceptions and are not represented as officially Commander-legal on 2026-10-15. Next unlocked: The Rani (index 56 / deck 57 of 62).'}
        for k,v in vals.items():
            if k in ix: row[ix[k]]=v
        out=io.StringIO(); csv.writer(out,lineterminator='').writerow(row); lines[i]=out.getvalue(); break
else: raise SystemExit('Madcap tracker row missing')
T.write_text('\n'.join(lines)+'\n',encoding='utf-8')
reread=json.loads(S.read_text(encoding='utf-8'))['decks'][DECK_ID]
assert reread['approval_status']=='APPROVED' and reread['lock_status']=='LOCKED' and reread['approved_list_sha256']==SHA
assert hashlib.sha256(A.read_bytes()).hexdigest()==SHA
print('The Madcap Jester approval finalized')
