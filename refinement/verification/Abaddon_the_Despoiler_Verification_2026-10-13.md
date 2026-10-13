# Abaddon the Despoiler — New-Cycle Refinement & Verification Certificate

**Deck:** #1 of 62  
**Review date:** 2026-10-13 (America/Chicago)  
**Source authority:** frozen October 12, 2026 current source package  
**Baseline source package SHA-256:** `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`  
**Baseline CSV SHA-256:** `fbeb7f75302b9ebedaf67aa58171de05764b6e6f97570be5657f0cbe8df37478`  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Normalized baseline decklist SHA-256:** `a58b6ad5499596eb64af79a83b210641e4e097c79803de87cca3ba2244fab91f`  
**Normalized revised decklist SHA-256:** `9629ba07807642736bce0b2c90038dd664da7b32b3892744808c8de4b526fb50`

## Final decision

**Two additions and two cuts.** This revision keeps Abaddon’s natural Bracket 4 / optimized ceiling and improves two distinct parts of its commander-first plan: pre-main-phase life loss to raise Abaddon’s cascade threshold, and reliable conversion of exile-cast token generation into direct damage. No land-count change was made.

## Change ledger

| Change | Card | Paired card | Rationale |
|---|---|---|---|
| Add | Court of Ambition | Cut Loyal Subordinate | Court triggers at upkeep before the first main phase, raising Abaddon’s current-turn cascade threshold if opponents choose life loss. It also makes you monarch and can provide card flow while monarch is retained. |
| Cut | Loyal Subordinate | Add Court of Ambition | Its life-loss ability triggers at beginning of combat, requires your commander, and therefore does not help first-main-phase cascade. It remains a solid card; the change favors a recurring pre-main engine. |
| Add | Warstorm Surge | Cut Rakdos, Lord of Riots | The Lost and the Damned creates a 3/3 Spawn when a spell is cast from outside your hand, including a cascade hit cast from exile. With Warstorm Surge already on the battlefield, each such Spawn ETB can deal 3 damage to any target; other creature ETBs also become damage. |
| Cut | Rakdos, Lord of Riots | Add Warstorm Surge | Rakdos discounts only creature spells and supplies a large evasive body. Warstorm instead converts the existing exile-cast token engine into direct damage. This sacrifices creature-cost reduction and a 6/6 flyer/trampler; it is a strategic trade-off rather than a claim Rakdos is universally weak. |

## Commander-first strategy after changes

Primary plan remains: cast spells from hand with mana value at or below life opponents have lost this turn to trigger Abaddon’s cascade; use low-cost all-opponent damage, upkeep life loss, rituals/fast mana, and spell/impulse value to establish the threshold and fuel cascading. Passionate Archaeologist, Keeper of Secrets, and The Lost and the Damned convert exile-casts into damage/value/tokens. The Ruinous Powers, Prosper, Wild-Magic Sorcerer, Nalfeshnee, and draw/tutor tools extend the value chain. The Underworld Breach + Lion’s Eye Diamond + Brain Freeze package remains a separate compact combo line under its documented starting-resource conditions.

The two changes strengthen different stages of that plan rather than replacing it: Court helps set up cascade before first main phase; Warstorm makes later Spawn output more lethal. The list retains its 34 lands and existing fast-mana/ritual package, and does not add a generic Grixis combo package merely for raw power.

## Candidate review closeout

A current-cycle, commander-specific review has been documented in `Abaddon_the_Despoiler_Candidate_Decisions_2026-10-13.csv` (15 key candidates). High-impact alternatives were explicitly resolved for this revision:

- **Accepted:** Court of Ambition; Warstorm Surge.
- **Rejected for this revision:** Blood for the Blood God! (promising but its 11 mana value, hand-discard clause, and reliance on multiple creature deaths make it higher-variance than the chosen package); Descent into Avernus (symmetrically accelerates opposing players); Dark Apostle (slow, telegraphed extra-cascade activation redundant with Abaddon); Heralds of Tzeentch (mostly a body plus one cascade); Let the Galaxy Burn (overlap with the current board-control/cascade suite); Poxwalkers (its strongest loop depends on being in the graveyard and no dedicated self-mill/sacrifice package exists); Pink Horror (valid spell-ping candidate but not a stronger change than the selected packages); Mutalith Vortex Beast (variable coin-flip value); Bloodthirster (combat-dependent, less central); Spear Spewer (symmetrical self-damage and lower ceiling); Cryptolith Fragment // Aurora of Emrakul (tapped three-mana rock plus symmetrical life loss); Kill! Maim! Burn! (playable, but no clearly better cut than the accepted changes).
- **Inconclusive; baseline retained:** Aurora Phoenix over Mind’s Desire. The earlier test cast neither candidate in its 3+3 games, used unmatched starting libraries, and included a timeout; it is not evidence of performance superiority. It was not rerun or used to justify a change.

