# Davros, Dalek Creator — Current-Cycle Refinement Decision Record

**Date:** 2026-10-14  
**Approval status:** APPROVAL_READY — complete gate passed; explicit user approval still required  
**Authoritative current-cycle baseline:** `refinement/decklists/Davros_Dalek_Creator_Current_Cycle_Baseline_2026-10-14.txt`  
**Baseline SHA-256:** `5c1d4a499704137318f0df3adceabaa048207536525fc4f0f49fb2625009c8bc`  
**Approval candidate:** `refinement/decklists/Davros_Dalek_Creator_Approval_Candidate_2026-10-14.txt`  
**Candidate SHA-256:** `aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc`

## Complete approval gate

The SHA-bound complete approval gate ran successfully on 2026-10-14 against the freshly refreshed current-cycle Oracle cache.

- Count: **100**
- Distinct names: **95** (basic-land repeats account for the difference)
- Commander color identity: **B/R/U**
- Rules gate: **PASS**
- Official Commander legality gate: **PASS**
- Project exceptions: **none**
- Gate errors: **none**
- Overall result: **APPROVAL_READY**
- Gate artifact: `refinement/verification/davros_dalek_creator_2026-10-14/gate_output/Davros_Dalek_Creator_2026-10-14_Complete_Gate.json`

The first gate attempt failed closed only because the then-current Oracle cache lacked three candidate names: `Court of Ambition`, `Entropic Battlecruiser`, and `Labyrinth Raptor`. The repository then performed a fresh validated Scryfall metadata refresh, rebuilt the current-cycle cache with 543 resolved names and zero unresolved records, and reran this exact candidate successfully. The decklist was not changed to bypass the gate.

This result does not itself approve or lock the deck. Explicit user approval remains required.

## Baseline provenance and research-package discrepancy

