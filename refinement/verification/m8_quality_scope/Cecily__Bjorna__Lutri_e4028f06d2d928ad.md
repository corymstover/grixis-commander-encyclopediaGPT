# M8 exact-current 98-main + partners + companion judgment — #8 Cecily / Bjorna / Lutri

2026-10-28. **KEEP Cory's specifically exception-authorized M7 Rev2 configuration without any changes.** Raw source `refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt`, SHA-256 `e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d`. **101 physical in the text** = **two commanders + 98 library cards + one separate companion**; 100 physical actual Commander deck. Exactly 100 distinct names / 100 rows, Island x2, no other name repeated. Bracket 4 — Spellslinger / Wheels / Hand Size Matters. Never collapse Lutri into the library, mistake it for a third commander, or silently remove owner-approved exceptions.

**Critical legality scope:** This is a **project-only** deck with explicit exceptions for *Trade Secrets* and *Yawgmoth's Bargain* (Commander-banned) and *Lutri, the Spellchaser* as companion (officially banned in Commander as companion). Those are not officially legal under ordinary sanctioned Commander. Any official-legal projection needs real replacement/companion removal and therefore is a different deck requiring Cory's direction; the exact approved encyclopedia entry is preserved. The Oct23 100-name selected Oracle file, 10 Game Changers and color identities are archived in `refinement/verification/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23_Verification.md`.

