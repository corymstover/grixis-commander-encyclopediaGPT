# Deck #29 Lord of Tresserhorn — M7 Rev1 whole-99 commander-first review

Date: 2026-10-25 America/Chicago. Exact approval candidate raw SHA-256: `fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85`.

## Scope and provenance
- Base: the October 14, 2026 approved canonical `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt` with original raw SHA `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`; preserved unchanged.
- Research: GrokBot PR #677, 15 material candidates, 12 complete 100-card configurations, source-bound Oracle/rules evidence, EDHREC general/optimized discovery, Commander Spellbook, bounded mechanics and seeded goldfish.
- Owner's new explicit approval: complete five-swap list and exact raw SHA as presented in conversation October 25. Research-only alternatives remain not approved.
- New exact candidate: `refinement/decklists/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.txt`.
- Whole-99: 35 land faces, 64 noncommander nonland physical cards, 98 distinct names, 3x Swamp only repeat, and one commander.

## Commander identity and reasoning
Lord of Tresserhorn is a 4-mana 10/4 Zombie. His triggered enters penalty loses 2 life, sacrifices two creatures and lets a target opponent draw two; his {B} regeneration protects only against destruction, never a sacrifice. The primary plan is suppress/counter/pay for that trigger, protect/evasion/haste Lord, and convert 10 power into lethal infect (Phyresis/Tainted Strike/Kediss/Chandra's Ignition) or 22 double-strike commander damage (Uncaged Fury). The second plan retains recursive Zombie fodder and sacrifice combo engines, including Gravecrawler, Altar, Rooftop Storm, Soultrader, Artist and Bombardment. This is commander-first Bracket 4 rather than a generic Grixis cEDH transformation.

## Exact five owner-approved swaps

| Add | Cut | Strategic gain and cost |
| --- | --- | --- |
| Fierce Guardianship | Stubborn Denial | Free protection while Lord is a battlefield commander; unavailable free when Lord is still a spell. Generic-staple overlap disclosed. |
| Consign to Memory | Feed the Swarm | One-blue counter to Lord’s enters trigger, but enchantment removal is reduced. |
| Black Market Connections | Cover of Darkness | Shapeshifter/changeling fodder plus Treasure/draw; costs life, comes online next main phase. |
| Ornithopter of Paradise | Fellwar Stone | Color-fixing creature doubles as Lord sacrifice fodder; summoning sickness costs immediate ramp. |
| Skullclamp | Sheoldred’s Edict | Repeatable draw off sacrificed creatures; loses an instant speed edict for untargetable threats. |

**Owner-history warning:** Stubborn Denial was an October14 owner ADD; the other four cuts were October14 audit KEEPs. Every cut was openly flagged before approval. The project owner approved all five together.

## Tested alternatives and risk disclosures
- Alternative four-swaps keeping the Edict, Skullclamp over Muddle, Skullclamp over Nightscape Familiar, Soul's Fire, Distortion Strike, and Aqueous Form were explored; no additional owner-approved swaps.
- Temur Battle Rage was a prior owner CUT and was **not** silently reintroduced.
- Spot removal falls from five to three named spells (Terminate, Deadly Rollick, Chaos Warp). Consign's replacement of Feed means Chaos Warp is the only permanent enchantment answer, with Otawara bounce as temporary interaction.
- Four-colorless general engine and generic staples were not indiscriminately added. Fierce Guardianship is broadly prevalent elsewhere in the encyclopedia, but has a specific zero-mana protection use.
- The 20,000-seed no-opponent turn-6 deployment proxy increases 0.6121 → 0.6613 and with free protection in hand increases 0.1208 → 0.1969; those are **not** multiplayer win rates.

## Rules and source-bound verification
- 100 physical / 98 unique / Swamp x3 only repeats / 35 lands / UBR identity / Commander legal in Oct23 source / three Game Changers (Demonic Tutor, Fierce Guardianship, Vampiric Tutor) / no exceptions.
- The named instant Consign to Memory counters the *trigger* while on stack, unlike a permanent suppression effect; Dress Down must be active when Lord enters.
- Regeneration does not replace sacrifice. Kediss deals noncombat damage to other opponents (infect carries if Lord has infect) and it is not commander combat damage.
- Uncaged Fury raises Lord to 11 power and grants double strike, dealing 22 commander damage if both hits connect; mere double strike on base 10 power deals 20, below lethal commander damage.
- Gravecrawler recursion requires a different Zombie present and a payable recast path; no unconditional zero-mana loop without its actual prerequisites.
- Tested at engineering PR #707 exact head `0d4c51d2c5756a0c6207fe4b5d47d4e8afdd0920`, separate from owner authority; 14 finite P0/P1 source-bound case fixtures, five P0 plus nine P1. Any broader M6 certification, multi-agent independence or actual multiplayer test is **not claimed**.

Power Bracket **4 — Optimized**. Archidekt tags **Infect / Voltron / Aristocrats**. All 61 other canonical decks are outside change scope.
