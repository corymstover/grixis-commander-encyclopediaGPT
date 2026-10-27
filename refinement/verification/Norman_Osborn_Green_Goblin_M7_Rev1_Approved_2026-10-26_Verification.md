# Deck #43 — Norman Osborn // Green Goblin — M7 Rev1 approval and canonical-lock verification

Date: 2026-10-26 (America/Chicago)
Cycle: global-restart-2026-10-13
Status: **OWNER-APPROVED EXACT 100-CARD LIST; LOCK PENDING MERGE/POST-MERGE READBACK**
Power Bracket: **5 — cEDH**
Archidekt tags: **Mayhem / Graveyard Casting / Turbo Combo**

## Exact list, authority and preservation

- Canonical approved list: `refinement/decklists/Norman_Osborn_Green_Goblin_M7_Rev1_Approved_2026-10-26.txt`
- Exact raw UTF-8 LF SHA-256: `c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9`
- Exactly 100 lines with `1x`, commander first, **100 distinct card names**, zero companion, zero nonbasic duplicates, **23 lands**. Blue/black/red identity, no project-authorized exceptions.
- Historical exact approved Oct15 source preserved unchanged at `refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt` with raw SHA-256 `23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`.
- Prior Oct15 verification `refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md` and approval record `refinement/approvals/Norman_Osborn_Green_Goblin_Approved_2026-10-15.md` preserved.
- Canonical roster key `Goben__Gene_Splice_Savant` is the alternate printing of Norman Osborn // Green Goblin, not a new commander/63rd entry.
- Engineering PR #725: https://github.com/corymstover/GrokBotMTGCompanion/pull/725, merged commit `82d660f880dfe064f8007c26144f0e8d0d7851c7`, candidate commit `f98793c3673a8a99fcae394fb02885f3cb424a2d`.

## Five exact owner-approved changes

| Removed | Added | Commander-first benefit and cost |
|---|---|---|
| Yawgmoth's Will | Fervent Mastery | Tutor-three/random-discard-three opens fresh Mayhem casts; discounted mayhem from `3RR` to `1RR`. Loses Will's high-ceiling replay; random discard is not deterministic with extra cards in hand. |
| City of Traitors | Cephalid Coliseum | Blue land and threshold draw-three/discard-three. Trades two-colorless acceleration; activation needs threshold, a different U source and sacrifice. |
| Defense Grid | Samut, Tyrant of Naktamun | Grants our instants/sorceries split second on either turn. Does not directly protect Thassa's Oracle creature or Underworld Breach enchantment. |
| Demonic Counsel | Intuition | No-delirium triple-choice instant tutor for Breach/Oracle resources. Cards put into GY are not discarded/Mayhem eligible without later discard. |
| Will of the Jeskai | Inti, Seneschal of the Sun | Two-mana repeating attacking discard outlet and one impulse play per discard event. Loses the original spell's expensive wheel/flashback mode. |

## Actual mechanical, Oracle and legality evidence — boundaries

1. Exact physical 100/100 singleton structure and five 1:1 deltas were independently compared to `refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt`. Original 23-land count preserved.
2. The complete previous Oct15 baseline received a historical dedicated Oracle/Commander-legal audit; the five proposed additions were individually checked for Commander legality and UBR identity using public card-specific Scryfall evidence, plus official updated Commander banned-list checkpoint.
3. No fresh **100/100 live external Scryfall API scan** was run for this exact Rev1. Available local historical cross-deck Oracle snapshots cover **66/100**, with 34 unsupported by that *partial* local index; the prior whole-baseline audit is distinct, and those 34 are not independently certified anew by this local index. This must not be misrepresented as a new live 100-card audit.
4. `data/grixis/m7/norman_rev1/test_norman_rev1.py`: **12/12 targeted local tests PASS** for hash/structure, MDFC sorcery transform and colored cost, both command-zone cast faces/shared commander tax/Cavern Human, generic reductions and nonstacking alternative costs, Mayhem zone/timing, Necropotence/Yawgmoth's Will interactions, Intuition non-discard, Coliseum threshold/blue, Lion's Eye Diamond activation timing, Breach escape resource requirements, Samut/Inti scope and corrected source JSON/Markdown.
5. The previous generated Norman interaction documentation contained two rules errors. Engineering PR #725 versioned corrections establish that either MDFC creature face can be cast directly from the command zone and Cavern naming Human protects either actual cast creature spell; LED's instant-only timing prevents activation during another spell's cost-payment step. Full source-generator repro requires a locked historical bulk Oracle snapshot that was unavailable; generated files were patched with explicit tests, not claimed to have been fully regenerated.
6. Four **general engineering GitHub workflows on exact PR head `f98793c...` succeeded**, including the general M7 contract. They are not a Norman-specific full-live legality CI job; the 12 Norman-specific tests were run locally.
7. No randomized multiplayer endpoint, measured win-rate, universal M6/M7/M8 milestone acceptance, or unverified infinite/resource-positive combo line is asserted.

## Owner authorization and post-merge requirements

Cory expressly approved exact M7 Rev1 SHA-256 `c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9` and canonical locking. No repeat approval is needed. Before declaring LOCKED externally, confirm post-merge approved-list exact raw SHA matches, `state/current_deck_overrides.json` identifies `refinement/decklists/Norman_Osborn_Green_Goblin_M7_Rev1_Approved_2026-10-26.txt` as approved/locked, tracker index 42 (human Deck #43) carries that hash/date, prior Oct15 files still exist at unchanged hashes, and neighboring #42 remains canonical unchanged.

This versioned certification is for Deck #43 only. Next unlocked: **Deck #44 Obeka, Brute Chronologist**.
