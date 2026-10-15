import csv, hashlib, io, json
from pathlib import Path

SHA='cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03'
CYCLE='global-restart-2026-10-13'; DATE='2026-10-14'; DECK='Kefka__Court_Mage'
cand=Path('refinement/decklists/Kefka_Court_Mage_Approval_Candidate_2026-10-14.txt')
appr=Path('refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt')
gatep=Path('refinement/verification/kefka_court_mage_2026-10-14/gate_output/Kefka_Court_Mage_2026-10-14_Complete_Gate.json')
statep=Path('state/current_deck_overrides.json'); trackp=Path('refinement/Deck_Refinement_Tracker_2026-10-12.csv')
record=Path('refinement/approvals/Kefka_Court_Mage_Approved_2026-10-14.md')
raw=cand.read_bytes()
assert hashlib.sha256(raw).hexdigest()==SHA
g=json.loads(gatep.read_text())
assert g['deck_sha256']==SHA and g['overall_result']=='APPROVAL_READY' and not g['errors']
assert g['count']==100 and g['distinct_names']==100 and sorted(g['commander_color_identity'])==['B','R','U']
assert g['rules_gate']=='PASS' and g['official_legality_gate']=='PASS' and not g['project_exceptions']
appr.write_bytes(raw); assert hashlib.sha256(appr.read_bytes()).hexdigest()==SHA
s=json.loads(statep.read_text()); assert s['cycle_id']==CYCLE
s.setdefault('decks',{})[DECK]={
 'approval_status':'APPROVED','lock_status':'LOCKED','final_gate_passed':True,'user_approval_date':DATE,'current_stage':'LOCKED',
 'approved_list_sha256':SHA,'quality_gate_version':'Deck Quality Gates v3 + mandatory whole-list audit + Complete Approval Gate v1',
 'approval_basis':'Explicit user approval of exact SHA-bound revised Kefka candidate after complete current-cycle audit and clean fail-closed gate.',
 'complete_gate_artifact':str(gatep),'whole_list_audit_artifact':'refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md',
 'approval_record_artifact':str(record),'approved_list_artifact':str(appr)}
statep.write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
record.parent.mkdir(parents=True,exist_ok=True)
record.write_text(f'''# Kefka, Court Mage // Kefka, Ruler of Ruin — APPROVED / LOCKED

Cycle: `{CYCLE}`  
Approval date: {DATE}  
Approved SHA-256: `{SHA}`  
Power Bracket: **5 — cEDH**  
Archidekt tags: **Discard / Trigger Copy / Turbo**

Verification: 100 cards; 100 distinct names; 28 lands; B/R/U identity PASS; rules PASS; official Commander legality PASS; no project exceptions; fresh Oracle cache PASS; complete gate APPROVAL_READY with zero errors.

Final red-team corrections before approval: `Cyclonic Rift -> Valley Floodcaller`; `Opposition Agent -> Demonic Counsel`; `Psychosis Crawler -> Fellwar Stone`.

This deck is locked unless explicitly reopened by the user.
''')
lines=trackp.read_text().splitlines(); head=next(csv.reader([lines[0]])); ix={v:i for i,v in enumerate(head)}
for i in range(1,len(lines)):
 row=next(csv.reader([lines[i]]))
 if row[ix['deck_id']]==DECK:
  row += ['']*(len(head)-len(row))
  vals={'baseline_status':'CURRENT APPROVED FINAL LIST — current-cycle canonical list locked; frozen source exports preserved unchanged.','final_gate_passed':'YES','final_list_hash':SHA,'user_approval_date':DATE,'refinement_status':f'APPROVED / LOCKED — current {CYCLE} cycle','consistency_test_complete':'PASS — exact approved artifact verified at 100 cards / 100 distinct names / 28 lands; candidate and approved artifact byte-match SHA.','swap_decision_ledger_complete':'PASS — exact 19-swap SHA-bound revised Kefka candidate explicitly approved by user on 2026-10-14.','notes':f'CURRENT-CYCLE RECONCILIATION {DATE}: Kefka explicitly approved and locked at SHA {SHA}. 100 cards / 100 names / 28 lands; B/R/U, rules, legality PASS; no exceptions; PB5 cEDH; next unlocked deck: Kess, Dissident Mage.'}
  for k,v in vals.items(): row[ix[k]]=v
  out=io.StringIO(); csv.writer(out,lineterminator='').writerow(row); lines[i]=out.getvalue(); break
else: raise SystemExit('Kefka tracker row missing')
trackp.write_text('\n'.join(lines)+'\n')
print('Kefka approval finalized')
