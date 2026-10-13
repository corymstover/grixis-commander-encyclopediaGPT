# Abaddon the Despoiler — Current Card-by-Card Audit

**Audit refreshed by automated closeout run (UTC):** 2026-10-13T06:44:29.581734Z
**Scryfall default_cards bulk updated (UTC):** 2026-10-12T21:06:24.577+00:00
**Scryfall overlay generated (UTC):** 2026-10-13T06:44:29.581734+00:00
**Authority:** frozen 2026-10-12 FINAL CSV/TXT pair
**Source package SHA-256:** `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`
**Abaddon TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`
**Abaddon CSV SHA-256:** `fbeb7f75302b9ebedaf67aa58171de05764b6e6f97570be5657f0cbe8df37478`
**Decklist changes:** none

## Exact-printing Oracle / identity / legality result

**Automated current-source run:** refresh summary, freshness validator, and Abaddon exact-name audit passed in GitHub Actions. The exact Abaddon audit ran after the refreshed Scryfall overlay was generated; the successful metadata commit was created only after these validation steps succeeded.

- Overall result: **PASS — all 94 Abaddon cards matched current Scryfall bulk metadata**.
- Distinct card names: **94/94**; total copies: **100/100**.
- Exact set + collector number + card-name matches: **94/94**.
- Scryfall IDs / Oracle IDs / nonblank Oracle text: **94/94 / 94/94 / 94/94**.
- Color identity within Abaddon's UBR identity: **94/94**.
- Current Scryfall Commander legality marked legal: **94/94**.
- Registered project exception rows for Abaddon: **0**.
- The companion CSV contains every exact card row with full current Oracle text, Oracle-text SHA-256, Scryfall/Oracle IDs, exact set/collector printing, color identity, Commander identity, Commander legality, release date and match status.

## Priority cards

| Card | Exact printing | Color identity | Current Commander legality |
|---|---|---|---|
| Bituminous Blast | J25 742 | B,R | legal |
| Boltwave | FDN 79 | R | legal |
| Thermo-Alchemist | INR 403 | R | legal |

### Oracle text confirmed from the exact-printing rows

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

The fresh Scryfall `default_cards` refresh summary generated at `2026-10-13T06:44:29.581734+00:00` reports `bulk_updated_at=2026-10-12T21:06:24.577+00:00`, 5,964/5,964 exact global print/name matches, zero missing/ambiguous/name-variant rows, zero blank Oracle text/Oracle IDs, zero color-identity mismatches, zero unresolved printing/exception rows, and zero unexpected official-illegal rows. The Abaddon-specific audit gate passed: all 94 distinct names are exact-matched; all 94 have Oracle IDs and nonblank Oracle text; all 94 color identities fit UBR; all 94 are marked Commander-legal; no Abaddon project exceptions apply. The official Commander banned list was checked on October 13, 2026; no card in this frozen Abaddon list is named on it. The October 12, 2026 Wizards Banned & Restricted announcement changed Competitive Brawl, not tabletop Commander.

## Corrected cascade-hit analysis

The prior triage's claim that mana-value-1 and mana-value-3 spells had no lower-mana-value nonland hits was incorrect. The frozen deck has **seven** 0-mana-value nonlands: **Ancestral Vision, Chrome Mox, Inevitable Betrayal, Lion's Eye Diamond, Lotus Petal, Pact of Negation, and Profane Tutor**.

A mana-value-1 cascade source can potentially hit any of these seven. A mana-value-3 source can potentially hit any nonland with mana value 0, 1, or 2. These are possible hits, not guaranteed outcomes. Ancestral Vision, Inevitable Betrayal, and Profane Tutor have no mana cost but may be cast when an effect permits casting without paying that cost; Inevitable Betrayal requires a legal target. Pact of Negation requires a legal spell target. Chrome Mox can enter without an imprint card and then fail to produce mana. Cascade at mana value 0 (for example, a cascade instance granted to Pact of Negation) has no legal hit because no card has negative mana value.

Cascade resolves before its source spell. A mana-value-1 tutor's top-deck setup cannot feed that same spell's cascade; it can set up a later spell. A spell's own later damage or cast triggers cannot retroactively grant cascade to that spell. Playing a land from exile does not cast a spell or gain Abaddon's hand-only cascade, but it **does** trigger Prosper, Tome-Bound's Treasure ability because Prosper cares about playing a card from exile.

## Combo and interaction disposition

The Underworld Breach + Lion's Eye Diamond + Brain Freeze line has a worked uninterrupted sequence from an explicit starting state with escape costs, six-card fuel replacement, storm counts, milling allocations, mana accounting, and a Wheel of Fortune finish. It is rules-coherent from those conditions, but is not an unconditional infinite, a guaranteed win through interaction, or evidence of reliable assembly. Relevant cascade, alternate-cost, cast-from-exile, damage-threshold, copy-vs-cast, and wipe-timing interactions have substantial documented coverage; this is not exhaustive proof of every possible game state.

## References

- [Scryfall bulk data documentation](https://scryfall.com/docs/api/bulk-data)
- [Official Commander banned list](https://mtgcommander.net/index.php/banned-list/)
- [Wizards Banned & Restricted announcement — October 12, 2026](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026)
- [Current Magic Comprehensive Rules](https://magic.wizards.com/en/rules), effective September 25, 2026

**Finalization:** current metadata preflight and exact 94-name audit pass; structural hash/count/singleton verification passed independently. Rules-interaction coverage is substantial but bounded, not exhaustive gameplay proof. The frozen list remains unchanged. The deck is not marked finalized until the user explicitly approves this exact unchanged 100-card list.