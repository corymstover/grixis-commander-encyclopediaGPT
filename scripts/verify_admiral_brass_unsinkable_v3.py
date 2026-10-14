#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import hashlib,re,tarfile
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/"source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
PROPOSAL=ROOT/"refinement/decklists/Admiral_Brass_Unsinkable_Proposed_Final_2026-10-13.txt"
EXPECTED="3857cf322615957d799b29d4fa753fa6f80086700c1053145675b345056b6dae"
def main():
    with tarfile.open(ARCHIVE,"r:gz") as tf:
        raw=tf.extractfile("TXT/Admiral_Brass__Unsinkable.txt").read().decode("utf-8-sig")
    original=Counter()
    for line in raw.splitlines():
        if not line.strip(): continue
        m=re.match(r"^(\d+)x (.+?) \([^()]*\) \S+ .*",line)
        if not m: raise ValueError(line)
        original[m.group(2)]+=int(m.group(1))
    data=PROPOSAL.read_bytes()
    if hashlib.sha256(data).hexdigest()!=EXPECTED: raise ValueError("proposal hash mismatch")
    proposed=Counter()
    lines=data.decode().splitlines()
    if lines[0]!="1x Admiral Brass, Unsinkable [Commander]": raise ValueError("commander first/marker failed")
    for line in lines:
        m=re.match(r"^(\d+)x (.+?)(?: \[Commander\])?$",line)
        if not m: raise ValueError(line)
        proposed[m.group(2)]+=int(m.group(1))
    if sum(proposed.values())!=100: raise ValueError("not 100")
    basics={"Island","Mountain","Swamp","Plains","Forest","Wastes"}
    if any(q!=1 for n,q in proposed.items() if n not in basics): raise ValueError("singleton")
    if original-proposed != Counter({"Revel in Riches":1}): raise ValueError(f"cuts {original-proposed}")
    if proposed-original != Counter({"Power Conduit":1}): raise ValueError(f"adds {proposed-original}")
    print("PASS: exact 100, singleton, commander first, canonical hash, and only intended one-for-one swap")
if __name__=="__main__": main()
