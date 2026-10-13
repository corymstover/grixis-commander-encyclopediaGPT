# Abaddon the Despoiler — Closeout Decision

**Date:** 2026-10-13 (America/Chicago)  
**Decklist authority:** frozen 2026-10-12 source package  
**Decklist changes:** none  
**Verification result:** READY FOR USER APPROVAL  
**Approval recorded:** NO — awaiting explicit user approval of the unchanged list

## 1. Decision

Retain the frozen Abaddon baseline unchanged and close the verification/research phase. No proposed candidate swap has sufficient evidence to justify changing the baseline. The inconclusive Aurora Phoenix vs. Mind's Desire Forge comparison is not a blocker: neither candidate was cast in the comparison games, so the test did not measure the choice. Keep Mind's Desire and do not repeat the same uninformative test.

The earlier final-verification snapshot said that approval-time metadata verification remained open. That statement is superseded by the successful current Scryfall metadata refresh summarized below.

## 2. Source and structural integrity

The independent local structural verification of the frozen source package passed:
- Source-package manifest: 165/165 files verified.
- Authoritative Abaddon CSV/TXT exports agree byte-for-byte with their archive copies.
- Main deck plus commander: 100 cards across 94 distinct card names.
- Commander marker: exactly one.
- Singleton compliance: pass; only Island x3, Mountain x3, and Swamp x3 repeat.
- Frozen list/hash: unchanged; no card additions, cuts, or substitutions made during this refinement.

## 3. Current card-object and legality verification

Current Scryfall metadata audit generated at **2026-10-13 07:13:47 UTC**, using the `default_cards` bulk snapshot updated **2026-10-12 21:06:24 UTC**.

Project-wide results:
- 62 decks / 5,964 decklist rows.
- Exact printing matches: 5,964/5,964.
- Unresolved or ambiguous printings: 0.
- Missing Oracle text or Oracle IDs: 0.
- Color-identity mismatches: 0.
- Unexpected officially illegal rows: 0.
- Unresolved project exceptions: 0.

Abaddon-specific results recorded by the refresh:
- 94/94 distinct card names matched current Scryfall card metadata.
- 94/94 have Scryfall and Oracle IDs and Oracle text.
- 94/94 color identities are compatible with the UBR commander identity.
- 94/94 metadata legality fields are marked legal.
- No Abaddon card is among the unexpected official-illegality rows.
- Bituminous Blast, Boltwave, and Thermo-Alchemist are covered by this refresh; the prior snapshot's narrow gap for these three cards is closed.

The official Commander banned-list checkpoint on 2026-10-13 found no Abaddon baseline card named on the list. The October 12, 2026 Wizards Banned & Restricted announcement did not change tabletop Commander legality.

## 4. Rules and interaction review — completion standard

The card-specific triage covers all 94 distinct card names and has no remaining literal triage-queue entries. This is a completed, bounded review to the project's reasonable verification standard; it is not a claim to have enumerated every possible game state.

The material interactions reviewed include:
- **Abaddon/cascade threshold:** opponent life lost during the current turn determines which hand-cast spells qualify for Abaddon's cascade grant. Track the actual life lost, rather than damage attempted or damage prevented. A cascade spell's hit must meet cascade's mana-value condition; zero-mana-value nonland cards are valid hits when they satisfy that condition.
- **Casting zone and timing:** Abaddon's grant applies to spells cast from hand during your turn; spells cast from exile by cascade do not receive that grant merely because they were cast during the turn. A cascaded spell can still trigger its own abilities and other applicable cast triggers.
- **Alternate-cost and exile-value payoffs:** Jeska's Will, Birgi // Harnfel, Passionate Archaeologist, The Ruinous Powers, Wild-Magic Sorcerer, and other exile/cast-value cards were checked for the distinction between exiling a card, casting it, and casting it from a particular zone.
- **Damage and life-loss engines:** Flame Rift and other life-loss enablers help establish Abaddon's cascade threshold. Thermo-Alchemist's tap/untap trigger condition and its relationship to noncreature-spell casting were checked. Damage amplifiers such as Solphim and Bloodletter of Aclazotz affect damage/life-loss events; their effects are not interchangeable and must be applied to the event they modify.
- **Removal/cascade lines:** Bituminous Blast's cascade and target restriction, and Blasphemous Act's creature-only damage, were checked against the deck's own damage payoffs.
- **Breach line:** Underworld Breach + Lion's Eye Diamond + Brain Freeze has a worked uninterrupted line from stated starting resources. LED's discard/sacrifice timing, escape costs, Brain Freeze storm count, and graveyard replenishment are part of the line. It is rules-coherent under those conditions, not an unconditional infinite or guaranteed win through interaction.
- **Copy/cast distinctions:** Copying a spell is not casting it, and copying an ability does not itself create a cast trigger. The deck's relevant copy/cascade and cast-trigger expectations were checked at this level.

The current review does not claim exhaustive game-state proof or actual playtest evidence. The Forge comparison was inconclusive, and the draw-density calculation is descriptive rather than a simulated win rate. These limitations are documented and do not require another identical test to close this baseline.

## 5. Final gate

**Technical verification: PASS.**  
**Decklist mutation: NONE.**  
**Candidate swap required: NO.**  
**User approval: PENDING.**  
**Finalized/locked by this closeout: NO.**

The only remaining gate is explicit user approval of the exact unchanged 100-card baseline. Do not set an approval date, change the tracker approval flag, or describe the deck as finalized before that approval is received.
