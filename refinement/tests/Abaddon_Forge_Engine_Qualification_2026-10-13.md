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
