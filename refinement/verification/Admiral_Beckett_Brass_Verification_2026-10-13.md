# Admiral Beckett Brass — New-Cycle Refinement & Verification Certificate

**Deck:** #2 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline authority:** frozen October 12, 2026 current FINAL source package  
**Active branch:** `refinement/campaign-2026-10-12`  
**Final status:** `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`

## Revision summary

- **Added:** The Indomitable; Zephyr Singer.
- **Cut:** Bident of Thassa; Daring Saboteur.
- Land count remained 35; no project-specific legality exception is used.
- Revised main deck + commander: **100 copies across 97 distinct names**. The commander's first-line marker appears exactly once.
- Normalized baseline list SHA-256: `eb73c86e728bbb07ef0d31e23c93f4048c5ca91771de0d28899407f6f11fd51d`
- Normalized revised list SHA-256: `40df97c47d37b4ae9d7f5c22623ab490c96c5dee9ab5be689a74ced25bb3be96`
- The original CSV/TXT files under the frozen source package were not changed.

## Authority, baseline and reconciliation

Authoritative baseline files are `02_Current_Decklists/CSV/Admiral_Beckett_Brass.csv` and `02_Current_Decklists/TXT/Admiral_Beckett_Brass.txt` within `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12.zip`.

- Baseline CSV SHA-256: `e6a2333e036935248c03705946576a461cb53bf78b30a1c6bda162e4f38c8dde`
- Baseline TXT SHA-256: `e9e161a015e8b86057d4d76424f901a0700715712cc542a78f9c74c6eabe21dc`
- Baseline counts: 100 total copies; 97 distinct card names; 35 lands.
- Revised normalized list: 97 output lines (basic land quantities stay on single quantity lines); total quantity check = 100.
- Revised CSV/TXT equivalence: PASS; both contain the same exact card-name quantities.
- Nonbasic duplicate check: PASS. Only repeated card names are Island ×3 and Mountain ×2; Swamp ×1. No repeated nonbasic card.
- Commander: one copy, first line; identity UBR.

## Commander-first strategy blueprint

Admiral Beckett Brass is a four-mana Grixis Pirate who gives other Pirates +1/+1 and steals a nonland permanent at the beginning of the end step from a player dealt combat damage by three or more Pirates that turn. That makes the deck’s main jobs unusually specific:

1. Have at least three Pirates connect with the **same** opponent during a turn.
2. Keep a sufficiently dense Pirate board and use lords/attack payoffs to make that board relevant in combat.
3. Improve evasive access and preserve draw/theft/value after removal or board resets.
4. Use Treasure, tribal buffs, theft effects and selective interaction to keep attacks productive while preventing blockers or removal from stopping the commander trigger.

The current baseline already supports that plan with 29 printed Pirate cards in the main deck plus Changeling Outcast (which has every creature type), numerous evasion/interaction pieces, Pirate token production, anthems, combat-damage draw, and theft engines. The 35-land baseline was retained; neither swap justifies altering the mana base.

## Candidate review

15 unique candidate decisions are recorded in `Admiral_Beckett_Brass_Candidate_Decisions_2026-10-13.csv`: 2 accepted/implemented and 13 rejected for this revision. Candidate rankings and EDHREC data were discovery and corroboration, not automatic-add rules.

### Implemented change 1 — The Indomitable for Bident of Thassa

