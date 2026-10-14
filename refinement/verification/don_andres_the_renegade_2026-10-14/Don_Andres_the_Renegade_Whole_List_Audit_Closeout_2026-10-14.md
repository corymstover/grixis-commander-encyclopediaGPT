# Don Andres, the Renegade — Whole-List Audit Closeout

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Status:** **APPROVAL_READY — NOT APPROVED / NOT LOCKED**  
**Authoritative baseline SHA-256:** `9e739e8f463dadf07c2516195995583d21ae4cd987d1af6f0f4cd695fadf7c57`  
**Frozen October TXT source SHA-256:** `5013e0b0b035880e74f5395e55115a58eb3f60ad922cd4bd29670d5f45d0ed2e`  
**Approval candidate SHA-256:** `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`

## Whole-list audit closure

All 99 noncommander slots were challenged for mana efficiency, curve, ramp, card access, stack and permanent interaction, protection, recursion, theft density, Pirate support, Treasure conversion, finishers, commander-specific necessity, and realistic outside alternatives.

The audit identified three material upgrade clusters:

1. remove self-recursion and generic/symmetrical value slots that do not directly exploit Don Andres's controlled-but-not-owned / stolen-spell text;
2. add repeatable or high-density theft engines and a commander-specific trigger multiplier; and
3. upgrade avoidable tapped/check/slow lands without reducing functional color access.

## Final proposed 13-card delta

1. `Buried Alive` -> `Mana Drain`
2. `Cunning Rhetoric` -> `Roaming Throne`
3. `Living Death` -> `Thieving Amalgam`
4. `Revel in Riches` -> `Thieving Varmint`
5. `Share the Spoils` -> `Court of Locthwain`
6. `Victimize` -> `Decadent Dragon // Expensive Taste`
7. `The Ruinous Powers` -> `Wand of Wonder`
8. `Gonti, Lord of Luxury` -> `Black Cat, Cunning Thief`
9. `Zara, Renegade Recruiter` -> `Jhoira, Weatherlight Corsair`
10. `Crumbling Necropolis` -> `City of Brass`
11. `Drowned Catacomb` -> `Misty Rainforest`
12. `Haunted Ridge` -> `Marsh Flats`
13. `Stormcarved Coast` -> `Verdant Catacombs`

## Important retained decisions

- `Animate Dead` and `Reanimate` remain because both can target opponent-owned creatures in graveyards, creating exactly the sort of controlled-but-not-owned creature Don rewards.
- `Admiral Beckett Brass`, `Kindred Discovery`, `Malcolm, Keen-Eyed Navigator`, both Breeches, `Ramirez DePietro, Pillager`, and `Coercive Recruiter` remain because Don turns stolen creatures into Pirates and therefore directly increases their functional density.
- `Brainstealer Dragon`, `Etali, Primal Storm`, `Plargg and Nassari`, `Stolen Strategy`, `Tasha, the Witch Queen`, `Laughing Jasper Flint`, `Vaan, Street Thief`, `Locke, Treasure Hunter`, `Outrageous Robbery`, `Praetor's Grasp`, `Siphon Insight`, `Thief of Sanity`, `Dauthi Voidwalker`, `Hostage Taker`, `Hurl Through Hell`, `Arcane Heist`, and `You Find Some Prisoners` remain the stolen-card core.
- `Insurrection` remains the dedicated mass-theft finisher; Don turns the borrowed creatures into enlarged menace/deathtouch Pirates for the finishing combat step.

## Candidate exhaustion and red-team

The project top-100 candidate set was reviewed as discovery evidence rather than instructions. Additional current candidates and the five audit-snapshot-only cards were manually challenged against the list.

Close alternatives included `Mind's Dilation`, `Xanathar, Guild Kingpin`, `Mob Rule`, `The Beast, Deathless Prince`, `Staff of Eden, Vault's Key`, `Fallen Shinobi`, `Tinybones, the Pickpocket`, `Cruelclaw's Heist`, `Nightveil Specter`, `Agent of Treachery`, `Bribery`, `Captivating Crew`, `Memory Plunder`, and `Zealous Conscripts`.

None produced a superior net slot after curve, immediacy, repeatability, theft-zone breadth, Pirate interaction, and commander dependence were compared. A second serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

## Rules and legality closure

The SHA-bound rules attestation passes the material interactions, including:

- Don's static effect on opponent-owned creatures you control;
- separate Don triggers for stolen noncreature spells;
- Roaming Throne naming Pirate doubling Don's Treasure trigger but not his static effect;
- Thieving Amalgam manifests remaining opponent-owned and therefore receiving Don's creature bonuses;
- Court of Locthwain, Wand of Wonder, Expensive Taste, and Black Cat producing qualifying stolen casts/permanents;
- Jhoira putting historic permanents directly onto the battlefield rather than casting them;
- Admiral Beckett Brass, Kindred Discovery, and Coercive Recruiter correctly seeing Don-created Pirate types;
- Arcane Heist cipher copies not themselves triggering Don, while opponent-owned spells cast through Arcane Heist do; and
- Animate Dead/Reanimate on opposing graveyards producing controlled-but-not-owned creatures.

Official Commander legality attestation: **PASS**. No project exception is required.

## Complete gate

The fail-closed complete gate was run against the exact approval candidate and fresh current-cycle Oracle data.

- Cards: **100**
- Distinct names: **99** (only `Island` repeats)
- Commander color identity: **B/R/U**
- Singleton compliance: **PASS**
- Rules gate: **PASS**
- Official Commander legality gate: **PASS**
- Project exceptions: **none**
- Errors: **0**
- Overall result: **APPROVAL_READY**

## Power classification

**Bracket 4 — Optimized**  
Tags: **Theft / Pirates / Treasure**

No state or tracker lock mutation is authorized until explicit user approval of SHA `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`.
