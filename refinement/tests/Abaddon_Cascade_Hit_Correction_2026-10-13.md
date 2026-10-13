# Abaddon the Despoiler — Cascade Hit Correction

**Date:** 2026-10-13 UTC  
**Frozen baseline:** 2026-10-12; unchanged  
**Authority:** current Scryfall bulk overlay exact-matched against the frozen card printings  
**Disposition:** This note supersedes conflicting cascade-hit claims in prior triage prose.

## Correct zero-mana-value nonlands

The deck contains exactly seven 0-mana-value nonlands:

1. Ancestral Vision
2. Chrome Mox
3. Inevitable Betrayal
4. Lion's Eye Diamond
5. Lotus Petal
6. Pact of Negation
7. Profane Tutor

**Wheel of Fate is not in this deck** and must not be counted.

## Correct cascade conclusions

- A cascade source with mana value 1 can potentially hit any of these seven cards.
- A cascade source with mana value 3 can potentially hit any nonland card with mana value 0, 1, or 2.
- These are possible hits, not guaranteed outcomes. Cascade skips lands and compares the hit's mana value against the source spell's mana value—not against Abaddon's life-loss threshold.
- Ancestral Vision, Inevitable Betrayal, and Profane Tutor have no mana cost; an effect such as cascade can permit them to be cast without paying that cost. Inevitable Betrayal still needs a legal target.
- Pact of Negation has mana value 0. If Abaddon grants it cascade when cast from hand during your turn, the cascade trigger has no legal hit because no card has negative mana value. A 0-mana-value spell can receive cascade but cannot hit another card through cascade.
- Chrome Mox may be cast from cascade but can enter without an imprint card and then fail to produce mana. No hit is guaranteed or necessarily useful.

## Ordering and exile-play corrections

Cascade resolves before the source spell. Therefore a mana-value-1 tutor cannot set up the top card and then reveal that card with its own cascade; it can set up a later spell. Damage and cast triggers that occur after a spell is cast cannot retroactively grant that spell cascade.

A land played from exile is not a spell cast and does not receive Abaddon's hand-only cascade or trigger spell-cast payoffs. It **does** trigger Prosper, Tome-Bound's Treasure ability because Prosper triggers when a card is played from exile.

## Scope

This corrects the identified false cascade claims. It does not claim a probability, a win rate, or exhaustive proof of every possible game state. The full current card-by-card audit is in `Abaddon_Current_Card_Audit_2026-10-13.csv` and its summary/report.
