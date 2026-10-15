#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OUT = ROOT / "refinement/decisions/Solkanar_the_Swamp_King_Whole_List_Decision_Ledger_2026-10-15.csv"
COMMANDER = "Sol'kanar the Swamp King"
CUTS = Counter({
    "Feed the Swarm": 1,
    "Fellwar Stone": 1,
    "Blightstep Pathway // Searstep Pathway": 1,
    "Dragonskull Summit": 1,
    "Drowned Catacomb": 1,
})
CUT_REASON = {
    "Feed the Swarm": "CUT — Withering Torment preserves creature/enchantment coverage at instant speed with a fixed two-life cost and remains a black spell.",
    "Fellwar Stone": "CUT — The Soul Stone keeps the two-mana ramp slot while being a black spell, indestructible and a late-game reanimation engine.",
    "Blightstep Pathway // Searstep Pathway": "CUT — Fell the Profane // Fell Mire preserves a land-capable slot while adding a black instant removal mode.",
    "Dragonskull Summit": "CUT — Raucous Theater is a fetchable Swamp Mountain with surveil and direct Swamp-matters synergy.",
    "Drowned Catacomb": "CUT — Undercity Sewers is a fetchable Island Swamp with surveil and direct Swamp-matters synergy.",
}
KEY_KEEP = {
    "Demon's Horn": "KEEP — parallel black-spell trigger to Sol'kanar; Painter's Servant naming black raises its ceiling dramatically.",
    "Painter's Servant": "KEEP — naming black turns all spells black for Sol'kanar/Demon's Horn and remains part of Painter/Grindstone.",
    "Grindstone": "KEEP — compact secondary finish with Painter's Servant; Painter is independently commander-essential.",
    "Blanket of Night": "KEEP — global Swamp conversion enables swampwalk and amplifies Coffers/Crypt Ghast/Dread Presence/Consuming Corruption.",
    "Urborg, Tomb of Yawgmoth": "KEEP — second global Swamp-conversion engine and key Coffers/commander support.",
    "Cabal Coffers": "KEEP — major mana engine with the deck's natural and global Swamp infrastructure.",
    "Crypt Ghast": "KEEP — doubles black mana from Swamps and rewards the typed-land plan.",
    "Dread Presence": "KEEP — Swamp-entry card selection/removal/lifegain engine.",
    "Consuming Corruption": "KEEP — Swamp-scaling black removal that also gains life.",
    "Exquisite Blood": "KEEP — core life-loss-to-life-gain engine and deterministic combo half with multiple gain-to-loss payoffs.",
    "Bloodthirsty Conqueror": "KEEP — redundant Exquisite Blood effect on a threat body; preserves compact combo density.",
    "Vito, Thorn of the Dusk Rose": "KEEP — efficient gain-to-loss payoff and Exquisite/Bloodthirsty combo half.",
    "Enduring Tenacity": "KEEP — resilient gain-to-loss payoff and combo half.",
    "Marauding Blight-Priest": "KEEP — each lifegain event drains every opponent; combos with Exquisite/Bloodthirsty engines.",
    "Starscape Cleric": "KEEP — BLB #116 black Bat Cleric; low-cost gain-to-loss payoff with offspring redundancy.",
    "Aetherflux Reservoir": "KEEP — converts repeated spell/lifegain sequences into a direct finisher.",
    "Bolas's Citadel": "KEEP — lifegain offsets life-paid spell velocity and black-spell casting advances the commander engine.",
    "K'rrik, Son of Yawgmoth": "KEEP — turns black pips into life payments that the deck is built to recover.",
}
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$")


def baseline() -> Counter[str]:
    with tarfile.open(BASELINE_TAR, "r:gz") as tf:
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sol_kanar_the_Swamp_King.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sol'kanar baseline member; found {len(matches)}")
        fh = tf.extractfile(matches[0])
        if fh is None:
            raise RuntimeError("Unable to extract Sol'kanar baseline")
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
    if sum(cards.values()) != 100 or len(cards) != 95:
        raise RuntimeError(f"Unexpected baseline structure: {sum(cards.values())} / {len(cards)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["card", "baseline_qty", "keep_qty", "cut_qty", "decision", "rationale"])
        for card in sorted((x for x in cards if x != COMMANDER), key=str.casefold):
            b = cards[card]; c = CUTS[card]; k = b - c
            decision = "KEEP" if c == 0 else ("CUT" if k == 0 else "PARTIAL")
            rationale = CUT_REASON.get(card) or KEY_KEEP.get(card) or "KEEP — retained after commander-first black-spell/lifegain, Swamp infrastructure, interaction, curve, mana and identity audit."
            w.writerow([card, b, k, c, decision, rationale])
    baseline_noncommander = sum(cards[x] for x in cards if x != COMMANDER)
    keep = sum(cards[x] - CUTS[x] for x in cards if x != COMMANDER)
    cut = sum(CUTS.values())
    if (baseline_noncommander, keep, cut) != (99, 94, 5):
        raise RuntimeError(f"Expected 99 / 94 KEEP / 5 CUT, found {baseline_noncommander} / {keep} / {cut}")
    print(f"Wrote {OUT.relative_to(ROOT)}: {baseline_noncommander} copies, {keep} KEEP / {cut} CUT")


if __name__ == "__main__":
    main()
