#!/usr/bin/env python3
from __future__ import annotations
import csv,re,tarfile
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
OUT=ROOT/'refinement/decisions/The_Madcap_Jester_Whole_List_Decision_Ledger_2026-10-15.csv'
COMMANDER='The Madcap Jester'
CUTS=Counter({'Ashiok, Nightmare Muse':1,'Brainstealer Dragon':1,'Counterspell':1,'Etali, Primal Storm':1,'Thief of Sanity':1})
REASONS={
'Ashiok, Nightmare Muse':'CUT — five-mana token-mediated exile engine loses to three-mana Ashiok, Nightmare Weaver immediate +2 library exile.',
'Brainstealer Dragon':'CUT — seven-mana theft payoff is too slow at Jester’s natural cEDH ceiling; Dauthi Voidwalker provides two-mana graveyard hate and commander-specific replacement/exile utility.',
'Counterspell':'CUT — UU interaction is redundant beside the retained free/cheap protection suite; Lightning Greaves more directly unlocks the commander attack engine.',
'Etali, Primal Storm':'CUT — six mana plus a separate attack step without native haste is slower than the commander’s own exile access and loses to compact Oracle infrastructure.',
'Thief of Sanity':'CUT — fragile combat-damage theft is too slow; Tainted Pact completes the existing Oracle finish and doubles as flexible instant-speed selection.'}
KEEP={
'Extract':'KEEP — one-mana opponent-library exile becomes commander-enabled access to the selected card.',
'Sadistic Sacrament':'KEEP — direct multi-card opponent-library exile scales with Jester permission.',
'Bitter Ordeal':'KEEP — gravestorm can exile selected cards from opponent libraries and Jester turns those exiles into playable resources.',
"Tasha's Hideous Laughter":'KEEP — signature burst library exile; with Jester it functions as a large temporary resource draw across opponents.',
'Psychic Surgery':'KEEP — repeatable library-control exile after opponent shuffles; direct Jester trigger engine.',
'Inside Information':'KEEP — low-cost targeted library exile and life-based alternative casting remains highly commander-specific.',
"Jester's Cap":'KEEP — searches and exiles three selected cards from an opponent library, becoming targeted theft with Jester.',
"Jester's Scepter":'KEEP — immediate five-card library exile; controller may look at the face-down exiled cards, supporting Jester play permission under current casting rules.',
"Dragon's Smile":'KEEP — registered future-release exception; free-casts one exile spell each turn and produces library exile on combat damage.',
'Bilbo, Thief in the Night':'KEEP — discounts spells cast outside hand and supplies graveyard casting on attack.',
'Don Andres, the Renegade':'KEEP — buffs and monetizes opponent-owned permanents cast through the theft engine.',
'Gonti, Night Minister':'KEEP — Treasure payoff for spells not owned plus repeatable combat-driven opponent-library exile.',
'Prosper, Tome-Bound':'KEEP — cast-from-exile Treasure engine supports stolen-spell velocity.',
'Party Thrasher':'KEEP — convoke for noncreature spells from exile plus self-exile card selection.',
'Passionate Archaeologist':'KEEP — commander-granted damage payoff for every spell cast from exile.',
'Nalfeshnee':'KEEP — copies spells cast from exile, multiplying Jester theft value.',
'Plargg and Nassari':'KEEP — repeatable multi-library exile and free casting if allowed to survive to upkeep.',
'Sire of Stagnation':'KEEP — opponent landfall exiles library cards while drawing cards, creating repeated Jester access.',
'Circu, Dimir Lobotomist':'KEEP — low-cost spellcasting turns into repeatable top-card library exile.',
'Laughing Jasper Flint':'KEEP — repeatable opponent-library exile keyed to outlaw count and stolen-spell casting.',
'Wild-Magic Sorcerer':'KEEP — first spell cast from exile gains cascade, directly rewarding Jester’s core play pattern.',
'Thassa\'s Oracle':'KEEP — existing compact cEDH finish now properly paired with Consultation/Pact.',
'Underworld Breach':'KEEP — existing Breach/LED/Brain Freeze compact win engine.',
'Brain Freeze':'KEEP — Breach win component and, against opponents while Dauthi is present, can become qualifying library exile via replacement.'}
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+(?:\s+\*[^*]+\*)?\s+\[[^\]]+\]\s*$')

def baseline():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('The_Madcap_Jester.txt')]
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
    if sum(c.values())!=100 or len(c)!=100: raise RuntimeError(f'unexpected baseline: {sum(c.values())}/{len(c)}')
    if c[COMMANDER]!=1: raise RuntimeError('commander baseline mismatch')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['card','baseline_qty','keep_qty','cut_qty','decision','rationale'])
        for card in sorted((x for x in c if x!=COMMANDER),key=str.casefold):
            b=c[card]; cut=CUTS[card]; keep=b-cut
            dec='KEEP' if cut==0 else ('CUT' if keep==0 else 'PARTIAL')
            w.writerow([card,b,keep,cut,dec,REASONS.get(card) or KEEP.get(card) or 'KEEP — retained after commander-first exile-theft, cEDH-ceiling, interaction, curve and mana audit.'])
    base=sum(c[x] for x in c if x!=COMMANDER); keep=sum(c[x]-CUTS[x] for x in c if x!=COMMANDER); cut=sum(CUTS.values())
    if (base,keep,cut)!=(99,94,5): raise RuntimeError(f'ledger totals mismatch: {base}/{keep}/{cut}')
    print(f'Wrote {OUT.relative_to(ROOT)}: {base} copies, {keep} KEEP / {cut} CUT')

if __name__=='__main__': main()
