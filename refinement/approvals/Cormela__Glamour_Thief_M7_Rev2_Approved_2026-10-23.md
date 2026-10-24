# Cormela, Glamour Thief — M7 Rev2 six-swap owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED**, tracker deck #9/index 8, raw SHA-256 `d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd`.

## Exact owner authority

After ChatGPT presented the **full 100-card** Cormela M7 Rev2 six-swap list, Power Bracket 5/cEDH, Archidekt tags Storm / Aristocrats / Combo, source verification and engineering [PR #684](https://github.com/corymstover/GrokBotMTGCompanion/pull/684), and explicitly requested exact hash approval for canonical lock, Cory replied:

> Approve

This is owner consent only for Cormela Rev2 **exact raw d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd**, not a blanket approval of the M7 research backlog, not authority to reopen other new-cycle locked decks, and not acceptance of aggregated M6.10/M7/M8 completion.

## Historical and current provenance

- New approved artifact: `refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt`, exact raw SHA `d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd`.
- Original October 14 canonical approved list `refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt` raw `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b` preserved byte-for-byte. Registry key and tracker `deck_id` use **Cormela__Glamour_Thief** (double underscore), while historical/new canonical filenames use **Cormela_Glamour_Thief** (single underscore). Preserve that distinction without silent renaming.
- Engineering GrokBot first-pass [PR #657](https://github.com/corymstover/GrokBotMTGCompanion/pull/657) exact five-swap research raw `1cb098f4d1089f6989dfdb79b4abcd149000dfa5f90b923bda72ffa36aa2c8b1`, research-only and not canonical.
- ChatGPT independent [PR #684](https://github.com/corymstover/GrokBotMTGCompanion/pull/684) exact head `6a267c9f38f8e8d610e1ac8f2f7bc69dbe0bb56b`, candidate six swap including additional anti-hate slot; exact head [Actions run #40052202543](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40052202543) **SUCCESS** for eight new source-bound tests and inherited historical first-pass tests.
- Selected 2026-10-23 Scryfall Oracle IDs and text for all 100 names copied from archived 169-name first-pass source; current exact Scryfall evidence with **no banned/project-exception cards**, not newly fetched or mischaracterized as an independent third-model review.

## Six expressly approved one-for-one swaps

| Add | Remove | Main benefit and cost |
| --- | --- | --- |
| Mistrise Village | Undercity Sewers | Untapped with Mountain type, protects one key spell; lose Sewers surveil and black access. |
| Underground River | Exotic Orchard | Guaranteed untapped U/B; lose conditional red source, pay life on colored use. |
| Frantic Search | Faithless Looting | Converts Cormela's restricted spell-only UBR through land untap; lose cheap flashback looting. |
| Twinflame | Gitaxian Probe | Cormela legend-rule death recursion, infinite with Birgi and separate Dualcaster Mage loop; lose free peek/storm cantrip. |
| Hexing Squelcher | Red Elemental Blast | Our spell casts cannot be countered while it lives, ward other creatures; lose second cheap blue-specific answer. |
| Into the Flood Maw | Preordain | At {U}, answer any opposing nonland permanent if a tapped Fish gift was promised; loses one cheap sorcery cantrip and gives tapped 1/1 Fish to opponent. |

Into the Flood Maw is the independent post-floor improvement, specifically against Cursed Totem, Null Rod, Rule of Law and similar permanent hate. Its target changes under the promised-gift condition according to the actual Oracle text and Wizards Bloomburrow gift rules. Compared source-bound alternatives Snap/Abrade; neither matched both {U} cost and opposing artifact/enchantment/creature bounce breadth in the decisive win turn. Six reflects the quality-positive stopping point, **not** a cap or quota.

## Exact gate and bounded rules

- **Exactly 100 physical**, one Cormela commander, 99 library, 100 distinct singleton names, **30 lands, 13 mana artifacts, 20 unchanged Game Changers**, Commander color identity U/B/R, all names officially Commander `legal`, **zero project exceptions**. **Power Bracket 5 — cEDH**; tags **Storm / Aristocrats / Combo**.
- Cormela `{1}, {T}` for UBR is a haste-enabled mana ability; resulting UBR can pay only for instant and/or sorcery spells. It cannot pay for Hexing Squelcher, creature/artifact activations or Cormela's own `{1}` activation. Frantic Search untaps up to three lands but needs actually tapped lands to gain that mana. Her dies trigger can return an instant/sorcery already in the graveyard when it goes on the stack.
- Twinflame creates a hasty legendary copy. Legend rule sends one to graveyard; Cormela dies trigger can return previously resolved Twinflame. **Finite alone** (requires an extra unrestricted {1} per cast); with Birgi's red on spell casts infinite recasts/storm. Dualcaster Mage + Twinflame separately makes infinite hasty tokens. No unsupported Twinflame altar infinite.
- Hexing Squelcher protects spells, not activated/triggered abilities against Stifle effects and not prevention of casting. Mistrise Village needs Mountain/Forest to enter untapped and costs {U} plus tap to make next spell uncounterable.
- Into the Flood Maw targets an **opponent's** permanent, not your own; gifting a tapped Fish is necessary to target an opposing nonland artifact/enchantment. Fish token is a real cost; the effect is temporary bounce.
- Commander Spellbook first-pass included combos 23 → 25, all 25 preserved in six-swap (Preordain was not a listed combo piece). The database scan is not claimed as a fresh exhaustive search or executable win-rate test.
- No new formal sealed M6 I/J for changed six-swap list; first-pass I/J remains **five-swap scoped**. Selected snapshot/finite tests support this specific approval separately. Cory's Pass C owner-equivalent waiver remains **non-independent**. The eight previous M7 owner-approved locked lists, historical source exports and remaining roster deck records are unchanged.
