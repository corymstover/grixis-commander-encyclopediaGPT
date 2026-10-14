# Kefka, Court Mage // Kefka, Ruler of Ruin — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Authoritative source: `GrixisFINAL60--2026.zip / Kefka__Court_Mage.csv` and `GrixisFINALTXT60--2026.zip / Kefka__Court_Mage.txt`  
Source CSV SHA-256: `46c0446a51d7f915030c6e1f593f76143a1c41d70f1297c7b9680563471321b8`  
Source TXT SHA-256: `3b71d085c5637935ab3be41e9d16fbf380ccb685aa0b829b32e0c00e1eaaa17e`  
Baseline artifact: `refinement/decklists/Kefka_Court_Mage_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline artifact SHA-256: `c61a613da1aeaae2fb179ad09b1b68a6301231742f8957f102275d4467fe8074`  
Approval candidate: `refinement/decklists/Kefka_Court_Mage_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03`

## Source reconciliation

The current FINAL60 CSV and FINALTXT exports agree exactly on the 100-card quantity/name map. The baseline is 100 cards, 100 distinct names, and 30 lands. Older v8.1.4 profile/ranking/audit material is supporting research only and does not overwrite the latest exports.

An earlier current-cycle candidate at SHA `2bb99011d85cc48841cb76edcddb8ba75696153b5e81bb36283880ff691f5acc` was red-teamed against fresher six-month Kefka tournament aggregates before approval. That review identified three material upgrades and the earlier candidate was superseded before any approval: `Cyclonic Rift -> Valley Floodcaller`, `Psychosis Crawler -> Fellwar Stone`, and `Opposition Agent -> Demonic Counsel`. No historical candidate is treated as approved.

## Commander blueprint and natural ceiling

**Primary commander plan:** repeatedly exploit Kefka's enters/attacks trigger to compress every hand while converting card-type diversity among the discarded cards into cards for Kefka's controller. Haste, blink, copy, and temporary-copy effects are unusually valuable because they create additional Kefka ETBs or immediate attack triggers. Efficient discard payoffs are retained only when they justify their slot at cEDH speed. The transformed Ruler of Ruin face remains a real secondary engine rather than ignored text.

**Natural ceiling: Power Bracket 5 — cEDH.** Kefka has multiple 2026 tournament top cuts, including wins, runner-up finishes, and additional high finishes. Current cEDH aggregate data shows substantial tournament volume and establishes Kefka as a genuine competitive commander. This is not a generic-Grixis elevation: the final list deliberately retains and adds Kefka-specific trigger repetition, haste, discard payoff, and transformation infrastructure.

### Commander-specific spine retained or added

- `Harmonic Prodigy` doubles Kefka's triggered abilities because both Kefka faces are Wizards.
- `Essence Flux` and `Displacer Kitten` produce additional Kefka enters triggers.
- `Anger` can be discarded to Kefka's own ETB; with a Mountain land type controlled, Kefka gains haste in time to attack that turn.
- `Arena of Glory` can both help pay for Kefka and grant haste when its special mana is spent on the creature spell.
- `Gogo, Mysterious Mime` can become a Kefka copy at beginning of combat while retaining the Gogo name, avoiding the legend rule; Gogo and Kefka gain haste and both attack, producing two Kefka attack triggers. Gogo does not create an additional Kefka ETB because it changes characteristics without entering.
- `Phantasmal Image` and `Phyrexian Metamorph` can enter as Kefka copies. Their Kefka ETB triggers occur before the legend rule leaves only one permanent with the Kefka name.
- `Saw in Half` can destroy Kefka and create two Kefka-copy tokens if Kefka dies this way. Both token ETBs trigger before state-based actions apply the legend rule.
- `Molten Duplication` creates a hasty Kefka-copy token. The legend rule requires one Kefka to be kept, but the token's ETB trigger already triggers; keeping the hasty token also permits an immediate Kefka attack trigger before the delayed sacrifice.
- `Tinybones, Bauble Burglar` and `Waste Not` remain efficient front-face discard payoffs that directly exploit Kefka's discard events.
- The Ruler of Ruin face remains strategically meaningful through ordinary opponent life loss during the controller's turn, including combat and effects such as `Orcish Bowmasters`; the list does not force a slow dedicated `Psychosis Crawler` package solely to demonstrate the back face.

## Exact current-cycle changes

### Cuts — 19

1. `Animate Dead` — generic reanimation redundancy; the candidate keeps `Reanimate` and prioritizes Kefka trigger infrastructure.
2. `Dauthi Voidwalker` — powerful generic stax, but `Phyrexian Metamorph` has direct commander ETB synergy and flexible clone utility.
3. `Geth's Grimoire` — four-mana discard payoff is too slow at the established cEDH ceiling.
4. `Kroxa, Titan of Death's Hunger` — incremental discard/value is below rate and does not multiply Kefka's trigger.
5. `Laughing Mad` — insufficient competitive rate relative to direct copy/haste infrastructure.
6. `Liliana's Caress` — redundant narrow discard damage payoff.
7. `Megrim` — redundant narrow discard damage payoff at three mana.
8. `Monument to Endurance` — slower value engine than the selected commander-specific package.
9. `Nightscape Familiar` — cost reduction is useful but lower impact than true fast mana and Kefka haste/copy effects.
10. `Sheoldred, the Apocalypse` — powerful generic payoff but does less for Kefka's unique trigger architecture than the accepted additions.
11. `Strionic Resonator` — can copy triggers, but repeated two-mana activation is less efficient than Harmonic Prodigy and selected copy effects.
12. `Windfall` — wheel redundancy trimmed while `Wheel of Fortune` remains; the slot becomes more commander-specific/efficient.
13. `Mountain` — removed for a higher-output competitive mana package while Mountain land types remain available from dual/shock lands.
14. `Swamp` — removed as the singleton mana base is tightened.
15. `Xander's Lounge` — tapped land is too slow for the cEDH ceiling.
16. `Exotic Orchard` — weakest remaining fixing land relative to the selected fetch/haste land package.
17. `Cyclonic Rift` — excellent generic interaction, but current Kefka data strongly favors `Valley Floodcaller`; the deck already retains sufficient cheap interaction.
18. `Opposition Agent` — strong generic stax, but the final red-team preferred proactive `Demonic Counsel` tutor density over another commander-independent disruption piece.
19. `Psychosis Crawler` — synergizes with transformed Kefka but is a five-mana payoff layered behind an eight-mana transformation and is materially below cEDH rate; the back face remains live without forcing this package.

