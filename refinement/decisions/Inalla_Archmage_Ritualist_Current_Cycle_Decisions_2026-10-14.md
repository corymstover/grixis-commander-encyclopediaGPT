# Inalla, Archmage Ritualist — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Baseline artifact: `refinement/decklists/Inalla_Archmage_Ritualist_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline SHA-256: `f842f8be78716026dce3b8d713c6cd9dd2bfc3d5358628832fd6e98ca5005439`  
Authoritative source: `GrixisFINAL60--2026.zip / Inalla__Archmage_Ritualist.csv`  
Source CSV SHA-256: `2ffc4b99b3aa6c1a910fdd7b667fa63708b831e6834662d0dce1504ddc41d922`  
Approval-candidate artifact: `refinement/decklists/Inalla_Archmage_Ritualist_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`

## Source reconciliation

The latest FINAL CSV/TXT export is the card-membership baseline. The older v8.1.4 card-audit material is stale for Inalla: it records `Counterspell`, `Ertai Resurrected`, `Scholar of the Ages`, `Venser, Shaper Savant`, and `Wizard's Retort`, while the current FINAL export instead contains `Archmage of Echoes`, `Dour Port-Mage`, `Molten Echoes`, `Panharmonicon`, and `Stonybrook Banneret`. The FINAL export therefore controls baseline membership; the older audit remains research evidence only.

## Commander blueprint and natural ceiling

**Primary plan:** exploit Inalla's command-zone Eminence trigger as the deck's combo engine. The optimized list is not built to cast Inalla routinely; Wizard ETBs become duplicated tutor, recursion, card-selection, protection, and combo effects for one additional mana.

**Natural ceiling:** **Power Bracket 5 — cEDH.** Current 2026 tournament evidence shows repeated Inalla top cuts, including a second-place finish on 2026-10-11. Current cEDH aggregate evidence also concentrates heavily on the Spellseeker / Scholar of the Ages shell. This is therefore Inalla's demonstrated natural ceiling rather than a generic Grixis promotion.

### Primary commander-specific win routes

- `Spellseeker` plus Inalla's Eminence trigger is a one-card command-zone-assisted combo line using `Culling the Weak`, `Unearth`, `Burnt Offering`, `Finale of Promise`, `Entomb`, `Reanimate`, `Scholar of the Ages`, and `Shallow Grave`, producing arbitrarily many hasty Scholar tokens and mana/value sufficient to win.
- `Bloodline Necromancer` + `Ruthless Technomancer` + Inalla forms a separate commander-dependent loop producing arbitrarily many Treasures, Wizard tokens, ETB/LTB/death/sacrifice events, and colored mana. Inalla can then be cast and her five-Wizard activated ability closes the game.
- `Vedalken Aethermage` and `Step Through` provide Wizardcycling access to the creature package.
- `Apprentice Necromancer` is intentionally retained because it is a Wizard: an Inalla-created token copy gains haste and can immediately activate its tap ability, turning Eminence into fast reanimation infrastructure.
- `Thundertrap Trainer` is the final red-team replacement for Samut. It is a two-mana Wizard whose ETB looks at the top four cards for a noncreature, nonland card; Inalla can copy the Trainer and duplicate that selection effect for one additional mana.

### Secondary win routes

- `Thassa's Oracle` + `Demonic Consultation` or `Tainted Pact`.
- `Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze` when the normal graveyard/card-volume prerequisites are met.
- `Hoarding Broodlord` + `Saw in Half` as a compact tutor/value engine capable of assembling deterministic lines.

## Material baseline defects corrected

The baseline is structurally valid at 100 cards but operates below Inalla's demonstrated ceiling. It spends many slots on slower Wizard-tribal/ETB-value multiplication (`Panharmonicon`, `Molten Echoes`, `Naban`, `Archmage of Echoes`, `Kindred Discovery`, `Azami`) while omitting critical pieces of the contemporary Inalla cEDH engine.

Most materially, the baseline contains `Spellseeker`, `Culling the Weak`, `Burnt Offering`, `Unearth`, `Entomb`, `Reanimate`, and `Shallow Grave`, but omits both `Finale of Promise` and `Scholar of the Ages`. The standard command-zone-assisted Spellseeker line is therefore incomplete in the baseline. The candidate restores that line directly rather than merely adding generic Grixis power.

The baseline also uses commander-dependent free spells (`Fierce Guardianship`, `Deflecting Swat`, `Deadly Rollick`) even though optimized Inalla normally remains in the command zone. `Force of Negation` is also downgraded because it cannot protect the deck's proactive combo during its controller's turn.

## Mandatory 99-slot whole-list audit

