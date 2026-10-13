# Admiral Beckett Brass — Proposed Final Verification

**Date:** 2026-10-13  
**Status:** TECHNICAL VERIFICATION PASS — awaiting explicit approval of this exact revised list  
**Authoritative frozen baseline:** 2026-10-12 FINAL CSV/TXT exports; preserved unchanged  
**Approved change:** cut 1x Coastal Piracy; add 1x The Indomitable (LCC #75)  
**Decklist change count:** one-for-one replacement only

## 1. Exact revised list and hashes

- Copy/paste list: `refinement/decklists/Admiral_Beckett_Brass_Proposed_Final_2026-10-13.txt`
- Clean-list SHA-256 (UTF-8, LF, trailing newline): `bd636ec183ae8829eefa0e4c71db00c96d82a55919131f1a3cc4907fe5af5a94`
- Source-format TXT SHA-256 after replacing the original printed line `1x Coastal Piracy (tle) 156 [Draw]` with `1x The Indomitable (lcc) 75 [Draw]`: `4b5367469355080ecae0e8fea5a8cc995bffb3bbc62f562c68fcae255236018e`
- Original frozen baseline TXT SHA-256: `e9e161a015e8b86057d4d76424f901a0700715712cc542a78f9c74c6eabe21dc`
- The original frozen baseline files and their hashes are not overwritten. The revised list is a separate proposal artifact pending final approval.

## 2. Structural integrity

- Card quantity total: **100**.
- Decklist rows / distinct card names: **97 / 97**.
- Commander: exactly one, Admiral Beckett Brass, on the first line.
- Singleton: PASS. No nonbasic card name is repeated.
- Repeated basics: Island x3 and Mountain x2; Swamp x1.
- Coastal Piracy: absent from revised list.
- The Indomitable: present exactly once.
- One-for-one quantity delta: 100 cards before, 100 cards after.
- No other card name or quantity changed.

## 3. New card Oracle text, identity, and legality

Chosen printing: **The Indomitable — The Lost Caverns of Ixalan Commander, LCC #75**.

Current card record and published Wizards rulings:
- Mana cost: `{2}{U}{U}`; mana value 4.
- Type: legendary artifact — Vehicle.
- Oracle text: trample; whenever a creature you control deals combat damage to a player, draw a card; crew 3; you may cast this card from your graveyard as long as you control three or more tapped Pirates and/or Vehicles.
- Power/toughness: 6/6.
- Color identity: blue only; fits Admiral Beckett Brass's blue-black-red identity.
- Commander legality: legal.
- Rules nuance: only tapped Pirates and tapped Vehicles count toward the graveyard-casting permission. It checks the condition as casting begins; the permission does not change when you may cast the card, and you still pay its full costs.

References:
- https://www.mtg.wtf/card/lcc/75/The-Indomitable
- https://www.mtg.wtf/card/tle/156/Coastal-Piracy

The outgoing Coastal Piracy printing (TLE #156) is also Commander legal and has blue color identity. Its relevant Oracle text is an optional draw trigger when a creature you control deals combat damage to an opponent. The Indomitable's draw trigger is mandatory and triggers on combat damage to any player; this distinction is intentional and documented in the candidate ledger.

## 4. Unchanged-list verification inheritance

The frozen baseline's 2026-10-13 Scryfall refresh passed 5,964/5,964 exact printing matches across 62 decks, with zero missing Oracle text/IDs, color-identity mismatches, unresolved printings, unresolved exceptions, or unexpected officially illegal rows. All 94 distinct names in the original Beckett baseline had current card metadata. This change removes Coastal Piracy and adds The Indomitable; no other card identity or legality status is altered.

The new card's Oracle text, blue color identity, and Commander legality were checked independently against the current card record and rulings above. This report does not claim that a new 62-deck metadata refresh was run for this one-card candidate.

## 5. Strategic check

The replacement preserves the combat-damage draw role while adding a 6/6 trampler and a repeatable graveyard-cast permission. The graveyard condition naturally rewards attacking with three tapped Pirates and/or Vehicles. This ability is not a free cast and does not permit casting at otherwise-illegal times. Mandatory draw and artifact-removal vulnerability remain the primary tradeoffs.

No further swap is introduced. No other card is changed.

## 6. Final approval gate

- Structural count and singleton checks: **PASS**.
- New card current Oracle / identity / Commander legality: **PASS**.
- Frozen baseline preserved: **PASS**.
- Candidate decision ledger updated to user-approved swap: **PASS**.
- Exact revised list approved for final lock: **PENDING**.
- Tracker `final_gate_passed`: remains **NO** until the user explicitly approves this exact revised list.
