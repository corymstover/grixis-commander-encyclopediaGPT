# Mishra, Eminent One — Current-Cycle Decision Closeout

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## Source reconciliation

The authoritative current FINAL TXT export contains exactly 100 cards / 100 distinct names / 34 lands. Raw FINAL TXT SHA-256: `0b33d376fc8cc82966b5004ae992ab19ffee8ebda69e710c61ac936be8696dd6`. Normalized current-cycle project-format baseline SHA-256: `831dbbdb0ba5006612205b961b513f477afa113a327b200dad5883dd962032f2`.

The project candidate-ranking file is stale against current FINAL membership for this commander: several cards ranked as candidates (including Cryogen Relic, Smelting Vat, Oni-Cult Anvil, and Esoteric Duplicator) are already present in the authoritative baseline. The FINAL export therefore controlled membership; candidate rankings were used only as research evidence.

## Commander blueprint and natural ceiling

Mishra is a noncreature-artifact copy commander. The optimized plan is to turn the beginning-of-combat Warform into repeated ETB/LTB value, temporary activated abilities, artifact sacrifice/tutor fuel, token multiplication, and commander-native combo finishes. High-value copy targets include Gonti's Aether Heart, Mindslaver, Coveted Jewel, Portal to Phyrexia, Spine of Ish Sah, Cryogen Relic, Ichor Wellspring, Lich's Relic, The Mightstone and Weakstone, Worldwalker Helm, and utility artifacts whose abilities can be used immediately because the Warform gains haste.

Natural ceiling: **Power Bracket 4 — Optimized**. A small self-tagged cEDH population exists, but current evidence does not justify replacing Mishra's five-mana combat engine with a generic Grixis Oracle/Breach shell merely to force a Bracket 5 label.

## Exact proposed changes

### Nonland
1. Brain Freeze -> Determined Iteration
2. Underworld Breach -> Machine God's Effigy
3. Mycosynth Wellspring -> Ichor Wellspring
4. Oni-Cult Anvil -> Master Transmuter
5. Servo Schematic -> Prized Statue
6. Fabricate -> Transmute Artifact
7. Time Sieve -> Lich's Relic
8. Mystical Tutor -> Nihil Spellbomb
9. Cloud Key -> Repurposing Bay
10. Gilded Lotus -> The Mightstone and Weakstone
11. Jhoira, Weatherlight Captain -> Uthros Research Craft

### Mana base
12. Blightstep Pathway // Searstep Pathway -> Badlands
13. Clearwater Pathway // Murkwater Pathway -> Flooded Strand
14. Riverglide Pathway // Lavaglide Pathway -> Misty Rainforest
15. Sokenzan, Crucible of Defiance -> Verdant Catacombs
16. Bojuka Bog -> Inventors' Fair

## Material decisions

- **Determined Iteration** is not merely token value. By ordering the beginning-of-combat triggers so Mishra resolves first, Iteration can populate the newly created Warform. With Gonti's Aether Heart this is a documented three-card infinite-turn loop, giving the deck another commander-native finish.
- **Machine God's Effigy** can preserve useful creature abilities on a noncreature artifact. Its copy modification is itself copiable, so Mishra can later copy the Effigy and create a hasty Warform carrying those abilities. Nonlegendary utility creatures such as Master Transmuter, Goblin Engineer, and Goblin Welder are especially attractive copy choices.
- **Ichor Wellspring** is premium Warform material: the normal Warform cycle draws on ETB and again when the token is sacrificed into the graveyard. Cryogen Relic remains as even stronger redundancy because it draws on entering or leaving.
- **Master Transmuter** converts temporary artifacts or expendable artifacts into expensive real artifacts from hand. Thousand-Year Elixir allows newly controlled Transmuter-style tap abilities to be used immediately.
- **Prized Statue** is a direct optimization over Servo Schematic: a normal Warform copy creates a Treasure on ETB and another when sacrificed into the graveyard, producing mana-flexible artifact tokens instead of Servos.
- **Transmute Artifact** is a material upgrade over Fabricate because it turns an expendable artifact into a selected artifact directly on the battlefield rather than merely tutoring to hand.
- **Lich's Relic** is a current Reality Fracture upgrade. Each Warform copy can pay {2} on entry to destroy up to one creature or planeswalker for each opponent, giving Mishra repeatable multiplayer board control from a one-mana artifact.
- **Nihil Spellbomb** replaces generic Mystical Tutor because the deck already has extensive tutoring. As a Warform target it can immediately sacrifice itself to clear a graveyard and can draw a card when the black payment is made. This preserves dedicated graveyard interaction while allowing Bojuka Bog to leave the mana base.
- **Repurposing Bay** converts temporary Warforms into real library artifacts. Warform retains the copied artifact's mana value, and the token survives through the postcombat main phase, so the Bay can sacrifice it at sorcery speed to tutor an artifact with mana value exactly one greater.
- **The Mightstone and Weakstone** replaces Gilded Lotus at the same mana value. The original supplies draw/removal plus two artifact-restricted mana; a Warform copy repeats the ETB mode and can immediately tap for two mana because it has haste.
- **Uthros Research Craft** is a current artifact-specific draw upgrade over Jhoira. Mishra's power 5 can station it above the 3-counter threshold in one activation; from there every artifact spell draws before that spell resolves, and the Craft is itself searchable/recurrable as an artifact.
- **Inventors' Fair** adds another artifact-specific tutor land. Badlands and three additional fetchlands improve untapped/fetchable Grixis fixing while keeping the deck at 34 lands.

