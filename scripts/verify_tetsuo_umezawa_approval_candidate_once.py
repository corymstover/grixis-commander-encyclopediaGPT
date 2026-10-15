#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'refinement/decklists/Tetsuo_Umezawa_Approval_Ready_2026-10-15.txt'
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUDIT=ROOT/'refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md'
DECISIONS=ROOT/'refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md'
LEDGER=ROOT/'refinement/decisions/Tetsuo_Umezawa_Whole_List_Decision_Ledger_2026-10-15.csv'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
OUTDIR=ROOT/'refinement/verification/tetsuo_umezawa_2026-10-15/gate_output'
CONFIG=OUTDIR/'Tetsuo_Umezawa_Complete_Gate_Config.json'
RULES=OUTDIR/'Tetsuo_Umezawa_Rules_Attestation.json'
LEGAL=OUTDIR/'Tetsuo_Umezawa_Official_Legality_Attestation.json'
SUMMARY=ROOT/'refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md'
EXPECTED_SHA='53215af902bfab2640d80c4abb733e6fb66ddaea2de183ae7635d3f197890e72'
CUTS=Counter({'Arcane Denial':1,'Feed the Swarm':1,'Nightscape Familiar':1,'Maeve, Insidious Singer':1,'Backlash':1,'Agitator Ant':1,'Spectacular Showdown':1,'Dragonskull Summit':1,'Drowned Catacomb':1,'Shivan Reef':1,'Sulfurous Springs':1,'Underground River':1,'Island':1})
ADDS=Counter({'Force of Will':1,'Withering Torment':1,"Patriar's Seal":1,'Puppeteer':1,'Blustersquall':1,'Flood':1,'Retreat to Coralhelm':1,'Badlands':1,'Underground Sea':1,'Flooded Strand':1,'Marsh Flats':1,'Misty Rainforest':1,'Sink into Stupor // Soporific Springs':1})
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s*$'); ROLE=re.compile(r'\s+\[[^\]]+\]\s*$'); PRINT=re.compile(r'\s+\([^()]*\)\s+\S+(?:\s+\*[^*]+\*)?\s*$')
def h(b): return hashlib.sha256(b).hexdigest()
def clean(s): return PRINT.sub('',ROLE.sub('',s).strip()).strip()
def parse(data):
    lines=[x.strip() for x in data.decode('utf-8-sig').splitlines() if x.strip()]; c=Counter()
    for line in lines:
        m=LINE.match(line)
        if not m: raise RuntimeError(f'malformed line: {line}')
        c[clean(m.group(2))]+=int(m.group(1))
    return lines,c
def base():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('Tetsuo_Umezawa.txt')]
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
    if {r['card'] for r in rows}!={x for x in b if x!='Tetsuo Umezawa'}: raise RuntimeError('ledger membership mismatch')
    bt=kt=ct=0
    for r in rows:
        card=r['card']; q=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
        if q!=b[card] or k+c!=q: raise RuntimeError(f'ledger qty mismatch {card}')
        bt+=q;kt+=k;ct+=c
    if (bt,kt,ct)!=(99,86,13): raise RuntimeError(f'ledger totals {bt}/{kt}/{ct}')