Every noncommander baseline slot was reviewed. Accounting is exact: **50 noncommander cards retained + 49 noncommander cards cut = all 99 baseline noncommander slots.** The candidate adds 49 cards and returns to exactly 100 cards including Inalla.

### Retained 50 noncommander cards

`An Offer You Can't Refuse`; `Ancient Tomb`; `Animate Dead`; `Apprentice Necromancer`; `Arcane Signet`; `Blood Crypt`; `Bloodline Necromancer`; `Bloodstained Mire`; `Burnt Offering`; `Chrome Mox`; `Command Tower`; `Culling the Weak`; `Dark Ritual`; `Demonic Tutor`; `Entomb`; `Fellwar Stone`; `Flusterstorm`; `Force of Will`; `Grim Monolith`; `Imperial Seal`; `Island`; `Lim-Dûl's Vault`; `Lion's Eye Diamond`; `Lotus Petal`; `Mana Vault`; `Morphic Pool`; `Mox Diamond`; `Mystical Tutor`; `Otawara, Soaring City`; `Pact of Negation`; `Persist`; `Polluted Delta`; `Reanimate`; `Ruthless Technomancer`; `Scalding Tarn`; `Shallow Grave`; `Simian Spirit Guide`; `Sol Ring`; `Spellseeker`; `Steam Vents`; `Step Through`; `Swamp`; `Swan Song`; `Talisman of Dominance`; `Talisman of Indulgence`; `Thassa's Oracle`; `Unearth`; `Vampiric Tutor`; `Vedalken Aethermage`; `Watery Grave`.

### Cut 49 baseline cards

`Aether Channeler`; `Archaeomancer`; `Archmage of Echoes`; `Ashnod's Altar`; `Azami, Lady of Scrolls`; `Baral, Chief of Compliance`; `Blightstep Pathway // Searstep Pathway`; `Brainstorm`; `Chaos Warp`; `Clearwater Pathway // Murkwater Pathway`; `Cyclonic Rift`; `Deadly Rollick`; `Deflecting Swat`; `Displace`; `Dour Port-Mage`; `Dragonskull Summit`; `Drowned Catacomb`; `Dualcaster Mage`; `Fabled Passage`; `Fierce Guardianship`; `Force of Negation`; `Ghostly Flicker`; `Harmonic Prodigy`; `Haunted Ridge`; `Kess, Dissident Mage`; `Kindred Discovery`; `Luxury Suite`; `Molten Echoes`; `Naban, Dean of Iteration`; `Naru Meha, Master Wizard`; `Panharmonicon`; `Patron Wizard`; `Phyrexian Altar`; `Ponder`; `Preordain`; `Riptide Laboratory`; `Riverglide Pathway // Lavaglide Pathway`; `Shipwreck Marsh`; `Shivan Reef`; `Snapcaster Mage`; `Stonybrook Banneret`; `Stormcarved Coast`; `Sulfur Falls`; `Sulfurous Springs`; `Takenuma, Abandoned Mire`; `Talisman of Creativity`; `Training Center`; `Underground River`; `Xander's Lounge`.

### Added 49 cards

`Blood Pet`; `Hexing Squelcher`; `Hoarding Broodlord`; `Kefka, Court Mage // Kefka, Ruler of Ruin`; `Ragavan, Nimble Pilferer`; `Thundertrap Trainer`; `Scholar of the Ages`; `Ad Nauseam`; `Borne Upon a Wind`; `Brain Freeze`; `Cabal Ritual`; `Chain of Vapor`; `Demonic Consultation`; `Essence Flux`; `Final Fortune`; `Intuition`; `Mental Misstep`; `Red Elemental Blast`; `Sacrifice`; `Saw in Half`; `Tainted Pact`; `Beseech the Mirror`; `Finale of Promise`; `Gamble`; `Lively Dirge`; `Rite of Flame`; `Unmarked Grave`; `Wheel of Fortune`; `Mox Opal`; `Wishclaw Talisman`; `Mystic Remora`; `Necropotence`; `Rhystic Study`; `Underworld Breach`; `Arid Mesa`; `Badlands`; `Cavern of Souls`; `City of Brass`; `City of Traitors`; `Exotic Orchard`; `Flooded Strand`; `Gemstone Caverns`; `Mana Confluence`; `Marsh Flats`; `Misty Rainforest`; `Underground Sea`; `Verdant Catacombs`; `Volcanic Island`; `Wooded Foothills`.

## Strategic effect of the rebuild

