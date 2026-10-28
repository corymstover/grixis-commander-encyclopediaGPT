# Owner approval — Deck #62 Zevlor, Elturel Exile M7 Rev1

Date: **2026-10-27 (America/Chicago)**  
Cycle: `global-restart-2026-10-13`  
Decision: **Cory explicitly approved** the exact complete 100-card six-swap Zevlor M7 Rev1 candidate, pinned to the raw SHA below, and authorized engineering CI and a narrowly scoped canonical lock after green verification.

## Owner's exact authorization

> Approve Deck #62 Zevlor M7 Rev1: the exact six swaps and complete 100-card list with SHA-256 071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f. Proceed with the required engineering CI and canonical lock.

That authorization applies **only** to this exact candidate. It is not consent to change any earlier deck, the October 15 Zevlor source, alternative eight-/nine-swap portfolios, or the project-wide historical test-governance manifest.

- Owner-approved exact raw UTF-8 candidate SHA-256: `071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f`.
- Canonical new approved artifact: `refinement/decklists/Zevlor_Elturel_Exile_M7_Rev1_Approved_2026-10-27.txt`; byte-identical to exact tested GrokBot candidate.
- Original approved/locked October 15 artifact **preserved unchanged**: `refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt`, SHA `d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9`.
- Structure: one Zevlor commander, 99 cards in library, 100 physical, 97 distinct names, Island/Mountain/Swamp ×2 only, 34 land cards; Grixis color identity and Commander legality in exact 2026-10-27 Scryfall snapshot.
- Natural ceiling: Bracket 4 — Optimized. Tags: Targeted Spells / Spell Copy / Theft-Control.

## Six exact approved replacements

| Cut from Oct15 | Approved addition | Real opportunity cost |
|---|---|---|
| Abrade | End of the Hunt | Loses instant artifact removal and precise burn for a copied highest-value exile edict |
| Terminate | Strategic Betrayal | Loses instant targeted creature removal for copied opponent-chosen exile and graveyard clearing |
| Gamble | Gifts Ungiven | Trades one-mana tutor for four-mana opponent-partitioned hand/graveyard construction |
| Dark Ritual | Rousing Refrain | Trades cheap black mana for high-ceiling copied hand-size red mana and suspend |
| Portent | Traumatic Critique | Trades one-blue topdeck manipulation for UR X-target card selection and possible damage |
| Counterspell | Cruelclaw's Heist | Loses an unconditional instant stack answer for copied sorcery hand exile |

## Bounded engineering success and limits

- [Engineering exact-source pull request #748](https://github.com/corymstover/GrokBotMTGCompanion/pull/748) **merged** to the M7 integration branch, tested original head `4145603e8a13c3470486f9663c15239f247ff3d6`, merge commit `ae45cb6c13797228df0c0f380a04d3dfe92f82a2`.
- [Dedicated GitHub Actions run #40629369955](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40629369955) **SUCCESS**: 23 source-bound bounded tests, all 16 original Zevlor M6 case IDs (5 P0 / 11 P1) scoped to exact M7 SHA, six addition checks, and structural/deckwide M7 gate.
- Engineering `data/grixis/m7/decision_reviews/Zevlor__Elturel_Exile_rev1.json`: eleven material card judgments, full physical 99-slot opportunity audit, two actual complete eight-/nine-swap source portfolios rejected on strategic role quality.
- Historical M6 I/J has only input attestation, with `phase_b_replayed:false`. New M7 case correspondence is not an invented historical Phase B replay, independent third-model rereview or comprehensive multiplayer rules simulation.
- **Canonical lock takes effect only after the canonical exact-head certification-transfer and owner-lock CI gates pass and the PR merges.** This document records exact owner consent and tested engineering provenance, not premature success of an unmerged branch.

All other 61 commander lists and approval states remain unchanged.
