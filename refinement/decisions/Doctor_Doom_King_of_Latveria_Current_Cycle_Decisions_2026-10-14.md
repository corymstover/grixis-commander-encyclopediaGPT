# Doctor Doom, King of Latveria — Current-Cycle Refinement Decision Record

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Status:** working approval candidate; explicit user approval still required  
**Baseline SHA-256:** `08825dee74f034bc38415fe7370cccc3fe69de7887769577dd32f98f5bbd4572`  
**Candidate SHA-256:** `c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58`

## Mandatory whole-list audit

All 99 noncommander slots were challenged against their actual roles, commander necessity, curve, mana, interaction density, redundancy, and current alternatives. The deck remains at 38 lands after the proposed land-for-land change, and the five nonland additions have the same combined mana value as the five nonland cuts, so the nonland curve does not increase.

The audit identified one structurally weak package: `Liliana's Caress`, `Geth's Grimoire`, and `Waste Not` only reward **opponents** discarding, while Doom's Oracle text rewards **you** discarding lands. `Dark Deal` is the weakest wheel in this commander because discarding a hand containing multiple lands is still one Doom trigger and Dark Deal then draws one fewer card. `Oskar, Rubbish Reclaimer` is strong in generic discard, but only recovers nonlands and overlaps broader recovery already supplied by Moonstone, Containment Construct, and Norman Osborn. `Smoldering Marsh` is the least commander-specific land among realistic land cuts and preserves the 38-land count when exchanged for Dakmor Salvage.

## Proposed changes

| OUT | IN | Decision rationale |
|---|---|---|
| Liliana's Caress | Glorious Purpose | Replaces opponent-discard punishment with a two-mana Plan that rewards every connive, grows the conniving creature, and converts six connives into a four-card free-cast/value burst. Doom, Kang, Ultron, Lethal Scheme, and Villainous Hideout all naturally advance it. |
| Geth's Grimoire | Chameleon, Master of Disguise | Grimoire depends on opponents discarding. Chameleon can enter as a Doom copy while retaining a different name, creating another independent Doom engine without a legend-rule conflict; mayhem also lets the deck cast Chameleon after deliberately discarding it. |
| Waste Not | Roaming Throne | Waste Not rewards the wrong side of the discard exchange. Throne can choose Villain, doubling both of Doom's triggered abilities and many other Villain triggers throughout the deck. |
| Dark Deal | Psychic Frog | Dark Deal compresses all lands discarded from a hand into one Doom trigger. Psychic Frog is a two-mana, zero-mana-cost repeatable discard outlet: each land can be discarded as a separate activation/event, creating a separate Doom trigger while Frog becomes a threat and can draw on combat. |
| Oskar, Rubbish Reclaimer | Spark Double | Oskar only converts nonland discards and is redundant with broader graveyard/discard access. Spark Double can become a nonlegendary Doom copy and independently doubles the commander's core drain/connive engine; it can copy another engine when Doom is unavailable. |
| Smoldering Marsh | Dakmor Salvage | Keeps 38 lands while turning a low-utility conditional dual into renewable discard ammunition. Dredge 2 can replace a later draw to return Dakmor after it is discarded, enabling repeatable Doom loops with existing Trade Routes/Bone Miser or Surly Badgersaur infrastructure. |

## Important retained cards

- `Wheel of Fortune` and `Windfall` remain despite Doom only seeing one land-discard trigger from a multi-card hand discard. Their role is high-efficiency refill after this deck has deliberately depleted its hand, and Bone Miser, Surly Badgersaur, Archfiend of Ifnir, Cool but Rude, Monument to Endurance, and other cards still process individual discarded cards.
- `Change of Fortune` is retained over Dark Deal because it is self-focused and its refill scales with the total number of cards already discarded that turn.
- `Cool but Rude`, `Tectonic Reformation`, `Trade Routes`, `Seismic Assault`, `Bone Miser`, `Surly Badgersaur`, `Containment Construct`, `Crucible of Worlds`, `Moonstone, Harsh Mistress`, `Monument to Endurance`, `Green Goblin, Nemesis`, `Prowler, Clawed Thief`, and `Shadow of the Grave` form the commander-specific land/self-discard core.
- `Lethal Scheme`, `Kang, Temporal Tyrant`, and `Villainous Hideout` are already present in the authoritative baseline despite appearing near the top of the candidate-ranking file due to the research-package snapshot discrepancy.

## Candidate exhaustion / red-team review

Serious alternatives reviewed included `Coastal Peak`, `Typhoid Mary, Fractured`, `Living Laser`, `Ledger Shredder`, `Red Ghost, Intangible Genius`, `Archnemesis`, `Doctor Octopus, Master Planner`, `Doom's Time Platform`, `The Frightful Four`, `Progenitor's Icon`, `Withering Torment`, `Blasphemous Act`, `Glint-Horn Buccaneer`, `Teferi's Ageless Insight`, `Swiftfoot Boots`, `Putrid Imp`, `Land's Edge`, and the cycling-land tail.

None produced a new material improvement after slot-cost comparison. The closest alternatives were Ledger Shredder and Putrid Imp as additional discard outlets, Living Laser as a discard-volume combat payoff, and Archnemesis as value/pressure. Psychic Frog is the superior free discard outlet because each activation can separate land discards while also supplying threat/card advantage; the two Doom-copy creatures and Roaming Throne give more direct commander redundancy than the five-mana-plus tribal/value challengers. Glorious Purpose has stronger commander-specific connive coverage than generic draw/value options. Dakmor Salvage is the land candidate with the highest strategic leverage because it is both a land slot and reusable discard fuel.

A second serious pass produced **zero new material improvements**.

## Current external-evidence checkpoint

Current EDHREC optimized Doom data is supporting evidence only. It strongly supports the retained commander-specific core and the proposed copy/connive package: Glorious Purpose has high lift in optimized Doom lists; Spark Double, Psychic Frog, Chameleon, and Roaming Throne all appear in optimized Doom subsets, including cycling/control shells. Conversely, Waste Not and Liliana's Caress have low lift in optimized discard-tagged Doom decks. These observations corroborate, but do not substitute for, the commander-first slot analysis.

## Power classification

**Bracket 4 — Optimized**  
Proposed tags: **Land Discard / Villains / Connive**
