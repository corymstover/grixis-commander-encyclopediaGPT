# Don Andres, the Renegade — Current-Cycle Refinement Decision Record

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Status:** working approval candidate; explicit user approval still required  
**Baseline SHA-256:** `9e739e8f463dadf07c2516195995583d21ae4cd987d1af6f0f4cd695fadf7c57`  
**Candidate SHA-256:** `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`

## Mandatory whole-list audit

All 99 noncommander slots were challenged for mana efficiency, ramp, draw, interaction, protection, recursion, theft density, Pirate synergies, finishers, commander-specific payoffs, and high-impact alternatives.

The baseline has ample mana acceleration and card access but three structural weaknesses:

1. a small self-recursion package (`Buried Alive`, `Living Death`, `Victimize`) that does not itself steal opponents' cards and became increasingly redundant once the strongest theft engines were compared slot-for-slot;
2. several slow or symmetrical value cards (`Cunning Rhetoric`, `Share the Spoils`, `The Ruinous Powers`, `Revel in Riches`) that are less reliable than proactive theft engines; and
3. four avoidable slow/check lands in a no-budget three-color optimized mana base.

The deck keeps `Animate Dead` and `Reanimate` because both can target opposing graveyards, creating creatures Don controls but does not own. It keeps the commander-specific Pirate package and the mass-theft finisher `Insurrection`.

## Proposed changes

| OUT | IN | Decision rationale |
|---|---|---|
| Buried Alive | Mana Drain | Buried Alive only sets up the deck's own graveyard and loses value after the weakest self-recursion cards are removed. Mana Drain repairs the stack-interaction gap while producing mana for the deck's expensive theft engines. |
| Cunning Rhetoric | Roaming Throne | Rhetoric is reactive and opponent-dependent. Throne naming Pirate doubles Don's Treasure trigger and also doubles many Pirate triggers from Admiral Beckett Brass, Malcolm, Breeches, Ramirez, and others. |
| Living Death | Thieving Amalgam | Living Death is symmetrical recursion. Amalgam directly steals the top card of every opponent's library as a manifested creature each round; those face-down creatures are controlled but not owned, so Don turns them into 4/4 menace/deathtouch Pirates while he remains in play. |
| Revel in Riches | Thieving Varmint | Revel is a five-mana delayed Treasure payoff. Varmint is a two-mana, two-mana-per-turn accelerator specifically for casting spells you don't own, which directly advances Don's stolen-spell engine. |
| Share the Spoils | Court of Locthwain | Share is symmetrical and opponents can consume the shared exile pool. Court repeatedly targets an opponent's library, grants durable permission, supplies monarch draw, fixes mana for the stolen card, and can cast a stolen spell for free while you are monarch. |
| Victimize | Decadent Dragon // Expensive Taste | Victimize only returns your own creatures and needs a sacrifice. Expensive Taste permanently banks two cards from an opponent's library; stolen creatures become Don-buffed Pirates and stolen noncreatures trigger Don. The Dragon side then supplies an evasive Treasure-producing body. |
| The Ruinous Powers | Wand of Wonder | Ruinous Powers offers one random paid card per upkeep. Wand can cast one to three opponents' instants/sorceries for free per activation, so every spell is eligible to trigger Don and generate Treasure. |
| Gonti, Lord of Luxury | Black Cat, Cunning Thief | Black Cat costs one more mana but examines nine cards, banks two face-down cards indefinitely, and fixes mana for both. It is a material upgrade in selection and stolen-card volume over Gonti's one-of-four selection. |
| Zara, Renegade Recruiter | Jhoira, Weatherlight Corsair | Zara temporarily borrows one creature from a defending player's hand after attacking. Jhoira steals a historic permanent on entry and every attack, keeps it permanently, and is itself a Pirate. Stolen creatures immediately receive Don's static bonuses. |
| Crumbling Necropolis | City of Brass | Removes an unconditional tapped land for unconditional untapped Grixis fixing. |
| Drowned Catacomb | Misty Rainforest | Fetches the deck's Island-typed duals/shocks/triome and removes check-land sequencing risk. |
| Haunted Ridge | Marsh Flats | Fetches the deck's Swamp-typed duals/shocks/triome and removes slow-land sequencing risk. |
| Stormcarved Coast | Verdant Catacombs | Fetches the deck's Swamp-typed duals/shocks/triome and removes slow-land sequencing risk. |

