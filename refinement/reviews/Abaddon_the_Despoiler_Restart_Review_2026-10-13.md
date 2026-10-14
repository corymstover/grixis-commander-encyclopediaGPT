# Abaddon the Despoiler — Full Restart Review

**Deck #1 of 62 · Review date: 2026-10-13 · Status: APPROVED / LOCKED — FRESH RESTART REVIEW PASSED**

Frozen source: October 12 authoritative CSV/TXT archives. Baseline normalized-list hash: `a58b6ad5499596eb64af79a83b210641e4e097c79803de87cca3ba2244fab91f`. Final exact list hash: `fd66ea20135a77322113f69cd6ac583fde381a1af08ffac348c9f1f4d8227e15`.

## Baseline and scope

The frozen Abaddon CSV/TXT baseline was reopened and reconciled: 100 copies, 94 unique card names, 34 lands. The whole list was reassessed, not merely the prior 15-candidate shortlist. Historical reports were treated as evidence to challenge, not current approval. The full-list review matrix covers every baseline card name plus the three new candidates; the decision ledger records accepted and rejected alternatives. Frozen source exports and previous-cycle artifacts remain immutable.

## Final changes

| Add | Cut | Decision rationale |
|---|---|---|
| **Protection Racket** | Loyal Subordinate | Its upkeep trigger resolves before the first main phase. Each opponent either pays life equal to the revealed card's mana value, increasing Abaddon's threshold, or lets the card go to your hand. It supplies either threshold progress or card advantage without requiring Abaddon to survive. |
| **Ancient Cellarspawn** | Nightscape Familiar | The deck frequently casts spells without paying their mana costs through cascade. Cellarspawn triggers targeted life loss equal to the difference between mana spent and mana value, and discounts Demon/Horror/Nightmare spells. This is more commander-specific than the Familiar's generic blue/red discount. |
| **Aurora Phoenix** | Bituminous Blast | A recurring cascade creature can receive a second cascade trigger from Abaddon when the threshold is met and returns from the graveyard to hand whenever a spell with cascade is cast. Bituminous Blast's five-mana rate for four damage to one creature is weak in this removal-dense shell. |

The prior-cycle additions **Court of Ambition** and **Warstorm Surge** were not carried forward automatically. Protection Racket is preferred over Court for lower cost and the life-loss/card-advantage choice. Rakdos, Lord of Riots is retained instead of Warstorm Surge because its threshold-scaled creature discount is cheaper and helps deploy the creature engine; Ancient Cellarspawn adds a lower-cost cast-for-less payoff.

## Commander-first strategic blueprint

**Primary plan:** cause opponent life loss early in the turn, then cast spells from hand whose mana values are at or below the aggregate opponent life lost that turn to gain Abaddon's cascade. Cheap all-opponent burn, repeatable pingers, Bloodletter of Aclazotz, Solphim, fast mana and cost reduction help cross the threshold and continue the chain.

**Cascade and exile value:** Abaddon, Call Forth the Tempest, Noise Marine, Aurora Phoenix and Wild-Magic Sorcerer create or extend cascade chains. The Lost and the Damned, Keeper of Secrets, Passionate Archaeologist, Prosper, The Ruinous Powers and Nalfeshnee reward spells cast from exile. Ancient Cellarspawn adds a targeted life-loss trigger when mana spent is below mana value; this can increase the threshold for later hand-cast spells in the same turn. Aurora Phoenix supplies recurring cascade pressure from the graveyard.

**Threshold setup:** Boltwave and Flame Rift deliver large aggregate opponent life loss for one mana. Thermo-Alchemist, Kessig Flamebreather, Exalted Flamer, Vivi Ornitier, Bloodletter and Solphim increase repeatable damage. Protection Racket gives upkeep life-loss-or-card decisions before main phase. Neheb converts prior opponent life loss into postcombat red mana; Rakdos discounts creature spells based on the same life-loss metric.

**Backup line:** Underworld Breach + Lion's Eye Diamond + Brain Freeze remains a compact graveyard/storm line with normal graveyard-size, escape-cost, mana and interaction prerequisites. It remains a backup rather than turning the list into a generic combo shell.

**Natural power ceiling:** optimized Bracket 4. The deck has fast mana, tutors, free interaction, high cascade density and a compact combo line, but retains its commander-first life-loss/cascade identity rather than being forced into a cEDH shell.

## Full-list and candidate review

Every baseline card was reviewed for role, commander synergy, efficiency, redundancy, curve/mana contribution, interaction, resilience and contribution to a win condition. The retained package includes 34 lands; fast mana and rituals; six tutors; draw/wheels/cantrips; free and low-cost interaction; threshold burn/pingers; cascade and exile payoffs; and the Breach backup line. The matrix records per-card dispositions, including the three cuts and three additions.

Candidate review included Protection Racket, Ancient Cellarspawn, Aurora Phoenix, Blood for the Blood God!, Court of Ambition, Warstorm Surge, Magnus the Red, Florian, Voldaren Scion, Black Waltz No. 3, Guttersnipe, Spear Spewer, Keen Duelist, Poxwalkers, Descent into Avernus, Dark Apostle, Heralds of Tzeentch, Let the Galaxy Burn, Mutalith Vortex Beast, Pink Horror, Bloodthirster, Cryptolith Fragment // Aurora of Emrakul, Plague Drone, Chaos Mutation, Sloppity Bilepiper, Chromatic Lantern, Tzaangor Shaman, Blight Grenade and Mandate of Abaddon. Candidate rankings were treated as discovery evidence, never automatic inclusions.

