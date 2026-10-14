# Cult of Skaro — Current-Cycle Refinement Decision Record

**Date:** 2026-10-14  
**Approval status:** APPROVED AND LOCKED  
**Authoritative current-cycle baseline:** `refinement/decklists/Cult_of_Skaro_Current_Cycle_Baseline_2026-10-14.txt`  
**Baseline SHA-256:** `cc2f7a54479dbe166ada8253d42cc1ac9ebc7b3fdf229d9572f5631f269f3b6f`  
**Approved list:** `refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt`  
**Approved-list SHA-256:** `4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b`

## Approval and lock

The user explicitly approved this exact SHA-bound candidate on 2026-10-14 after the complete approval gate returned `APPROVAL_READY`. Cult of Skaro is now approved and locked for the current `global-restart-2026-10-13` cycle. Do not revise, reopen, or replace this list unless the user explicitly requests it.

## Complete approval gate

The SHA-bound complete approval gate ran successfully on 2026-10-14 against the freshly refreshed current-cycle Oracle cache.

- Count: **100**
- Distinct names: **94** (basic-land repeats account for the difference)
- Commander color identity: **B/R/U**
- Rules gate: **PASS**
- Official Commander legality gate: **PASS**
- Project exceptions: **none**
- Gate errors: **none**
- Overall result: **APPROVAL_READY**
- Gate artifact: `refinement/verification/cult_of_skaro_2026-10-14/gate_output/Cult_of_Skaro_2026-10-14_Complete_Gate.json`

## Baseline provenance

The current-cycle baseline is the repository's October 13 Cult of Skaro list. Relative to the frozen October 12 package, that list contained the historical prior-cycle Skorpekh Lord to Ashad, the Lone Cyberman change. Under the October 13 global restart, Cult was unapproved and that prior decision was not inherited as locked; every slot was re-audited before the current approval.

## Strategic identity and ceiling

Cult of Skaro is optimized as an artifact-creature/Dalek attack-trigger deck. The commander does not need to deal combat damage: it needs to attack. The strongest commander-first plan therefore prioritizes haste/protection, extra combats, additional independent Cult attack triggers, copies that can themselves be declared as attackers, and selective copying of Cult's triggered ability. The artifact-creature swarm remains important because one of Cult's random modes scales the whole artifact board and another creates Daleks.

The natural ceiling is **Bracket 4 — Optimized**. Cult is four mana and produces substantial value, but its primary engine remains combat-dependent and its attack mode is random. The deck can support a compact commander-native infinite-combat finish without becoming a generic Grixis combo shell.

## Approved nonland changes

- **Arcane Denial → Mana Drain.** Same interaction role with a materially higher optimization ceiling; the stored colorless mana helps deploy expensive artifact engines or extra-combat turns.
- **Artificer Class → Scientist Supreme of A.I.M.** Scientist is a two-mana commander-specific trigger multiplier. On the controller's turn it can pay 2 life to copy Cult's artifact-source attack trigger after the random mode has been selected. Artificer Class is slower, requires large level-up investments, and its late artifact-copy mode is awkward with a legendary commander.
- **Cryptothrall → Great Train Heist.** Cryptothrall is strong protection but redundant with Padeem, Lightning Greaves, Swiftfoot Boots, free interaction, and the added Plaza of Heroes. Great Train Heist directly converts one Cult attack into another combat and another Cult trigger, while its other spree modes remain useful with the artifact army.
- **Foundry Inspector → Mana Vault.** The deck retains Enthusiastic Mechanaut, Etherium Sculptor, Shuri, and artifact mana. Mana Vault provides a substantially stronger burst-mana ceiling for the deck's expensive artifact engines and extra-combat turns.
- **Mechanized Production → Helm of the Host.** Helm is one of the strongest Cult-specific engines. At the beginning of each combat on the controller's turn it creates a nonlegendary hasty Cult copy when equipped to the commander; that token can be declared as an attacker and produce its own independent random Cult trigger. Additional combats create additional Helm tokens.
- **Tezzeret, Master of the Bridge → Sword of Feast and Famine.** Tezzeret is powerful generic artifact payoff, but Sword advances the combat plan and combines with the already-present Aggravated Assault for repeatable/infinite combats when the equipped attacker connects and the lands can produce at least {3}{R}{R}. Every loop creates additional opportunities to attack with Cult.
- **Unwinding Clock → Full Throttle.** Unwinding Clock is useful generic artifact infrastructure but does little to multiply Cult's defining attack trigger. Full Throttle creates two additional combats and untaps creatures that attacked, allowing Cult and the artifact army to attack through all three combats in the turn.

## Approved land changes

- **Crumbling Necropolis → Plaza of Heroes.** Removes a guaranteed tapped land and adds legendary fixing plus an emergency hexproof/indestructible protection mode for Cult.
- **Shipwreck Marsh → Spire of Industry.** In this artifact-dense deck, Spire is reliable untapped Grixis fixing from the opening turns rather than conditional late fixing.
- **Stormcarved Coast → Arena of Glory.** Arena remains a red source while offering a commander-specific haste line: when its exerted mana is spent on Cult, Cult gains haste and can produce an attack trigger immediately.

## Important retained packages

The approved list intentionally retains the Doctor Who/Dalek/Cyberman identity core: Ashad, Auton Soldier, Cyberman Patrol, Cybermen Squadron, Dalek Drone, Dalek Squadron, Davros, Doomsday Confluence, Genesis of the Daleks, Missy, The Cyber-Controller, The Dalek Emperor, The Master, Multiplied, Their Name Is Death, and the Doctor Who interaction suite.

It also retains the commander-copy/trigger package of Irenicus's Vile Duplication, Nanogene Conversion, Phyrexian Metamorph, Roaming Throne, Sakashima of a Thousand Faces, Shuri, Spark Double, and Strionic Resonator. Adaptive Omnitool remains because it creates a second attack-based value trigger while digging six cards for an artifact.

Canoptek Spyder is retained as a repeatable draw engine for the deck's high density of nontoken artifact creatures. Padeem plus Greaves/Boots and the added Plaza absorb the protection role vacated by Cryptothrall.

## Rules checkpoints verified

1. Cult's random mode is chosen when each triggered ability is put onto the stack.
2. Strionic Resonator and Scientist Supreme copy the already-selected mode; they do not reroll it.
3. Roaming Throne causes a separate Cult trigger, and that separate trigger independently selects a random mode.
4. Helm of the Host triggers at the beginning of every combat on the controller's turn, including additional combats; its nonlegendary hasty Cult tokens can trigger Cult when actually declared as attackers.
5. Tokens created already attacking, such as myriad tokens from Auton Soldier, were not declared as attackers and therefore do not trigger their copied Cult attack abilities for that combat.
6. Aggravated Assault + Sword of Feast and Famine produces repeatable/infinite combats only if the equipped creature can connect and the untapped lands can make at least {3}{R}{R} each loop.
7. Full Throttle and Great Train Heist correctly untap the relevant attackers for their additional combats.
8. Arena of Glory grants haste only when its exerted mana is spent on the creature spell.

## Approved Archidekt classification

- Power Bracket: **4 — Optimized**
- Tags: **Artifacts / Extra Combats / Copies**

This exact list is approved and locked. Reopen it only upon explicit user instruction.
