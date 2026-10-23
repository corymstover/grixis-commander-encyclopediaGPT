# Admiral Brass, Unsinkable M7 Rev3 — exact-source-bound owner approval verification

Date: 2026-10-23 (America/Chicago). Scope: exact Deck #3 M7 Rev3 and nothing else; aggregate M6.10/M7/M8 milestones remain separate.

## Byte authority and historical source integrity

1. Cory explicitly approved `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7` with instruction to canonical lock on October 23, 2026.
2. Frozen engineering Rev3 source: `corymstover/GrokBotMTGCompanion:data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable_ChatGPT_Rev3.txt` (PR #651, head `eb40e8e965c79762d9881b1a26dfd1289c49a5eb`).
3. The identical exact raw UTF-8 source copied without modification to `refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt`; SHA-256 `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`. The new canonical registry, tracker, and source-bound regression test must all agree.
4. Original Oct13 approved-source TXT preserved and measured raw SHA-256 `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc`. The older registry's historical digest `e66e3a59719401f41830e9938997a87a45a1b0dcaa0663b0ec7b44e10077dd39` does not match actual physical source; previous_approved_list_sha256 preserves the registry value, previous_approved_source_raw_sha256 preserves the measured physical file value. No silent rewrite, unverified equivalence or old Proposed_Final promotion.
5. Compared with the actual preserved Oct13 approved-source list, eight net card cuts/additions. Brass's Tunnel-Grinder long split-face printing is only name normalization, not a ninth physical change.

## Recount, rules and strategic evidence

- 100 physical cards / 97 distinct names / 1 commander in first row; Island x2, Mountain x2, Swamp x2; otherwise no duplicate nonbasics.
- 33 front-face land cards, eight mana rocks; color identity U/B/R, no Commander ban, no project-specific exception.
- Pirate-combat and Admiral reanimation identity preserved; Changeling Outcast retained for evasive Pirate support.
- Current Oracle/Scryfall research checked replacement identities and targeted interaction/legality. Faithless Looting's `{2}{R}` flashback retained; Ripples of Undeath mills three during precombat first main and may return a qualifying creature/enchantment to hand at life cost; unlike controlled Looting discard, the mill is random. Thassa's end-step exile/return blink resets a finality-counter-bearing creature as a new object when possible. Conjurer's Closet was compared rather than blindly added.
- 25 Rev3 source-bound focused regressions; [engineering Rev3 GitHub Actions SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659693); [original Rev2 focused SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659793); [M6 J provenance guard SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659744); [M7 decision contract SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40041659702). These are exact engineering PR-head scoped gates, not an aggregate full-repository pytest pass or a new strict Rev3 M6 I/J certification.
- Power Bracket 4 — Optimized; tags Pirates / Reanimator / Aggro.
- No representative controlled multi-player win-rate statistical claim.

## Canonical post-merge receipt

This record is created by a source-bound approval PR. The PR must pass its own exact-head tests before merge. After merge, independently re-fetch `main` and verify the raw file SHA-256 `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`, the registry row and tracker #3. The PR URL, merge SHA and checks provide the external merge receipt; do not preclaim them before completion.