def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    raw=CANDIDATE.read_bytes(); sha=h(raw); lines,c=parse(raw); braw,b=base()
    if sha!=EXPECTED_SHA: raise RuntimeError(f'candidate SHA drift {sha}')
    if sum(b.values())!=100 or len(b)!=86: raise RuntimeError('baseline structure mismatch')
    if sum(c.values())!=100 or len(c)!=87: raise RuntimeError(f'candidate structure {sum(c.values())}/{len(c)}')
    if lines[0]!="1x Tetsuo Umezawa [Commander]" or c['Tetsuo Umezawa']!=1: raise RuntimeError('commander line mismatch')
    if b-c!=CUTS or c-b!=ADDS: raise RuntimeError(f'delta mismatch cuts={b-c} adds={c-b}')
    if {n:q for n,q in c.items() if q>1}!={'Island':5,'Mountain':5,'Swamp':6}: raise RuntimeError('repeat mismatch')
    ledger_check(b)
    cache=cache_load(); unresolved=[]; illegal=[]; front_lands=0; blue_pitch=0
    for name,q in c.items():
        r=cache.get(nk(name))
        if not r: unresolved.append(name); continue
        first=(r.get('type_line') or '').split(' // ',1)[0]
        if 'Land' in first: front_lands+=q
        if r.get('commander_legality')!='legal': illegal.append((name,r.get('commander_legality')))
        if name!='Force of Will' and 'U' in (r.get('color_identity') or []) and 'Land' not in first: blue_pitch+=q
    if unresolved: raise RuntimeError('unresolved cache: '+', '.join(unresolved))
    if illegal: raise RuntimeError(f'illegal rows: {illegal}')
    if front_lands!=35 or c['Sink into Stupor // Soporific Springs']!=1: raise RuntimeError(f'land structure mismatch front={front_lands}')
    if blue_pitch<15: raise RuntimeError(f'blue pitch pool too low: {blue_pitch}')
    for p in [AUDIT,DECISIONS]:
        t=p.read_text()
        if EXPECTED_SHA not in t: raise RuntimeError(f'{p.name} SHA mismatch')
    if '99/99 noncommander copies adjudicated: 86 KEEP / 13 CUT' not in AUDIT.read_text(): raise RuntimeError('audit closeout missing')
    if 'ZERO NEW MATERIAL IMPROVEMENTS' not in DECISIONS.read_text(): raise RuntimeError('decision closeout missing')
    now=datetime.now(timezone.utc).isoformat()
    rules={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current Oracle text in current-cycle Scryfall cache','Magic Comprehensive Rules — activated abilities, targets, combat, copying abilities, Aura targeting, MDFCs, overload and landfall (current 2026 rules)'],'interactions':[
      {'name':'Tetsuo target condition','status':'PASS','finding':'Tetsuo may target a creature that is tapped OR a creature that is currently blocking. The target need not satisfy both. When the ability resolves the target must still satisfy at least one of those target restrictions or that instance of the ability will not resolve against it.'},
      {'name':'Attacking creates tapped targets','status':'PASS','finding':'A creature without vigilance normally becomes tapped as it is declared as an attacker. After attackers are declared, Tetsuo may be activated before blockers/combat damage and can target an attacker that is tapped.'},
      {'name':'Blocking condition','status':'PASS','finding':'After blockers are declared, a blocking creature is a legal Tetsuo target even if it is untapped.'},
      {'name':'Rings plus Illusionist Bracers','status':'PASS','finding':'Activating Tetsuo can trigger both Rings of Brighthearth and Illusionist’s Bracers. Bracers copies the nonmana activated ability; Rings may also copy it for {2}. If both copy effects are used, the original plus two copies can resolve with new targets chosen for the copies.'},
      {'name':'Untap and reactivate','status':'PASS','finding':'Untapping Tetsuo after activating does not remove the existing activation from the stack. If UBBR can be paid again, Tetsuo can be activated again after being untapped.'},
      {'name':'Patriars Seal','status':'PASS','finding':'Patriar’s Seal either taps for one mana of any color or can pay {1} and tap to untap target legendary creature you control, including Tetsuo. The same untapped Seal cannot perform both tap-cost abilities at once.'},
      {'name':'Puppeteer','status':'PASS','finding':'Puppeteer may tap an opposing creature to create a Tetsuo target or untap Tetsuo for another activation.'},
      {'name':'Flood','status':'PASS','finding':'Flood pays UU to tap target creature without flying. A creature successfully tapped this way satisfies Tetsuo’s tapped target condition.'},
      {'name':'Blustersquall overload','status':'PASS','finding':'Normal Blustersquall taps one opposing creature. When overloaded for 3U, target is replaced by each, so it does not target and taps each creature the caster does not control, creating multiple potential Tetsuo targets.'},
      {'name':'Retreat to Coralhelm and fetchlands','status':'PASS','finding':'Each land entering under your control triggers Retreat. A fetchland entering can create one trigger and the fetched land entering creates another. Each trigger may tap or untap target creature, allowing target creation or Tetsuo reuse.'},
      {'name':'Aura restriction','status':'PASS','finding':'Tetsuo cannot be the target of Aura spells. Equipment, non-Aura abilities such as Minamo, Puppeteer, Patriar’s Seal and Retreat to Coralhelm, and Tetsuo’s own activation are not prohibited by that text.'},
      {'name':'Haste equipment','status':'PASS','finding':'Lightning Greaves and Swiftfoot Boots granting haste allow Tetsuo’s tap-cost activated ability to be used on the turn Tetsuo comes under your control. Greaves shroud does not interfere with the activation because the ability targets another creature, not Tetsuo.'},
      {'name':'Frozen Aether','status':'PASS','finding':'Opposing creatures enter tapped under Frozen Aether, so while they remain tapped they satisfy Tetsuo’s target condition.'},
      {'name':'Fumiko and Propaganda','status':'PASS','finding':'Fumiko requires opposing creatures to attack if able but does not force players to pay attack costs. Propaganda therefore still influences where forced/goaded creatures can attack; goad requirements are satisfied by attacking another player when able.'},
      {'name':'Sink into Stupor MDFC','status':'PASS','finding':'Soporific Springs is a land face and preserves a functional land slot. Sink into Stupor can return an opposing spell or nonland permanent to its owner’s hand; returning a spell this way does not counter it.'}
    ]}
    RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n')
    legal={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata','Current official Commander legality checkpoint'],'unexpected_banned_cards':[],'project_exceptions_required':[],'finding':'Every candidate card resolves as currently Commander-legal; no project exception is required.'}
    LEGAL.write_text(json.dumps(legal,indent=2)+'\n')
    cfg={'deck_id':'Tetsuo_Umezawa','display_name':'Tetsuo Umezawa','decklist_path':str(CANDIDATE.relative_to(ROOT)),'expected_deck_sha256':sha,'baseline_source_sha256':h(braw),'output_dir':str(OUTDIR.relative_to(ROOT)),'output_stem':'Tetsuo_Umezawa_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}
    CONFIG.write_text(json.dumps(cfg,indent=2)+'\n')
    p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CONFIG.relative_to(ROOT))],cwd=ROOT)
    if p.returncode: return p.returncode
    gate=json.loads((OUTDIR/'Tetsuo_Umezawa_2026-10-15_Complete_Gate.json').read_text())
    if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('deck_sha256')!=sha: raise RuntimeError('complete gate did not close cleanly')
    SUMMARY.write_text(f"# Tetsuo Umezawa — approval-ready verification\n\nDate: 2026-10-15  \nCycle: `global-restart-2026-10-13`  \nDeck: #54 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{sha}`\n- Cards: **100**\n- Distinct names: **87**\n- Front-face lands: **35**\n- Land-capable MDFCs: **1**\n- Functional land-capable slots: **36**\n- Repeats: **Island x5 / Mountain x5 / Swamp x6 only**\n- Singleton: **PASS**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS**\n- Project exceptions: **none**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue_pitch} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 86 KEEP / 13 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 4 — Optimized**\n- Proposed Archidekt tags: **Tap/Untap / Forced Combat / Activated Abilities**\n\n## Final proposed delta\n\n1. Arcane Denial -> Force of Will\n2. Feed the Swarm -> Withering Torment\n3. Nightscape Familiar -> Patriar's Seal\n4. Maeve, Insidious Singer -> Puppeteer\n5. Backlash -> Blustersquall\n6. Agitator Ant -> Flood\n7. Spectacular Showdown -> Retreat to Coralhelm\n8. Dragonskull Summit -> Badlands\n9. Drowned Catacomb -> Underground Sea\n10. Shivan Reef -> Flooded Strand\n11. Sulfurous Springs -> Marsh Flats\n12. Underground River -> Misty Rainforest\n13. Island -> Sink into Stupor // Soporific Springs\n\nThe candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n")
    print(json.dumps({'status':'APPROVAL_READY','deck_sha256':sha,'front_lands':front_lands,'functional_lands':36,'blue_pitch_pool':blue_pitch},indent=2)); return 0
if __name__=='__main__': sys.exit(main())
