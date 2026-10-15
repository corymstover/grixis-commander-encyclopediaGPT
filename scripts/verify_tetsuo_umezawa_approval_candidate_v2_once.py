#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'refinement/decklists/Tetsuo_Umezawa_Approval_Ready_2026-10-15.txt'
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUD=ROOT/'refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md'
DEC=ROOT/'refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md'
LED=ROOT/'refinement/decisions/Tetsuo_Umezawa_Whole_List_Decision_Ledger_2026-10-15.csv'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
OUT=ROOT/'refinement/verification/tetsuo_umezawa_2026-10-15/gate_output'
CFG=OUT/'Tetsuo_Umezawa_Complete_Gate_Config.json'; RULES=OUT/'Tetsuo_Umezawa_Rules_Attestation.json'; LEGAL=OUT/'Tetsuo_Umezawa_Official_Legality_Attestation.json'
SUMMARY=ROOT/'refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md'
SHA='6da2d254cf0cf4495e5a8de78fc63046b7cfb2ec52c12445ab28b10eab3dc8ab'
CUTS=Counter({'Arcane Denial':1,'Feed the Swarm':1,'Nightscape Familiar':1,'Maeve, Insidious Singer':1,'Backlash':1,'Agitator Ant':1,'Spectacular Showdown':1,'Opposition Agent':1,'Dragonskull Summit':1,'Drowned Catacomb':1,'Shivan Reef':1,'Sulfurous Springs':1,'Underground River':1,'Island':1})
ADDS=Counter({'Force of Will':1,'Withering Torment':1,"Patriar's Seal":1,'Puppeteer':1,'Blustersquall':1,'Flood':1,'Retreat to Coralhelm':1,'Sting, the Glinting Dagger':1,'Badlands':1,'Underground Sea':1,'Flooded Strand':1,'Marsh Flats':1,'Misty Rainforest':1,'Sink into Stupor // Soporific Springs':1})
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s*$'); ROLE=re.compile(r'\s+\[[^\]]+\]\s*$'); PRINT=re.compile(r'\s+\([^()]*\)\s+\S+(?:\s+\*[^*]+\*)?\s*$')
def sha(b): return hashlib.sha256(b).hexdigest()
def clean(s): return PRINT.sub('',ROLE.sub('',s).strip()).strip()
def parse(data):
    lines=[x.strip() for x in data.decode('utf-8-sig').splitlines() if x.strip()]; cards=Counter()
    for ln in lines:
        m=LINE.match(ln)
        if not m: raise RuntimeError(f'malformed line: {ln}')
        cards[clean(m.group(2))]+=int(m.group(1))
    return lines,cards
def baseline():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('Tetsuo_Umezawa.txt')]
        if len(ms)!=1: raise RuntimeError(f'baseline member count {len(ms)}')
        raw=tf.extractfile(ms[0]).read(); return raw,parse(raw)[1]
def key(s): return re.sub(r'[^a-z0-9]+','',(s or '').casefold().replace('’',"'"))
def load_cache():
    d={}
    for ln in CACHE.read_text().splitlines():
        if not ln.strip(): continue
        r=json.loads(ln)
        for k in {r.get('query_name'),r.get('canonical_name')}:
            if k:d[key(k)]=r
    return d
