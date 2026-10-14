# Inalla, Archmage Ritualist — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Baseline artifact: `refinement/decklists/Inalla_Archmage_Ritualist_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline SHA-256: `f842f8be78716026dce3b8d713c6cd9dd2bfc3d5358628832fd6e98ca5005439`  
Authoritative source: `GrixisFINAL60--2026.zip / Inalla__Archmage_Ritualist.csv`  
Source CSV SHA-256: `2ffc4b99b3aa6c1a910fdd7b667fa63708b831e6834662d0dce1504ddc41d922`  
Approval-candidate artifact: `refinement/decklists/Inalla_Archmage_Ritualist_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `f8e7c35700e72acba3eac4596aa3faf8702f8aa3257fca07dc35bde3029ad472`

## Source reconciliation

The latest FINAL CSV/TXT export is the card-membership baseline. The older v8.1.4 card-audit material is stale for Inalla: it records `Counterspell`, `Ertai Resurrected`, `Scholar of the Ages`, `Venser, Shaper Savant`, and `Wizard's Retort`, while the current FINAL export instead contains `Archmage of Echoes`, `Dour Port-Mage`, `Molten Echoes`, `Panharmonicon`, and `Stonybrook Banneret`. The FINAL export therefore controls baseline membership; the older audit remains research evidence only.

## Commander blueprint and natural ceiling

**Primary plan:** exploit Inalla's command-zone Eminence trigger as a combo engine. The deck is not built to cast Inalla routinely; instead, Wizard ETBs become duplicate tutor, recursion, protection, and combo effects for one additional mana.

**Natural ceiling:** **Bracket 5 — cEDH.** Current tournament evidence establishes that Inalla is not merely theoretically cEDH-capable. Inalla has repeatedly top-cut 2026 competitive events, including a second-place finish on 2026-10-11. Current cEDH aggregate evidence also concentrates heavily on the Spellseeker / Scholar of the Ages shell. This is therefore the commander's demonstrated natural ceiling rather than an artificial generic-combo promotion.

**Primary commander-specific win routes:**
- `Spellseeker` plus Inalla's Eminence trigger is a one-card command-zone-assisted combo line using `Culling the Weak`, `Unearth`, `Burnt Offering`, `Finale of Promise`, `Entomb`, `Reanimate`, `Scholar of the Ages`, and `Shallow Grave`, producing arbitrarily many hasty Scholar tokens and mana/value sufficient to win.
- `Bloodline Necromancer` + `Ruthless Technomancer` + Inalla forms a separate commander-dependent loop that produces arbitrarily many Treasures, Wizard tokens, ETB/LTB/death/sacrifice events, and colored mana; Inalla can then be cast and her five-Wizard activated ability closes the game.
- `Vedalken Aethermage` and `Step Through` provide Wizardcycling access to the commander-specific creature package.
- `Apprentice Necromancer` remains intentionally because it is itself a Wizard: an Inalla-created hasty token copy can activate its tap ability immediately, converting the commander's Eminence ability into fast reanimation infrastructure.

**Secondary/backup win routes:**
- `Thassa's Oracle` + `Demonic Consultation` or `Tainted Pact`.
- `Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze` when graveyard/card-volume conditions support the loop.
- `Hoarding Broodlord` + `Saw in Half` functions as a compact tutor/value engine that can assemble deterministic lines without requiring Inalla to be cast.

## Material baseline defects corrected

The baseline is structurally legal at 100 cards but is built substantially below Inalla's demonstrated ceiling. It spends many slots on slower Wizard-tribal/ETB-value multiplication (`Panharmonicon`, `Molten Echoes`, `Naban`, `Archmage of Echoes`, `Kindred Discovery`, `Azami`) while omitting critical pieces of the contemporary Inalla cEDH engine.

Most materially, the baseline contains `Spellseeker`, `Culling the Weak`, `Burnt Offering`, `Unearth`, `Entomb`, `Reanimate`, and `Shallow Grave`, but omits both `Finale of Promise` and `Scholar of the Ages`. That leaves the standard command-zone-assisted Spellseeker line incomplete. The candidate restores that line directly rather than merely adding generic Grixis power.

The baseline also uses commander-dependent free spells (`Fierce Guardianship`, `Deflecting Swat`, `Deadly Rollick`) even though optimized Inalla normally remains in the command zone. Those cards are therefore unreliable in the deck's primary operating posture. `Force of Negation` is also downgraded because it cannot protect the deck's own proactive combo on its controller's turn.

## Mandatory 99-slot whole-list audit

Every noncommander baseline slot was reviewed. Accounting is exact: **50 noncommander cards retained + 49 noncommander cards cut = all 99 baseline noncommander slots.** The candidate adds 49 cards, returning to exactly 100 cards including Inalla.

### Retained 50 noncommander cards

