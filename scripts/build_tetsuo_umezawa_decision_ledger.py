#!/usr/bin/env python3
from __future__ import annotations
import csv,re,tarfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
OUT=ROOT/'refinement/decisions/Tetsuo_Umezawa_Whole_List_Decision_Ledger_2026-10-15.csv'
COMMANDER='Tetsuo Umezawa'
CUTS=Counter({'Arcane Denial':1,'Feed the Swarm':1,'Nightscape Familiar':1,'Maeve, Insidious Singer':1,'Backlash':1,'Agitator Ant':1,'Spectacular Showdown':1,'Opposition Agent':1,'Dragonskull Summit':1,'Drowned Catacomb':1,'Shivan Reef':1,'Sulfurous Springs':1,'Underground River':1,'Island':1})
REASONS={
'Arcane Denial':'CUT — Force of Will better protects a mana-intensive tap-ability commander while tapped out.',
'Feed the Swarm':'CUT — Withering Torment gives instant-speed creature/enchantment interaction.',
'Nightscape Familiar':'CUT — does not reduce Tetsuo first cast UBR or UBBR activation because neither contains generic mana; replace with colored ramp plus untap.',
'Maeve, Insidious Singer':'CUT — four-mana body plus three mana per goad loses to Puppeteer as direct tap/untap engine.',
'Backlash':'CUT — Blustersquall is more efficient single-target tap and scales to mass tap.',
'Agitator Ant':'CUT — optional opponent participation is less reliable than Flood repeatable target creation.',
'Spectacular Showdown':'CUT — one-shot high-cost overload loses to repeatable Retreat to Coralhelm tap/untap engine.',
'Opposition Agent':'CUT — generic stax slot replaced by Sting, the Glinting Dagger as repeatable beginning-of-combat Tetsuo untap plus haste.',
'Dragonskull Summit':'CUT — upgrade to Badlands.',
'Drowned Catacomb':'CUT — upgrade to Underground Sea.',
'Shivan Reef':'CUT — upgrade to premium fetchland.',
'Sulfurous Springs':'CUT — upgrade to premium fetchland.',
'Underground River':'CUT — upgrade to premium fetchland.',
'Island':'PARTIAL CUT — convert one of six copies into land-capable Sink into Stupor // Soporific Springs while retaining five basics.'}
KEEP={
'Aphetto Alchemist':'KEEP — direct untap engine for Tetsuo.',
'Fatestitcher':'KEEP — repeatable tap/untap permanent supports target creation and commander reuse.',
"Magewright's Stone":'KEEP — cheap repeatable Tetsuo untap.',
"Minamo, School at Water's Edge":'KEEP — land-slot untap for legendary Tetsuo.',
'Thousand-Year Elixir':'KEEP — haste-equivalent for tap abilities plus repeatable untap.',
'Rings of Brighthearth':'KEEP — copies Tetsuo activated ability for {2}.',
"Illusionist's Bracers":'KEEP — copies equipped Tetsuo activated ability.',
'Frozen Aether':'KEEP — opposing creatures enter tapped and satisfy Tetsuo target condition.',
'Fumiko the Lowblood':'KEEP — forces opponent creatures to attack, naturally tapping non-vigilance attackers.',
'Disrupt Decorum':'KEEP — mass goad is a high-impact forced-combat enabler.',
'Verity Circle':'KEEP — converts opposing nonattack tapping into card advantage.',
'Borrowing 100,000 Arrows':'KEEP — tapped-creature payoff/draw tied to deck state.',
'Lightning Greaves':'KEEP — haste lets Tetsuo activate immediately; shroud does not interfere because Tetsuo targets another creature.',
'Swiftfoot Boots':'KEEP — haste/protection for immediate commander activation.'}
LINE=re.compile(r'^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$')
def baseline():
    with tarfile.open(TAR,'r:gz') as tf:
        ms=[m for m in tf.getmembers() if m.isfile() and m.name.endswith('Tetsuo_Umezawa.txt')]
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
    if sum(c.values())!=100 or len(c)!=86: raise RuntimeError(f'unexpected baseline: {sum(c.values())}/{len(c)}')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['card','baseline_qty','keep_qty','cut_qty','decision','rationale'])
        for card in sorted((x for x in c if x!=COMMANDER),key=str.casefold):
            b=c[card]; cut=CUTS[card]; keep=b-cut
            dec='KEEP' if cut==0 else ('CUT' if keep==0 else 'PARTIAL')
            w.writerow([card,b,keep,cut,dec,REASONS.get(card) or KEEP.get(card) or 'KEEP — retained after commander-first tap/untap, forced-combat, interaction, curve and mana audit.'])
    base=sum(c[x] for x in c if x!=COMMANDER); keep=sum(c[x]-CUTS[x] for x in c if x!=COMMANDER); cut=sum(CUTS.values())
    if (base,keep,cut)!=(99,85,14): raise RuntimeError(f'ledger totals mismatch: {base}/{keep}/{cut}')
    print(f'Wrote {OUT.relative_to(ROOT)}: {base} copies, {keep} KEEP / {cut} CUT')
if __name__=='__main__': main()
