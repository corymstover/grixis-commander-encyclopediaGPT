#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OUT = ROOT / "refinement/decisions/Sedris_the_Traitor_King_Whole_List_Decision_Ledger_2026-10-15.csv"
COMMANDER = "Sedris, the Traitor King"
CUTS = Counter({
    "Counterspell": 1,
    "Underworld Breach": 1,
    "Fellwar Stone": 1,
    "Blightstep Pathway // Searstep Pathway": 1,
    "Clearwater Pathway // Murkwater Pathway": 1,
    "Riverglide Pathway // Lavaglide Pathway": 1,
    "Fabled Passage": 1,
    "Bojuka Bog": 1,
})
CUT_REASON = {
    "Counterspell": "CUT — Force of Will better protects tap-out Sedris and unearth/reanimation turns.",
    "Underworld Breach": "CUT — generic recursion whose escape fuel consumes Sedris's graveyard resource; replace with repeatable self-mill/card selection.",
    "Fellwar Stone": "CUT — lowest-synergy generic rock; replace with burst commander acceleration while retaining dense colored rocks/fixing.",
    "Blightstep Pathway // Searstep Pathway": "CUT — replace with untapped typed BR dual Badlands.",
    "Clearwater Pathway // Murkwater Pathway": "CUT — replace with premium fetchland Flooded Strand.",
    "Riverglide Pathway // Lavaglide Pathway": "CUT — replace with premium fetchland Misty Rainforest.",
    "Fabled Passage": "CUT — basic-only fetch sequencing loses to Marsh Flats in the current typed-dual manabase.",
    "Bojuka Bog": "CUT — replace tapped utility land with fetchable Island/Swamp that surveils to feed Sedris.",
}
KEY_KEEP = {
    "Convergence of Dominion": "KEEP — reduces Sedris-granted {2}{B} unearth to {B}; one-mana floor makes extra generic reducers redundant.",
    "Obeka, Brute Chronologist": "KEEP — core end-the-turn protection against resolved unearth delayed exile triggers.",
    "Sundial of the Infinite": "KEEP — repeatable end-the-turn control for unearth delayed exile triggers.",
    "Teferi's Veil": "KEEP — attacking unearthed creatures phase out before the next end-step exile can remove them.",
    "Deadeye Navigator": "KEEP — blink rescue for unearthed creatures plus retained Peregrine Drake mana engine.",
    "Peregrine Drake": "KEEP — part of retained Deadeye Navigator mana engine and valuable untap ETB.",
    "River Kelpie": "KEEP — draws whenever a permanent enters from a graveyard and when graveyard spells are cast.",
    "Twilight Diviner": "KEEP — graveyard-entry payoff that creates one lasting creature-copy token each turn.",
    "Metamorphosis Fanatic": "KEEP — powerful reanimation ETB and excellent Sedris unearth target.",
    "Corpse Connoisseur": "KEEP — creature tutor-to-graveyard that can itself be unearthed.",
    "Dread Return": "KEEP — can be milled and cast from the graveyard without Sedris; flashback converts spare/unearthed bodies into permanent reanimation.",
    "Panharmonicon": "KEEP — doubles the deck's dense creature ETB tutor/removal/reanimation/value package.",
}
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$")


def baseline() -> Counter[str]:
    with tarfile.open(BASELINE_TAR, "r:gz") as tf:
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sedris__the_Traitor_King.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sedris baseline member; found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Sedris baseline")
        raw = fh.read().decode("utf-8-sig")
    out = Counter()
    for line in raw.splitlines():
        if not line.strip():
            continue
        m = LINE_RE.match(line)
        if not m:
            raise RuntimeError(f"Malformed baseline line: {line}")
        out[m.group(2).strip()] += int(m.group(1))
    return out


def main() -> None:
    cards = baseline()
    if sum(cards.values()) != 100 or len(cards) != 99:
        raise RuntimeError(f"Unexpected baseline structure: {sum(cards.values())} / {len(cards)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["card", "baseline_qty", "keep_qty", "cut_qty", "decision", "rationale"])
        for card in sorted((x for x in cards if x != COMMANDER), key=str.casefold):
            b = cards[card]; c = CUTS[card]; k = b - c
            decision = "KEEP" if c == 0 else ("CUT" if k == 0 else "PARTIAL")
            rationale = CUT_REASON.get(card) or KEY_KEEP.get(card) or "KEEP — retained after commander-first unearth/reanimation, interaction, curve, mana and identity audit."
            w.writerow([card, b, k, c, decision, rationale])
    baseline_noncommander = sum(cards[x] for x in cards if x != COMMANDER)
    keep = sum(cards[x] - CUTS[x] for x in cards if x != COMMANDER)
    cut = sum(CUTS.values())
    if (baseline_noncommander, keep, cut) != (99, 91, 8):
        raise RuntimeError(f"Expected 99 / 91 KEEP / 8 CUT, found {baseline_noncommander} / {keep} / {cut}")
    print(f"Wrote {OUT.relative_to(ROOT)}: {baseline_noncommander} copies, {keep} KEEP / {cut} CUT")


if __name__ == "__main__":
    main()
