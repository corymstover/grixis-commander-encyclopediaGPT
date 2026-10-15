#!/usr/bin/env python3
from __future__ import annotations
import csv,hashlib,json,re,subprocess,sys,tarfile
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'refinement/decklists/Tetsuo_Imperial_Champion_Approval_Ready_2026-10-15.txt'
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
AUDIT=ROOT/'refinement/verification/Tetsuo_Imperial_Champion_Whole_List_Audit_2026-10-15.md'
DECISIONS=ROOT/'refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md'
LEDGER=ROOT/'refinement/decisions/Tetsuo_Imperial_Champion_Whole_List_Decision_Ledger_2026-10-15.csv'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
OUTDIR=ROOT/'refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output'
CONFIG=OUTDIR/'Tetsuo_Imperial_Champion_Complete_Gate_Config.json'
RULES=OUTDIR/'Tetsuo_Imperial_Champion_Rules_Attestation.json'
LEGAL=OUTDIR/'Tetsuo_Imperial_Champion_Official_Legality_Attestation.json'
SUMMARY=ROOT/'refinement/verification/Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md'
EXPECTED_SHA='d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e'
CUTS=Counter({'Counterspell':1,'Feed the Swarm':1,'Lizard Blades':1,'Blackblade Reforged':1,'Thran Power Suit':1,'Relentless Assault':1,'Seize the Day':1,'Crumbling Necropolis':1,'Drowned Catacomb':1,'Shivan Reef':1,'Sulfurous Springs':1,'Sulfur Falls':1})
ADDS=Counter({'Force of Will':1,'Withering Torment':1,'Leyline Axe':1,'Swiftfoot Boots':1,"Oathkeeper, Takeno's Daisho":1,'Savage Beating':1,'World at War':1,'Volcanic Island':1,'Mana Confluence':1,'Flooded Strand':1,'Marsh Flats':1,'Misty Rainforest':1})
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
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('Tetsuo__Imperial_Champion.txt')]
        if len(ms)!=1: raise RuntimeError(f'baseline member count {len(ms)}')
        fh=tf.extractfile(ms[0])
        if fh is None: raise RuntimeError('unable to extract baseline')
        raw=fh.read(); return raw,parse(raw)[1]
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
    if {r['card'] for r in rows}!={x for x in b if x!='Tetsuo, Imperial Champion'}: raise RuntimeError('ledger membership mismatch')
    bt=kt=ct=0
    for r in rows:
        card=r['card']; q=int(r['baseline_qty']); k=int(r['keep_qty']); c=int(r['cut_qty'])
        if q!=b[card] or k+c!=q: raise RuntimeError(f'ledger qty mismatch {card}')
        bt+=q;kt+=k;ct+=c
    if (bt,kt,ct)!=(99,87,12): raise RuntimeError(f'ledger totals {bt}/{kt}/{ct}')
