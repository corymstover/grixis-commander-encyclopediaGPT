# Anhelo, the Painter — explicit M7 Rev2 approval and canonical lock

Date: **2026-10-23** (America/Chicago)
Cycle: `global-restart-2026-10-13`
Owner: **Cory Stover**
Decision: **APPROVED / LOCKED**, exact Deck #4 ChatGPT independent M7 Rev2 candidate only.

## Exact owner authorization

> I explicitly approve and authorize canonical locking of Anhelo, the Painter M7 Rev2, exact 100-card raw SHA-256 865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77. Proceed with canonical verification, approval PR, merge, post-merge locking, and then Deck #5 Ashad.

This explicitly authorizes only the exact 100-card UTF-8 content matching raw SHA-256 `865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77`; no other list and no blanket M6.10/M7/M8 milestone approval.

- Approved new canonical source: `refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt`.
- Frozen engineering candidate: `corymstover/GrokBotMTGCompanion:data/grixis/m7/candidate_lists/Anhelo__the_Painter_ChatGPT_Rev2.txt` on [PR #652](https://github.com/corymstover/GrokBotMTGCompanion/pull/652), head `ceeda7b280f378a2f195fd15005268080f5cb09a`.
- Independent decision review: `data/grixis/m7/decision_reviews/Anhelo__the_Painter_ChatGPT_Rev2_independent_comparison.md`; direct focused regression `tests/test_m7_anhelo_chatgpt_rev2.py`.
- Original Oct13 physical approved file remains untouched: `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt`.

## Approved seven net one-for-one changes

| Add | Cut |
| --- | --- |
| Forsaken Miner | Primal Amulet // Primal Wellspring |
| Skyclave Shade | Talisman of Indulgence |
| Sinister Concierge | Fellwar Stone |
| Case of the Stashed Skeleton | Maestros Ascendancy |
| Fable of the Mirror-Breaker // Reflection of Kiki-Jiki | Lagomos, Hand of Hatred |
| City of Brass | Haunted Ridge |
| Misty Rainforest | Shipwreck Marsh |

The seven are not a presentation cap; they survived an independent comparison of the previous approved source, first-pass five swaps, higher-mana alternatives and open-ended challenger research. Core Anhelo casualty spell-copy/combo identity, Feed the Swarm enchantment removal, and static mana-source coverage are retained.

## Exact candidate and strategic verification

- **100 physical cards**, 94 distinct names, one commander first line; Islands, Mountains and Swamps three each, otherwise singleton.
- **34 physical front-face lands**, **seven mana rocks**; 41 static mana sources. Commander identity **U/B/R** and no designated project ban exception.
- **Seven** Game Changers; Power Bracket **4 — Optimized**.
- Archidekt tags **Spell Copy / Casualty Aristocrats / Spellslinger Combo**.
- Source-bound Oracle and rules analysis addressed Forsaken Miner's crime trigger when sacrificed while targeting, recurring casualty bodies, Sinister Concierge death/suspend, Case of the Stashed Skeleton, split-face Fable, and mana/cut tradeoffs.
- [Independent Rev2 focused workflow #40043498281](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498281), [original source-bound Anhelo workflow #40043498183](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498183), M6 J provenance guard #40043498257 and M7 decisive contract #40043498172 were green on engineering PR head `ceeda7b280f378a2f195fd15005268080f5cb09a`. This does **not** imply formal new Rev2 strict M6 I/J certification or complete historical test-suite success.

## Historical approval provenance exception — preserved

The Oct13 canonical registry stored `d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e`, but the immutable originally approved-source TXT's actual raw SHA-256 is `8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972`. Both are retained in separate state fields and source file bytes preserved. They are **not** silently reconciled, nor is the old digest asserted to be the file's raw hash.

## Post-merge receipt

Merge this PR only after exact-head canonical CI passes. Re-fetch canonical `main` after merging; independently hash the approved list and compare state/tracker. PR number, merge SHA and Actions serve as the later externally verifiable receipt. This approval is scoped to Deck #4; first three M7 locks remain unchanged.