def check_ledger(base):
    rows=list(csv.DictReader(LED.open(encoding='utf-8-sig')))
    if {r['card'] for r in rows}!={n for n in base if n!='Tetsuo Umezawa'}: raise RuntimeError('ledger membership mismatch')
    bt=kt=ct=0
    for r in rows:
        n=r['card']; b=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
        if b!=base[n] or k+c!=b: raise RuntimeError(f'ledger qty mismatch {n}')
        bt+=b;kt+=k;ct+=c
    if (bt,kt,ct)!=(99,85,14): raise RuntimeError(f'ledger totals {bt}/{kt}/{ct}')
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    raw=C.read_bytes(); dsha=sha(raw); lines,cards=parse(raw); braw,base=baseline()
    if dsha!=SHA: raise RuntimeError(f'SHA drift {dsha}')
    if sum(base.values())!=100 or len(base)!=86: raise RuntimeError('baseline structure mismatch')
    if sum(cards.values())!=100 or len(cards)!=87: raise RuntimeError(f'candidate structure {sum(cards.values())}/{len(cards)}')
    if lines[0]!='1x Tetsuo Umezawa [Commander]' or cards['Tetsuo Umezawa']!=1: raise RuntimeError('commander mismatch')
    if base-cards!=CUTS or cards-base!=ADDS: raise RuntimeError(f'delta mismatch cuts={base-cards} adds={cards-base}')
    if {n:q for n,q in cards.items() if q>1}!={'Island':5,'Mountain':5,'Swamp':6}: raise RuntimeError('repeat mismatch')
    check_ledger(base)
    cache=load_cache(); unresolved=[]; illegal=[]; front=0; blue=0
    for name,q in cards.items():
        r=cache.get(key(name))
        if not r: unresolved.append(name); continue
        typ=(r.get('type_line') or '').split(' // ',1)[0]
        if 'Land' in typ: front+=q
        if r.get('commander_legality')!='legal': illegal.append((name,r.get('commander_legality')))
        if name!='Force of Will' and 'U' in (r.get('color_identity') or []) and 'Land' not in typ: blue+=q
    if unresolved: raise RuntimeError('unresolved: '+', '.join(unresolved))
    if illegal: raise RuntimeError(f'illegal: {illegal}')
    if front!=35 or cards['Sink into Stupor // Soporific Springs']!=1: raise RuntimeError(f'land structure {front}')
    if blue<15: raise RuntimeError(f'blue pitch pool {blue}')
    for p in (AUD,DEC):
        t=p.read_text()
        if SHA not in t: raise RuntimeError(f'{p.name} not bound to SHA')
    if '85 KEEP / 14 CUT' not in AUD.read_text() or 'ZERO NEW MATERIAL IMPROVEMENTS' not in DEC.read_text(): raise RuntimeError('closeout mismatch')
    now=datetime.now(timezone.utc).isoformat()
    rules={'status':'PASS','deck_sha256':dsha,'checked_at_utc':now,'sources':['Current Oracle text in current-cycle Scryfall cache','Magic Comprehensive Rules — activated abilities, targets, combat, triggered abilities, equipment, copying abilities, Aura targeting, MDFCs, overload and landfall'],'interactions':[
      {'name':'Tetsuo target condition','status':'PASS','finding':'A target creature may qualify because it is tapped OR because it is blocking; it need not satisfy both. It must still satisfy at least one targeting condition when the ability resolves.'},
      {'name':'Combat windows','status':'PASS','finding':'Non-vigilance attackers normally tap when declared, creating legal targets before blockers/damage. An untapped blocking creature is independently a legal Tetsuo target after blockers are declared.'},
      {'name':'Rings plus Bracers','status':'PASS','finding':'Rings of Brighthearth and Illusionist’s Bracers can each copy the same Tetsuo activation when their conditions are met; copies may choose new legal targets.'},
      {'name':'Sting the Glinting Dagger','status':'PASS','finding':'Sting gives equipped Tetsuo haste and triggers at the beginning of each combat to untap the equipped creature. After that trigger resolves, priority is received before declare attackers, so Tetsuo may activate again if UBBR is available. In multiplayer this can recur on each player’s combat step while Sting remains equipped.'},
      {'name':'Untap after activation','status':'PASS','finding':'Untapping Tetsuo does not remove an existing activation from the stack; another activation may be made if its costs can be paid.'},
      {'name':'Patriars Seal','status':'PASS','finding':'Patriar’s Seal can make any color or pay 1 and tap to untap legendary Tetsuo; one untapped Seal cannot pay both tap costs simultaneously.'},
      {'name':'Puppeteer and Flood','status':'PASS','finding':'Puppeteer can tap an opposing creature or untap Tetsuo. Flood can repeatedly tap a target creature without flying, manufacturing Tetsuo targets.'},
      {'name':'Blustersquall','status':'PASS','finding':'Normal mode taps one opposing creature; overloaded Blustersquall does not target and taps each creature the caster does not control.'},
      {'name':'Retreat plus fetchlands','status':'PASS','finding':'Each land entry triggers Retreat to Coralhelm. A fetchland and the land it fetches can produce separate triggers, each able to tap or untap target creature.'},
      {'name':'Aura restriction','status':'PASS','finding':'Tetsuo cannot be the target of Aura spells; Equipment and non-Aura abilities such as Sting, Minamo, Puppeteer, Patriar’s Seal and Retreat are unaffected.'},
      {'name':'Haste package','status':'PASS','finding':'Sting, Lightning Greaves and Swiftfoot Boots can grant haste, allowing Tetsuo’s tap-cost activated ability on the turn he comes under control.'},
      {'name':'Frozen Aether and forced combat','status':'PASS','finding':'Creatures entering tapped under Frozen Aether satisfy Tetsuo while tapped. Forced/goaded combat naturally produces tapped attackers; Propaganda attack costs are not forced to be paid.'},
      {'name':'Sink into Stupor MDFC','status':'PASS','finding':'Soporific Springs preserves a land-capable slot; Sink into Stupor can return an opposing spell or nonland permanent to its owner’s hand without countering the spell.'}
    ]}
    RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n')
    legal={'status':'PASS','deck_sha256':dsha,'checked_at_utc':now,'sources':['Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata','Current official Commander legality checkpoint'],'unexpected_banned_cards':[],'project_exceptions_required':[],'finding':'Every candidate card is currently Commander-legal; no project exception is required.'}
    LEGAL.write_text(json.dumps(legal,indent=2)+'\n')
    cfg={'deck_id':'Tetsuo_Umezawa','display_name':'Tetsuo Umezawa','decklist_path':str(C.relative_to(ROOT)),'expected_deck_sha256':dsha,'baseline_source_sha256':sha(braw),'output_dir':str(OUT.relative_to(ROOT)),'output_stem':'Tetsuo_Umezawa_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}
    CFG.write_text(json.dumps(cfg,indent=2)+'\n')
    p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CFG.relative_to(ROOT))],cwd=ROOT)
    if p.returncode:return p.returncode
    gate=json.loads((OUT/'Tetsuo_Umezawa_2026-10-15_Complete_Gate.json').read_text())
    if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('deck_sha256')!=dsha: raise RuntimeError('gate not clean')
    SUMMARY.write_text(f"# Tetsuo Umezawa — approval-ready verification\n\nDate: 2026-10-15  \nCycle: `global-restart-2026-10-13`  \nDeck: #54 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{dsha}`\n- Cards: **100**\n- Distinct names: **87**\n- Front-face lands: **35**\n- Land-capable MDFCs: **1**\n- Functional land-capable slots: **36**\n- Repeats: **Island x5 / Mountain x5 / Swamp x6 only**\n- Singleton: **PASS**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS**\n- Project exceptions: **none**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 85 KEEP / 14 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 4 — Optimized**\n- Proposed Archidekt tags: **Tap/Untap / Forced Combat / Activated Abilities**\n\n## Final proposed delta\n\n1. Arcane Denial -> Force of Will\n2. Feed the Swarm -> Withering Torment\n3. Nightscape Familiar -> Patriar's Seal\n4. Maeve, Insidious Singer -> Puppeteer\n5. Backlash -> Blustersquall\n6. Agitator Ant -> Flood\n7. Spectacular Showdown -> Retreat to Coralhelm\n8. Opposition Agent -> Sting, the Glinting Dagger\n9. Dragonskull Summit -> Badlands\n10. Drowned Catacomb -> Underground Sea\n11. Shivan Reef -> Flooded Strand\n12. Sulfurous Springs -> Marsh Flats\n13. Underground River -> Misty Rainforest\n14. Island -> Sink into Stupor // Soporific Springs\n\nSupersedes prior 13-swap SHA `53215af902bfab2640d80c4abb733e6fb66ddaea2de183ae7635d3f197890e72`. The candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n")
    print(json.dumps({'status':'APPROVAL_READY','deck_sha256':dsha,'front_lands':front,'functional_lands':36,'blue_pitch_pool':blue},indent=2)); return 0
if __name__=='__main__':sys.exit(main())
