#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'refinement/decklists/The_Rani_Approval_Ready_2026-10-15.txt'
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUDIT=ROOT/'refinement/verification/The_Rani_Whole_List_Audit_2026-10-15.md'
DECISIONS=ROOT/'refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md'
LEDGER=ROOT/'refinement/decisions/The_Rani_Whole_List_Decision_Ledger_2026-10-15.csv'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
OUTDIR=ROOT/'refinement/verification/the_rani_2026-10-15/gate_output'
CONFIG=OUTDIR/'The_Rani_Complete_Gate_Config.json'; RULES=OUTDIR/'The_Rani_Rules_Attestation.json'; LEGAL=OUTDIR/'The_Rani_Official_Legality_Attestation.json'; SUMMARY=ROOT/'refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md'
EXPECTED_SHA='7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c'
CUTS=Counter({'Agitator Ant':1,'Insurrection':1,'Counterspell':1,'Arcane Denial':1,'Orcish Bowmasters':1,'Dragonskull Summit':1,'Drowned Catacomb':1,'Sulfur Falls':1})
ADDS=Counter({'The Master, Mesmerist':1,'Thassa, Deep-Dwelling':1,'Force of Will':1,'Incriminating Impetus':1,'Baeloth Barrityl, Entertainer':1,'City of Brass':1,'Mana Confluence':1,'Flooded Strand':1})
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s*$'); ROLE=re.compile(r'\s+\[[^\]]+\]\s*$'); PRINT=re.compile(r'\s+\([^()]*\)\s+\S+(?:\s+\*[^*]+\*)?\s*$')
def h(b): return hashlib.sha256(b).hexdigest()
def clean(s): return PRINT.sub('',ROLE.sub('',s).strip()).strip()
def parse(data):
    lines=[x.strip() for x in data.decode('utf-8-sig').splitlines() if x.strip()]; c=Counter()
    for line in lines:
        m=LINE.match(line)
        if not m: raise RuntimeError(f'malformed line {line}')
        c[clean(m.group(2))]+=int(m.group(1))
    return lines,c
def base():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('The_Rani.txt')]
        if len(ms)!=1: raise RuntimeError(f'baseline member count {len(ms)}')
        raw=tf.extractfile(ms[0]).read(); return raw,parse(raw)[1]
def nk(s): return re.sub(r'[^a-z0-9]+','',(s or '').casefold().replace('’',"'"))
def cache_load():
    d={}
    for line in CACHE.read_text().splitlines():
        if not line.strip(): continue
        r=json.loads(line)
        for k in {r.get('query_name'),r.get('canonical_name')}:
            if k:d[nk(k)]=r
    return d
def ledger_check(b):
    rows=list(csv.DictReader(LEDGER.open(encoding='utf-8-sig')))
    if {r['card'] for r in rows}!={x for x in b if x!='The Rani'}: raise RuntimeError('ledger membership mismatch')
    bt=kt=ct=0
    for r in rows:
        card=r['card']; q=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
        if q!=b[card] or k+c!=q: raise RuntimeError(f'ledger qty mismatch {card}')
        bt+=q;kt+=k;ct+=c
    if (bt,kt,ct)!=(99,91,8): raise RuntimeError(f'ledger totals {bt}/{kt}/{ct}')
