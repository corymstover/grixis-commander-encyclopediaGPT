# Ashnod the Uncaring — finalization blockers and source reconciliation (2026-10-13)

Status: WORKING; not approved. This is a blocker record, not a finalized deck or permission to lock.

## Frozen source versus inherited audit
- Frozen GrixisFINALTXT60--2026.zip / Ashnod_the_Uncaring.txt: 100 card copies, 95 distinct names, 99 noncommander copies.
- Legacy deck_card_audit.csv for Ashnod: 95 exact-matched names, but NOT the same 95 names as the frozen October 12 baseline.
- Present in frozen baseline, missing from legacy audit: Dross Skullbomb; Esoteric Duplicator.
- Present in legacy audit, absent from frozen baseline: Aether Spellbomb; Urza's Bauble.
- Thus only 97/99 noncommander slots match archived card data. The inherited audit is not a fresh current-list Oracle verification.

## Rules red-team
- Ashnod has no once-per-turn or nontoken restriction; sacrifices must be paid as part of activation cost and mana abilities are excluded.
- Repurposing Bay qualifies and its search is copied; RETAIN as central engine.
- Bolas's Citadel sacrifices ten nonland permanents as activation cost; Ashnod can copy the 10-life-loss activated ability, for two instances. Its top-deck casting is an independent strength. RETAIN; do not substitute Mystic Forge solely for cheaper mana cost.
- Time Sieve qualifies for two extra turns from one activation if the original and copy resolve.
- Clan Crafter grants Ashnod a qualifying sacrifice-cost ability. RETAIN.
- Goblin Welder sacrifices during resolution, not as activation cost, so does not trigger Ashnod. Goblin Engineer and Scrap Welder do sacrifice as activation costs.

## Two proposed swaps (not yet approved)
- Audacious Reshapers -> Oni-Cult Anvil: lower-cost repeatable token-fed drain versus copied high-variance artifact deployment.
- Commander's Sphere -> Trading Post: repeatable copied draw/recursion versus ramp and copied single-use draw.
- Both proposals require full current Oracle, legality, identity and performance verification.

## Unresolved mandatory gates
1. Independently verify current Oracle, card identity, Commander legality and color identity for every proposed list card, including two additions and the two frozen-list cards absent from the inherited audit.
2. Close high-impact candidate comparisons with evidence-backed accept/reject reasons.
3. Controlled baseline-versus-proposal consistency/regression evaluation with limitations, then red-team and stopping-rule closure.
4. Present complete approval-ready list and request user approval; no auto-approval or lock.

Workflow standard: refinement/Grixis_Refinement_Protocol_v1.md section 10, uninterrupted execution until approval gate or material blocker.