Provenance: [engineering PR #683](https://github.com/corymstover/GrokBotMTGCompanion/pull/683), head `1dc33504fc6c5d3c91b99c457d3a99ac0b9ddb96`, review `data/grixis/m7/decision_reviews/Cecily__Bjorna__Lutri_ChatGPT_M7_Rev2_Independent.md`, Git blob `95d8595f23ca031d9a18bfcbe96d14e74959656e`, [exact candidate CI #40051402695](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40051402695) SUCCESS. Earlier Grok M6 I/J belonged to its different first-pass byte source and is not recertified. No fresh full Spellbook/win-rate sample is asserted.

Commander-first goal: *Cecily* has maximum hand size 11 and, on **attack**, draws one and loses one life, **then** checks whether hand contains 11 or more cards. If yes, she may cast an instant or sorcery **from hand without paying mana cost**. Ten cards before resolving her trigger can be enough; she need not connect. *Bjorna* `{T}` + sacrificing a real artifact deals one damage to target creature and goads it; it is a tap/cost ability, so summoning sickness and valid creature target matter. Echo and Strionic Resonator copy the actual source ability/trigger but do not waive costs to activate them. *Lutri* is a separately paid special-action companion retrieval and a castable spell-copy creature under the **named project exception**, not a free outside-the-game spell.

## Two physically separate commanders; one physically separate companion (not library copies)

- **Commander:** 1x Bjorna, Nightfall Alchemist
- **Commander:** 1x Cecily, Haunted Mage
- **Companion outside deck:** 1x Lutri, the Spellchaser

The role ledger below enumerates precisely **98** library physical copies with quantity. The three role-zone lines above intentionally **do not** use the library `- 1x` syntax and are excluded from the library-multiset test.

### 33 printed lands; Sea Gate Restoration MDFC separately assessed as optional land

- 1x Blightstep Pathway // Searstep Pathway
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Bojuka Bog
- 1x Clearwater Pathway // Murkwater Pathway
- 1x Command Tower
- 1x City of Brass
- 1x Dragonskull Summit
- 1x Drowned Catacomb
- 1x Mana Confluence
- 1x Haunted Ridge
- 2x Island
- 1x Luxury Suite
- 1x Morphic Pool
- 1x Mountain
- 1x Otawara, Soaring City
- 1x Polluted Delta
- 1x Riverglide Pathway // Lavaglide Pathway
- 1x Scalding Tarn
- 1x Shipwreck Marsh
- 1x Shivan Reef
- 1x Sokenzan, Crucible of Defiance
- 1x Steam Vents
- 1x Stormcarved Coast
- 1x Sulfur Falls
- 1x Sulfurous Springs
- 1x Swamp
- 1x Takenuma, Abandoned Mire
- 1x Training Center
- 1x Underground River
- 1x Watery Grave
- 1x Xander's Lounge

City/Confluence replace Crumbling Necropolis and Fabled Passage to improve untapped UBR but consume life and remove a shuffle/fetch basic option. Pathways are not all color modes at once; Bojuka Bog and Xander's enter tapped. Thirty-three printed lands plus **one optional MDFC land face** and nine rocks support the partner/hand-value curve, but high eight-mana Augury, seven-mana Suspicion and large spells may be dead without Cecily attack permission. MDFC land face cannot be simultaneously counted as a cast instant/sorcery in the same zone/time; no false 34 basic-land claim.

### 9 reusable mana rocks and hand-size support

- 1x Arcane Signet
- 1x Dimir Signet
- 1x Izzet Signet
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence
- 1x Thought Vessel

Thought Vessel removes maximum hand size only while actually present, not Cecily's own fixed eleven otherwise; the two commanders still need color access. Losing Seething Song and Mana Geyser reduces one-turn red burst while upgrading free Swat/Mana Drain; cannot assert acceleration is unchanged merely because the land count is stable.

### 14 hand-size, attacking-trigger, copied-trigger and wheel-damage engines

- 1x Academy Manufactor
- 1x Archmage Emeritus
- 1x Echo, Perceptive Prodigy
- 1x Harmonic Prodigy
- 1x Niv-Mizzet, Parun
- 1x Psychosis Crawler
- 1x Strionic Resonator
- 1x Teferi's Ageless Insight
- 1x Triskaidekaphile
- 1x Twenty-Toed Toad
- 1x The One Ring
- 1x Rhystic Study
- 1x Mystic Remora
- 1x Notion Thief

Harmonic Prodigy sees the Wizard-qualified Cecily and Niv/Archmage triggers but isn't a universal all-card doubler. Resonator `{2},{T}` can copy Cecily's attack trigger; Echo can copy a permitted creature-source activated or triggered ability but has summoning-sickness limits when tapping. Twenty-Toed Toad's **twenty-card** winning check occurs on its attack trigger **resolution**: with both attacking, put Cecily's draw/freecast trigger above Toad to raise hand before the check. Toad doesn't win merely by attacking with 19 cards. Triskaidekaphile checks **exactly thirteen cards** at the proper upkeep; it conflicts with plans that move hand much higher. Peer/Crawler/Insight can convert draw to damage but draw exhaustion or life loss can kill us. Rhystic/Remora are conditional on opponent payments, and Notion Thief steals only qualifying opponent draw (not a guaranteed wheel lock).

### 10 real artifact creation, Bjorna feed and spellslinger payoffs

- 1x Big Score
- 1x Brass's Bounty
- 1x Deadly Dispute
- 1x Ichor Wellspring
- 1x Oni-Cult Anvil
- 1x Third Path Iconoclast
- 1x Storm-Kiln Artist
- 1x Cormela, Glamour Thief
- 1x Goblin Electromancer
- 1x Robe of the Archmagi

These roles are not interchangeable: Big Score needs a discard cost and creates two Treasures on actual resolution; Bounty's quantity scales with owned lands; Dispute sacrifices an artifact/creature as additional cost; Wellspring can replace itself through sacrifice; Oni-Cult Anvil uses a distinct exile-cost/token chain. Iconoclast makes 1/1 artifacts on **noncreature spell casts**, while Storm-Kiln makes Treasure on **instant/sorcery casts or copies**. Bjorna needs a spare artifact, a legal creature target and untapped/tap-legal body; a copy of Cecily's trigger doesn't make more Bjorna resources. Cormela produces restricted instant/sorcery mana, Electromancer reduces appropriate spell costs, Robe grants draw only when attack/combat damage conditions apply. Removing Emry, Goblin Engineer and Sai has a real artifact recursion/fodder cost; retained engines and the new attack-copy effects win the prioritized hand-size ceiling here.

### 16 direct interaction, actual safety and stack access

- 1x Chaos Warp
- 1x Counterspell
- 1x Cyclonic Rift
- 1x Deflecting Swat
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Hexing Squelcher
- 1x Lightning Greaves
- 1x Mana Drain
- 1x Toxic Deluge
- 1x Kess, Dissident Mage
- 1x Vampiric Tutor
- 1x Mystical Tutor
- 1x Demonic Tutor
- 1x Frantic Search
- 1x Brainstorm

Kess recasts only once on our turn from grave; it is not a free hand-cast Cecily spell. Hexing Squelcher can help spells resist countering but not Stifle on attack triggers; free Swat/Fierce require a commander, Mana Drain requires UU, Greaves shroud can stop our own targeting, and Deluge risks destroying both commanders. Bojuka Bog is counted once above as a land, not again here.

### 16 freecast finishers, wheels, selection and recursive spell lines

- 1x Apex of Power
- 1x Fevered Suspicion
- 1x Echo of Eons
- 1x In Garruk's Wake
- 1x Jeska's Will
- 1x Mnemonic Deluge
- 1x Peer into the Abyss
- 1x Reforge the Soul
- 1x Sea Gate Restoration // Sea Gate, Reborn
- 1x Underworld Breach
- 1x Wheel of Fortune
- 1x Aminatou's Augury
- 1x Whispering Madness
- 1x Windfall
- 1x Trade Secrets
- 1x Yawgmoth's Bargain

These are the true reason for maximizing Cecily attack-copy triggers. Fevered Suspicion's rebound happens only after a real **cast from hand**; copied spells have no rebound. Augury permits several spells across card types from top cards but costs eight mana if hand-cast normally. Sea Gate offers land versus high-MV draw/no-hand-size and cannot be both. Wheel of Fortune, Reforge, Windfall, Whispering and Echo refill but may *drop* Cecily's hand below eleven; Peer into the Abyss with Insight can overdraw and trigger deck-out, and is not automatically lethal without Crawler/life-resource setup. Trade Secrets/Bargain are useful high-lift sources precisely because of the documented **project exceptions**; they are not endorsed as officially legal inclusions. Underworld Breach has real escape fuel/exile, not free recursive wheel permission.

## M6 P0/P1 source-case disposition and project exception boundary

Original `data/grixis/m6/test_blueprints/Cecily__Bjorna__Lutri.json`: **six P0** `C1 C2 K1 K2 K3 F1` and **nine P1** `K4 K5 E1 E2 W1 W2 W3 F2 F3`, **15 original groups**. These are original conceptual cases, not current I/J pass labels. New bounded fixtures verify source identity, threshold/ordering, distinct costs and project-only legality; no full game-stack/Monte Carlo claim.

| Group | Exact current proposition | Adversarial limitation |
|---|---|---|
| **P0 C1** | Bjorna paid `{T}`/artifact-sac hits a legal creature and goads. | No untapped/summoning-safe Bjorna, artifact or legal target: no activation. |
| **P0 C2** | Cecily attack draws 1/loses 1 and checks 11 then casts from hand. | Destroyed/prevented attack or fewer than 10 pre-draw cards removes the freecast. |
| **P0 K1** | Real artifact sacrifice and 1 damage on resolution goad target. | Goad is not a targeted player hit and needs legal creature target. |
| **P0 K2** | Ten cards before one trigger draws to eleven, then can choose a legal hand spell. | No hand spell/empty library/ability stopped: no free cast. |
| **P0 K3** | Harmonic Prodigy adds a triggered ability on qualifying Wizard sources. | Without Prodigy or wrong subtype no double; copying a trigger ≠ casting a spell. |
| **P0 F1** | Greaves/ward/interaction may keep Cecily attacking. | Removal before declaration or unsafe combat prevents source attack line. |
| **P1 K4** | Triskaidekaphile precisely 13 at upkeep can win. | 12/14 cards or timing missed: no win. |
| **P1 K5** | Exactly three owner-authorized project exceptions are present in their correct zones. | Outside project, this is not officially Commander legal; never self-authorize a projection. |
| **P1 E1** | Cecily attacking plus copied triggers can freecast different legal hand spells sequentially. | Prior freecasts reduce hand size; no automatic multiple cast from empty hand. |
| **P1 E2** | Real Ring/Remora/Rhystic plus named exceptional draw can reach 11. | Opponent payments, life and library stock limit card accumulation. |
| **P1 W1** | Peer drawn cards trigger actual Psychosis Crawler, if it survives. | Empty library, absent Crawler or opponent prevention stops win claim. |
| **P1 W2** | Peer + Ageless Insight replacement can magnify drawn cards. | Draw greater than library or odd count can lose game; no guaranteed safety. |
| **P1 W3** | Breach/wheels/Jeska's Will are present as conditional recast mana plan. | Escape cards, red mana and turn timing matter; not a free self-feeding engine. |
| **P1 F2** | Wheels may replenish after hand depleted. | They can shrink hand below Cecily 11 and neutralize attack trigger. |
| **P1 F3** | The project exception is declared, not smuggled into legal Commander. | Removing two banned library cards/Lutri companion changes the exact approved build and its power. |

## Counterfactual complete-list adjudication

Ten approved swaps: Strionic/Emry, Echo/Goblin Engineer, Toad/Sai, Sea Gate/Dark Deal, Swat/Mana Geyser, Mana Drain/Seething Song, Fevered/Cruel Ultimatum, Augury/Wheel of Misfortune, City/Crumbling, Confluence/Fabled Passage. Real drawbacks: slower eight-mana payoffs in hand, lost ritual burst, another symmetric wheel and reduced artifact recovery. Serious full-list alternatives are (1) **restore two rituals over Swat/Mana Drain** for faster hand casting but lose premium protection as attack-trigger freecasts expose Cecily, (2) **restore Sai/Emry over Toad/Resonator** for artifacts but sacrifice 20-hand instant win and attack trigger density, (3) **restore Dark Deal/Wheel Misfortune over Sea Gate/Augury** to improve cheap wheels at cost of hand-size stall and Cecily freecast ceiling, and (4) **replace a weak color-producing land with Reliquary Tower/another optional hand-size engine**, sacrificing needed UBR pips and overlapping Cecily/Robe/Insight. Under the explicit exception-governed commander-first objective, current ten swaps are still preferred. **No new cut/add; no claim that this is officially Commander legal outside project or final M8 accepted.**
