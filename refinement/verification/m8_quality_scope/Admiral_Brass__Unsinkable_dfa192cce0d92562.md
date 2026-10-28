# M8 exact-current whole-99 commander-first adjudication — Admiral Brass, Unsinkable (#3)

2026-10-28. **Decision: KEEP Cory's exact approved M7 Rev3 100; no add/cut or new owner approval.** Approved bytes: `refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt`; SHA-256 `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`. One Admiral Brass, Unsinkable; 100 physical, 97 names (Island/Mountain/Swamp twice), 33 lands, eight rocks, no singleton/color/Commander exception, Bracket 4, Pirates / Reanimator / Aggro. This is **not** Admiral Beckett Brass's three-Pirates-connect theft deck.

## Provenance and scope

- Cory's October 23 exact Rev3 approval is recorded in `refinement/verification/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23_Verification.md`, which preserves the predecessor physical SHA and its conflicting historical registry SHA as separate facts. The eight owner-approved swaps are the actual candidate decision; the long double-faced `Brass's Tunnel-Grinder // Tecutlan, the Searing Rift` spelling is a name normalization, not an extra swap.
- The pinned source-bound M7 whole-list decision lives at `data/grixis/m7/decision_reviews/Admiral_Brass__Unsinkable_ChatGPT_Rev3_independent_review.md` on engineering PR #651, head `eb40e8e965c79762d9881b1a26dfd1289c49a5eb`, Git blob `74897b0834e705b263f0576933f5d1a493174531`. Existing [Rev3 focused CI #40041659693](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659693), [Rev2 research #40041659793](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659793), [M6 J provenance #40041659744](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659744), and [M7 decision #40041659702](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659702) were separately green in that context. Twenty-five existing focused regression assertions are **not** a current independent J or new exhaustive Oracle/100-card test.
- A new canonical `tests/test_m8_admiral_brass_unsinkable_current.py` SHA-guards the present file, finite positive and adverse conditions for all **five original P0 and eight original P1** case groups, plus this exact 99-copy ledger. These are bounded current fixtures, **not** a Magic rules engine, a table-playtest, or new third-party adversarial review. Old tests requiring Pitiless Plunderer or Wonder do **not** transfer as current-card tests.

## Commander-first decision and actual cost

The five-mana Admiral mills up to four cards upon entering and returns a *target Pirate creature card* from your graveyard at the beginning of combat on your turn, as a base 4/4 with haste and a finality counter. That is the engine: actual graveyard setup plus Pirate density, repeatable combat-return pressure, relevant Pirate enter/attack triggers, and removal of finality by Power Conduit or a legitimate exile-return new object. It is not an automatic every-turn return if the commander dies, has no eligible graveyard target, or the target is exiled; and finality means dying normally exiles the returned Pirate. Changeling Outcast qualifies as Pirate, not by being printed a Pirate. The true win ceiling is large reanimation tempo, Piracy attacks, Shared Animosity and conditional extra combats from Port Razer—not a guaranteed loop.

The exact-current 99 noncommander *physical card copies* follow. Every row is assigned **once**, even where it has secondary utility.

### 33 lands — colored Grixis source access, tribal casting, a deliberate 34-to-33 risk

- 1x Ancient Tomb
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Cavern of Souls
- 1x Command Tower
- 1x Drowned Catacomb
- 1x Exotic Orchard
- 2x Island
- 1x Luxury Suite
- 1x Mana Confluence
- 1x Morphic Pool
- 2x Mountain
- 1x Otawara, Soaring City
- 1x City of Brass
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Secluded Courtyard
- 1x Shipwreck Marsh
- 1x Smoldering Marsh
- 1x Steam Vents
- 1x Stormcarved Coast
- 1x Sulfur Falls
- 2x Swamp
- 1x Training Center
- 1x Underground River
- 1x Underground Sea
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