### Adds — 19

1. `Anger` — discardable Kefka-specific haste engine.
2. `Arcane Signet` — efficient permanent acceleration toward a five-mana commander.
3. `Arena of Glory` — commander acceleration plus immediate haste.
4. `Final Fortune` — low-cost extra turn that creates another Kefka attack and supports turbo finish windows.
5. `Flooded Strand` — untapped fetch fixing and Tainted Pact-safe singleton mana.
6. `Gogo, Mysterious Mime` — commander-specific attack-trigger multiplier and haste source.
7. `Grim Monolith` — high-output acceleration toward Kefka and proactive lines.
8. `Hexing Squelcher` — efficient protection for Kefka and proactive win attempts.
9. `Into the Flood Maw` — one-mana interaction at the cEDH ceiling.
10. `Mnemonic Betrayal` — high-leverage resource conversion after Kefka/wheel/discard effects stock opposing graveyards.
11. `Molten Duplication` — two-mana Kefka ETB copy with haste and immediate attack potential if the token is retained.
12. `Phantasmal Image` — two-mana Kefka ETB copy with flexible clone utility.
13. `Phyrexian Metamorph` — flexible competitive clone that can copy Kefka for another ETB.
14. `Ragavan, Nimble Pilferer` — premium one-mana acceleration/value that helps reach the five-mana commander.
15. `Saw in Half` — commander-specific two-ETB copy effect with flexible creature utility.
16. `Talisman of Dominance` — efficient two-mana acceleration and color fixing.
17. `Valley Floodcaller` — current high-adoption Kefka cEDH infrastructure that grants flash timing to noncreature spells and supports compact competitive sequencing without requiring a dedicated off-plan bounce-combo package.
18. `Demonic Counsel` — efficient proactive tutor that improves compact win access without adding another commander-independent stax permanent.
19. `Fellwar Stone` — extremely high-adoption two-mana acceleration that materially improves deployment of a five-mana commander.

