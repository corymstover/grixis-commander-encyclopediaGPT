#!/usr/bin/env python3
from __future__ import annotations
import csv,re,tarfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASELINE_TAR=ROOT/'source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz'
OUT=ROOT/'refinement/decisions/Sauron_the_Dark_Lord_Whole_List_Decision_Ledger_2026-10-15.csv'
COMMANDER='Sauron, the Dark Lord'
CUTS=Counter({'Warg Rider':1,'Notion Thief':1,'Fellwar Stone':1,'Counterspell':1,'Drowned Catacomb':1,'Sulfurous Springs':1,'Underground River':1,'Island':1})
REASONS={
'Warg Rider':'CUT — Great Goblin, Foul-Hearted more directly converts the Army into Sauron combat-damage triggers through ETB/attack amass 3 plus Army trample.',
'Notion Thief':'CUT — strong generic wheel denial; Roaming Throne is a direct Sauron/Nazgûl trigger multiplier.',
'Fellwar Stone':'CUT — Mana Vault better solves the six-mana commander deployment bottleneck; colored fixing remains dense.',
'Counterspell':'CUT — Force of Will better protects tap-out commander/engine turns.',
'Drowned Catacomb':'CUT — Minas Morgul is a uniquely commander-specific evasion/Wraith engine land.',
'Sulfurous Springs':'CUT — Volcanic Island improves untapped typed fixing and Anger/Wonder support.',
'Underground River':'CUT — Flooded Strand improves typed dual access and color selection.',
'Island':'PARTIAL — reduce 2 to 1; multiple Island-typed duals remain for Wonder.'}
LINE_RE=re.compile(r'^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$')
def baseline():
 with tarfile.open(BASELINE_TAR,'r:gz') as tf:
  m=[x for x in tf.getmembers() if x.isfile() and x.name.endswith('Sauron__the_Dark_Lord.txt')]
  if len(m)!=1: raise RuntimeError(f'Expected one baseline; found {len(m)}')
  raw=tf.extractfile(m[0]).read().decode('utf-8-sig')
 out=Counter()
 for line in raw.splitlines():
  if not line.strip(): continue
  x=LINE_RE.match(line)
  if not x: raise RuntimeError(f'Malformed baseline line: {line}')
  out[x.group(2).strip()]+=int(x.group(1))
 return out
def main():
 cards=baseline()
 if sum(cards.values())!=100 or len(cards)!=90: raise RuntimeError(f'Unexpected baseline structure {sum(cards.values())}/{len(cards)}')
 OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f); w.writerow(['card','baseline_qty','keep_qty','cut_qty','decision','rationale'])
  for card in sorted((x for x in cards if x!=COMMANDER),key=str.casefold):
   b=cards[card]; c=CUTS[card]; k=b-c; d='KEEP' if c==0 else ('CUT' if k==0 else 'PARTIAL')
   r=REASONS.get(card,'KEEP — retained after commander-first Army/Ring/Wraith, interaction, curve, mana, and identity audit.')
   w.writerow([card,b,k,c,d,r])
 total=sum(cards[x] for x in cards if x!=COMMANDER); keep=sum(cards[x]-CUTS[x] for x in cards if x!=COMMANDER); cut=sum(CUTS.values())
 if (total,keep,cut)!=(99,91,8): raise RuntimeError(f'Expected 99/91/8, found {total}/{keep}/{cut}')
 print(f'Wrote ledger: {total} copies, {keep} KEEP / {cut} CUT')
if __name__=='__main__': main()