City of Brass replaces tapped Path of Ancestry with immediate any-color mana but charges life and loses tribal scry. More consequentially, Siren's Ruse replaced tapped Crumbling Necropolis, reducing actual lands to **33**; that is a genuine missed-land-drop risk for five-mana Admiral and high-end Pirates. Eight rocks, low creature interaction and efficient graveyard setup partly compensate but cannot be claimed to erase mana-screw risk. Cavern/Secluded Courtyard do not magically provide unrestricted colored noncreature mana, Ancient Tomb is colorless, and Exotic Orchard depends on opponents.

### 8 rocks — early Admiral and paid interaction

- 1x Arcane Signet
- 1x Dimir Signet
- 1x Izzet Signet
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

Sol Ring and Tomb accelerate generic mana without supplying Admiral's U/B/R pips; a Signet needs an existing mana payment, and Talismans cost life when used for colors. There is no free deterministic turn-three Admiral implied by eight rocks.

### 30 pirate/creature/tribal combat bodies or repeat-trigger engines — actual creature identity

- 1x Admiral Beckett Brass
- 1x Amphin Mutineer
- 1x Angrath's Marauders
- 1x Breeches, Brazen Plunderer
- 1x Breeches, Eager Pillager
- 1x Broadside Bombardiers
- 1x Captain Lannery Storm
- 1x Changeling Outcast
- 1x Coercive Recruiter
- 1x Corsair Captain
- 1x Dire Fleet Daredevil
- 1x Edward Kenway
- 1x Kitesail Larcenist
- 1x Warkite Marauder
- 1x Timestream Navigator
- 1x Gemcutter Buccaneer
- 1x Mary Read and Anne Bonny
- 1x Hostage Taker
- 1x Jhoira, Weatherlight Corsair
- 1x Malcolm, Alluring Scoundrel
- 1x Malcolm, Keen-Eyed Navigator
- 1x Merchant Raiders
- 1x Port Razer
- 1x Ramirez DePietro, Pillager
- 1x Roaming Throne
- 1x Siren Stormtamer
- 1x Skeleton Crew
- 1x The Indomitable
- 1x Thassa, Deep-Dwelling
- 1x Zara, Renegade Recruiter

The type/role headline is intentionally *not* “30 Pirates”: Thassa is a God, Throne is a Golem that must choose Pirate to double Admiral's triggered ability, and The Indomitable is a Vehicle needing legal crew. The group has 30 distinct allocated physical slots, including utility non-Pirates. Jhoira's steal line and Hostage Taker/Zara/Coercive Recruiter are conditional on legal game objects and timing, not permanent unconditional theft. Thassa can blink a controlled **nontoken** stolen permanent at the right end step to make a new object under our control, but it cannot blink a token for value, cannot rescue an illegal stolen target, and does not automatically put cards in a graveyard. Siren's Ruse returns a Pirate under **its owner's control** and can reset finality for a Pirate we own; it cannot launder opposing ownership into permanent theft. Kitesail Larcenist's triggered effect is actual enter-the-battlefield interaction, not a permanent all-board Treasure lock. Timestream Navigator requires the city's blessing and actual tap/activation resources and goes to the library bottom, not an unconditional infinite-combat line.

### 9 graveyard preparation, recursion and mass recovery

- 1x Animate Dead
- 1x Buried Alive
- 1x Entomb
- 1x Ripples of Undeath
- 1x Faithless Looting
- 1x Living Death
- 1x Patriarch's Bidding
- 1x Reanimate
- 1x Victimize

Entomb/Buried Alive select real creatures for the graveyard; Looting deliberately discards cards and has `{2}{R}` flashback. Ripples mills *random* top three cards during the precombat first main, then may take a legal creature or enchantment to hand for its actual mana/life payment. It does not guarantee hitting or returning a Pirate. Living Death affects each player and removes boards as it resolves, while Patriarch's Bidding lets **each player** choose a creature type; both expose reciprocal opponent value and graveyard hate. Victimize has an actual sacrifice/target cost. Reanimate life loss is a meaningful eight-drop exposure, not ignored.

### 10 answers and survival