## Important retained cards

- `Admiral Beckett Brass` is unusually commander-specific here: Don makes stolen creatures Pirates, helping satisfy the three-Pirate combat requirement and then permanently stealing another nonland permanent.
- `Kindred Discovery`, `Malcolm, Keen-Eyed Navigator`, `Breeches, Brazen Plunderer`, `Breeches, Eager Pillager`, `Ramirez DePietro, Pillager`, and `Coercive Recruiter` all gain value from Don turning controlled-but-not-owned creatures into Pirates.
- `Animate Dead` and `Reanimate` remain because they can take creatures from opponents' graveyards, unlike `Victimize`.
- `Brainstealer Dragon`, `Etali, Primal Storm`, `Plargg and Nassari`, `Stolen Strategy`, `Tasha, the Witch Queen`, `Laughing Jasper Flint`, `Vaan, Street Thief`, `Locke, Treasure Hunter`, `Outrageous Robbery`, `Praetor's Grasp`, `Siphon Insight`, `Thief of Sanity`, `Dauthi Voidwalker`, `Hostage Taker`, `Hurl Through Hell`, `Arcane Heist`, and `You Find Some Prisoners` remain as the core stolen-card engine.
- `Insurrection` remains the dedicated mass-theft finisher: Don turns the stolen creatures into larger menace/deathtouch Pirates for the lethal combat step.

## Candidate exhaustion / red-team review

The top-100 project ranking was reviewed as discovery evidence, not as an automatic prescription. High-ranked challengers included `Mind's Dilation`, `Xanathar, Guild Kingpin`, `Mob Rule`, `The Beast, Deathless Prince`, `Staff of Eden, Vault's Key`, `Thieving Amalgam`, `Wand of Wonder`, `Court of Locthwain`, `Thieving Varmint`, `Decadent Dragon // Expensive Taste`, `Fallen Shinobi`, `Tinybones, the Pickpocket`, `Cruelclaw's Heist`, and `Nightveil Specter`.

The five audit-only discrepancy cards were also manually reviewed: `Agent of Treachery`, `Bribery`, `Captivating Crew`, `Memory Plunder`, and `Zealous Conscripts`.

The closest rejected alternatives were:

- `Mind's Dilation` — extremely powerful, but seven mana with no immediate board effect; the high-end is already occupied by Brainstealer Dragon, Thieving Amalgam, Etali, and Insurrection, while Court/Wand provide cheaper repeated stolen casting.
- `Xanathar, Guild Kingpin` — strong but six mana and delayed until upkeep; the selected package produces more immediate and/or lower-cost stolen-card access.
- `Agent of Treachery` — excellent seven-mana theft, but Jhoira and Thieving Amalgam provide repeatable theft at the same high-end slot pressure.
- `Bribery` — strong guaranteed creature theft, but one-shot at five mana and narrower than the selected repeatable multi-zone engines.
- `Captivating Crew` — repeatable temporary theft but requires four additional mana per activation; Coercive Recruiter and the existing Pirate shell perform the temporary-theft role more efficiently.
- `Memory Plunder` — directly synergistic but substantially overlaps Arcane Heist and Dire Fleet Daredevil.
- `Black Cat, Cunning Thief` and `Jhoira, Weatherlight Corsair` were promoted despite not being top-ranked by the older candidate snapshot because current card text and recent optimized Don evidence show materially stronger theft functions.

A second serious pass produced **zero new material improvements**.

## External evidence checkpoint

Current EDHREC optimized Don data supports the retained core (Hostage Taker, Ramirez, Malcolm, Ragavan, Etali, Thief of Sanity, Laughing Jasper Flint, Breeches) and shows strong optimized adoption/synergy for Court of Locthwain and Wand of Wonder. Current optimized lists also use Black Cat and the newly released Jhoira in theft-focused builds. This evidence corroborates the slot analysis but does not substitute for it.

## Power classification

**Bracket 4 — Optimized**  
Proposed tags: **Theft / Pirates / Treasure**