The current-cycle baseline is the repository's October 13 Davros list. Relative to the frozen October 12 CSV/TXT exports, that historical list contains the prior-cycle `Steel Overseer -> The Master, Gallifrey's End` change. The October 13 global restart voided the old approval, not the existence of the latest list; therefore that list is used only as the current-cycle baseline and every slot is re-audited.

A material supporting-data inconsistency was found during the current audit. The authoritative October CSV and TXT exports agree with each other, and `csv_txt_reconciliation.csv` marks Davros `PASS`, but `deck_card_audit.csv` reflects a different six-card version. The audit contains `Auton Soldier`, `Court of Ambition`, `Crumbling Necropolis`, `Fell Specter`, `Megrim`, and `Shrieking Affliction` where the authoritative CSV/TXT instead contain `Ashad, the Lone Cyberman`, `Boltwave`, `Death in Heaven`, `Fiery Islet`, `Loyal Subordinate`, and `Sygg, River Cutthroat`. This also explains why Auton Soldier and Court of Ambition were absent from the ranked candidate pool: the ranking input treated them as already present. The current refinement compensates manually and does not rerun the research pipeline.

## Commander identity and natural ceiling

Davros is optimized as a **Dalek / villainous-choice / life-loss-discard engine** rather than generic Grixis artifacts or generic discard. Davros triggers at the beginning of **your** end step. The ability itself is not gated by an intervening-if trigger condition; on resolution it checks which opponents lost at least 3 life that turn, creates the Dalek if at least one opponent qualifies, then each qualifying opponent faces the draw-or-discard villainous choice.

The strongest commander-first plan is therefore:

1. Make as many opponents as possible lose at least 3 life during our own turn.
2. Multiply Davros's end-step trigger with artifact-source trigger copying and additional Davros copies.
3. Convert the villainous-choice discard branch into additional punishment/value.
4. Turn the generated 3/3 menace Daleks into meaningful combat pressure.

Natural ceiling: **Bracket 4 — Optimized**. Davros is efficient at four mana and can snowball value, but the payoff is delayed to the end step, depends on establishing the 3-life threshold, and gives opponents choices. The deck is optimized aggressively without replacing its identity with generic Grixis combo.

## Proposed nonland changes

- **The Rack -> Auton Soldier.** The Rack normally damages its chosen opponent during that opponent's upkeep, which does not help Davros qualify opponents during our turn. Auton Soldier can enter as a nonlegendary artifact copy of Davros, creating another independent end-step Davros trigger while remaining on-theme Doctor Who artifact support.
- **Bottomless Pit -> Court of Ambition.** Bottomless Pit makes opponents discard on their own upkeeps and therefore does little to establish Davros's own-turn threshold. Court acts on our upkeep: each opponent must either lose 3 life or discard, and monarch increases the pressure. Both branches directly support the Davros plan, especially with Entropic Battlecruiser.
- **Oppression -> Scientist Supreme of A.I.M.** Oppression primarily makes opponents discard while they cast spells on their turns and makes us discard while advancing our own turn. Scientist Supreme directly copies Davros's artifact-source triggered ability once during our turn for 2 life, multiplying the commander's actual payoff.
- **Great Intelligence's Plan -> Maestros Charm.** Great Intelligence's Plan is a six-mana, single-opponent villainous-choice value spell. Maestros Charm is a three-mana instant whose middle mode makes every opponent lose exactly 3 life, turning Davros on for the full table; its other modes remain useful card selection or removal.
- **The Master, Gallifrey's End -> Labyrinth Raptor.** The Master requires a nontoken artifact creature to die and does not trigger from ordinary Dalek-token deaths, making its payoff comparatively conditional without a dedicated sacrifice engine. Labyrinth Raptor directly weaponizes Davros and the 3/3 menace Daleks: blocked menace creatures force a blocking-creature sacrifice, and its pump ability increases the clock.
- **Liliana's Caress -> Entropic Battlecruiser.** Caress punishes each discard for 2 life, which by itself does not meet Davros's 3-life threshold. Once stationed to 1+, Entropic Battlecruiser makes an opponent lose exactly 3 whenever that opponent discards a card. This makes the discard branch of Court of Ambition, Geier Reach Sanitarium, Sycorax Commander, and other discard effects materially more commander-relevant. At 8+ it becomes an attacking artifact creature that forces every opponent to discard or lose 3.

## Proposed land changes

- **Dragonskull Summit -> City of Brass.** Replace conditional fixing with unconditional untapped Grixis fixing.
- **Drowned Catacomb -> Mana Confluence.** Same objective: unconditional untapped access to all three colors.
- **Haunted Ridge -> Plaza of Heroes.** Plaza helps cast Davros and other legends while adding a commander-protection line through hexproof and indestructible.
- **Shipwreck Marsh -> Marsh Flats.** Replace a conditional slow land with fetchland access to the deck's typed Grixis duals/shocks.
- **Stormcarved Coast -> Misty Rainforest.** Same mana-base optimization, with access to blue typed duals/shocks.

`Geier Reach Sanitarium` is intentionally retained. With Entropic Battlecruiser at station 1+, activating Sanitarium during our turn makes each opponent draw then discard; each opponent's discard then causes that opponent to lose 3, creating a repeatable Davros threshold enabler.

## Important retained packages

The Dalek/Cyberman identity core remains intact: Ashad, Cult of Skaro, Cyber Conversion, Cyberman Patrol, Cybermen Squadron, Dalek Drone, Dalek Squadron, Death in Heaven, Delete, Doomsday Confluence, Genesis of the Daleks, Missy, Sycorax Commander, The Cyber-Controller, The Dalek Emperor, The Valeyard, This Is How It Ends, Weeping Angel, and the Doctor Who support shell.

The exact-threshold package retains Boltwave and Loyal Subordinate. Perforating Artist, Missy, Wound Reflection, Tezzeret, Ensnared by the Mara, Sycorax Commander, and Torment of Hailfire remain as additional pressure/value engines that can establish or exploit qualifying life loss depending on choices and board state.

The discard-conversion package remains through Waste Not, Geth's Grimoire, Tinybones, and the proposed Entropic Battlecruiser rather than broad symmetrical discard effects whose timing is poorly aligned with Davros.

## Current external evidence checkpoint

Current EDHREC data (2026-10-14) lists Davros at roughly 5,991 decks. The commander page remains heavily centered on Daleks/artifacts, while optimized subsets strongly support the retained Dalek core. Court of Ambition appears in 50% of current optimized Davros decks, 70% of optimized artifact-tagged Davros decks, and 100% of the small optimized burn sample. Labyrinth Raptor is a high-lift Davros card and appears in 80% of the small optimized burn and optimized discard samples. These statistics are supporting evidence only; they do not override commander-first strategic judgment.

## Rules checkpoints verified

1. Davros's end-step ability triggers even if no opponent has yet lost 3 life as the end step begins; the life-loss condition is checked during resolution rather than as an intervening-if trigger condition.
2. Scientist Supreme can copy a Davros triggered ability because Davros is an artifact source; the copy independently performs Davros's resolution instructions.
3. Roaming Throne can choose Alien or Scientist and make Davros trigger an additional time.
4. Strionic Resonator can copy Davros's triggered ability.
5. Auton Soldier entering as a Davros copy is nonlegendary and supplies an additional Davros end-step trigger; normal myriad tokens are exiled at end of combat before the end step.
6. The Valeyard makes each qualifying opponent face each Davros villainous choice an additional time.
7. Court of Ambition plus an active 1+ Entropic Battlecruiser establishes the 3-life threshold regardless of whether an opponent takes Court's life-loss branch or discards a card.
8. Geier Reach Sanitarium plus an active 1+ Entropic Battlecruiser can establish the threshold during our turn through the opponents' discards.
9. Perforating Artist, Wound Reflection, and Missy share the beginning-of-end-step timing window with Davros; because we control the triggers, appropriate stack ordering can let their life-loss/damage effects resolve before Davros and establish qualification where their own conditions/choices allow it.
10. Maestros Charm and Loyal Subordinate each directly cause every opponent to lose exactly 3 life during our turn.
11. Labyrinth Raptor directly supports Davros and the generated Daleks because both have menace; blocked menace creatures trigger Raptor's forced-sacrifice ability.

## Proposed Archidekt classification

- Power Bracket: **4 — Optimized**
- Tags: **Daleks / Villainous Choice / Group Slug**

The deck is approval-ready but remains unapproved and unlocked until the user explicitly approves it.
