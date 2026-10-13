# Abaddon the Despoiler — Current Card-by-Card Audit

**Audit assembled (UTC):** 2026-10-13T06:20:27Z
**Scryfall default_cards bulk updated (UTC):** 2026-10-12T21:06:24.577+00:00
**Scryfall overlay generated (UTC):** 2026-10-13T04:36:45.235158+00:00
**Frozen baseline:** 2026-10-12 authoritative FINAL CSV/TXT pair
**Frozen TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`
**Decklist changes:** none

## Card-by-card result

- Exact set + collector number + card-name matches: **94/94**.
- Scryfall IDs and Oracle IDs present: **94/94** and **94/94**.
- Nonblank current Oracle text: **94/94**.
- Color identity within Abaddon's UBR identity: **94/94**.
- Current Scryfall Commander legality marked `legal`: **94/94**.
- Unexpected nonlegal rows or color mismatches: **0**.
- All 94 exact-printing rows are retained in the companion CSV with complete Oracle text, Scryfall ID, Oracle ID, text SHA-256, color identity, Commander identity, legality, release date and exact-match status.

## Priority cards

| Card | Exact printing | Oracle ID | Color identity | Commander legality |
|---|---|---|---|---|
| Bituminous Blast | J25 742 | `d291d8f7-bb67-470c-8794-cd553c91e5cc` | B,R | legal |
| Boltwave | FDN 79 | `bb8cccc8-e56f-42fa-a0d7-fc889b5e1c7b` | R | legal |
| Thermo-Alchemist | INR 403 | `228fbae1-423e-461d-b8c3-55786938a3cb` | R | legal |

### Current Oracle text

**Bituminous Blast** — Instant.

> Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order.)
> Bituminous Blast deals 4 damage to target creature.

**Boltwave** — Sorcery.

> Boltwave deals 3 damage to each opponent.

**Thermo-Alchemist** — Creature — Human Shaman.

> Defender
> {T}: This creature deals 1 damage to each opponent.
> Whenever you cast an instant or sorcery spell, untap this creature.

## Commander legality

The current Scryfall bulk overlay marks all 94 Abaddon rows legal in Commander and all color-identity checks pass. The official Commander banned list was inspected on October 13, 2026; no card in this Abaddon list is named on it. The October 12, 2026 Wizards Banned & Restricted announcement changed Competitive Brawl, not tabletop Commander.

## Cascade-hit correction

The previous interaction triage incorrectly said mana-value-1 and mana-value-3 spells had no lower-mana-value nonland hits. The deck contains five 0-mana-value nonlands: **Ancestral Vision, Chrome Mox, Inevitable Betrayal, Lion's Eye Diamond, and Lotus Petal**. A cascade source with mana value 1 can potentially hit these; a source with mana value 3 can potentially hit any nonland with mana value 0–2. Inevitable Betrayal requires a legal target; Chrome Mox may enter without an imprint card. These are possible hits, not guaranteed or always useful outcomes. Pact of Negation is the exception: at mana value 0, no card has a lower mana value.

Cascade resolves before its source spell. Therefore a mana-value-1 tutor's top-deck setup cannot feed that same spell's cascade, but can set up a later spell. Playing a land from exile does not cast a spell or gain Abaddon's hand-only cascade, but it does trigger Prosper, Tome-Bound's Treasure ability because Prosper cares about playing a card from exile.

## Combo and interaction disposition

The Underworld Breach + Lion's Eye Diamond + Brain Freeze line has a worked uninterrupted sequence from an explicit starting state with escape costs, six-card fuel replacement, storm counts, milling allocations, mana accounting and a Wheel of Fortune finish. It is rules-coherent from those conditions, but not an unconditional infinite, a guaranteed win through interaction, or evidence of reliable assembly. Relevant cascade, alternate-cost, cast-from-exile, damage-threshold, copy-vs-cast and wipe-timing interactions have substantial documented coverage; this is not exhaustive proof of every possible game state.

## References

- [Scryfall bulk data documentation](https://scryfall.com/docs/api/bulk-data)
- [Official Commander banned list](https://mtgcommander.net/index.php/banned-list/)
- [Wizards Banned & Restricted announcement — October 12, 2026](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026)
- [Current Magic Comprehensive Rules](https://magic.wizards.com/en/rules), effective September 25, 2026

**Finalization:** metadata verification passes for the frozen list. Do not mark the deck approved/finalized until the user explicitly approves the exact unchanged 100-card list.