- **Blood for the Blood God! — rejected for this revision:** its Bloodletter synergy and draw-eight effect are real, but mana value 11 makes it unavailable as a hit from the current cascade spells and it is a conditional hand-cast finisher. Mind's Desire is mana value 6, can be hit by cascade, and scales with spells cast earlier in the turn. The deck already has Bloodletter-amplified burn and the Breach line.
- **Magnus the Red — rejected:** strong token/cost-reduction concept with The Lost and the Damned, but five mana and token dependence; existing Birgi, Storm-Kiln Artist, Neheb, Rakdos and fast mana provide a more reliable resource package.
- **Florian — rejected:** on-plan card selection, but the list already has substantial draw, tutors, wheels and impulse/exile engines; no current slot was a clearly better cut.
- **Black Waltz No. 3 / Guttersnipe — rejected:** attractive pingers but overlap with Kessig Flamebreather, Exalted Flamer, Thermo-Alchemist, Vivi and damage multipliers.
- **Spear Spewer / Keen Duelist — rejected:** less reliable or more volatile threshold enablers than Boltwave, Flame Rift and repeatable pingers.
- **Poxwalkers — rejected:** strongest when already in the graveyard; no dedicated self-mill/sacrifice package reliably places it there.
- **Descent into Avernus — rejected:** symmetrical Treasures accelerate opponents as well as the deck.
- **Dark Apostle / Heralds of Tzeentch / Sloppity Bilepiper — rejected:** slower or less repeatable cascade support than Abaddon and Aurora Phoenix.
- **Let the Galaxy Burn / Mandate of Abaddon / Blight Grenade / Chaos Mutation — rejected:** board-control overlap, self-board risk or unreliable replacement effects relative to the retained removal suite.
- **Mutalith Vortex Beast / Pink Horror / Bloodthirster / Tzaangor Shaman — rejected:** higher variance, combat dependence or less direct commander synergy than the selected cascade package.

## Oracle discrepancy corrected

The inherited candidate-ranking metadata for **Ancient Cellarspawn** incorrectly stated that “each opponent loses life equal to the difference.” Current Oracle text says **“target opponent loses life equal to the difference.”** The final rules analysis uses the current target-one-opponent wording. Frozen source archives were not edited; the discrepancy is recorded in a separate active correction note.

## Rules and legality

- Abaddon's threshold counts total life lost by all opponents during the current turn; self-life loss does not count.
- Protection Racket triggers during upkeep. Paying life exiles the revealed card; declining payment puts it into your hand. It does **not** cast the card from exile.
- Ancient Cellarspawn's trigger resolves before the spell that caused it; it targets one opponent. A cascade hit cast without paying its mana cost has mana spent below mana value, but cost reductions do not change mana value.
- Aurora Phoenix returns only if it is in the graveyard immediately after a spell with cascade is cast. Its own cascade and Abaddon's granted cascade can both trigger when cast from hand with the threshold met.
- Bloodletter doubles opponent life loss during your turn, including loss caused by damage, only while it is on the battlefield.
- LED discards the hand as an activation cost; Breach escape requires exiling three other graveyard cards per cast. The combo has real resource and interaction constraints.
- The current Scryfall refresh recorded in the previous tracker pass covered all 94 baseline names; the three new candidates were separately checked against current card references. Protection Racket and Ancient Cellarspawn are black; Aurora Phoenix is red. All fit UBR and are Commander-legal.
- Official Commander ban-list checkpoint reviewed 2026-10-13; no final-list card is banned and no project exception is used.

Sources: [Ancient Cellarspawn Oracle/rulings/legal status](https://www.mtg.wtf/card/dsc/47/Ancient-Cellarspawn); [Protection Racket Oracle/legal status](https://www.mtg.wtf/card/ncc/140/Protection-Racket); [Aurora Phoenix Oracle/rulings/legal status](https://www.mtg.wtf/card/prm/86026/Aurora-Phoenix); [official Commander banned list](https://mtgcommander.net/index.php/banned-list/); [EDHREC Abaddon](https://edhrec.com/commanders/abaddon-the-despoiler); [EDHREC Abaddon Cascade](https://edhrec.com/commanders/abaddon-the-despoiler/cascade).

## Independent integrity audit

- Total: **100 cards including commander**.
- Unique names: **94**.
- Commander first line, exactly once, tagged `[Commander]`: **PASS**.
- Singleton/copy rule: **PASS**; only Island ×3, Mountain ×3 and Swamp ×3 repeat.
- Lands: **34**, unchanged.
- Color identity: **PASS**, all cards fit UBR.
- Project exceptions: **none**.
- Exact final list SHA-256 (UTF-8, LF, trailing newline): `fd66ea20135a77322113f69cd6ac583fde381a1af08ffac348c9f1f4d8227e15`.
- Multiplayer performance: no qualified matched-start simulator was available; no unsupported win-rate or superiority claim is made. The prior Aurora Phoenix vs. Mind's Desire six-game test cast neither card and remains explicitly inconclusive; it was not used as performance evidence.

## Final disposition

**APPROVED / LOCKED — FRESH RESTART REVIEW PASSED.** This approval applies only to the exact final hash above. The final list, card-by-card review matrix, candidate ledger, change ledger, correction note and verification certificate are stored as separate dated artifacts. Do not reopen unless a material correctness issue is discovered or the user explicitly requests it.
