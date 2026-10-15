#!/usr/bin/env python3
from __future__ import annotations
import csv,re,tarfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
OUT=ROOT/'refinement/decisions/The_Rani_Whole_List_Decision_Ledger_2026-10-15.csv'
COMMANDER='The Rani'
CUTS=Counter({'Agitator Ant':1,'Insurrection':1,'Counterspell':1,'Arcane Denial':1,'Orcish Bowmasters':1,'Dragonskull Summit':1,'Drowned Catacomb':1,'Sulfur Falls':1})
REASONS={
'Agitator Ant':'CUT — opponents may decline its counter/goad offer; The Master, Mesmerist provides deterministic repeatable goad plus damage payoff.',
'Insurrection':'CUT — eight-mana generic theft finisher is redundant with Hot Pursuit and loses to repeatable Thassa blink/Mark generation.',
'Counterspell':'CUT — Force of Will provides tap-out protection for commander-centric turns.',
'Arcane Denial':'CUT — interaction density remains sufficient; Incriminating Impetus directly advances Aura/goad/combat-damage identity.',
'Orcish Bowmasters':'CUT — generic high-power interaction loses to Baeloth Barrityl commander-specific mass-goad/Treasure interaction.',
'Dragonskull Summit':'CUT — conditional fixing upgraded to City of Brass.',
'Drowned Catacomb':'CUT — conditional fixing upgraded to Mana Confluence.',
'Sulfur Falls':'CUT — conditional fixing upgraded to Flooded Strand.'}
KEEP={
'Academy Manufactor':'KEEP — every investigate produces Clue/Food/Treasure instead of only a Clue.',
'Erdwal Illuminator':'KEEP — doubles the first investigate each turn.',
'Displacer Kitten':'KEEP — repeatedly blinks The Rani on noncreature spells, retriggering Mark creation.',
'Entity Tracker':'KEEP — Mark tokens and retained Aura suite are enchantment ETBs that fuel draw.',
'Hateful Eidolon':'KEEP — converts deaths of creatures carrying controlled Auras into cards.',
'Bjorna, Nightfall Alchemist':'KEEP — converts excess artifacts/Clues into targeted damage plus goad.',
'Hot Pursuit':'KEEP — early goad/suspect plus late mass-control payoff; replaces need for generic Insurrection.',
'Time Sieve':'KEEP — artifact-token engine payoff that can turn accumulated Clue/Food/Treasure into extra turns.',
'Maestros Confluence':'KEEP — flexible mass-goad mode can goad whole opposing boards while retaining removal/recursion modes.',
'Spectacular Showdown':'KEEP — scalable single-target or overloaded mass goad plus double strike.'}
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+(?:\s+\*[^*]+\*)?\s+\[[^\]]+\]\s*$')
def baseline():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('The_Rani.txt')]
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
    if sum(c.values())!=100 or len(c)!=94: raise RuntimeError(f'unexpected baseline {sum(c.values())}/{len(c)}')
    if c[COMMANDER]!=1: raise RuntimeError('commander mismatch')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['card','baseline_qty','keep_qty','cut_qty','decision','rationale'])
        for card in sorted((x for x in c if x!=COMMANDER),key=str.casefold):
            b=c[card]; cut=CUTS[card]; keep=b-cut; dec='KEEP' if cut==0 else ('CUT' if keep==0 else 'PARTIAL')
            w.writerow([card,b,keep,cut,dec,REASONS.get(card) or KEEP.get(card) or 'KEEP — retained after commander-first goad/Clue/Aura, interaction, curve and mana audit.'])
    bt=sum(c[x] for x in c if x!=COMMANDER); kt=sum(c[x]-CUTS[x] for x in c if x!=COMMANDER); ct=sum(CUTS.values())
    if (bt,kt,ct)!=(99,91,8): raise RuntimeError(f'ledger totals mismatch {bt}/{kt}/{ct}')
    print(f'Wrote {OUT.relative_to(ROOT)}: {bt} copies, {kt} KEEP / {ct} CUT')
if __name__=='__main__': main()
