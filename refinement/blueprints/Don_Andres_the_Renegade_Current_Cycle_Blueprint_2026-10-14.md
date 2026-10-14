# Don Andres, the Renegade — Current-Cycle Commander-First Blueprint

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Deck:** #14 / `Don_Andres__the_Renegade`  
**Authoritative baseline:** `refinement/decklists/Don_Andres_the_Renegade_Current_Cycle_Baseline_2026-10-14.txt`  
**Standardized baseline SHA-256:** `9e739e8f463dadf07c2516195995583d21ae4cd987d1af6f0f4cd695fadf7c57`  
**Frozen October TXT source SHA-256:** `5013e0b0b035880e74f5395e55115a58eb3f60ad922cd4bd29670d5f45d0ed2e`

## Commander identity

Current Oracle text:

> Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.
> Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.

Don Andres therefore has two linked theft axes:

1. **Stolen creatures** — creatures taken by control-changing effects, reanimated from opponents' graveyards, put directly onto the battlefield from opponents' zones, or cast from opponents' cards remain owned by the opponent. Don turns them into enlarged menace/deathtouch Pirates.
2. **Stolen noncreature spells** — casting opponents' instants, sorceries, artifacts, enchantments, planeswalkers, or battles triggers Don and creates two tapped Treasures.

The strongest deck therefore repeatedly accesses opponents' cards while exploiting the Pirate type Don grants to stolen creatures. Pure self-recursion, generic treasure production, and generic Grixis value are secondary unless they materially support those two axes.

## Primary game plan

1. Establish Don and efficient mana.
2. Generate cards from opponents' libraries, hands, graveyards, or permanents through Ragavan, Breeches, Grenzo, Vaan, Locke, Thief of Sanity, Laughing Jasper Flint, Praetor's Grasp, Siphon Insight, Outrageous Robbery, Hostage Taker, Dauthi Voidwalker, Arcane Heist, Court of Locthwain, Black Cat, Wand of Wonder, Decadent Dragon, and related engines.
3. Convert stolen creature permanents into oversized menace/deathtouch Pirates; leverage Malcolm, Admiral Beckett Brass, Kindred Discovery, Coercive Recruiter, Breeches, Ramirez, and other Pirate triggers around them.
4. Convert stolen noncreature casts into large Treasure bursts. Roaming Throne naming Pirate doubles Don's Treasure trigger and also amplifies many Pirate triggers.
5. Close through a snowballing stolen board, permanent theft from Admiral Beckett Brass, repeated theft engines, or Insurrection as the dedicated mass-theft finisher.

## Natural power ceiling

**Bracket 4 — Optimized.** Don produces substantial mana and combat pressure from theft but is dependent on opponents' card quality and does not naturally support a compact cEDH win package. Optimization therefore focuses on resilient, repeatable theft, efficient interaction, and high-quality mana without replacing the deck with unrelated Grixis combo lines.

## Source discrepancy resolved

The authoritative October CSV/TXT exports agree and are the baseline. `deck_card_audit.csv` contains a different five-card snapshot: it includes `Agent of Treachery`, `Bribery`, `Captivating Crew`, `Memory Plunder`, and `Zealous Conscripts` where the authoritative exports instead contain `Arcane Heist`, `Locke, Treasure Hunter`, `Seize the Spotlight`, `Share the Spoils`, and `You Find Some Prisoners`.

The current refinement preserves CSV/TXT authority and manually evaluates all five audit-only cards. No research-pipeline rerun is required.
