# Abaddon Breach Sequence Audit — Bounded Review

**Date:** 2026-10-13 UTC  
**Baseline:** 2026-10-12 frozen list  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**List changes:** none

## Scope and conclusion

This review assesses the existing Underworld Breach + Lion's Eye Diamond + Brain Freeze package at the rules-structure level. The combination is a resource-dependent graveyard engine, not an unconditional infinite loop. Its exact feasibility depends on initial zones, mana colors, library/graveyard contents, storm count, opponents' interaction, and the number of cards remaining to pay escape costs.

**Disposition: PARTIALLY VERIFIED — no deterministic turn sequence certified from the available source record.** The prior review identified an established starting state of Breach and LED on the battlefield, Brain Freeze in the graveyard, and six or more other cards available across hand/graveyard. This audit records the essential cost constraints but does not claim a guaranteed kill from arbitrary starting state.

## Step-by-step cost and zone constraints

1. **Underworld Breach must already be on the battlefield.** Its escape permission applies to cards in your graveyard and requires the card's own mana cost plus exiling three other cards from that graveyard for each escape cast. The three exiled cards are consumed as cost; those cards cannot also be counted as available future escape fuel.
2. **Lion's Eye Diamond must be on the battlefield and available to activate.** Its mana ability requires sacrificing LED and discarding your hand as costs, then adds three mana of one chosen color. Once activated, the hand is gone before the mana can be spent. The activation cannot be interrupted by ordinary responses to a mana ability, although players receive priority around the broader sequence.
3. **Brain Freeze must be in the graveyard or otherwise become accessible to cast.** Escaping it requires its {1}{U} cost plus exiling three other graveyard cards. If LED produces blue, its three mana can pay {1}{U} and leave one mana, but all other escape requirements still apply.
4. **Brain Freeze has storm.** Its storm trigger creates a copy for each spell cast before it that turn. These copies are not cast; they do not independently increase storm count, trigger ordinary cast abilities, or receive Abaddon-granted cascade. Storm-Kiln Artist is an explicit exception in this deck because its magecraft triggers on copying an instant or sorcery.
5. **Mill must preserve the engine.** Brain Freeze can target yourself to seed further cards into your graveyard, but the three-card escape payment for each subsequent escape and the cards consumed by prior costs must be paid from cards still available. Self-mill and opponent-mill amounts are choices per resolution of Brain Freeze or each storm copy; the pilot must count totals rather than assume a particular number of casts automatically mills out an opponent.
6. **A self-sustaining loop requires a fuel proof.** The sequence must account for each escape casting, all three exiled cards, available mana, and how each resolution generates enough additional cards/mana to continue. This review does not assert an infinite absent that accounting.
7. **The finish is not automatically secured by an opponent having an empty library.** A player loses when attempting to draw from an empty library and the game state reaches the relevant rule check; empty library alone is not an immediate loss. Wheel of Fortune/Windfall finishes also require that the caster can safely resolve the draw effect without losing first.
8. **The route can be stopped.** Countermagic, graveyard-hate effects, removing Breach or a needed permanent, exhausting escape fuel, or incorrect mana color can break the route. Do not describe it as deterministic through interaction.

## Rules distinctions relevant to Abaddon

- Abaddon's granted cascade requires casting the spell from hand and the mana value threshold based on aggregate opponent life lost this turn. LED and Brain Freeze escaped from the graveyard do not receive Abaddon-granted cascade solely from being cast.
- Storm copies are copies, not casts. They can trigger Storm-Kiln Artist's copy wording, but not cast-only effects such as Exalted Flamer of Tzeentch or cast-from-exile payoffs.
- Cost paid and mana value are separate. Alternate costs and cost reductions do not change a card's mana value for Abaddon's threshold or cascade's mana-value comparison.

## Verification status and required evidence for closure

The original source package names the combo and gives a common starting requirement but does not provide a complete card-by-card deterministic sequence. The current Forge AI pilot is not suitable evidence because it did not cast the competing candidate cards; no new Forge performance run is authorized by this audit.

To close this as **RULES-COHERENT WITH SPECIFIED CONDITIONS**, the evidence record must include a worked sequence with an explicit starting zone inventory, exact mana, every spell cast, each escape payment, storm count, self-mill allocation, and fuel ledger at each iteration. Until that is recorded and independently checked against the current Comprehensive Rules and Oracle text, retain **PARTIALLY VERIFIED**.

## Sources

- [Official Magic Comprehensive Rules, effective September 25, 2026](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt): storm (702.40), cascade (702.85), copies (707.10), and drawing from an empty library (121.4).
- [Scryfall — Underworld Breach](https://scryfall.com/card/thb/161/underworld-breach)
- [Scryfall — Lion's Eye Diamond](https://scryfall.com/card/mir/307/lions-eye-diamond)
- [Scryfall — Brain Freeze](https://scryfall.com/card/scg/29/brain-freeze)
- [EDHREC combo record](https://edhrec.com/combos/izzet/1368-3518-4856): useful discovery evidence for typical setup/fuel, not itself proof that a particular starting state executes without resource shortfall.

No list changes are authorized by this report.
