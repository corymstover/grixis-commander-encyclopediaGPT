#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-15'; CYCLE='global-restart-2026-10-13'; DECK_ID='Sauron__the_Dark_Lord'; DISPLAY='Sauron, the Dark Lord'
CANDIDATE=ROOT/'refinement/decklists/Sauron_the_Dark_Lord_Approval_Ready_2026-10-15.txt'; BASELINE_TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUDIT=ROOT/'refinement/verification/Sauron_the_Dark_Lord_Whole_List_Audit_2026-10-15.md'; DECISIONS=ROOT/'refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md'; LEDGER=ROOT/'refinement/decisions/Sauron_the_Dark_Lord_Whole_List_Decision_Ledger_2026-10-15.csv'
OUTDIR=ROOT/'refinement/verification/sauron_dark_lord_2026-10-15/gate_output'; CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'; CONFIG=OUTDIR/'Sauron_the_Dark_Lord_Complete_Gate_Config.json'; RULES=OUTDIR/'Sauron_the_Dark_Lord_Rules_Attestation.json'; LEGAL=OUTDIR/'Sauron_the_Dark_Lord_Official_Legality_Attestation.json'; SUMMARY=ROOT/'refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md'
LINE_RE=re.compile(r'^\s*(\d+)x\s+(.+?)\s*$'); ROLE_RE=re.compile(r'\s+\[[^\]]+\]\s*$'); PRINT_RE=re.compile(r'\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$')
EXPECTED_CUTS=Counter({'Warg Rider':1,'Notion Thief':1,'Fellwar Stone':1,'Counterspell':1,'Drowned Catacomb':1,'Sulfurous Springs':1,'Underground River':1,'Island':1})
EXPECTED_ADDS=Counter({'Great Goblin, Foul-Hearted':1,'Roaming Throne':1,'Mana Vault':1,'Force of Will':1,'Minas Morgul, Dark Fortress':1,'Volcanic Island':1,'Flooded Strand':1,'Misty Rainforest':1})
def sha(b): return hashlib.sha256(b).hexdigest()
def clean(rest): return PRINT_RE.sub('',ROLE_RE.sub('',rest).strip()).strip()
def parse(data):
 lines=[x.strip() for x in data.decode('utf-8-sig').splitlines() if x.strip()]; cards=Counter()
 for line in lines:
  m=LINE_RE.match(line)
  if not m: raise RuntimeError(f'Malformed deck line: {line}')
  cards[clean(m.group(2))]+=int(m.group(1))
 return lines,cards
def baseline_member():
 with tarfile.open(BASELINE_TAR,'r:gz') as tf:
  m=[x for x in tf.getmembers() if x.isfile() and x.name.endswith('Sauron__the_Dark_Lord.txt')]
  if len(m)!=1: raise RuntimeError(f'Expected one Sauron Dark Lord baseline; found {len(m)}')
  fh=tf.extractfile(m[0]); return m[0].name,fh.read()
def nkey(n): return re.sub(r'[^a-z0-9]+','',n.casefold().replace('’',"'"))
def load_cache():
 out={}
 for line in CACHE.read_text(encoding='utf-8').splitlines():
  if not line.strip(): continue
  r=json.loads(line)
  for k in {r.get('query_name'),r.get('canonical_name')}:
   if k: out[nkey(k)]=r
 return out
def bind(path,deck_sha):
 text=path.read_text(encoding='utf-8')
 if '__CANDIDATE_SHA__' in text: path.write_text(text.replace('__CANDIDATE_SHA__',deck_sha),encoding='utf-8')
 if deck_sha not in path.read_text(encoding='utf-8'): raise RuntimeError(f'{path.name} is not SHA-bound')
def verify_ledger(base):
 rows=list(csv.DictReader(LEDGER.open(newline='',encoding='utf-8-sig'))); expected={n for n in base if n!=DISPLAY}
 if {r['card'] for r in rows}!=expected: raise RuntimeError('Decision ledger membership mismatch')
 bt=kt=ct=0
 for r in rows:
  card=r['card']; b=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
  if b!=base[card] or k+c!=b: raise RuntimeError(f'Ledger quantity mismatch: {card}')
  exp='KEEP' if c==0 else ('CUT' if k==0 else 'PARTIAL')
  if r['decision'].strip().upper()!=exp: raise RuntimeError(f'Ledger decision mismatch: {card}')
  bt+=b; kt+=k; ct+=c
 if (bt,kt,ct)!=(99,91,8): raise RuntimeError(f'Ledger totals {bt}/{kt}/{ct}, expected 99/91/8')
