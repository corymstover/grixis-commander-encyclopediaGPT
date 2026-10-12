# Supplemental Card Metadata Resolution — Starscape Cleric

**Deck:** Sol'kanar the Swamp King  
**Exact printing in deck export:** Bloomburrow (BLB), collector number 116  
**Date checked:** 2026-10-12

The current card-audit overlay had one blank Oracle-text field for this row. The existing identity override already records the exact BLB #116 printing and distinguishes the normal card from a separate same-name token with a different Oracle identity.

The exact printing is corroborated by the following card record:
https://mtg.wtf/card/blb/116/Starscape-Cleric

That record gives mana cost {1}{B}, type Creature — Bat Cleric, Oracle text:
- Offspring {2}{B}
- Flying
- This creature can't block.
- Whenever you gain life, each opponent loses 1 life.

The record lists it as legal in Commander. This resolves the identity/text gap for this exact row for review purposes; it does **not** convert the inherited audit into a fresh Scryfall bulk-data audit and does not rewrite the immutable source-package card-audit file. Preserve the source overlay and use this dated supplemental resolution as the addendum until a current card-data snapshot is imported.
