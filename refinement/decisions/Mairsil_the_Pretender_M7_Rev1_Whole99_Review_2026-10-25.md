# Deck #33 — Mairsil, the Pretender — M7 Rev1 whole-99 commander-first audit

**Decision:** Six exact approved changes (Cory, 2026-10-25), raw 100-card SHA `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`. Bracket 4 — Optimized. The original October 14 source and all associated decisions remain historical records.

Mairsil cages owned artifact/creature cards from hand or graveyard, receives their **activated** abilities while they remain in exile with cage counters, and restricts each directly acquired ability to one activation per turn. The identity-driven strategy is graveyard preparation, selective caging, blink/recage, haste/untap, copies of activation instances and alternate activated-ability finishers. The 99 was reviewed for redundant or necessary payloads, mana source quality, activated-ability tempo, stack protection, toolbox draw, tutors, removal, and commander dependence.

## Approved six-slot comparison

| Selected addition | Actual cut | Improvement and opportunity cost |
|---|---|---|
| Marsh Flats | Haunted Ridge | Searches available Swamp-typed typed Grixis dual/shock now; gives up a safer standalone BR late land, adds life/search exposure. |
| Misty Rainforest | Shipwreck Marsh | Searches Island-typed Grixis dual/shock now; gives up a later untapped UB dual, adds life/search exposure. |
| Riptide Laboratory | Sokenzan, Crucible of Defiance | Mairsil is a Wizard and can be bounced to hand at instant speed for recaging/protection without tax; loses a red source and emergency Spirit tokens. |
| Cavern Harpy | Cephalid Inkshrouder | Caged pay-life self-return protects Mairsil from mass removal and resets by hand-cast; gives up free discard for graveyard setup, shroud and unblockability, and must pay four to recast. |
| Agatha's Soul Cauldron | Omen Hawker | On-board activated-ability mana fixing, creature ability sharing via its **own** exiles and graveyard hate; gives up the cheap one-mana restricted accelerator; Cauldron exiles and cages are separate. |
| Phyrexian Devourer | Torchling | Caged payload grants counter growth without its nonactivated sacrifice drawback, supporting power-to-damage Hateflayer lines; gives up red untap/redirection and is once per instance without Quicksilver. |

The fetches emerged in old M6 PRs #285/#440 as unapproved findings. Four additions beyond those were independently challenged in the whole-99 M7 process. Key protected Mairsil synergies include Quicksilver Elemental, Gilded Lotus, Horseshoe Crab, Morphling, Endling, Pack Rat, Rings of Brighthearth, Staff of Domination, Spark Double, Aetherling, Displacer Kitten, Asmodeus, Tree of Perdition, Hateflayer and Walking Ballista. Baseline still carries fast mana, 32 lands, tutors and stack interaction. The commander identity takes priority over Thassa's Oracle/Consultation shortcuts.

## Alternatives challenged

- **Sanctum of Eternity for Stormcarved Coast** would make seven swaps and a second commander bounce land, but adds another colorless output, and Sanctum only bounces on your own turn. Exact whole-100 challenger SHA `7327154c34cdc34fd18f1bde36b096d10491000da946b3b36d775e9bb6e76f33`.
- **Strionic Resonator for Fellwar Stone** would double later Mairsil ETB triggers, but costs another two mana to use and reduces early reliable colored mana for the four-mana UBR commander. Exact whole-100 challenger SHA `1e690ac39a8994635d2e72b47d15b8a7049b38ace92f1b3c4bfe1dcd0860950e`.
- **Pili-Pala** is another Quicksilver/Gilded Lotus line, but redundant with existing untap payloads.
- **Necrotic Ooze** could share activated graveyard abilities, but caging the best creature payloads exiles them outside Ooze's reach.
- **The One Ring** is exceptional generic card advantage but less Mairsil-specific than Cauldron's activated-mana/ability-sharing utility.
- **Swiftfoot Boots** avoids self-targeting conflicts of Greaves shroud, but spends an equip mana and loses Greaves' immediate zero-equip haste. It was considered and held.

The quality-based stop is six: removing further early colored sources, protected combo tools or core interaction did not show a clear net advantage. Six is not an automatic maximum. Ten material judgments, eight weak incumbents and two physical higher-count decks are preserved in engineering [PR #713](https://github.com/corymstover/GrokBotMTGCompanion/pull/713).

Source evidence combines the October 14 verified baseline and approved decision record, prior M6 PR #285/#440, EDHREC Mairsil Top/High Lift, Commander Spellbook, present Scryfall Oracle/legality for added cards and Wizards' Commander banned list. Structural checks and finite rules analysis are not controlled multiplayer simulation. No full new M6 I/J seal or technical third-model independence is asserted.

**Owner approval:** exactly six one-for-one changes, 100 cards/100 distinct/32 lands, raw SHA `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`; approved and locked upon canonical post-merge verification. **Tags:** Cage Toolbox / Activated Abilities / Combo.
