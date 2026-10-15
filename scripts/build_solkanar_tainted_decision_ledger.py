#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OUT = ROOT / "refinement/decisions/Solkanar_the_Tainted_Whole_List_Decision_Ledger_2026-10-15.csv"
COMMANDER = "Sol'Kanar the Tainted"
CUTS = Counter({
    "Arcane Denial": 1,
    "Fellwar Stone": 1,
    "Feed the Swarm": 1,
    "Lightning Greaves": 1,
    "Clackbridge Troll": 1,
    "Brainstealer Dragon": 1,
    "Disrupt Decorum": 1,
    "Dragonskull Summit": 1,
    "Drowned Catacomb": 1,
    "Riverglide Pathway // Lavaglide Pathway": 1,
    "Shivan Reef": 1,
    "Sulfurous Springs": 1,
    "Underground River": 1,
})
CUT_REASON = {
    "Arcane Denial": "CUT — Force of Will better protects tap-out Sol'Kanar without giving the countered player up to two cards.",
    "Fellwar Stone": "CUT — replace lowest-impact generic rock with Mana Vault burst acceleration toward five-mana commander.",
    "Feed the Swarm": "CUT — Withering Torment preserves creature/enchantment coverage at instant speed with fixed life loss.",
    "Lightning Greaves": "CUT — shroud can prevent Thassa/Closet/Planar Incision from targeting Sol'Kanar; Deflecting Swat protects without blocking friendly targeting.",
    "Clackbridge Troll": "CUT — lower-impact group-hug body replaced by Immortal Coil, a lethal commander-native cursed gift.",
    "Brainstealer Dragon": "CUT — seven-mana generic theft engine replaced by seven-mana self-donating Captive Audience.",
    "Disrupt Decorum": "CUT — Kardur already supplies blink-reusable forced combat; replace with repeatable Sol'Kanar reset engine.",
    "Dragonskull Summit": "CUT — replace conditional BR land with untapped typed Badlands.",
    "Drowned Catacomb": "CUT — replace conditional UB land with untapped typed Underground Sea.",
    "Riverglide Pathway // Lavaglide Pathway": "CUT — replace face-locked UR source with untapped typed Volcanic Island.",
    "Shivan Reef": "CUT — replace two-color pain source with premium fetchland Flooded Strand.",
    "Sulfurous Springs": "CUT — replace two-color pain source with premium fetchland Marsh Flats.",
    "Underground River": "CUT — replace two-color pain source with premium fetchland Misty Rainforest.",
}
KEY_KEEP = {
    "Thassa, Deep-Dwelling": "KEEP — repeatable end-step Sol'Kanar blink/reset engine and ETB reuse.",
    "Planar Incision": "KEEP — one-shot reset that can target an opponent-controlled Sol'Kanar and return it under its owner's control.",
    "Homeward Path": "KEEP — land-based recovery of owned creatures including transferred Sol'Kanar.",
    "Coveted Falcon": "KEEP — mass donation on disguise plus attack-based recovery of owned permanents.",
    "Demonic Pact": "KEEP — premium giftable losing-game curse; mode history persists through control changes of same object.",
    "Archfiend of the Dross": "KEEP — giftable losing-game threat with oil-counter clock.",
    "Greed's Gambit": "KEEP — front-loads cards/life/tokens and transfers continuing/leave-battlefield liabilities.",
    "Illusions of Grandeur": "KEEP — classic Donate payoff and life-swing curse.",
    "Fateful Handoff": "KEEP — draws from artifact/creature mana value then gives that permanent away; excellent with Immortal Coil and gift creatures.",
    "Bazaar Trader": "KEEP — repeatable artifact/creature/land donation outlet.",
    "Jon Irenicus, Shattered One": "KEEP — permanent creature donation plus goad and can't-be-sacrificed liability.",
    "Kain, Traitorous Dragoon": "KEEP — self-transferring combat-damage engine that draws cards and creates Treasures.",
    "Khârn the Betrayer": "KEEP — control-loss card advantage and political forced-combat piece.",
    "Xantcha, Sleeper Agent": "KEEP — enters under opponent control and converts opponent life into owner card draw.",
    "Puca's Mischief": "KEEP — repeatable nonland exchange engine.",
    "Shifting Grift": "KEEP — flexible artifact/creature/enchantment exchange card central to gift package.",
}
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$")


def baseline() -> Counter[str]:
    with tarfile.open(BASELINE_TAR, "r:gz") as tf:
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sol_kanar_the_Tainted.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Solkanar Tainted baseline member; found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Solkanar Tainted baseline")
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
    if sum(cards.values()) != 100 or len(cards) != 93:
        raise RuntimeError(f"Unexpected baseline structure: {sum(cards.values())} / {len(cards)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["card", "baseline_qty", "keep_qty", "cut_qty", "decision", "rationale"])
        for card in sorted((x for x in cards if x != COMMANDER), key=str.casefold):
            b = cards[card]; c = CUTS[card]; k = b - c
            decision = "KEEP" if c == 0 else ("CUT" if k == 0 else "PARTIAL")
            rationale = CUT_REASON.get(card) or KEY_KEEP.get(card) or "KEEP — retained after commander-first transfer/blink/curse, interaction, curve, mana and identity audit."
            w.writerow([card, b, k, c, decision, rationale])
    baseline_noncommander = sum(cards[x] for x in cards if x != COMMANDER)
    keep = sum(cards[x] - CUTS[x] for x in cards if x != COMMANDER)
    cut = sum(CUTS.values())
    if (baseline_noncommander, keep, cut) != (99, 86, 13):
        raise RuntimeError(f"Expected 99 / 86 KEEP / 13 CUT, found {baseline_noncommander} / {keep} / {cut}")
    print(f"Wrote {OUT.relative_to(ROOT)}: {baseline_noncommander} copies, {keep} KEEP / {cut} CUT")


if __name__ == "__main__":
    main()