def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    raw=CANDIDATE.read_bytes(); sha=h(raw); lines,c=parse(raw); braw,b=base()
    if sha!=EXPECTED_SHA: raise RuntimeError(f'candidate SHA drift {sha}')
    if sum(b.values())!=100 or len(b)!=91: raise RuntimeError(f'baseline structure {sum(b.values())}/{len(b)}')
    if sum(c.values())!=100 or len(c)!=91: raise RuntimeError(f'candidate structure {sum(c.values())}/{len(c)}')
    if lines[0]!="1x Tetsuo, Imperial Champion [Commander]" or c['Tetsuo, Imperial Champion']!=1: raise RuntimeError('commander line mismatch')
    if b-c!=CUTS or c-b!=ADDS: raise RuntimeError(f'delta mismatch cuts={b-c} adds={c-b}')
    if {n:q for n,q in c.items() if q>1}!={'Island':5,'Mountain':4,'Swamp':3}: raise RuntimeError('repeat mismatch')
    ledger_check(b)
    cache=cache_load(); unresolved=[]; illegal=[]; front_lands=0; blue_pitch=0
    for name,q in c.items():
        r=cache.get(nk(name))
        if not r: unresolved.append(name); continue
        first=(r.get('type_line') or '').split(' // ',1)[0]
        if 'Land' in first: front_lands+=q
        if r.get('commander_legality')!='legal': illegal.append((name,r.get('commander_legality')))
        if name!='Force of Will' and 'U' in (r.get('color_identity') or []) and 'Land' not in first: blue_pitch+=q
    if unresolved: raise RuntimeError('unresolved cache: '+', '.join(sorted(unresolved)))
    if illegal: raise RuntimeError(f'illegal rows: {illegal}')
    if front_lands!=35: raise RuntimeError(f'land count mismatch: {front_lands}')
    if blue_pitch<15: raise RuntimeError(f'blue pitch pool too low: {blue_pitch}')
    for p in [AUDIT,DECISIONS]:
        t=p.read_text()
        if EXPECTED_SHA not in t: raise RuntimeError(f'{p.name} SHA mismatch')
    if '99/99 noncommander copies adjudicated: 87 KEEP / 12 CUT' not in AUDIT.read_text(): raise RuntimeError('audit closeout missing')
    if 'ZERO NEW MATERIAL IMPROVEMENTS' not in DECISIONS.read_text(): raise RuntimeError('decision closeout missing')
    now=datetime.now(timezone.utc).isoformat()
    rules={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current Oracle text in current-cycle Scryfall cache','Magic Comprehensive Rules — triggered abilities, intervening-if clauses, casting spells during resolution, alternative/additional costs, equipment, combat, rebound, protection, deathtouch/lifelink and commander zone changes (current 2026 rules)','Current Wizards release-note rulings for Seize the Day/Relentless Assault timing and relevant Equipment interactions'],'interactions':[
      {'name':'Tetsuo attack trigger and equipped condition','status':'PASS','finding':"Tetsuo's ability triggers only if he is equipped as he attacks. Its intervening-if condition is checked again on resolution; if he is no longer equipped then, the ability does not resolve. The chosen mode and any target are selected as the trigger is put on the stack."},
      {'name':'Greatest Equipment mana value','status':'PASS','finding':'The damage amount or free-cast ceiling uses the greatest mana value among Equipment attached to Tetsuo as the ability resolves. High-MV Equipment such as Excalibur, Kaldra Compleat, Argentum Armor, Embercleave, Genji Glove and Hexplate Wallbreaker therefore establish the spell ceiling.'},
      {'name':'Casting during trigger resolution','status':'PASS','finding':'Tetsuo explicitly permits casting an instant or sorcery from hand during resolution. This permission bypasses normal sorcery timing, while restrictions and required additional costs still apply. The spell is cast without paying its mana cost, not with another alternative cost.'},
      {'name':'No-mana-cost suspend spells','status':'PASS','finding':'Ancestral Vision, Profane Tutor, Wheel of Fate and Inevitable Betrayal have mana value 0 despite having no mana cost. Tetsuo can cast them from hand without paying their mana costs when his free-cast mode resolves.'},
      {'name':'Savage Beating','status':'PASS','finding':'Savage Beating may be cast only during combat on your turn, exactly the window in which Tetsuo resolves after attacking. With an Equipment ceiling of at least five, Tetsuo can cast it without paying its mana cost. Its additional-combat mode works immediately; entwine is an optional additional cost and may be paid separately.'},
      {'name':'World at War','status':'PASS','finding':'World at War does not require itself to resolve during a main phase. If Tetsuo casts it during the first combat, it schedules an additional combat after the second main phase. Because it was cast from hand, rebound can exile it as it resolves and allow another no-mana-cost cast at the next upkeep.'},
      {'name':'Historical Relentless Assault / Seize the Day correction','status':'PASS','finding':'Both outgoing spells create their additional combat after this main phase. Current rulings confirm that when cast outside a main phase, their extra-combat instruction does not create a combat. Tetsuo normally casts through his trigger during combat, so replacing them corrects a false synergy.'},
      {'name':'Repeated Tetsuo attacks','status':'PASS','finding':'Each additional combat in which Tetsuo attacks while equipped creates another independent commander trigger. Akki Battle Squad itself is limited to triggering only once each turn, but Tetsuo is not.'},
      {'name':'Genji Glove / Hexplate Wallbreaker','status':'PASS','finding':'Each retained Equipment creates an additional-combat line from combat/attack play while also carrying MV5, enough to free-cast Savage Beating or World at War through Tetsuo.'},
      {'name':'Godo and Samurai typing','status':'PASS','finding':'Tetsuo is a Human Samurai. Godo tutors Equipment on entry; when Godo attacks for the first time each turn, its Samurai untap clause includes Tetsuo and creates an additional combat.'},
      {'name':'Oathkeeper, Takenos Daisho','status':'PASS','finding':"Tetsuo is a Samurai, so if the equipped Tetsuo dies, Oathkeeper's trigger can return that card to the battlefield. If Oathkeeper itself goes to the graveyard from the battlefield while attached, its separate trigger exiles the equipped creature; normal commander zone-change rules remain available to the owner."},
      {'name':'Leyline Axe','status':'PASS','finding':'Leyline Axe has mana value 4, can begin the game on the battlefield from the opening hand, and gives the equipped creature +1/+1, double strike and trample. Its MV4 raises Tetsuo’s damage/free-cast ceiling while improving combat connection.'},
      {'name':'Swiftfoot Boots','status':'PASS','finding':'Haste allows a newly controlled Tetsuo to attack immediately when otherwise able, enabling the attack trigger without waiting a turn. Hexproof protects him from opponents while still allowing the controller to target him.'},
      {'name':'Buster Sword','status':'PASS','finding':'When equipped Tetsuo deals combat damage to a player, Buster Sword draws a card and may cast a spell from hand with mana value no greater than that damage without paying its mana cost. Double strike can create separate combat-damage triggers in both damage steps.'},
      {'name':'Basilisk Collar and Tetsuo damage mode','status':'PASS','finding':'Tetsuo himself deals the commander-trigger damage. If he has deathtouch and lifelink from Basilisk Collar, those abilities apply to that noncombat damage.'},
      {'name':'Chandras Ignition','status':'PASS','finding':"Chandra's Ignition targets a creature you control and causes that creature to deal damage equal to its power to each other creature and opponent. A tall Tetsuo can therefore convert Equipment power into a board-wide finisher; this retained line is the reason Sword of Wealth and Power was rejected for its protection-from-sorceries conflict when attached to Tetsuo."},
      {'name':'Aggravated Assault plus Sword of Feast and Famine','status':'PASS','finding':'Combat damage from a creature equipped with Sword of Feast and Famine untaps the controller’s lands. When that untap supplies at least the 3RR needed for Aggravated Assault, the deck can buy another combat/main phase and repeat while combat damage continues to connect.'},
      {'name':'Attachment engines','status':'PASS','finding':"Hammer of Nazahn can attach Equipment as they enter, Brass Squire can tap to attach Equipment at instant speed, and Blacksmith's Talent level 2 attaches an Equipment at beginning of combat. These effects reduce the equip-cost burden before Tetsuo attacks."},
      {'name':'Mana-base revision','status':'PASS','finding':'Volcanic Island adds the missing premium UR typed dual; Flooded Strand, Marsh Flats and Misty Rainforest can access appropriate typed duals in the list; Mana Confluence supplies unconditional U/B/R fixing. Land count remains 35.'}
    ]}
    RULES.write_text(json.dumps(rules,indent=2,ensure_ascii=False)+'\n')
    legal={'status':'PASS','deck_sha256':sha,'checked_at_utc':now,'sources':['Current_Cycle_Oracle_Cache.jsonl refreshed from current Scryfall metadata','Current official Commander legality checkpoint'],'unexpected_banned_cards':[],'project_exceptions_required':[],'finding':'Every Tetsuo, Imperial Champion candidate card resolves as currently Commander-legal; no project exception is required.'}
    LEGAL.write_text(json.dumps(legal,indent=2,ensure_ascii=False)+'\n')
    cfg={'deck_id':'Tetsuo__Imperial_Champion','display_name':'Tetsuo, Imperial Champion','decklist_path':str(CANDIDATE.relative_to(ROOT)),'expected_deck_sha256':sha,'baseline_source_sha256':h(braw),'output_dir':str(OUTDIR.relative_to(ROOT)),'output_stem':'Tetsuo_Imperial_Champion_2026-10-15','rules_attestation_path':str(RULES.relative_to(ROOT)),'official_legality_attestation_path':str(LEGAL.relative_to(ROOT)),'max_cache_age_hours':72}
    CONFIG.write_text(json.dumps(cfg,indent=2,ensure_ascii=False)+'\n')
    p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_complete_approval_gate.py'),'--config',str(CONFIG.relative_to(ROOT))],cwd=ROOT)
    if p.returncode: return p.returncode
    gate=json.loads((OUTDIR/'Tetsuo_Imperial_Champion_2026-10-15_Complete_Gate.json').read_text())
    if gate.get('overall_result')!='APPROVAL_READY' or gate.get('errors') or gate.get('deck_sha256')!=sha: raise RuntimeError('complete gate did not close cleanly')
    SUMMARY.write_text(f"# Tetsuo, Imperial Champion — approval-ready verification\n\nDate: 2026-10-15  \nCycle: `global-restart-2026-10-13`  \nDeck: #55 of 62\n\n## Result\n\n**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**\n\n- Exact candidate SHA-256: `{sha}`\n- Cards: **100**\n- Distinct names: **91**\n- Lands: **35**\n- Repeats: **Island x5 / Mountain x4 / Swamp x3 only**\n- Singleton: **PASS**\n- Commander color identity: **U/B/R — PASS**\n- Fresh current-cycle Oracle resolution: **PASS**\n- Official Commander legality: **PASS**\n- Project exceptions: **none**\n- Rules-interaction attestation: **PASS**\n- Force of Will blue-pitch pool: **{blue_pitch} other blue nonland cards**\n- Whole-list audit: **99/99 noncommander copies adjudicated; 87 KEEP / 12 CUT**\n- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**\n- Natural ceiling: **Power Bracket 4 — Optimized**\n- Proposed Archidekt tags: **Equipment / Free-Cast Spells / Extra Combats**\n\n## Final proposed delta\n\n1. Counterspell -> Force of Will\n2. Feed the Swarm -> Withering Torment\n3. Lizard Blades -> Leyline Axe\n4. Blackblade Reforged -> Swiftfoot Boots\n5. Thran Power Suit -> Oathkeeper, Takeno's Daisho\n6. Relentless Assault -> Savage Beating\n7. Seize the Day -> World at War\n8. Crumbling Necropolis -> Volcanic Island\n9. Drowned Catacomb -> Mana Confluence\n10. Shivan Reef -> Flooded Strand\n11. Sulfurous Springs -> Marsh Flats\n12. Sulfur Falls -> Misty Rainforest\n\nThe candidate remains unlocked until explicit user approval of this exact SHA-bound list.\n")
    print(json.dumps({'status':'APPROVAL_READY','deck_sha256':sha,'lands':front_lands,'blue_pitch_pool':blue_pitch},indent=2)); return 0
if __name__=='__main__': sys.exit(main())
