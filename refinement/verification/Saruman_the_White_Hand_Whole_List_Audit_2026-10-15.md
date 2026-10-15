# Saruman, the White Hand — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #48 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Saruman__the_White_Hand.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Saruman_the_White_Hand_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `__CANDIDATE_SHA__`

## Audit result

- Commander: **Saruman, the White Hand**.
- Noncommander copies adjudicated: **99/99**.
- Result: **86 KEEP / 13 CUT**.
- Baseline: **100 cards / 94 distinct names / 34 front-face lands + Kazuul's Fury MDFC = 35 functional land-capable slots**.
- Candidate target: **100 cards / 97 distinct names / 31 front-face lands + four MDFCs = 35 functional land-capable slots**.
- Repeats target: **Island x2 / Mountain x2 / Swamp x2 only**.
- Singleton: **PASS target — only basic lands repeat**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Saruman_the_White_Hand_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final thirteen-card delta

1. Surrounded by Orcs -> Volcanic Salvo
2. Faithless Looting -> Treasure Cruise
3. Reanimate -> Force of Will
4. Fiery Inscription -> Soul's Fire
5. Crumbling Necropolis -> Volcanic Island
6. Drowned Catacomb -> City of Brass
7. Smoldering Marsh -> The Black Gate
8. Shivan Reef -> Flooded Strand
9. Sulfurous Springs -> Marsh Flats
10. Underground River -> Misty Rainforest
11. Island -> Sea Gate Restoration // Sea Gate, Reborn
12. Mountain -> Shatterskull Smashing // Shatterskull, the Hammer Pass
13. Swamp -> Sink into Stupor // Soporific Springs

## Commander-first findings

- **Volcanic Salvo** is a direct Saruman exploit: its mana value remains 12 even when its generic cost is heavily reduced, so a low-cost Salvo still creates an amass-12 trigger.
- **Treasure Cruise** similarly retains mana value 8 while delve can reduce actual payment to {U}.
- **Force of Will** retains mana value 5 under its alternate cost and protects the commander/closing turn.
- **Soul's Fire** converts the Army into direct damage without sacrificing it; Saruman's cast trigger resolves before Soul's Fire, increasing the Army before damage is determined.
- The three added spell/land MDFCs preserve land access while increasing the number of noncreature spells available to trigger Saruman.
- Fetchlands/premium fixing replace inherited lands that provide less sequencing, fixing, or commander-specific value.

## Source reconciliation

The inherited `deck_card_audit.csv` membership snapshot is stale for this deck and does not exactly match the authoritative FINAL TXT. The current audit therefore uses the FINAL TXT membership as decklist truth. Stale audit membership is not used to infer cuts or additions.

## Candidate exhaustion

Material challengers reviewed include Fling, Essence Harvest, Temporal Trespass, Storm of Saruman, Shark Typhoon, Uncover the Moon-Letters, Dreadhorde Invasion, March from the Black Gate, additional creature-based Orc/Goblin engines, Dark Ritual, Mana Sculpt, and commander-independent All Will Be One combo conversions. None produced a stronger commander-first final configuration than the candidate.

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
