#!/usr/bin/env python3
from __future__ import annotations
import csv,re,tarfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
OUT=ROOT/'refinement/decisions/Tetsuo_Imperial_Champion_Whole_List_Decision_Ledger_2026-10-15.csv'
COMMANDER='Tetsuo, Imperial Champion'
CUTS=Counter({'Counterspell':1,'Feed the Swarm':1,'Lizard Blades':1,'Blackblade Reforged':1,'Thran Power Suit':1,'Relentless Assault':1,'Seize the Day':1,'Crumbling Necropolis':1,'Drowned Catacomb':1,'Shivan Reef':1,'Sulfurous Springs':1,'Sulfur Falls':1})
REASONS={
'Counterspell':'CUT — Force of Will protects mana-intensive Equipment/combat turns while tapped out.',
'Feed the Swarm':'CUT — Withering Torment upgrades the creature/enchantment slot to instant speed.',
'Lizard Blades':'CUT — Leyline Axe preserves double strike while adding trample, +1/+1, MV4 and opening-hand deployment.',
'Blackblade Reforged':'CUT — Swiftfoot Boots improves commander recovery with tutor-able haste and hexproof.',
'Thran Power Suit':"CUT — Oathkeeper, Takeno's Daisho is a more commander-specific Samurai resilience piece.",
'Relentless Assault':'CUT — extra-combat clause only functions when resolving during a main phase; Tetsuo free-casts during combat.',
'Seize the Day':'CUT — same main-phase dependency; replace with a combat-time-compatible extra-combat spell.',
'Crumbling Necropolis':'CUT — always-tapped fixing upgraded to Volcanic Island.',
'Drowned Catacomb':'CUT — conditional fixing upgraded to Mana Confluence.',
'Shivan Reef':'CUT — painland upgraded to premium fetchland.',
'Sulfurous Springs':'CUT — painland upgraded to premium fetchland.',
'Sulfur Falls':'CUT — conditional dual upgraded to premium fetchland.'}
KEEP={
'Excalibur, Sword of Eden':'KEEP — MV12 gives Tetsuo a massive damage/free-cast ceiling and equips legendary Tetsuo cheaply.',
'Genji Glove':'KEEP — MV5 Equipment with a commander-native extra-combat attack trigger.',
'Hexplate Wallbreaker':'KEEP — MV5 Equipment enabling repeated combat from the first combat each turn.',
'Akki Battle Squad':'KEEP — modified-creature extra-combat payoff tied directly to Equipment gameplay.',
'Aggravated Assault':'KEEP — repeatable extra-combat engine; combines naturally with Sword of Feast and Famine.',
'Sword of Feast and Famine':'KEEP — untap engine, protection, and Aggravated Assault combat loop piece.',
'Basilisk Collar':'KEEP — Tetsuo deals his damage-mode damage, so deathtouch/lifelink apply to it.',
'Buster Sword':'KEEP — combat-damage draw plus a second free-cast channel.',
"Swordsman's Steel":'KEEP — commander-focused Equipment density payoff and major Voltron scaling.',
'Hammer of Nazahn':'KEEP — Equipment auto-attachment plus indestructible protection.',
'Blacksmith\'s Talent':'KEEP — creates Equipment, auto-attaches at level 2, and grants equipped creatures double strike/haste at level 3.',
'Chandra\'s Ignition':'KEEP — tall-Tetsuo sweeper/finisher; reason to reject Sword of Wealth and Power self-interaction.',
'Ancestral Vision':'KEEP — Tetsuo can cast this MV0/no-mana-cost spell through his attack-trigger permission.',
'Profane Tutor':'KEEP — Tetsuo can cast this MV0/no-mana-cost spell through his attack-trigger permission.',
'Wheel of Fate':'KEEP — Tetsuo can cast this MV0/no-mana-cost spell through his attack-trigger permission.',
'Inevitable Betrayal':'KEEP — Tetsuo can cast this MV0/no-mana-cost spell through his attack-trigger permission.'}
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$')
def baseline():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('Tetsuo__Imperial_Champion.txt')]
        if len(ms)!=1: raise RuntimeError(f'expected one baseline member, found {len(ms)}')
        raw=tf.extractfile(ms[0]).read().decode('utf-8-sig')
    c=Counter()
    for ln in raw.splitlines():
        if not ln.strip(): continue
        m=LINE.match(ln)
        if not m: raise RuntimeError(f'malformed baseline line: {ln}')
        c[m.group(2).strip()]+=int(m.group(1))
    return c
def main():
    c=baseline()
    if sum(c.values())!=100 or len(c)!=91: raise RuntimeError(f'unexpected baseline: {sum(c.values())}/{len(c)}')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['card','baseline_qty','keep_qty','cut_qty','decision','rationale'])
        for card in sorted((x for x in c if x!=COMMANDER),key=str.casefold):
            b=c[card]; cut=CUTS[card]; keep=b-cut
            dec='KEEP' if cut==0 else ('CUT' if keep==0 else 'PARTIAL')
            w.writerow([card,b,keep,cut,dec,REASONS.get(card) or KEEP.get(card) or 'KEEP — retained after commander-first Equipment/free-cast/extra-combat, interaction, curve and mana audit.'])
    base=sum(c[x] for x in c if x!=COMMANDER); keep=sum(c[x]-CUTS[x] for x in c if x!=COMMANDER); cut=sum(CUTS.values())
    if (base,keep,cut)!=(99,87,12): raise RuntimeError(f'ledger totals mismatch: {base}/{keep}/{cut}')
    print(f'Wrote {OUT.relative_to(ROOT)}: {base} copies, {keep} KEEP / {cut} CUT')
if __name__=='__main__': main()