Both cards draw from creatures dealing combat damage to players. The Indomitable adds a 6/6 trampler Vehicle and permits casting from the graveyard while controlling at least three tapped Pirates and/or Vehicles. The official ruling states that the casting permission does not alter normal timing, costs must still be paid, and the threshold is checked as casting begins. Since attacking Pirates normally remain tapped after combat, the condition is feasible in the commander’s plan. [Oracle/rulings](https://www.mtg.wtf/card/lcc/43/The-Indomitable)

Trade-offs are material: Bident makes its draw optional and has a {1}{U}, tap ability that forces creatures to attack if able; The Indomitable’s combat-damage draw is mandatory. Multiple combat steps or a nearly empty library can make mandatory draw a risk. EDHREC’s current optimized category displays The Indomitable in 45% of 73 decks and Bident in 42%; Bident’s Lift is higher (28x vs. 19x), which argues that this is not a popularity-proven superiority. The decision rests on recursion/resilience plus the 6/6 trample body, with its costs explicitly recorded. [EDHREC Optimized cohort](https://edhrec.com/commanders/admiral-beckett-brass/optimized)

### Implemented change 2 — Zephyr Singer for Daring Saboteur

Zephyr Singer is a 3/4 Siren Pirate with convoke, flying and vigilance. When it enters, it puts a flying counter on **each creature that actually convoked it**. It does not grant flying to all Pirates. The counters persist while those creatures remain on the battlefield. A creature tapped to convoke is tapped and typically cannot also attack that turn, so this is a tempo investment in future turns; convoke with spare Pirates/tokens when you still need three Pirates to attack. [Oracle and rulings](https://mtg.wtf/card/mom/86/Zephyr-Singer)

Daring Saboteur is a valuable two-mana Pirate that can pay {2}{U} to become unblockable and then draw/discard. That is cheaper and provides one-creature filtering, so the swap is not costless. The deck’s existing unblockable/evasion suite is strong; Singer’s distinct advantage is persistent evasion across multiple convokers plus a flying/vigilant Pirate body, making the three-Pirate same-opponent threshold more repeatable across several turns. EDHREC’s current 73-deck optimized cohort shows Zephyr Singer in 22% (16/73) and Daring Saboteur in 23% (17/73); the sample is modest and not gameplay evidence. [EDHREC Optimized cohort](https://edhrec.com/commanders/admiral-beckett-brass/optimized)

## Rules and interactions checked

- **Admiral Beckett Brass trigger:** checked for its three-or-more-Pirates requirement on a single player and its end-step timing. The rules text checks what occurred earlier that turn; Beckett Brass need not have been on the battlefield at the time the Pirates dealt damage, and the control-change effect lasts indefinitely. [Oracle/rulings](https://mtg.wtf/card/sld/1561/Admiral-Beckett-Brass)
- **The Indomitable graveyard permission:** three or more tapped Pirates/Vehicles are required at the start of casting from graveyard. Normal timing still applies and the {2}{U}{U} cost is paid. If countered or destroyed after being recast, it returns to the graveyard and may be recast later if the condition is met. [Official card text/rulings mirror](https://www.mtg.wtf/card/lcc/43/The-Indomitable)
- **Zephyr Singer/convoke:** only creatures actually tapped to pay by convoke receive flying counters. Those creatures are tapped and normally cannot attack on that same turn. [Oracle/rulings](https://mtg.wtf/card/mom/86/Zephyr-Singer)
- **Rejected Admiral’s Order nuance:** Raid gives a {U} alternative cost only during the same turn its controller attacked; it does not discount the spell on opponents’ later turns merely because the player attacked earlier in the round. Replacing Counterspell would make the counter more expensive (three rather than two mana) outside that condition; Counterspell is retained.
- **Baseline row gaps closed:** current card references confirm Commander legality and Oracle text for Daring Piracy, Daring Saboteur, Dire Fleet Captain, and Storm the Vault // Vault of Catlacan, which the inherited card audit had tagged “not reverified in candidate-ranking table.” [Daring Piracy](https://mtg.wtf/card/j22/33/Daring-Piracy), [Daring Saboteur](https://mtg.wtf/card/lcc/151/Daring-Saboteur), [Dire Fleet Captain](https://mtg.wtf/card/xln/221/Dire-Fleet-Captain), [Storm the Vault](https://mtg.wtf/card/rix/173a/Storm-the-Vault)
- No deterministic infinite combo was added or claimed. There are no new combo prerequisites/loop claims to certify.

## Current identity and legality verification

The project’s current Scryfall `default_cards` refresh is summarized on the active-cycle tracker/status as generated at `2026-10-13T07:03:26.694525Z` (bulk file updated `2026-10-12T21:06:24.577Z`). The reported global audit matched 5,964/5,964 baseline card-list rows by exact printing/name with no missing Oracle IDs/text, unresolved printings, commander identity mismatches, or unexpected illegal statuses outside registered exceptions. The baseline audit for this deck has all 97 rows with color-identity check `PASS`, commander identity UBR, and no registered project exceptions.

The two additions were checked against current card references: both are Commander-legal, blue color identity, and no project exception applies. The official Commander banned list was inspected on 2026-10-13; none of the final-list names is named on it. [Official Commander banned list](https://mtgcommander.net/index.php/banned-list/)

This certificate does not claim every original printing was re-downloaded individually; it records the current project-wide exact-printing metadata refresh plus direct card-specific confirmation of the additions and previously flagged rows.

## Consistency assessment (exact, limited scope)

For a 99-card library with 30 functional Pirate cards (29 printed Pirate cards plus Changeling Outcast), the exact hypergeometric probability that an un-mulliganed opening seven contains at least three Pirate cards is **35.7563%**; the expected count is **2.121** in seven. Probability of at least two is **68.5953%**. This is a raw composition calculation only. It does not model mulligans, mana, attack availability, blockers, opponents, survival, or whether three Pirates connect with one opponent, and it is not a win-rate/deck-quality score.

No qualified matched-start multiplayer simulator or representative game sample was available for a card-level performance comparison. The final decision therefore makes no unsupported win-rate or multiplayer-superiority claim. This limitation is explicit, not hidden.

## Verification gates

| Gate | Outcome | Evidence / limits |
|---|---|---|
| Structural count and singleton | **PASS** | 100 total; 97 card names; 35 lands; one commander marker; no nonbasic duplicates; CSV/TXT quantities agree. |
| Identity, Oracle, current legal status, ban-list checkpoint | **PASS** | Current project-wide exact-printing refresh; both additions individually checked; official Commander banned list checked 2026-10-13; no project exception. |
| Commander-first strategic blueprint | **PASS** | Trigger and its same-opponent, three-Pirate combat requirement drive the selected changes. |
| Candidate decision coverage | **PASS** | 15 unique candidate decisions recorded; two additions/two cuts; rejects have reasons. |
| Rules/interactions | **PASS** | Relevant commander, convoke and graveyard-casting timing verified; no unsupported combo claim. |
| Consistency / performance | **PASS WITH LIMITS** | Exact hypergeometric density check; no qualified gameplay comparison or win-rate claim. |
| Audit record / normalized hash | **PASS** | Revised copy list, CSV, candidate decisions, actual add/cut rows and hash are recorded separately from baseline. |
| Automatic finalization | **PASS** | All mandatory gates pass with limitations documented; active-cycle protocol requires automatic locking and no separate approval. |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This applies only to the exact revised list with normalized SHA-256 `40df97c47d37b4ae9d7f5c22623ab490c96c5dee9ab5be689a74ced25bb3be96`. Any subsequent list change requires a new revision and verification.

## Exact final copy-and-paste list

```text
1x Admiral Beckett Brass [Commander]
1x Admiral Brass, Unsinkable
1x Ancient Tomb
1x Arcane Signet
1x Badlands
1x Black Market Connections
1x Blood Crypt
1x Bloodstained Mire
1x Breeches, Brazen Plunderer
1x Breeches, Eager Pillager
1x Captain Lannery Storm
1x Captain Vargus Wrath
1x Cavern of Souls
1x Changeling Outcast
1x Chaos Warp
1x Coastal Piracy
1x Coercive Recruiter
1x Command Tower
1x Corsair Captain
1x Counterspell
1x Cover of Darkness
1x Crumbling Necropolis
1x Cyclonic Rift
1x Daring Piracy
1x Deflecting Swat
1x Demonic Tutor
1x Dimir Signet
1x Dire Fleet Captain
1x Dire Fleet Neckbreaker
1x Dire Fleet Poisoner
1x Don Andres, the Renegade
1x Double Down
1x Drowned Catacomb
1x Edward Kenway
1x Exotic Orchard
1x Fathom Fleet Captain
1x Feed the Swarm
1x Fierce Guardianship
1x Fiery Cannonade
1x Forerunner of the Coalition
1x Francisco, Fowl Marauder
1x Glint-Horn Buccaneer
1x Herald's Horn
1x Hostage Taker
3x Island
1x Izzet Signet
1x Jeska's Will
1x Kari Zev, Skyship Raider
1x Kindred Discovery
1x Lightning Greaves
1x Luxury Suite
1x Malcolm, Alluring Scoundrel
1x Malcolm, Keen-Eyed Navigator
1x Mana Confluence
1x Mana Drain
1x March of the Drowned
1x Merchant Raiders
1x Morphic Pool
2x Mountain
1x Otawara, Soaring City
1x Path of Ancestry
1x Polluted Delta
1x Port Razer
1x Ragavan, Nimble Pilferer
1x Raise the Palisade
1x Rakdos Signet
1x Ramirez DePietro, Pillager
1x Roaming Throne
1x Scalding Tarn
1x Secluded Courtyard
1x Shared Animosity
1x Shipwreck Marsh
1x Shivan Reef
1x Siren Stormtamer
1x Smoldering Marsh
1x Sol Ring
1x Steam Vents
1x Storm Fleet Sprinter
1x Storm the Vault // Vault of Catlacan
1x Stormcarved Coast
1x Sulfur Falls
1x Swamp
1x Talisman of Creativity
1x Talisman of Dominance
1x Talisman of Indulgence
1x The Indomitable
1x Toxic Deluge
1x Training Center
1x Underground River
1x Underground Sea
1x Vampiric Tutor
1x Volcanic Island
1x Warkite Marauder
1x Watery Grave
1x Xander's Lounge
1x Zara, Renegade Recruiter
1x Zephyr Singer
```