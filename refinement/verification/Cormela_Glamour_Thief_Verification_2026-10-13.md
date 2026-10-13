# Cormela, Glamour Thief — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Addition: Galvanic Iteration.
- Cut: Grapeshot.
- Final list: 100 copies, 100 distinct card names, 30 lands; no duplicates. Commander is first line.
- Revised TXT SHA-256: `cb81718ff186d28f97bc17ce1c9ce880e02a8a90e96df8c539cfbc05beb2fe75`.
- Baseline raw CSV SHA-256: `0780ccdcace7e54df75ddf15d02e9d4368e3d102ef7a1eb3c7123d9bb9479703`.
- Baseline raw TXT SHA-256: `10639176c36a7a55853cd1c65f22ac31e22b99dd15d7e95607b1d03acb74babd`.
- Normalized baseline-name SHA-256: `949ad1d40e2af9af6c17d487f05c046c67232dd2b347e1670ce9f6e020521615`.

## Commander-first plan

Cormela’s haste, spell-only UBR-only mana ability, and death trigger returning an instant or sorcery form a compact graveyard-enabled spell-combo engine. The baseline already contains multiple efficient rituals, tutors, protection spells, recursion, and storm payoffs. This is a narrow adjustment rather than a rebuild.

## Change rationale and rules

Galvanic Iteration costs {U}{R} and creates a delayed trigger to copy the next instant or sorcery cast that turn; it has flashback {1}{U}{R}. It can copy Brain Freeze or a high-impact ritual/tutor. The copy is not cast and therefore does not itself increase storm count. If Galvanic Iteration is still in the graveyard when Cormela’s death trigger resolves, Cormela can return it to hand; after flashback, it is exiled. Grapeshot deals 1 damage to any target and has storm. Cutting it reduces redundant direct-damage finishing/removal, while Brain Freeze and Tendrils of Agony remain.

Direct current Oracle and legality references: [Galvanic Iteration](https://mtg.wtf/card/msc/184/Galvanic-Iteration), [Grapeshot](https://mtg.wtf/card/msc/803/Grapeshot), [Cormela](https://mtg.wtf/card/snc/301/Cormela-Glamour-Thief). Cormela is Commander-legal and has UBR identity. Galvanic Iteration and Grapeshot are Commander-legal and fit the commander identity. The official Commander ban list was checked 2026-10-13; no final-list card is newly banned. No project exception applies.

## Structural and metadata checks

- Final TXT: 100 lines, one copy per line, commander on line one.
- Final CSV: 100 rows, quantity total 100, all card names unique.
- Color identity: all final cards are within UBR; baseline list was covered by the project’s refreshed Scryfall metadata report generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z, reported 5,964/5,964 exact printing/name matches.
- Official legality: current official Commander ban list checked 2026-10-13; no project exception.
- Candidate review: 16 candidates assessed, one accepted and 15 rejected with reasons.
- Consistency review: tutors, rituals, interaction, graveyard recursion, storm finishers and 30-land count assessed. No numerical goldfish or matched-seed multiplayer test was run; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock this list in the new cycle; frozen baseline exports remain immutable.