`An Offer You Can't Refuse`; `Ancient Tomb`; `Animate Dead`; `Apprentice Necromancer`; `Arcane Signet`; `Blood Crypt`; `Bloodline Necromancer`; `Bloodstained Mire`; `Burnt Offering`; `Chrome Mox`; `Command Tower`; `Culling the Weak`; `Dark Ritual`; `Demonic Tutor`; `Entomb`; `Fellwar Stone`; `Flusterstorm`; `Force of Will`; `Grim Monolith`; `Imperial Seal`; `Island`; `Lim-Dûl's Vault`; `Lion's Eye Diamond`; `Lotus Petal`; `Mana Vault`; `Morphic Pool`; `Mox Diamond`; `Mystical Tutor`; `Otawara, Soaring City`; `Pact of Negation`; `Persist`; `Polluted Delta`; `Reanimate`; `Ruthless Technomancer`; `Scalding Tarn`; `Shallow Grave`; `Simian Spirit Guide`; `Sol Ring`; `Spellseeker`; `Steam Vents`; `Step Through`; `Swamp`; `Swan Song`; `Talisman of Dominance`; `Talisman of Indulgence`; `Thassa's Oracle`; `Unearth`; `Vampiric Tutor`; `Vedalken Aethermage`; `Watery Grave`.

### Cut 49 baseline cards

`Aether Channeler`; `Archaeomancer`; `Archmage of Echoes`; `Ashnod's Altar`; `Azami, Lady of Scrolls`; `Baral, Chief of Compliance`; `Blightstep Pathway // Searstep Pathway`; `Brainstorm`; `Chaos Warp`; `Clearwater Pathway // Murkwater Pathway`; `Cyclonic Rift`; `Deadly Rollick`; `Deflecting Swat`; `Displace`; `Dour Port-Mage`; `Dragonskull Summit`; `Drowned Catacomb`; `Dualcaster Mage`; `Fabled Passage`; `Fierce Guardianship`; `Force of Negation`; `Ghostly Flicker`; `Harmonic Prodigy`; `Haunted Ridge`; `Kess, Dissident Mage`; `Kindred Discovery`; `Luxury Suite`; `Molten Echoes`; `Naban, Dean of Iteration`; `Naru Meha, Master Wizard`; `Panharmonicon`; `Patron Wizard`; `Phyrexian Altar`; `Ponder`; `Preordain`; `Riptide Laboratory`; `Riverglide Pathway // Lavaglide Pathway`; `Shipwreck Marsh`; `Shivan Reef`; `Snapcaster Mage`; `Stonybrook Banneret`; `Stormcarved Coast`; `Sulfur Falls`; `Sulfurous Springs`; `Takenuma, Abandoned Mire`; `Talisman of Creativity`; `Training Center`; `Underground River`; `Xander's Lounge`.

### Added 49 cards

`Blood Pet`; `Hexing Squelcher`; `Hoarding Broodlord`; `Kefka, Court Mage // Kefka, Ruler of Ruin`; `Ragavan, Nimble Pilferer`; `Samut, Tyrant of Naktamun`; `Scholar of the Ages`; `Ad Nauseam`; `Borne Upon a Wind`; `Brain Freeze`; `Cabal Ritual`; `Chain of Vapor`; `Demonic Consultation`; `Essence Flux`; `Final Fortune`; `Intuition`; `Mental Misstep`; `Red Elemental Blast`; `Sacrifice`; `Saw in Half`; `Tainted Pact`; `Beseech the Mirror`; `Finale of Promise`; `Gamble`; `Lively Dirge`; `Rite of Flame`; `Unmarked Grave`; `Wheel of Fortune`; `Mox Opal`; `Wishclaw Talisman`; `Mystic Remora`; `Necropotence`; `Rhystic Study`; `Underworld Breach`; `Arid Mesa`; `Badlands`; `Cavern of Souls`; `City of Brass`; `City of Traitors`; `Exotic Orchard`; `Flooded Strand`; `Gemstone Caverns`; `Mana Confluence`; `Marsh Flats`; `Misty Rainforest`; `Underground Sea`; `Verdant Catacombs`; `Volcanic Island`; `Wooded Foothills`.

## Strategic effect of the rebuild

- **Spellseeker line completed:** `Finale of Promise` and `Scholar of the Ages` restore the core one-card Inalla engine.
- **Turbo density increased:** additional rituals, fast mana, low-cost tutors, and graveyard tutors move the deck to the speed required by its actual competitive ceiling.
- **Protection corrected for command-zone play:** protection no longer assumes Inalla has been cast. `Hexing Squelcher`, `Samut`, efficient stack interaction, and one-mana interaction protect proactive turns without making the commander a prerequisite for the protection spell to function.
- **Reanimator density increased:** `Unmarked Grave`, `Lively Dirge`, `Entomb`, `Reanimate`, `Persist`, `Animate Dead`, `Shallow Grave`, and `Apprentice Necromancer` support both Scholar and the alternate Wizard lines.
- **Backup wins added without replacing identity:** Oracle/Consultation/Pact and Breach/LED/Brain Freeze provide cEDH resilience, but the deck's most distinctive and highest-priority line remains Spellseeker + Inalla Eminence.
- **Mana base rebuilt for speed and Tainted Pact:** the candidate uses 27 unique land names and premium untapped fixing/acceleration, satisfying Tainted Pact's no-duplicate-name requirement across the entire 100-card candidate.