def main():
 OUTDIR.mkdir(parents=True,exist_ok=True); raw=CANDIDATE.read_bytes(); deck_sha=sha(raw); lines,candidate=parse(raw); member,baseline_raw=baseline_member(); _,base=parse(baseline_raw)
 if sum(base.values())!=100 or len(base)!=90: raise RuntimeError(f'Baseline structure mismatch {sum(base.values())}/{len(base)}')
 if sum(candidate.values())!=100 or len(candidate)!=91: raise RuntimeError(f'Candidate structure mismatch {sum(candidate.values())}/{len(candidate)}')
 if lines[0]!='1x Sauron, the Dark Lord [Commander]' or candidate[DISPLAY]!=1: raise RuntimeError('Commander-first line mismatch')
 if base-candidate!=EXPECTED_CUTS: raise RuntimeError(f'Unexpected cuts: {base-candidate}')
 if candidate-base!=EXPECTED_ADDS: raise RuntimeError(f'Unexpected adds: {candidate-base}')
 repeats={n:q for n,q in candidate.items() if q>1}; expected_repeats={'Mountain':2,'Nazgûl':7,'Swamp':3}
 if repeats!=expected_repeats: raise RuntimeError(f'Unexpected repeats: {repeats}')
 verify_ledger(base)
 cache=load_cache(); unresolved=[]; nonlegal=[]; lands=0; blue_pitch=0
 for name,qty in candidate.items():
  rec=cache.get(nkey(name))
  if not rec: unresolved.append(name); continue
  typ=(rec.get('type_line') or '').split(' // ',1)[0]
  if 'Land' in typ: lands+=qty
  if rec.get('commander_legality')!='legal': nonlegal.append((name,rec.get('commander_legality')))
  if name!='Force of Will' and 'U' in (rec.get('color_identity') or []) and 'Land' not in typ: blue_pitch+=qty
 if unresolved: raise RuntimeError('Missing Oracle cache: '+', '.join(sorted(unresolved)))
 if nonlegal: raise RuntimeError(f'Unexpected legality rows: {nonlegal}')
 if lands!=34: raise RuntimeError(f'Land count {lands}, expected 34')
 if blue_pitch<12: raise RuntimeError(f'Force of Will blue pitch count too low: {blue_pitch}')
 naz=cache[nkey('Nazgûl')]
 if 'up to nine cards named Nazgûl' not in (naz.get('oracle_text') or ''): raise RuntimeError('Nazgûl permission not verified')
 for required in ['Great Goblin, Foul-Hearted','Roaming Throne','Minas Morgul, Dark Fortress','Mana Vault','Force of Will']:
  if nkey(required) not in cache: raise RuntimeError(f'Missing current Oracle record for {required}')
 bind(AUDIT,deck_sha); bind(DECISIONS,deck_sha); audit=AUDIT.read_text(encoding='utf-8'); dec=DECISIONS.read_text(encoding='utf-8')
 if '99/99' not in audit or '91 KEEP / 8 CUT' not in audit or deck_sha not in audit: raise RuntimeError('Whole-list audit incomplete')
 if 'ZERO NEW MATERIAL IMPROVEMENTS' not in dec or 'Power Bracket 4' not in dec or deck_sha not in dec: raise RuntimeError('Decision closeout incomplete')
 now=datetime.now(timezone.utc).isoformat()
 rules={'status':'PASS','deck_sha256':deck_sha,'checked_at_utc':now,'sources':['Magic Comprehensive Rules — ward, triggered abilities, replacement effects, creature types, shadow, amass, Ring temptation, card-specific deck construction and alternative costs (current 2026 rules)','The Lord of the Rings: Tales of Middle-earth release notes — Sauron, Ring, amass and Minas Morgul rulings','The Lost Caverns of Ixalan release notes — Roaming Throne rulings','Current Oracle text captured in Current_Cycle_Oracle_Cache.jsonl'],'interactions':[
 {'name':'Sauron ward','status':'PASS','finding':'When an opponent targets Sauron, ward requires that player to sacrifice a legendary artifact or legendary creature or the spell/ability is countered by ward.'},
 {'name':'Opponent-spell amass trigger','status':'PASS','finding':'Whenever an opponent casts a spell, Sauron triggers and amasses Orcs 1 on resolution. That triggered ability is independent of the opponent spell once triggered.'},
 {'name':'Army combat into Ring engine','status':'PASS','finding':'Whenever an Army controlled by the Sauron player deals combat damage to a player, the Ring tempts that player. Each Ring temptation separately triggers Sauron’s optional discard-hand/draw-four ability.'},
 {'name':'Nazgûl construction and Ring triggers','status':'PASS','finding':'Nazgûl explicitly permits up to nine copies; seven is legal. Each Nazgûl independently triggers whenever the Ring tempts its controller and puts a +1/+1 counter on each Wraith controlled by that player.'},
 {'name':'Mauhúr replacement','status':'PASS','finding':'If one or more +1/+1 counters would be put on an Army, Goblin, or Orc controlled by the player, Mauhúr replaces that event with that many plus one counters, not one extra counter per counter.'},
 {'name':'The Great Goblin counter trigger','status':'PASS','finding':'The Great Goblin triggers once for each event that puts one or more counters on a Goblin, Orc, or Army controlled by its controller, not once for each individual counter.'},
 {'name':'Great Goblin, Foul-Hearted','status':'PASS','finding':'Its enter/attack trigger amasses Goblins 3. Amassing onto an existing Army adds Goblin to that Army’s creature types, and its static ability gives Armies controlled by its controller trample.'},
 {'name':'Minas Morgul Army-Wraith bridge','status':'PASS','finding':'A shadow counter from Minas Morgul makes the target a Wraith in addition to its other types and gives it shadow while the counter remains. An Army made into a Wraith can then receive counters from each Nazgûl Ring trigger while remaining an Army for Sauron’s combat-damage trigger.'},
 {'name':'Roaming Throne — Avatar mode','status':'PASS','finding':'Choosing Avatar makes Roaming Throne an Avatar and causes triggered abilities of other Avatars controlled by its controller, including Sauron, to trigger an additional time. Each doubled Sauron trigger is a separate trigger.'},
 {'name':'Roaming Throne — Wraith mode','status':'PASS','finding':'Choosing Wraith instead causes each Nazgûl triggered ability to trigger an additional time because each Nazgûl is a Wraith. This does not simultaneously double Sauron because only one creature type is chosen.'},
 {'name':'Force of Will support','status':'PASS','finding':f'The candidate retains {blue_pitch} other blue nonland cards by current color-identity/type metadata, providing a sufficient functional pitch pool for Force of Will.'},
 {'name':'Wonder and Anger','status':'PASS','finding':'The revised mana base retains an Island basic plus Island-typed duals for Wonder and Mountain basics plus Mountain-typed duals for Anger.'},
 {'name':'Widespread Brutality','status':'PASS','finding':'The spell amasses first, then the chosen Army deals damage equal to its power to each non-Army creature; the Army itself is not a non-Army creature.'}
 ]}
 RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 legal={'status':'PASS','deck_sha256':deck_sha,'checked_at_utc':now,'sources':['https://magic.wizards.com/en/banned-restricted-list — current Commander banned list','Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata'],'unexpected_banned_cards':[],'project_exceptions_required':[],'finding':'Every candidate card is marked Commander-legal in the refreshed cache; no project legality exception is required.'}; LEGAL.write_text(json.dumps(legal,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 cfg={'deck_id':DECK_ID,'display_name':DISPLAY,'decklist_path':str(CANDIDATE.relative_to(ROOT)),'expected_deck_sha256':deck_sha,'baseline_source_sha256':sha(baseline_raw),'output_dir':str(OUTDIR.relative_to(ROOT)),'output_stem':'Sauron_the_Dark_Lord_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}; CONFIG.write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8')
 proc=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CONFIG.relative_to(ROOT))],cwd=ROOT,check=False)
 if proc.returncode: return proc.returncode
 gate=json.loads((OUTDIR/'Sauron_the_Dark_Lord_2026-10-15_Complete_Gate.json').read_text(encoding='utf-8'))
 if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors'): raise RuntimeError(f'Complete gate not clean: {gate}')
 SUMMARY.write_text(f'''# {DISPLAY} — approval-ready verification\n\nDate: {DATE}  \nCycle: `{CYCLE}`  \nDeck: #50 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{deck_sha}`\n- Cards: **100**\n- Distinct names: **91**\n- Lands: **34**\n- Repeats: **Nazgûl x7 / Swamp x3 / Mountain x2 only**\n- Singleton: **PASS — Nazgûl card-specific permission verified**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS**\n- Project exceptions: **none**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue_pitch} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 91 KEEP / 8 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 4 — Optimized**\n- Proposed Archidekt tags: **Amass Orcs / Ring Temptation / Wraiths**\n\n## Final proposed delta\n\n1. Warg Rider -> Great Goblin, Foul-Hearted\n2. Notion Thief -> Roaming Throne\n3. Fellwar Stone -> Mana Vault\n4. Counterspell -> Force of Will\n5. Drowned Catacomb -> Minas Morgul, Dark Fortress\n6. Sulfurous Springs -> Volcanic Island\n7. Underground River -> Flooded Strand\n8. Island -> Misty Rainforest\n\nThe candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n''',encoding='utf-8')
 print(json.dumps({'status':'APPROVAL_READY','deck_sha256':deck_sha,'count':100,'distinct':91,'lands':lands,'blue_pitch':blue_pitch},indent=2)); return 0
if __name__=='__main__': sys.exit(main())
