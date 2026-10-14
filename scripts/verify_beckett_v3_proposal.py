#!/usr/bin/env python3
"""Independently check Beckett's proposed exact list against the frozen source."""
from collections import Counter
from pathlib import Path
import hashlib, re, tarfile

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/"source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
PROPOSAL=ROOT/"refinement/decklists/Admiral_Beckett_Brass_v3_Proposed_2026-10-13.txt"
EXPECTED_SHA="b28a48e9de33f3ab53c35e7185721cd54b3f595f09eed9db988167aa492124c9"
BASICS={"Island","Mountain","Swamp","Plains","Forest","Wastes"}

def parse_original(line):
    m=re.match(r"^(\d+)x (.+?) \([^()]*\) \S+ .*",line)
    if not m: raise ValueError(f"bad baseline line: {line}")
    return int(m.group(1)),m.group(2)

def parse_clean(line):
    m=re.match(r"^(\d+)x (.+?)(?: \[Commander\])?$",line)
    if not m: raise ValueError(f"bad proposal line: {line}")
    return int(m.group(1)),m.group(2)

def main():
    with tarfile.open(ARCHIVE,"r:gz") as tf:
        source=tf.extractfile("TXT/Admiral_Beckett_Brass.txt").read().decode("utf-8-sig").splitlines()
    original=Counter()
    for line in source:
        if line.strip():
            qty,name=parse_original(line);original[name]+=qty
    raw=PROPOSAL.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=EXPECTED_SHA: raise ValueError("proposed clean-list hash mismatch")
    lines=raw.decode("utf-8").splitlines()
    if not lines or lines[0]!="1x Admiral Beckett Brass [Commander]": raise ValueError("commander must be first and marked")
    proposed=Counter()
    for line in lines:
        qty,name=parse_clean(line);proposed[name]+=qty
    if sum(proposed.values())!=100: raise ValueError("not exactly 100 cards")
    if any(qty!=1 for name,qty in proposed.items() if name not in BASICS): raise ValueError("singleton violation")
    removed=original-proposed;added=proposed-original
    if removed!=Counter({"Coastal Piracy":1,"Glint-Horn Buccaneer":1}): raise ValueError(f"unexpected cuts: {removed}")
    if added!=Counter({"The Indomitable":1,"Zephyr Singer":1}): raise ValueError(f"unexpected additions: {added}")
    print("PASS: exact 100 cards, singleton, commander first, unchanged 98 baseline cards, 2 intended swaps, canonical proposal SHA-256")

if __name__=="__main__": main()