- **Spellseeker line completed:** `Finale of Promise` and `Scholar of the Ages` restore Inalla's defining one-card combo engine.
- **Turbo density increased:** rituals, fast mana, low-cost tutors, and graveyard tutors reach the speed required by the commander's competitive ceiling.
- **Protection corrected for command-zone play:** interaction no longer assumes Inalla has been cast. `Hexing Squelcher` plus efficient stack interaction protects proactive turns without requiring the commander on the battlefield.
- **Reanimator density increased:** `Unmarked Grave`, `Lively Dirge`, `Entomb`, `Reanimate`, `Persist`, `Animate Dead`, `Shallow Grave`, and `Apprentice Necromancer` support Scholar and alternative Wizard lines.
- **Backup wins added without replacing identity:** Oracle/Consultation/Pact and Breach/LED/Brain Freeze provide cEDH resilience, while Spellseeker + Inalla Eminence remains the signature route.
- **Mana base rebuilt for speed and Tainted Pact:** 27 unique land names; the entire candidate has 100 distinct card names.

## Adversarial second pass and rules red-team

Current EDHREC cEDH evidence, recent tournament lists, and high-performing 2026 Inalla lists were compared against the candidate after the first rebuild.

- **Apprentice Necromancer — RETAINED.** It appears in multiple successful 2026 lists and is unusually commander-specific because Inalla's hasty token copy can activate immediately.
- **Thundertrap Trainer — ADDED on final red-team.** The first frozen draft contained `Samut, Tyrant of Naktamun`. Rules review identified that Samut gives the controller's instant and sorcery spells split second. If Samut remains on the battlefield, `Finale of Promise` has split second and its resolution cannot cast the targeted spells while Finale itself remains on the stack. The same issue prevents the cast-during-resolution portion of a bargained `Beseech the Mirror`. Because Finale is structural to the signature Spellseeker line, this anti-synergy is material. Samut was removed before formal approval and Thundertrap Trainer replaced it. Trainer provides a low-cost Wizard ETB that Inalla can duplicate and appears in the 2026-10-11 runner-up list.
- **Spectral Arcanist — REJECTED.** Strong recursion synergy but four-mana setup and lower aggregate/tournament adoption make it weaker than the retained recursion/tutor core.
- **Corpse Dance / Dance of the Dead / Necromancy — REJECTED as additional redundancy.** All are defensible, but another reanimation effect would require cutting interaction, acceleration, or a distinct deterministic route.
- **Orcish Bowmasters — REJECTED.** Excellent generic cEDH card, but it does not materially exploit Inalla.
- **Valley Floodcaller — REJECTED.** Useful flash/untap utility, but less central than the deterministic Wizard package and existing protection suite.
- **Micromancer — REJECTED.** Inalla can duplicate its ETB, but four mana plus the Eminence payment is materially slower than Spellseeker and direct tutors.
- **Pyroblast / Daze / Into the Flood Maw / Dispel — REJECTED as additional interaction.** All are credible and appear in successful lists. No existing candidate slot is clearly weaker after accounting for acceleration, deterministic redundancy, and commander identity.
- **Starting Town / Training Center / Forbidden Orchard / Phyrexian Tower — REJECTED after mana-base challenge.** The chosen 27-land configuration remains fast, fully singleton for Tainted Pact, and sufficiently color-dense.
- **Generic Wizard-tribal value package — REJECTED.** `Panharmonicon`, `Molten Echoes`, `Naban`, `Archmage of Echoes`, and similar cards are slower than Inalla's demonstrated combo ceiling.

## Rules checkpoints before formal gate

- Inalla's Eminence trigger functions while she is in the command zone.
- The token made by Inalla gains haste and is exiled at the beginning of the next end step.
- The Scholar-based Spellseeker line requires correct trigger ordering and priority around sacrifice spells, Finale of Promise, Entomb/Reanimate, and Inalla triggers.
- The Bloodline/Ruthless loop is commander-dependent and must be independently attested.
- `Thundertrap Trainer` is a Wizard; both the original and an Inalla token copy can generate separate ETB selection triggers.
- `Tainted Pact` is structurally supported by 100 distinct names in the candidate.
- `Samut, Tyrant of Naktamun` is intentionally absent from the final candidate because its split-second static ability conflicts with the primary Finale-of-Promise line and bargained Beseech casting during resolution.

## Closure

After the large cEDH rebuild, tournament/aggregate comparison, and the Samut rules correction, the candidate was challenged again against current Inalla cEDH lists, alternative Wizards, interaction, reanimation, and mana-base configurations. The final serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

Candidate state before formal gate:
- 100 cards
- 100 distinct names
- 27 lands
- commander-first Eminence / Spellseeker / reanimator identity preserved
- natural ceiling: **Power Bracket 5 — cEDH**
- proposed Archidekt tags: **Spellseeker Combo / Reanimator / Turbo**
- no project legality exception expected

The candidate remains **NOT APPROVED** until the complete fail-closed Oracle/color-identity/legality/rules gate passes and the user explicitly approves the exact SHA-bound candidate.