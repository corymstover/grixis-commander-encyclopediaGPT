# Abaddon Test Engine Qualification — Forge Review

**Date:** 2026-10-13  
**Candidate engine:** Card-Forge/forge  
**Status:** PARTIAL SUPPORT EVIDENCE; NOT QUALIFIED FOR THE REGISTERED CONFIRMATORY TEST  
**Gameplay runs performed:** 0

## 1. What was checked

The official Card-Forge repository's current card scripts were located for the key interactions below. These are source-code presence checks, not a live installed-engine test.

| Card | Repository evidence | What the script indicates |
|---|---|---|
| Abaddon the Despoiler | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/a/abaddon_the_despoiler.txt) | Continuous effect applies cascade to qualifying spells cast from hand during your turn, with a mana-value threshold tied to opponents' life lost that turn. |
| Aurora Phoenix | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/a/aurora_phoenix.txt) | Printed cascade and a graveyard trigger that returns it to hand when its controller casts a spell with cascade. |
| Mind's Desire | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/m/minds_desire.txt) | Storm and exile/play permission are scripted. |
| Underworld Breach | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/u/underworld_breach.txt) | Grants escape to nonland cards in the graveyard and has an end-step sacrifice trigger. |
| Brain Freeze | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/b/brain_freeze.txt) | Mills three cards and has storm. |
| Lion's Eye Diamond | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/l/lions_eye_diamond.txt) | Discards hand, sacrifices itself, and produces three mana of one color at instant speed. |
| Wild-Magic Sorcerer | [card script](https://github.com/Card-Forge/forge/blob/6c1810dd0b42213f9ad768d1b5f251753e1e298d/forge-gui/res/cardsfolder/w/wild_magic_sorcerer.txt) | Grants cascade to the first spell its controller casts from exile each turn. |

## 2. Documented engine capabilities and limitations

The Forge project documents command-line AI self-play, including Commander mode and examples of three-player Commander games: [Forge AI documentation](https://github.com/Card-Forge/forge/blob/master/docs/AI.md).

The same documentation explicitly cautions that its AI is poor at most combo decks, and that long self-play games can lag. Abaddon's list includes a compact Underworld Breach/Lion's Eye Diamond/Brain Freeze combo and complex cascade/exile sequencing, so AI self-play outcomes would be conditional on Forge's card implementation and AI policy, not an unbiased estimate of the deck's real-table win rate.

## 3. Qualification gates still not passed

The following are not yet demonstrated:

1. All 94 distinct card names in the isolated variant resolve to the intended card scripts/printings in a pinned Forge release.
2. The selected installed build can load this exact list in Commander mode without substitution, missing-card, or unsupported-effect warnings.
3. Relevant interactions—especially Abaddon's granted cascade, Aurora Phoenix's graveyard trigger, cascade stack ordering, exile casts, storm copies, escape costs, and the Breach loop—behave correctly in that build.
4. The simulator can provide the controlled paired starts and structured event logs required by the registered test protocol.

No Forge binary was installed or run as part of this source inspection. The seven entries above are a targeted source-code sample, not a 94-card coverage audit. Therefore **the engine is not qualified and no gameplay test has been run**.

## 4. Efficient next step

If Forge is pursued, pin a specific release/commit, audit all 94 card identities and relevant scripts, then run a tiny scripted smoke test for the Abaddon/Aurora interaction and a separate Breach/LED/Brain Freeze sequence. Inspect logs and compare them with manually established expected events. Only if those checks pass should Forge be used for exploratory self-play. Do not call that exploratory AI self-play the registered paired confirmatory test unless the fixed-start, event-log, and sample controls can actually be implemented.

A failed or incomplete engine gate is not a deck failure. It means the proposed test method cannot yet support a reliable performance conclusion.


## 5. Follow-up source audit — pinned release identified, not installed

**Follow-up date:** 2026-10-13

A later source-only investigation identified Forge release **`forge-2.0.15`** as a reproducible candidate pin. Its release page records publication on 2026-09-28, and its annotated tag resolves to commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676` (tag object `b18e110a32462958aeda4b7fbac48c06399a2c23`). The tag object is marked unsigned/unverified by GitHub; it is a usable version identifier, not a cryptographically signed provenance guarantee. [Release page](https://github.com/Card-Forge/forge/releases/tag/forge-2.0.15) · [tag object](https://api.github.com/repos/Card-Forge/forge/git/tags/b18e110a32462958aeda4b7fbac48c06399a2c23) · [resolved commit](https://github.com/Card-Forge/forge/commit/4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676).

The six specific card scripts directly fetched from this exact commit resolve to the expected names and Oracle texts for Abaddon the Despoiler, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, and Lion's Eye Diamond. This improves the earlier evidence from unpinned current-branch links to a version-pinned script sample. It remains a **six-card source sample**, not the required 94-card audit. (The earlier seventh script, Wild-Magic Sorcerer, has not yet been fetched at this pinned commit.)

| Qualification item | Follow-up evidence | Status |
|---|---|---|
| Specific release pin | `forge-2.0.15` → commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676` | Identified |
| Key-card scripts at the pinned commit | Abaddon, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, Lion's Eye Diamond | Source text inspected |
| All 94 distinct deck card identities | Not audited at this release | Pending |
| Executable downloaded/installed/launched | Not performed in this environment | Pending |
| Exact 100-card variant loaded under Commander rules | Not performed | Pending |
| Deterministic interaction smoke tests and event logs | Not performed | Pending |
| Controlled paired starts and repeatable seeds | Not demonstrated | Pending |
| Gameplay results | 0 | Not run |

The exact pinned Abaddon script expresses its continuous effect as applying Cascade to cards you control/own on the stack that were cast from hand, restricted to your turn, with the CMC comparison to `Count$LifeOppsLostThisTurn`. Aurora Phoenix is scripted with printed Cascade and a SpellCast trigger in the graveyard for a spell with Cascade. This source-level reading supports the intended interaction; **it does not prove that the running engine implements every relevant stack/trigger edge case correctly**.

Forge's official wiki describes it as a Magic rules engine with support for up to eight players and says it includes over 99% of Magic cards, while explicitly describing the project as independent from Wizards of the Coast. The broad catalog claim is not a substitute for our exact 94-card check. The user guide distinguishes snapshots (daily builds) from releases, describing releases as intended to be stable but not bug-free. [Forge overview](https://github.com/Card-Forge/forge/wiki/) · [User Guide and release notes](https://github.com/Card-Forge/forge/wiki/User-Guide).

### Next technical action

Use the pinned release to fetch/inspect all 94 distinct card identities and identify missing, ambiguous, or scripted-but-unverified effects. The variant has 94 distinct names across 100 cards; the commander is included and no companion is present. Then install/run the exact release in a capable environment, import the exact test variant in Commander mode, and capture console/event output for hand-cast Abaddon cascade, Aurora in graveyard, both possible trigger orderings, cascade casting from exile, storm copies, and the Breach/LED/Brain Freeze line. Keep the engine unqualified until the observed events match the rules-derived expected sequence.

**Current decision remains unchanged:** Forge is not qualified for confirmatory or exploratory gameplay testing yet. No gameplay was run, no swap was approved, and no list was altered.
