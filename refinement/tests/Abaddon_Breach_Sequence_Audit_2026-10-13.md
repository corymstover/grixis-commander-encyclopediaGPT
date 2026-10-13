# Abaddon Breach Package Audit — Bounded Rules Verification

**Date:** 2026-10-13 UTC  
**Baseline:** 2026-10-12 frozen list  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Decklist changes:** None

## Rules facts checked against current sources

- **Underworld Breach:** Escape grants permission to cast a card from the graveyard by paying its mana cost and exiling three other cards from that graveyard for each escape cast.
- **Lion's Eye Diamond (LED):** Its activation sacrifices LED and discards the controller's hand as costs, then adds three mana of one chosen color. The mana ability resolves before a player can respond to that mana ability. Cards discarded are in the graveyard and may become escape fuel if not exiled to pay a cost.
- **Brain Freeze:** It is an instant with storm and mills a target player for three cards. Storm counts spells cast before it that turn. Storm copies are not cast and do not themselves increase storm count.
- **Abaddon:** Only spells cast from hand can receive cascade from Abaddon. Escaping LED or Brain Freeze from the graveyard does not give them Abaddon-granted cascade.
- **Empty libraries:** An empty library alone is not a loss. A player loses when required to draw more cards than remain in their library and the applicable state-based action is processed.
- **Trigger exception:** Storm-Kiln Artist sees copies of instant/sorcery spells; cast-only triggers do not trigger from storm copies.

Current reference set: [Official Magic Comprehensive Rules, effective September 25, 2026](https://magic.wizards.com/en/rules), including Escape (702.138), Storm (702.40), copies (707.10), and loss from drawing (104.3c). Relevant card references: [Underworld Breach](https://scryfall.com/card/thb/161/underworld-breach), [Lion's Eye Diamond](https://scryfall.com/card/mir/307/lions-eye-diamond), [Brain Freeze](https://scryfall.com/card/scg/29/brain-freeze), and [Abaddon the Despoiler](https://scryfall.com/card/40k/171/abaddon-the-despoiler).

## Worked, uninterrupted example

This example establishes one line from one specified state. It does not prove a free infinite, a guaranteed line from arbitrary resources, or resilience through interaction.

### Starting state

- You control Underworld Breach, Lion's Eye Diamond, and an untapped land that can produce red.
- Your graveyard contains Brain Freeze, Wheel of Fortune, and exactly six expendable fuel cards. Wheel and Brain Freeze are reserved; do not count them as fuel.
- Your hand is empty.
- You have cast no spells this turn.
- Your library contains 70 cards.
- Each of the three opponents has 90 cards in their library.
- No opponent interacts; no relevant replacement effect changes mill/draw events.

### Ten escape cycles

For each cycle (k=1ldots10):

1. Activate LED, sacrificing it and discarding your empty hand; add ({U}{U}{U}). LED is now in your graveyard.
2. Escape LED from your graveyard. Its mana cost is {0}; exile three other graveyard cards as the escape cost. Use three of the six current fuel cards. LED resolves to the battlefield.
3. Escape Brain Freeze from your graveyard by paying {1}{U} and exiling the other three fuel cards. It resolves to the graveyard after its spell effect.
4. Before Brain Freeze is cast, exactly (2k-1) spells have been cast this turn: two per prior cycle, plus this cycle's escaped LED. Brain Freeze has (2k-1) storm copies, for (2k) total resolutions including the original spell.
5. Assign exactly two Brain Freeze resolutions to yourself, milling six cards into your graveyard; those six cards become the next cycle's fuel. Assign the other (2k-2) resolutions to opponents. Across cycles 1–10, allocate 30 total resolutions to each opponent.

### Fuel, storm, and library accounting

- Each cycle exiles six fuel cards total: three to escape LED and three to escape Brain Freeze.
- Each cycle mills six new cards into your graveyard to replace that fuel. On cycle 10, those six cards are preserved as fuel for the finishing escape.
- Storm resolutions across the ten casts: (sum_{k=1}^{10}2k=110).
- Self-targeted resolutions: 20, milling (20\times3=60) cards. Your library goes from 70 to 10.
- Opponent-targeted resolutions: (110-20=90). Assign 30 to each opponent; (30\times3=90) cards milled per opponent, leaving each with an empty library.
- Mana: each cycle adds three blue mana with LED and spends two on the escaped Brain Freeze. Net gain is one blue mana per cycle, so ten cycles leave ten blue mana. The LED spell cast and the Brain Freeze spell each count toward future storm counts; LED's activated ability itself is not a spell cast.

### Finish with Wheel of Fortune

After cycle 10, each opponent has an empty library, your library has ten cards, LED is back on the battlefield, and your graveyard has Wheel of Fortune, Brain Freeze, and the six cards milled in the final cycle.

1. Escape Wheel of Fortune for {2}{R}, exiling three other graveyard cards from the final six-card fuel pool.
2. Pay {R} with the untapped red-producing land and {2} with two of the ten floating blue mana.
3. Wheel resolves. You draw seven from your ten-card library and do not lose from drawing.
4. Each opponent is instructed to draw seven from an empty library. Each loses when the required draw fails and the applicable state-based action is processed.

### Disposition

**RULES-COHERENT WITH SPECIFIC CONDITIONS — worked uninterrupted example provided.** The card-zone, escape-cost, mana, storm-count, fuel, and library arithmetic is explicit for this starting state. This does not demonstrate an unconditional infinite, a guaranteed kill through interaction, or that the deck reliably assembles the line.

No new Forge AI comparison is warranted; the previous Aurora Phoenix vs Mind's Desire pilot remains inconclusive, and this is rules/accounting evidence rather than gameplay performance evidence. No deck changes are authorized by this report.

No card changes are authorized by this report.