## Retained commander-native packages

- **Mishra + Gonti's Aether Heart + Strionic Resonator**: infinite turns with {2} available each turn.
- **Mishra + Gonti's Aether Heart + Lithoform Engine**: infinite turns with {2} available each turn.
- **Mishra + Gonti's Aether Heart + Determined Iteration**: infinite turns.
- **Mishra + Urza, Lord High Artificer + Worldwalker Helm + Thousand-Year Elixir**: infinite artifact/creature tokens and infinite blue mana.
- **Mishra + Mindslaver + Strionic Resonator/Lithoform Engine**: repeatable opponent-turn control structures.
- **Mystic Forge + Sensei's Divining Top + Etherium Sculptor or Enthusiastic Mechanaut + Aetherflux Reservoir** remains a secondary artifact-combo finish.
- **Krark-Clan Ironworks + Scrap Trawler + Myr Retriever** remains the artifact recursion/sacrifice core.

## Red-team corrections and rejected challengers

- **Thousand-Year Elixir stays.** It is not merely generic haste/untap support; it is part of the Worldwalker Helm + Urza commander combo and also materially improves Master Transmuter.
- **Underworld Breach + Lotus Petal + Brain Freeze was verified as functional before being cut.** Breach and Brain Freeze are removed for identity reasons, not because the combo was incorrectly assumed to fail. Lotus Petal remains as efficient artifact fast mana.
- **Sundial of the Infinite** was rejected after review. It can exile Mishra's delayed sacrifice trigger and permanently retain a Warform, but it is lower-impact without the commander and competes with stronger engines that exploit the token immediately.
- **Idol of Oblivion** is efficient but redundant against Cryogen Relic, Ichor Wellspring, Coveted Jewel, Uthros Research Craft, The One Ring, Mystic Forge, Rhystic Study, and Mystic Remora.
- **Panharmonicon** can multiply ETB triggers, but Determined Iteration, Strionic Resonator, and Lithoform Engine interact with Mishra more broadly and occupy the higher-impact multiplication slots.
- **Audacious Reshapers** is strong but less deterministic than Arcum Dagsson, Transmute Artifact, Whir of Invention, Repurposing Bay, Goblin Engineer, Inventors' Fair, and the existing tutor suite.
- **Sculpting Steel** and **The Mycosynth Gardens** provide additional copy redundancy, but the final list already has Mishra, Machine God's Effigy, Brudiclad, Esoteric Duplicator, Worldwalker Helm, Determined Iteration, Strionic Resonator, and Lithoform Engine; neither displaced a stronger final slot.

## Whole-list closeout

- Current FINAL membership reconciliation: **COMPLETE**
- Mandatory 99-slot whole-list audit: **COMPLETE — 83 KEEP / 16 CUT**
- Candidate-ranking review: **COMPLETE; stale membership was not allowed to override FINAL**
- Current optimized Mishra evidence review: **COMPLETE**
- Commander-identity review: **PASS**
- Adversarial rules/combo red-team: **COMPLETE**
- Mana-base red-team: **PASS**
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**
- Exact candidate structure: **100 cards / 100 distinct names / 34 lands**
- Singleton compliance: **PASS**
- Commander color identity: **PASS — U/B/R only**
- Current Oracle/rules/combo verification: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE**

## Approval state

This exact SHA-bound candidate is **APPROVAL_READY — NOT APPROVED / NOT LOCKED**. It must not be marked approved or locked until the user explicitly approves it.
