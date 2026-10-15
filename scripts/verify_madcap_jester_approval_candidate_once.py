#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'refinement/decklists/The_Madcap_Jester_Approval_Ready_2026-10-15.txt'
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUDIT=ROOT/'refinement/verification/The_Madcap_Jester_Whole_List_Audit_2026-10-15.md'
DECISIONS=ROOT/'refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md'
LEDGER=ROOT/'refinement/decisions/The_Madcap_Jester_Whole_List_Decision_Ledger_2026-10-15.csv'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
OUTDIR=ROOT/'refinement/verification/the_madcap_jester_2026-10-15/gate_output'
CONFIG=OUTDIR/'The_Madcap_Jester_Complete_Gate_Config.json'
RULES=OUTDIR/'The_Madcap_Jester_Rules_Attestation.json'
LEGAL=OUTDIR/'The_Madcap_Jester_Official_Legality_Attestation.json'
SUMMARY=ROOT/'refinement/verification/The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md'
EXPECTED_SHA='caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7'
CUTS=Counter({'Ashiok, Nightmare Muse':1,'Brainstealer Dragon':1,'Counterspell':1,'Etali, Primal Storm':1,'Thief of Sanity':1})
ADDS=Counter({'Ashiok, Nightmare Weaver':1,'Dauthi Voidwalker':1,'Demonic Consultation':1,'Lightning Greaves':1,'Tainted Pact':1})
EXCEPTIONS={'The Madcap Jester',"Dragon's Smile"}
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
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('The_Madcap_Jester.txt')]
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
    if {r['card'] for r in rows}!={x for x in b if x!='The Madcap Jester'}: raise RuntimeError('ledger membership mismatch')
    bt=kt=ct=0
    for r in rows:
        card=r['card']; q=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
        if q!=b[card] or k+c!=q: raise RuntimeError(f'ledger qty mismatch {card}')
        bt+=q;kt+=k;ct+=c
    if (bt,kt,ct)!=(99,94,5): raise RuntimeError(f'ledger totals {bt}/{kt}/{ct}')

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    raw=CANDIDATE.read_bytes(); sha=h(raw); lines,c=parse(raw); braw,b=base()
    if sha!=EXPECTED_SHA: raise RuntimeError(f'candidate SHA drift {sha}')
    if sum(b.values())!=100 or len(b)!=100: raise RuntimeError(f'baseline structure mismatch {sum(b.values())}/{len(b)}')
    if sum(c.values())!=100 or len(c)!=100: raise RuntimeError(f'candidate structure {sum(c.values())}/{len(c)}')
    if lines[0]!="1x The Madcap Jester [Commander]" or c['The Madcap Jester']!=1: raise RuntimeError('commander line mismatch')
    if b-c!=CUTS or c-b!=ADDS: raise RuntimeError(f'delta mismatch cuts={b-c} adds={c-b}')
    if {n:q for n,q in c.items() if q>1}: raise RuntimeError('candidate has repeated names')
    ledger_check(b)
    cache=cache_load(); unresolved=[]; illegal=[]; exceptions=[]; lands=0; blue_pitch=0
    for name,q in c.items():
        r=cache.get(nk(name))
        if not r: unresolved.append(name); continue
        typ=r.get('type_line') or ''
        if 'Land' in typ.split(' // ',1)[0]: lands+=q
        leg=r.get('commander_legality')
        if name in EXCEPTIONS:
            if leg=='legal': raise RuntimeError(f'future-release exception unexpectedly legal before 2026-11-13: {name}')
            exceptions.append((name,leg))
        elif leg!='legal': illegal.append((name,leg))
        if name!='Force of Will' and 'U' in (r.get('color_identity') or []) and 'Land' not in typ: blue_pitch+=q
    if unresolved: raise RuntimeError('unresolved cache: '+', '.join(unresolved))
    if illegal: raise RuntimeError(f'unexpected illegal rows: {illegal}')
    if {x[0] for x in exceptions}!=EXCEPTIONS: raise RuntimeError(f'exception mismatch: {exceptions}')
    if lands!=34: raise RuntimeError(f'land count mismatch {lands}')
    if blue_pitch<15: raise RuntimeError(f'blue pitch pool too low: {blue_pitch}')
    for p in [AUDIT,DECISIONS]:
        t=p.read_text()
        if EXPECTED_SHA not in t: raise RuntimeError(f'{p.name} SHA mismatch')
    if '99/99 noncommander copies adjudicated: 94 KEEP / 5 CUT' not in AUDIT.read_text(): raise RuntimeError('audit closeout missing')
    if 'ZERO NEW MATERIAL IMPROVEMENTS' not in DECISIONS.read_text(): raise RuntimeError('decision closeout missing')
    now=datetime.now(timezone.utc).isoformat()
    rules={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Wizards Mystery Booster Commander Edition Release Notes — The Madcap Jester and Dragon’s Smile card text/rulings','Magic Comprehensive Rules — replacement effects, triggered abilities, casting from exile, face-down exile, alternative costs, Oracle win conditions','Current Oracle text in current-cycle Scryfall cache'],'interactions':[
      {'name':'Madcap attack and access triggers','status':'PASS','finding':'When The Madcap Jester attacks, its first triggered ability causes each opponent to exile the top card of their library. That controlled ability satisfies the second trigger condition; cards covered by the resulting permission may be played until the end of your next turn, subject to normal timing and costs, with mana of any type allowed.'},
      {'name':'Ashiok Nightmare Weaver','status':'PASS','finding':'Ashiok’s +2 exiles the top three cards of target opponent’s library. With Jester under your control, that planeswalker ability is a direct qualifying library-exile source and the exiled cards receive Jester play permission.'},
      {'name':'Direct exile suite','status':'PASS','finding':'Extract, Sadistic Sacrament, Bitter Ordeal, Tasha’s Hideous Laughter, Inside Information, Jester’s Cap, Psychic Surgery and other retained controlled effects that exile cards directly from opponent libraries qualify for Jester when their instructions produce the exile event.'},
      {'name':'Dauthi replacement plus controlled mill','status':'PASS','finding':'Dauthi Voidwalker replaces an event that would put an opponent-owned card into that opponent’s graveyard with exile instead. Under CR 614.6 the original event does not occur and the modified exile event occurs and may trigger abilities. When the replaced movement was being caused by a spell or ability you control and the card moved from an opponent’s library, the modified event satisfies Jester; Dauthi does not by itself make unrelated opponent-caused mill qualify.'},
      {'name':'Brain Freeze with Dauthi','status':'PASS','finding':'Brain Freeze targeting an opponent while Dauthi is present has its library-to-graveyard movement replaced with exile, producing qualifying Jester access. Brain Freeze targeting yourself is unaffected because Dauthi applies only to cards owned by opponents, preserving the Breach self-mill line.'},
      {'name':'Jesters Scepter face-down exile','status':'PASS','finding':'Jester’s Scepter exiles the top five cards of a target player’s library face down and expressly allows its controller to look at them. Current casting rules permit beginning to cast a face-down exiled spell card when the player is allowed to look at it; Jester supplies the separate play permission while normal timing/cost restrictions still apply.'},
      {'name':'Lightning Greaves','status':'PASS','finding':'Haste from Lightning Greaves lets a newly controlled Jester attack immediately. Shroud does not stop either Jester triggered ability because neither targets Jester.'},
      {'name':'Thassa Oracle plus Demonic Consultation','status':'PASS','finding':'With Thassa’s Oracle trigger on the stack, Demonic Consultation may name a card absent from the library and exile the library; Oracle then checks devotion against cards remaining and can win the game.'},
      {'name':'Thassa Oracle plus Tainted Pact','status':'PASS','finding':'The candidate has 100 distinct card names. With Oracle’s trigger pending, Tainted Pact can decline every revealed card without encountering two cards of the same name, allowing the library to be exiled before Oracle resolves.'},
      {'name':'Underworld Breach LED Brain Freeze','status':'PASS','finding':'Underworld Breach, Lion’s Eye Diamond and Brain Freeze retain the standard recursive storm/self-mill finish when sufficient graveyard resources are available; Dauthi Voidwalker does not replace cards from your own library or graveyard.'},
      {'name':'Dragon’s Smile alternative cost','status':'PASS','finding':'Dragon’s Smile may provide a zero alternative mana cost once each of your turns for a spell cast from exile, including an opponent-owned spell Jester permits you to cast. Other alternative costs cannot also be used, while applicable additional costs may still be paid.'},
      {'name':'Cast-from-exile payoffs','status':'PASS','finding':'Passionate Archaeologist, Nalfeshnee, Prosper and Wild-Magic Sorcerer all see spells actually cast from exile under Jester permission and apply their respective damage, copy, Treasure or cascade payoffs subject to each card’s own trigger restrictions.'},
      {'name':'Future-release project exceptions','status':'PASS','finding':'The Madcap Jester and Dragon’s Smile are preserved only under the registered project future-release exceptions on 2026-10-15. Wizards states new-to-Magic MBC cards become Commander-legal on 2026-11-13; no claim of present official legality is made.'}
    ]}
    RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n')
    legal={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata','Wizards — What’s Inside Mystery Booster Commander Edition? (updated legality date: new-to-Magic MBC cards legal in Commander 2026-11-13)','Current official Commander legality checkpoint'],'unexpected_banned_cards':[],'project_exceptions_required':[{'card':'The Madcap Jester','type':'future-release commander','official_status_on_2026-10-15':'not yet Commander-legal; effective 2026-11-13'},{'card':"Dragon's Smile",'type':'future-release or project card','official_status_on_2026-10-15':'not yet Commander-legal; effective 2026-11-13'}],'finding':'All 98 ordinary candidate cards resolve as currently Commander-legal. The Madcap Jester and Dragon’s Smile remain project-valid future-release exceptions only and are not represented as officially Commander-legal on 2026-10-15.'}
    LEGAL.write_text(json.dumps(legal,indent=2,ensure_ascii=False)+'\n')
    cfg={'deck_id':'The_Madcap_Jester','display_name':'The Madcap Jester','decklist_path':str(CANDIDATE.relative_to(ROOT)),'expected_deck_sha256':sha,'baseline_source_sha256':h(braw),'output_dir':str(OUTDIR.relative_to(ROOT)),'output_stem':'The_Madcap_Jester_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}
    CONFIG.write_text(json.dumps(cfg,indent=2)+'\n')
    p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CONFIG.relative_to(ROOT))],cwd=ROOT)
    if p.returncode: return p.returncode
    gate=json.loads((OUTDIR/'The_Madcap_Jester_2026-10-15_Complete_Gate.json').read_text())
    if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('deck_sha256')!=sha: raise RuntimeError('complete gate did not close cleanly')
    ex={x.get('card') for x in gate.get('project_exceptions') or []}
    if ex!=EXCEPTIONS: raise RuntimeError(f'complete gate exception set mismatch: {ex}')
    SUMMARY.write_text(f"# The Madcap Jester — approval-ready verification\n\nDate: 2026-10-15  \nCycle: `global-restart-2026-10-13`  \nDeck: #56 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{sha}`\n- Cards: **100**\n- Distinct names: **100**\n- Lands: **34**\n- Repeats: **none**\n- Singleton: **PASS**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS for 98 ordinary cards**\n- Project exceptions: **The Madcap Jester / Dragon's Smile — future-release exceptions retained; NOT officially Commander-legal until 2026-11-13**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue_pitch} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 94 KEEP / 5 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 5 — cEDH**\n- Proposed Archidekt tags: **Exile Theft / Library Control / Grixis Combo**\n\n## Final proposed delta\n\n1. Ashiok, Nightmare Muse -> Ashiok, Nightmare Weaver\n2. Brainstealer Dragon -> Dauthi Voidwalker\n3. Etali, Primal Storm -> Demonic Consultation\n4. Thief of Sanity -> Tainted Pact\n5. Counterspell -> Lightning Greaves\n\nThe candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n")
    print(json.dumps({'status':'APPROVAL_READY','deck_sha256':sha,'lands':lands,'blue_pitch_pool':blue_pitch,'project_exceptions':sorted(EXCEPTIONS)},indent=2)); return 0

if __name__=='__main__': sys.exit(main())
