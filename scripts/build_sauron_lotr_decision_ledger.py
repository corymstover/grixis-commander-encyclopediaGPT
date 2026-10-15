#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_TAR = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OUT = ROOT / "refinement/decisions/Sauron_Lord_of_the_Rings_Whole_List_Decision_Ledger_2026-10-15.csv"
COMMANDER = "Sauron, Lord of the Rings"
CUTS = Counter({
    "Knollspine Dragon": 1,
    "Notion Thief": 1,
    "In the Darkness Bind Them": 1,
    "Stitch Together": 1,
    "Counterspell": 1,
    "Crumbling Necropolis": 1,
    "Drowned Catacomb": 1,
    "Sulfurous Springs": 1,
    "Underground River": 1,
    "Island": 1,
    "Mountain": 1,
    "Swamp": 1,
})
CUT_REASON = {
    "Knollspine Dragon": "CUT — conditional ETB draw needs prior opponent damage that turn; unreliable from Sauron's often-precombat cast-trigger reanimation.",
    "Notion Thief": "CUT — generic Grixis wheel/value piece; replace with commander-specific acceleration.",
    "In the Darkness Bind Them": "CUT — flavorful but slow five-mana saga; Ring/Nazgûl identity remains dense without it.",
    "Stitch Together": "CUT — threshold-dependent battlefield recursion loses to deterministic two-mana Dance of the Dead.",
    "Counterspell": "CUT — Force of Will better protects tap-out Sauron/reanimation turns.",
    "Crumbling Necropolis": "CUT — always tapped; replace with premium untapped typed fixing.",
    "Drowned Catacomb": "CUT — conditional dual; replace with unconditional three-color fixing.",
    "Sulfurous Springs": "CUT — replace painland with fetchland for typed-land access.",
    "Underground River": "CUT — replace painland with fetchland for typed-land access.",
    "Island": "PARTIAL — reduce from two to one while retaining Island-typed duals for Wonder.",
    "Mountain": "PARTIAL — reduce from two to one while retaining Mountain-typed duals for Anger.",
    "Swamp": "PARTIAL — reduce from three to two while preserving basic black access.",
}
KEY_KEEP = {
    "Entomb": "KEEP — best one-mana graveyard tutor; directly sets Sauron's cast-trigger reanimation.",
    "Buried Alive": "KEEP — core graveyard setup that can seed Anger/Wonder plus a premium target.",
    "Reanimate": "KEEP — premier one-mana reanimation spell.",
    "Animate Dead": "KEEP — efficient two-mana reanimation core.",
    "Necromancy": "KEEP — flexible reanimation core with emergency instant-speed mode.",
    "Persist": "KEEP — efficient two-mana recursion for nonlegendary threats.",
    "Victimize": "KEEP — efficient two-creature recursion that converts expendable bodies into value.",
    "Living Death": "KEEP — mass reanimation/reset that strongly rewards intentional graveyard setup.",
    "Nazgûl": "KEEP — four copies are permitted by Nazgûl's deckbuilding text and directly reward Ring temptation.",
    "Call of the Ring": "KEEP — repeatable Ring temptation and card advantage that sustains the Nazgûl package.",
    "Anger": "KEEP — graveyard haste engine; revised mana base retains ample Mountain-typed lands.",
    "Wonder": "KEEP — graveyard evasion engine; revised mana base retains ample Island-typed lands.",
    "The Mouth of Sauron": "KEEP — thematic self-mill/amass engine that can target its controller to stock the graveyard.",
    "Sauron, the Dark Lord": "KEEP — thematic high-impact threat; Ring temptation can refill while discarding reanimation targets.",
    "Relic of Sauron": "KEEP — thematic ramp plus draw/discard outlet supporting both commander casting and graveyard setup.",
    "Sneak Attack": "KEEP — cheats large threats into play and naturally stocks them for later recursion.",
}
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s+\([^()]*\)\s+\S+\s+\[[^\]]+\]\s*$")


def baseline() -> Counter[str]:
    with tarfile.open(BASELINE_TAR, "r:gz") as tf:
        matches = [m for m in tf.getmembers() if m.isfile() and m.name.endswith("Sauron__Lord_of_the_Rings.txt")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one Sauron baseline member; found {len(matches)}")
        raw = tf.extractfile(matches[0]).read().decode("utf-8-sig")
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
            rationale = CUT_REASON.get(card) or KEY_KEEP.get(card) or "KEEP — retained after commander-first graveyard/reanimation, interaction, curve, and identity audit."
            w.writerow([card, b, k, c, decision, rationale])
    if sum(cards[x] for x in cards if x != COMMANDER) != 99:
        raise RuntimeError("Noncommander baseline copy count is not 99")
    keep = sum(cards[x] - CUTS[x] for x in cards if x != COMMANDER)
    cut = sum(CUTS.values())
    if (keep, cut) != (87, 12):
        raise RuntimeError(f"Expected 87 KEEP / 12 CUT, found {keep} / {cut}")
    print(f"Wrote {OUT.relative_to(ROOT)}: 99 copies, {keep} KEEP / {cut} CUT")


if __name__ == "__main__":
    main()