## Mandatory 99-slot whole-list audit

Every noncommander baseline slot was reviewed. Accounting is exact: **80 retained noncommander slots + 19 cuts = all 99 baseline noncommander slots.** Nineteen singleton additions restore the list to exactly 100 cards / 100 distinct names. The candidate has **28 lands**.

## Adversarial second pass

- **Valley Floodcaller — ACCEPTED after final red-team.** Fresh six-month Kefka data places it among the commander's most common competitive cards. The candidate does not add the Banishing Knack/Retraction Helix package, so Valley remains efficient flash/combo infrastructure rather than replacing Kefka with an unrelated dedicated loop.
- **Fellwar Stone — ACCEPTED over Psychosis Crawler.** Accelerating a five-mana commander is materially more important at cEDH speed than a five-mana payoff that requires Kefka's eight-mana transformation to become a dedicated feedback engine.
- **Demonic Counsel — ACCEPTED over Opposition Agent.** Current evidence supports the tutor as a proactive slot; removing a generic stax creature reduces commander-independent clutter while preserving cEDH access to compact wins.
- **Gogo, Mysterious Mime — RETAINED.** Four mana is a real cost, but Gogo is one of the few cards that both grants Kefka haste and creates a second Kefka attack trigger without invoking the legend rule.
- **Hexing Squelcher — RETAINED.** Its uncounterability/ward package protects both the five-mana commander and compact win attempts.
- **Phyrexian Metamorph — RETAINED over Dauthi Voidwalker.** This intentionally trades a generic stax piece for a flexible clone with direct commander ETB synergy.
- **Cursed Totem — REJECTED.** Competitive lists can accept it, but it directly shuts off Kefka's `{8}` transformation and undermines the encyclopedia's requirement that the back face remain strategically meaningful.
- **Samut, Tyrant of Naktamun — REJECTED.** Its split-second static ability can conflict with the free cast performed during a bargained `Beseech the Mirror` resolution; the candidate does not accept that anti-synergy.
- **Dedicated Valley Floodcaller bounce-combo package — REJECTED.** It would consume additional slots for a generic combo that does not require Kefka; Oracle and Breach already provide compact secondary wins.
- **The One Ring — REJECTED.** Strong generic value but four mana and no Kefka-specific trigger, haste, discard, or transformation interaction.
- **Birgi, God of Storytelling // Harnfel, Horn of Bounty — REJECTED.** Good turbo support, but the accepted fast-mana package and commander-specific effects are higher priority within the identity constraint.
- **Faerie Mastermind / Wan Shi Tong — REJECTED.** Efficient competitive value engines, but neither improves Kefka's ETB/attack/transform architecture as much as the selected cards.
- **Additional discard payoffs — REJECTED.** The baseline demonstrated diminishing returns from Caress/Megrim/Grimoire/Monument-style redundancy. `Tinybones` and `Waste Not` are the retained direct front-face payoffs for distinct reasons.

## Closure

The final candidate is **100 cards, 100 distinct names, and 28 lands**. Its primary identity is **Kefka trigger repetition + haste + discard compression**, with Oracle/Consultation-Pact and Breach/LED/Brain Freeze retained as compact cEDH secondary routes. The back face remains strategically relevant through ordinary life-loss events without forcing an overcosted dedicated payoff.

After the mandatory 99-slot audit, current tournament/aggregate cEDH comparison, clone/haste challenge, generic-staple challenge, discard-payoff challenge, mana-base review, and a second red-team that corrected three material misses in the preliminary candidate, the exact SHA-bound candidate has **ZERO NEW MATERIAL IMPROVEMENTS** pending rules/Oracle/legality verification.

Candidate remains **NOT APPROVED** until the exact SHA-bound list passes fresh Oracle/color-identity, current official Commander legality, independent rules verification, the complete fail-closed gate, and explicit user approval.