Rankings and EDHREC inclusion are discovery/supporting signals only, not automatic inclusion rules. EDHREC’s current cascade subset lists Court of Ambition in about 33% and Warstorm Surge in about 30% of its 568 Abaddon cascade decks, a useful corroborating observation but not proof of superiority. See [EDHREC Abaddon Cascade](https://edhrec.com/commanders/abaddon-the-despoiler/cascade).

## Rules and legality verification

- **Abaddon:** current text and identity verified in the source card audit/refresh; color identity UBR. The active-cycle tracker’s Scryfall default-cards refresh says all 94/94 baseline card names were checked, with 5,964/5,964 project-wide exact print/name matches, no missing Oracle text/IDs, unresolved printings, identity mismatches, or unexpected illegal statuses.
- **Court of Ambition:** `{2}{B}{B}`, mana value 4, black identity, Commander legal. Its ability creates monarch on entry; the upkeep trigger makes each opponent choose discard or life loss (6 while you are monarch, otherwise 3). Since this trigger happens during upkeep, the resulting life loss is in the current turn before main phase and can increase Abaddon’s cascade threshold. Opponents who discard do not contribute the corresponding life loss.
- **Warstorm Surge:** `{5}{R}`, mana value 6, red identity, Commander legal. Its ability triggers when a creature enters under your control and that creature deals damage equal to its power to any target. A 3/3 Spawn made by The Lost and the Damned therefore deals 3 damage through Surge if Surge is already on the battlefield when the Spawn enters. The change does not retroactively trigger for creatures that entered before Surge resolves.
- **Cut cards:** Loyal Subordinate is black identity; its current Oracle text makes opponents lose 3 life at beginning of combat if you control your commander. Rakdos, Lord of Riots is black-red identity; it can only be cast if an opponent lost life that turn and discounts creature spells based on opponent life loss. Both identities fit UBR, neither requires a project exception, and their effects/trade-offs are documented above.
- The official Commander banned list was inspected on October 13, 2026; none of the revised list’s card names is on that list. The October 12 Wizards B&R announcement changed Competitive Brawl, not tabletop Commander. No project-specific exception is used in this deck. Current references: [Official Commander banned list](https://mtgcommander.net/index.php/banned-list/), [Wizards B&R announcement — October 12, 2026](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026), [Court of Ambition rules/text/legal status](https://www.mtg.wtf/card/cmr/645/Court-of-Ambition), and [Warstorm Surge rules/text/legal status](https://www.mtg.wtf/card/40k/209/Warstorm-Surge).

## Structural verification

- Main deck plus commander: **100/100**.
- Unique card names: **94**, unchanged from the baseline; two card names were cut and two new card names added.
- Commander marker: exactly one, first line.
- Singleton: **PASS**; the only repeated names are Island ×3, Mountain ×3 and Swamp ×3.
- Baseline CSV/TXT: **PASS**; prior independent reconciliation was 100 copies / 94 names and byte-match to the canonical archives.
- Revised CSV/TXT equivalence: **PASS**; they contain the same 100 copies.
- Land count: **34**, unchanged.
- Commander color identity: **PASS**. Added cards are black-only and red-only respectively; cut cards were black and black-red; all are contained within UBR. No identity mismatch or project exception.
- Source baseline is preserved byte-for-byte; the revised list is a separate version.

## Consistency/performance scope and limitations

A two-for-two singleton swap does not change the 99-card library size, land count, or basic-land counts. The chance to open at least one of the two new singleton cards in a seven-card sample from the 99-card library is approximately **13.7%** (and **19.3%** within ten cards); this is only a descriptive hypergeometric draw-density calculation, not a mulligan model, game simulation, matchup test, or win-rate estimate. The previous hypergeometric baseline analysis remains descriptive. No qualified matched-start multiplayer simulator or representative playtest is available in this refinement run, so multiplayer performance is recorded as **not applicable / not measured**, not silently promoted to a pass on game quality. There is no asserted win-rate gain.

## Final technical gate status

| Gate | Result | Evidence/limitation |
|---|---|---|
| 1. Deck count, singleton, CSV/TXT reconciliation, revision hash | PASS | Independent local parser; 100 copies; 94 names; singleton/basic-land rule satisfied; revision hash recorded. |
| 2. Oracle identity, color identity, current official legality, project exceptions | PASS | Baseline current Scryfall audit plus exact card references for additions/cuts and current official Commander banned-list checkpoint; no exceptions. |
| 3. Commander-first strategic blueprint | PASS | Cascade threshold, life-loss setup, cast-from-exile value, Spawn damage conversion, backup Breach line and natural ceiling documented. |
| 4. Full-list and candidate review | PASS | 15 targeted candidates decisioned; four actual card changes paired and explained; no high-impact candidate left pending. |
| 5. Rules and relevant interactions | PASS | Court upkeep threshold timing; Lost and the Damned / Warstorm Surge token triggers; cut card effects; Breach combo remains qualified by prerequisites. |
| 6. Scoped consistency/performance assessment | PASS WITH LIMITS | Exact draw-density check and unchanged list structure; no reliable multiplayer test, win-rate claims, or use of invalid prior variant test. |
| 7. Final record, hashes, change log, certificate | PASS | Revised list, normalized hash, candidate decision ledger, actual add/cut ledger and this verification certificate stored separately from baseline. |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`** under the 2026-10-13 active-cycle auto-finalization protocol. No additional user sign-off is required in this cycle. The status applies only to the exact revision with normalized list hash `9629ba07807642736bce0b2c90038dd664da7b32b3892744808c8de4b526fb50`; any subsequent change requires a new verification revision.

## Exact copy-and-paste decklist

```text
1x Abaddon the Despoiler [Commander]
1x Ancestral Vision
1x Ancient Tomb
1x Arcane Signet
1x Badlands
1x Birgi, God of Storytelling // Harnfel, Horn of Bounty
1x Bituminous Blast
1x Blasphemous Act
1x Blood Crypt
1x Bloodletter of Aclazotz
1x Bloodstained Mire
1x Boltwave
1x Brain Freeze
1x Brainstorm
1x Cabal Ritual
1x Call Forth the Tempest
1x Chrome Mox
1x City of Brass
1x Command Tower
1x Court of Ambition
1x Dark Ritual
1x Deadly Rollick
1x Deflecting Swat
1x Delayed Blast Fireball
1x Demonic Tutor
1x Exalted Flamer of Tzeentch
1x Exotic Orchard
1x Fierce Guardianship
1x Flame Rift
1x Flooded Strand
1x Flusterstorm
1x Force of Negation
1x Force of Will
1x Gamble
1x Imperial Seal
1x Inevitable Betrayal
3x Island
1x Jeska's Will
1x Keeper of Secrets
1x Kessig Flamebreather
1x Lion's Eye Diamond
1x Lotus Petal
1x Luxury Suite
1x Mana Confluence
1x Mana Vault
1x Marsh Flats
1x Mind's Desire
1x Misty Rainforest
1x Morphic Pool
3x Mountain
1x Mystic Remora
1x Mystical Tutor
1x Nalfeshnee
1x Neheb, the Eternal
1x Nightscape Familiar
1x Noise Marine
1x Otawara, Soaring City
1x Pact of Negation
1x Passionate Archaeologist
1x Polluted Delta
1x Ponder
1x Profane Tutor
1x Prosper, Tome-Bound
1x Pyroblast
1x Rhystic Study
1x Rite of Flame
1x Scalding Tarn
1x Sol Ring
1x Solphim, Mayhem Dominus
1x Steam Vents
1x Storm-Kiln Artist
3x Swamp
1x Swan Song
1x Takenuma, Abandoned Mire
1x Talisman of Creativity
1x Talisman of Dominance
1x Talisman of Indulgence
1x The Lost and the Damned
1x The Ruinous Powers
1x Thermo-Alchemist
1x Training Center
1x Underground Sea
1x Underworld Breach
1x Urborg, Tomb of Yawgmoth
1x Vampiric Tutor
1x Verdant Catacombs
1x Vivi Ornitier
1x Volcanic Island
1x Warstorm Surge
1x Watery Grave
1x Wheel of Fortune
1x Wild-Magic Sorcerer
1x Windfall
1x Xander's Lounge
```