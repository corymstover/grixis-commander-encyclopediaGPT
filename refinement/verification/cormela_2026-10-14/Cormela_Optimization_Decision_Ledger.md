# Cormela, Glamour Thief — optimization decision ledger

**Cycle date:** 2026-10-14  
**Authoritative baseline:** `refinement/decklists/Cormela_Glamour_Thief_Current_Cycle_Baseline_2026-10-14.txt`  
**Baseline clean SHA-256:** `7f541e2146c5d83f4415a01026af3b61767bec10fa13762fb95c47d1ac62d95f`  
**Frozen source-member SHA-256:** `10639176c36a7a55853cd1c65f22ac31e22b99dd15d7e95607b1d03acb74babd`  
**Approval candidate:** `refinement/decklists/Cormela_Glamour_Thief_Approval_Candidate_2026-10-14.txt`  
**Candidate SHA-256:** `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b`

## Blueprint

Cormela is treated at her natural **cEDH ceiling**: a Grixis instant/sorcery combo commander whose haste and restricted UBR ritual ability help assemble and pay for spell loops, while her death trigger converts sacrifice, cloning, and reanimation effects into deterministic recursion engines. The primary identity package remains Cormela + Saw in Half / reanimation + sacrifice-mana effects. Compact Grixis cEDH wins and premium stack interaction are allowed as secondary/failover packages, but the deck is not reduced to a generic commander-agnostic Thoracle shell.

Primary wins retained or strengthened:
- Cormela + Saw in Half recursion loops using mana-positive rituals.
- Cormela + Goryo's Vengeance or Shallow Grave + Ashnod's Altar / Phyrexian Altar loops.
- Cormela + Birgi + Molten Duplication loop.
- Dualcaster Mage + Molten Duplication token loop.
- Underworld Breach / Brain Freeze spell-combo lines.
- Tendrils of Agony as a storm payoff.
- Thassa's Oracle + Demonic Consultation or Tainted Pact as compact cEDH failover.

## Accepted swaps

| # | Cut | Add | Decision rationale |
|---:|---|---|---|
| 1 | Footsteps of the Goryo | Goryo's Vengeance | Same commander-recursion role but instant speed and one mana cheaper. Cormela is legendary; Commander Spellbook indexes deterministic Cormela + Goryo + altar loops. |
| 2 | Goblin Electromancer | Demonic Consultation | Electromancer is a slow exposed cost reducer. Consultation adds a one-mana tutor/exile effect and forms a compact deterministic win with Thassa's Oracle. |
| 3 | Grapeshot | Pyroblast | Grapeshot is redundant with Brain Freeze/Tendrils and deterministic loop payoffs. Pyroblast materially improves stack interaction against blue decks and protects combo attempts. |
| 4 | Mana Drain | Mindbreak Trap | Mana Drain is strong but UU and reactive at two mana; Mindbreak Trap is premium cEDH stack interaction that can answer uncounterable/stacked spell sequences and can be free in contested turns. |
| 5 | Mizzix's Mastery | Rite of Flame | Mastery is high-ceiling but four mana and graveyard-dependent. Rite is one-mana acceleration that directly improves Cormela/combo speed and storm count. |
| 6 | Mox Amber | Arcane Signet | Amber is unreliable before Cormela/another legend resolves. Signet always fixes all three colors and advances the commander from an empty board. |
| 7 | Nightscape Familiar | Thassa's Oracle | Familiar is a vulnerable two-mana reducer with limited impact. Oracle adds a compact secondary win that materially raises the deck's resilience and ceiling. |
| 8 | Presumed Dead | Shallow Grave | Presumed Dead returns the creature tapped, which conflicts with immediately reusing Cormela's tap ability in recursion loops. Shallow Grave returns the top creature card with haste and is independently indexed in deterministic Cormela + altar loops. |
| 9 | Storm-Kiln Artist | Tainted Pact | Artist is a four-mana engine and therefore slow at cEDH speed. Pact is instant-speed selection and, because the candidate has no repeated card names, forms a compact Oracle win. |
| 10 | Twinflame | Molten Duplication | Both support Dualcaster loops; Molten Duplication also directly copies Cormela and forms a commander-specific loop with Birgi, increasing identity density. |
| 11 | Viscera Seer | Orcish Bowmasters | Seer is a free sac outlet but does not generate mana, while the deck retains Ashnod's/Phyrexian Altar and Phyrexian Tower. Bowmasters is premium low-cost interaction against draw engines and creates useful sacrifice bodies. |
| 12 | Goblin Bombardment | Wishclaw Talisman | Bombardment is another non-mana sacrifice outlet and is redundant with stronger commander-loop outlets. Wishclaw is an efficient universal tutor that improves access to both Cormela engines and failover wins. |
| 13 | Urborg, Tomb of Yawgmoth | Phyrexian Tower | Urborg provides limited marginal fixing in a three-color fetch/dual manabase. Tower is an untapped land plus commander-aligned sacrifice outlet and burst black mana. |
| 14 | Xander's Lounge | Flooded Strand | The triome is always tapped and the candidate does not need cycling enough to justify the tempo loss. Flooded Strand fetches blue duals/Undercity Sewers and improves untapped-source density. |

## Strong retained cards / rejected cuts

- **Saw in Half:** indispensable commander-specific engine; retained despite being narrower than generic cEDH interaction.
- **Demonic Gifts:** retained because it directly enables Cormela altar loops and reinforces the commander-first identity.
- **Ashnod's Altar / Phyrexian Altar:** retained as mana-producing sacrifice outlets central to deterministic Cormela loops.
- **Birgi, God of Storytelling:** retained for spell-chain efficiency and the Cormela + Molten Duplication loop.
- **Dualcaster Mage:** retained because Molten Duplication preserves a compact independent win line while Molten also serves Cormela directly.
- **Tendrils of Agony:** retained as an identity-consistent storm payoff even though Brain Freeze/Breach and Oracle lines exist.
- **Demonic Gifts over additional generic tutor/interaction:** retained because removing it would materially erode Cormela-specific recursion density for only a marginal generic-power gain.

## Evidence boundary

Current Oracle identity/color/Commander-legality evidence is supplied by the GitHub-produced current-cycle Scryfall cache. Official format legality is independently reconciled to Wizards' current Commander banned list. Nontrivial combo functionality is separately attested against current Oracle records, the September 25, 2026 Comprehensive Rules, and Commander Spellbook as a discovery/cross-check source. Popularity/inclusion data is observational only and is not used as proof of card power.

No claim is made that simulation proves universal superiority. The decision is based on commander-specific role fit, cEDH opportunity cost, current rules/legality, and removal of slower or redundant pieces while preserving the commander's defining engines.