- 1x Chaos Warp
- 1x Counterspell
- 1x Siren's Ruse
- 1x Cyclonic Rift
- 1x Deadly Rollick
- 1x Deflecting Swat
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Mana Drain
- 1x Toxic Deluge

Fierce Guardianship and Deadly Rollick need a commander-controlled situation for the free alternative; Swat's free mode also does, and Siren's Ruse has actual Pirate targeting and owner-return limitations. Mana Drain/Counterspell need `{U}{U}`, Deluge charges life and can destroy our own Pirates, and Cyclonic Rift overload is a seven-mana mode. Counterplay includes exile of Admiral's graveyard targets, removal before combat, counterspells and blockers.

### 9 access, support, pump and paid secondary engines

- 1x Black Market Connections
- 1x Demonic Tutor
- 1x Jeska's Will
- 1x Kindred Discovery
- 1x Lightning Greaves
- 1x Power Conduit
- 1x Shared Animosity
- 1x Vampiric Tutor
- 1x Brass's Tunnel-Grinder // Tecutlan, the Searing Rift

Power Conduit removes an actual counter as a cost on a controlled permanent and must have a legal target for its subsequent counter placement; removing finality does not undo Admiral's base 4/4 setting. Kindred Discovery and Shared Animosity scale from real creature-type/attack instances. Greaves shroud can block our own later targets. Tutors/top-deck selection aren't independent wins, Black Market Connections demands upkeep life choices, and Jeska's Will mana/impulse output varies with actual game state.

## All original P0/P1 case groups: current-card disposition and adverse branches

The original `data/grixis/m6/test_blueprints/Admiral_Brass__Unsinkable.json` provides **P0 five** (`C01`, `K01`, `K02`, `K03`, `F01`) and **P1 eight** (`K04`, `K05`, `E01`, `E02`, `W01`, `W02`, `F02`, `F03`) conceptual groups. The engineering Oct23 M7 Rev3 focused tests support retained-card regressions but are not a transfer receipt. New bounded canonical fixtures below deliberately exercise the exact present source and adverse cases; no old M6 J independence is asserted.

| Original | Current bounded positive case | Adverse case and superseded historical branch |
|---|---|---|
| **P0 C01** | Admiral entering mills up to four actual library cards. | Short/empty library mills fewer; absent Admiral no ETB. No guaranteed Pirate hit. |
| **P0 K01** | At beginning of *our* combat, a targeted Pirate in grave returns 4/4 hasty with finality. | No commander, enemy combat or absent target yields no legal return; the effect is not a cast. |
| **P0 K02** | Finality sends a would-die returned Pirate to exile, not its grave. | Nonfinality death goes to grave. Historical *Pitiless Plunderer* natural-death Treasure branch is **SUPERSEDED (card removed)**; no current-Plunderer test/pass. |
| **P0 K03** | Power Conduit can tap, remove one actual finality counter from a controlled permanent and place a legal counter elsewhere; 4/4 setting remains. | No counter/Conduit untapped status/legal target cannot pay required full costs. |
| **P0 F01** | Real Pirate in yard can be target. | Graveyard exile or no target in yard prevents reanimation; opponent can interact. |
| **P1 K04** | Changeling Outcast really qualifies as Pirate. | Historical *Wonder* graveyard grant-flying branch is **SUPERSEDED (card removed)**; Thassa is no team-wide flying grant. |
| **P1 K05** | Living Death and Bidding can bring back multiple creatures with real prerequisites. | Both have real opponent benefits; neither is a unilateral free wipe/reanimate. |
| **P1 E01** | Roaming Throne choosing Pirate can add a second Admiral combat trigger with two actual eligible Pirate targets. | Choosing a different type, absent Throne or only one valid target cannot manufacture a second distinct creature. |
| **P1 E02** | Real Skeleton Crew/Gemcutter/Recruiter/Hostage Taker/Zara ETBs and the new Thassa nontoken blink role remain. | No token theft laundering; Siren's Ruse returns under *owner*, unlike Thassa's normal controlled creature return. |
| **P1 W01** | Shared Animosity, Marauders and conditional Port Razer extra combat provide a genuine attack win route, with targeted Entomb/Buried Alive feed. | No hit, legal next target or remaining Razer: no repeat-combat claim. |
| **P1 W02** | Living Death/Bidding and actually stocked yard can produce a mass Pirate board. | No yard or opponent's more valuable recursion can defeat the plan; Looting setup is not guaranteed. |
| **P1 F02** | Returned Pirates are one-shot while finality persists; Power Conduit or correctly timed new-object blink may reset it. | Original finality death exiles; token/blink/owner boundaries and responses matter. |
| **P1 F03** | Ripples can mill three; Looting deliberately discards a Pirate. | Ripples may miss all Pirates, random mill is not a tutor, and insufficient resources/yard still fail. |