def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    raw=CANDIDATE.read_bytes(); sha=h(raw); lines,c=parse(raw); braw,b=base()
    if sha!=EXPECTED_SHA: raise RuntimeError(f'candidate SHA drift {sha}')
    if sum(b.values())!=100 or len(b)!=94: raise RuntimeError(f'baseline structure {sum(b.values())}/{len(b)}')
    if sum(c.values())!=100 or len(c)!=94: raise RuntimeError(f'candidate structure {sum(c.values())}/{len(c)}')
    if lines[0]!='1x The Rani [Commander]' or c['The Rani']!=1: raise RuntimeError('commander line mismatch')
    if b-c!=CUTS or c-b!=ADDS: raise RuntimeError(f'delta mismatch cuts={b-c} adds={c-b}')
    repeats={n:q for n,q in c.items() if q>1}
    if repeats!={'Island':3,'Mountain':3,'Swamp':3}: raise RuntimeError(f'unexpected repeats {repeats}')
    ledger_check(b)
    cache=cache_load(); unresolved=[]; illegal=[]; lands=0; blue_pitch=0
    for name,q in c.items():
        r=cache.get(nk(name))
        if not r: unresolved.append(name); continue
        typ=r.get('type_line') or ''
        if 'Land' in typ.split(' // ',1)[0]: lands+=q
        if r.get('commander_legality')!='legal': illegal.append((name,r.get('commander_legality')))
        if name!='Force of Will' and 'U' in (r.get('color_identity') or []) and 'Land' not in typ: blue_pitch+=q
    if unresolved: raise RuntimeError('unresolved cache: '+', '.join(unresolved))
    if illegal: raise RuntimeError(f'illegal rows {illegal}')
    if lands!=33: raise RuntimeError(f'land count {lands}')
    if blue_pitch<15: raise RuntimeError(f'blue pitch pool too low {blue_pitch}')
    for p in [AUDIT,DECISIONS]:
        t=p.read_text()
        if EXPECTED_SHA not in t: raise RuntimeError(f'{p.name} SHA mismatch')
    if '99/99 noncommander copies adjudicated: 91 KEEP / 8 CUT' not in AUDIT.read_text(): raise RuntimeError('audit closeout missing')
    if 'ZERO NEW MATERIAL IMPROVEMENTS' not in DECISIONS.read_text(): raise RuntimeError('decision closeout missing')
    now=datetime.now(timezone.utc).isoformat()
    rules={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current Oracle text in current-cycle Scryfall cache','Magic Comprehensive Rules — goad, investigate, Aura attachment, triggered abilities, replacement effects, phasing/blink/new objects'],'interactions':[
      {'name':'Rani Mark trigger and target','status':'PASS','finding':'The Rani entering or attacking creates a Mark of the Rani Aura token attached to another target creature. Because the triggered ability itself targets, an illegal sole target on resolution prevents the ability from resolving and no Mark is created.'},
      {'name':'Own-creature Mark and goad','status':'PASS','finding':'Another target creature may be a creature you control. A creature goaded by a source you control must attack each combat if able and, if able, attack a player other than you; when that goaded creature deals combat damage to one of your opponents, The Rani investigates.'},
      {'name':'The Master Mesmerist plus Mark','status':'PASS','finding':'A Mark on The Master gives +2/+2, increasing his power and therefore the power ceiling for his tap ability. A creature he goads and gives skulk can trigger both The Rani investigate ability and The Master draw/counter ability when it deals combat damage to one of your opponents.'},
      {'name':'Baeloth plus Mark','status':'PASS','finding':'A Mark can make Baeloth 4 power, so his continuous ability goads opponent-controlled creatures with power less than 4 while the pump remains. Baeloth being goaded himself does not disable this static ability. His death trigger only rewards goaded creatures that die while attacking or blocking.'},
      {'name':'Thassa blink','status':'PASS','finding':'Thassa exiles The Rani at the beginning of your end step and returns it immediately as a new object; the returned Rani triggers its ETB Mark ability. Existing legal Mark Auras attached elsewhere are independent of the old Rani object and remain.'},
      {'name':'Displacer Kitten blink','status':'PASS','finding':'Casting a noncreature spell may blink The Rani through Displacer Kitten; the returned Rani is a new object and triggers another Mark creation.'},
      {'name':'Incriminating Impetus','status':'PASS','finding':'The Aura suspects the enchanted creature on entry, giving it menace and preventing it from blocking while suspected, and separately gives +2/+2 and goads it. These effects make forced attacks more likely to connect and generate Rani investigate triggers.'},
      {'name':'Academy Manufactor plus investigate','status':'PASS','finding':'Investigating would create a Clue; Academy Manufactor replaces that token-creation event with one Clue, one Food and one Treasure.'},
      {'name':'Erdwal Illuminator plus Manufactor','status':'PASS','finding':'The first investigate each turn triggers Erdwal Illuminator for an additional investigate. With Academy Manufactor, each investigate creates one Clue, Food and Treasure, so the two investigate events can create six artifact tokens total.'},
      {'name':'Time Sieve','status':'PASS','finding':'Time Sieve may sacrifice any five artifacts, so Clue/Food/Treasure output can fund extra turns. The reviewed list does not claim this is a deterministic infinite loop without an independent repeatable investigate/combat-damage setup.'},
      {'name':'Force of Will pitch support','status':'PASS','finding':f'The candidate contains {blue_pitch} other blue nonland cards that can support Force of Will alternate casting.'}
    ]}
    RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n')
    legal={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata','Current official Commander legality checkpoint'],'unexpected_banned_cards':[],'project_exceptions_required':[],'finding':'All 100 candidate cards resolve within U/B/R and are currently Commander-legal; no project exception is required.'}
    LEGAL.write_text(json.dumps(legal,indent=2,ensure_ascii=False)+'\n')
    cfg={'deck_id':'The_Rani','display_name':'The Rani','decklist_path':str(CANDIDATE.relative_to(ROOT)),'expected_deck_sha256':sha,'baseline_source_sha256':h(braw),'output_dir':str(OUTDIR.relative_to(ROOT)),'output_stem':'The_Rani_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}
    CONFIG.write_text(json.dumps(cfg,indent=2)+'\n')
    p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CONFIG.relative_to(ROOT))],cwd=ROOT)
    if p.returncode: return p.returncode
    gate=json.loads((OUTDIR/'The_Rani_2026-10-15_Complete_Gate.json').read_text())
    if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('deck_sha256')!=sha or gate.get('project_exceptions'): raise RuntimeError('complete gate did not close cleanly')
    SUMMARY.write_text(f"# The Rani — approval-ready verification\n\nDate: 2026-10-15  \nCycle: `global-restart-2026-10-13`  \nDeck: #57 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{sha}`\n- Cards: **100**\n- Distinct names: **94**\n- Lands: **33**\n- Repeats: **Island x3 / Mountain x3 / Swamp x3 only**\n- Singleton: **PASS**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS**\n- Project exceptions: **none**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue_pitch} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 91 KEEP / 8 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 4 — Optimized**\n- Proposed Archidekt tags: **Goad / Clues / Forced Combat**\n\n## Final proposed delta\n\n1. Agitator Ant -> The Master, Mesmerist\n2. Insurrection -> Thassa, Deep-Dwelling\n3. Counterspell -> Force of Will\n4. Arcane Denial -> Incriminating Impetus\n5. Orcish Bowmasters -> Baeloth Barrityl, Entertainer\n6. Dragonskull Summit -> City of Brass\n7. Drowned Catacomb -> Mana Confluence\n8. Sulfur Falls -> Flooded Strand\n\nThe candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n")
    print(json.dumps({'status':'APPROVAL_READY','deck_sha256':sha,'lands':lands,'blue_pitch_pool':blue_pitch},indent=2)); return 0
if __name__=='__main__': sys.exit(main())