## Adversarial second pass

Current EDHREC cEDH evidence, recent tournament lists, and high-performing 2026 Inalla lists were compared against the candidate after the first rebuild.

### Serious challengers retained/rejected

- **Apprentice Necromancer — RETAINED.** It is less common than the aggregate's median creature package but appears repeatedly in successful 2026 tournament lists. More importantly, it is unusually commander-specific: an Inalla token copy has haste and can immediately use the Apprentice's tap ability. It survives the challenge over another generic wheel or value spell.
- **Thundertrap Trainer — REJECTED after direct comparison.** It is efficient and a recent runner-up list used it, but it supplies card selection rather than a deterministic Inalla line. The candidate's existing creature slots are either core combo pieces, high-leverage protection, acceleration, or alternate commander-dependent combo pieces. No cut produced a net commander-first improvement.
- **Spectral Arcanist — REJECTED.** Strong recursion synergy but four-mana setup and lower aggregate/tournament adoption make it weaker than the retained recursion/tutor core at the current slot pressure.
- **Corpse Dance / Dance of the Dead / Necromancy — REJECTED as additional redundancy.** All are defensible reanimation cards and recent tournament lists use some of them, but the candidate already has sufficient reanimation density. Adding more requires cutting interaction, acceleration, or a distinct deterministic route.
- **Orcish Bowmasters — REJECTED.** High standalone cEDH quality and present in the October 11 runner-up, but it neither advances the Spellseeker line nor becomes materially stronger because Inalla is the commander.
- **Valley Floodcaller — REJECTED.** Useful flash/untap utility, but less central than `Samut`/`Hexing Squelcher` as proactive-turn protection and less deterministic than the retained combo Wizards.
- **Micromancer — REJECTED.** Inalla can duplicate its ETB and a recent runner-up used it, but four mana plus an Eminence payment is materially slower than Spellseeker and the deck's direct tutors. It does not displace a core slot.
- **Pyroblast / Daze / Into the Flood Maw / Dispel — REJECTED as additional interaction.** All are credible cEDH options and several appear in current top-performing lists. The candidate already carries Force of Will, Pact, Offer, Flusterstorm, Mental Misstep, Swan Song, Red Elemental Blast, Chain of Vapor, and commander-specific protection bodies. Additional interaction would require removing acceleration or deterministic redundancy rather than a clearly inferior generic interaction slot.
- **Starting Town / Training Center / Forbidden Orchard / Phyrexian Tower — REJECTED after mana-base challenge.** Each is playable. The 27-land candidate already has 27 unique names, strong early untapped fixing, fetch/dual density, two basics, Cavern, Ancient Tomb, City of Traitors, Gemstone Caverns, and Tainted Pact compatibility. No single land challenger clearly dominates the chosen slot across early and late game states.
- **Generic Wizard-tribal value package — REJECTED.** `Panharmonicon`, `Molten Echoes`, `Naban`, `Archmage of Echoes`, `Kindred Discovery`, and similar cards increase Wizard value but are slower than the commander's actual cEDH combo ceiling and dilute the Spellseeker/reanimator plan.

## Rules checkpoints before formal gate

- Inalla's Eminence ability functions while she is in the command zone, so the deck does not need to cast its commander to use the copy engine.
- The Inalla-created token gains haste and is exiled at the beginning of the next end step; haste is relevant to `Apprentice Necromancer` token copies and to the arbitrarily large Scholar-token finish.
- The Scholar-based Spellseeker line depends on careful trigger ordering and holding priority around sacrifice spells, Finale of Promise, Entomb/Reanimate, and the Inalla triggers; this must be separately attested before approval.
- The Bloodline/Ruthless loop is commander-dependent and must be verified separately before approval.
- `Tainted Pact` is supported by 100 distinct card names in the candidate; the candidate contains no duplicated basic land name.
- `Samut, Tyrant of Naktamun` protects instant and sorcery spells via split second while it remains on the battlefield, but does not shut off triggered abilities or mana abilities and does not retroactively protect Samut while Samut itself is still on the stack.

## Closure

After the 49-card cEDH rebuild, a second serious pass compared the candidate against the October 11, 2026 Inalla runner-up, other high-performing 2026 tournament lists, current Inalla cEDH aggregate data, commander-specific combo references, alternative interaction suites, alternative Wizards, additional reanimation effects, and the mana base. The second pass produced **ZERO NEW MATERIAL IMPROVEMENTS** under the project's commander-first standard.

Candidate state before formal gate:
- 100 cards
- 100 distinct names
- 27 lands
- commander-first Eminence / Spellseeker / reanimator identity preserved
- natural ceiling: **Power Bracket 5 — cEDH**
- proposed Archidekt tags: **Spellseeker Combo / Reanimator / Turbo**
- no project legality exception expected

The candidate remains **NOT APPROVED** until the complete fail-closed Oracle/color-identity/legality/rules gate passes and the user explicitly approves the exact SHA-bound candidate.