These thirteen **case-group conditions have been reconciled and executed in bounded fixtures**, but the removed Plunderer and Wonder subbranches are **retired**, not new passes. There is no historical exact SHA M7 M6-transfer receipt, independently successful J, game-engine stack proof, live new full-deck Oracle refresh or experimental win rate certified by this document. That honest scope is the basis of the grandfathered-case accounting, not permission to waive subsequent M8 requirements.

## Explicit opportunity-cost challenge: serious alternative complete 100s

The eight approved swaps retain stronger Pirate/reanimator identity than the October 13 source on balance: Larcenist creates new ETB disruption, Navigator adds conditional extra turn, Warkite improves attack-through defense, Jhoira gives real Pirate-dependent steal pressure, Ruse adds interactive reset/draw, Ripples supplies repeat graveyard feed, Thassa provides recurring ETB/finality reset and stolen-permanent control, and City unblocks early colors. The removed Scallywag, Francisco, Fathom Captain, Plunderer, Crumbling Necropolis, Forerunner, Wonder and Path of Ancestry have nonzero roles; their loss is charged, not dismissed.

| Complete alternative based on this legal current 100 | Genuine gain | Why incumbent still wins for this commander-first goal |
|---|---|---|
| Thassa, Deep-Dwelling → Conjurer's Closet | Repeatable end-step blink of owned creatures without blue mana, less vulnerable to enchantment removal | Five mana artifact lacks Thassa's flexible creature-control return; Thassa's end-step interaction with genuinely stolen nontoken permanents is the preferred broader ceiling. Closet is a good metagame swap, not an automatic improvement. |
| Thassa → Wonder; Siren's Ruse → Crumbling Necropolis | Restores a 34th land and team flying once Wonder is genuinely in grave with an Island; more clean evasion | Loses two distinct repeatable/flexible finality resets, ETB reuses and the Thassa current-control interaction, which are primary commander engine multipliers. Wonder-in-yard is also conditional. |
| Jhoira, Weatherlight Corsair → Pitiless Plunderer; Ripples of Undeath → Forerunner of the Coalition | Better raw death-Treasure conversion and specific Pirate top-deck setup | Loses a real steal-capable reanimatable Pirate body and repeatable precombat graveyard material. Plunderer cannot profit from finality exile as a death, so its presumed primary loop is undercut by the commander. |
| Siren's Ruse → Crumbling Necropolis; City of Brass → Path of Ancestry | 34 lands, tribal scry and less life bleeding under attrition | Two tapped lands slow early colors, and cutting Ruse loses a rare low-cost stack-speed Pirate/finality/ETB reset. Real mana pressure keeps this a defensible risk-oriented alternate, not a demonstrated improvement. |

The highest-confidence **warning**, not a proposed swap, is the **33-land** source count for a five-mana commander; it merits real opening-hand testing after M8. Pirate density and synergy are high enough that a random graveyard engine might miss, and concentrated creature-board win lines invite sweepers. The current four complete alternative 100s each lose enough commander-specific leverage or speed that no supported replacement is a clear upgrade over the owner's approved Rev3. **No changes proposed.** This stop is a bounded expert judgment, not a mathematical unique optimum or final M8 owner sign-off.
