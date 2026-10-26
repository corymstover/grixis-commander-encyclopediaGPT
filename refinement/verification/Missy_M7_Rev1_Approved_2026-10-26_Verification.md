# Deck #38 Missy — M7 Rev1 Exact-List Verification

**Owner-approved raw SHA-256:** `f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d`  
**Artifact:** `refinement/decklists/Missy_M7_Rev1_Approved_2026-10-26.txt`  
**Date:** 2026-10-26 (America/Chicago).

## Card-level and deck-level gates

| Check | Result |
| --- | --- |
| Total physical cards, commander included | **100 — PASS** |
| Distinct card names | **97 — PASS** |
| Basic lands | Island x2, Swamp x3; all nonbasics/nonbasic cards singleton |
| Land count | **35** |
| Commander and color identity | Missy; U/B/R, no out-of-identity cards — PASS |
| Current Scryfall Oracle/legality snapshot | **97/97 names resolved**, current official Commander legality PASS |
| Project exceptions | None |
| Exact list vs reviewed candidate | SHA-bound unchanged — PASS |
| Natural strategy | Missy morph reuse / Cyberman ETBs / sacrifice-aristocrats / villainous choices |
| Power | Bracket 4 — Optimized |

## Rules and strategic boundaries

- Missy converts an eligible **nonartifact creature** dying into a face-down tapped 2/2 Cyberman artifact. Printed morph bodies returning this way may later turn face up; after turning face up, they cease to be artifacts unless another effect applies, enabling repeated sacrifice/death loops with the commander present.
- Altar of the Brood mills on Cyberman artifact entries, including zero-power morph creatures that would not mill via Altar of Dementia's power-counted sacrifice ability.
- Yawgmoth, Thran Physician's activated sacrifice mode requires life payment and a legal target as appropriate. Carrion Feeder, the Altars, and Viscera Seer provide distinct sacrifice lines.
- Gift of Doom offers protection via its face-down/morph interaction but does not prevent exile or all removal. Goblin Sharpshooter ordinarily has summoning sickness and is not an immediately available tap kill unless it has haste; untap trigger sequencing matters.
- Cavern of Souls supports Missy only when an appropriate creature type is named, e.g. Time Lord. Fetchlands can find matching basic types/duals; Marsh Flats and Misty Rainforest are colorless identity lands legal in Grixis.
- Removed cards do lose some big-board Cyberman pressure (Squadron), vehicle-themed theft (Cybership) and slower repeatable morph draw (Aphetto); engine speed, Commander protection and sacrifice access are more valuable for this exact list.

## Evidence boundaries

Engineering M7 decision `data/grixis/m7/decision_reviews/Missy_rev1.json`; Oracle snapshot `data/grixis/m7/oracle_snapshots/Missy_Rev1_Scryfall_20261026.json`; source-scoped tests `tests/test_m7_missy_rev1.py`, merged engineering PR #719, M7 CI SUCCESS. These are finite mechanical assertions and Oracle checks, **not** an independently completed broad M6 I/J simulation. All outstanding source-blueprint game-state cases are separately itemized as deferred in the certification transfer.

The October 15 list, hash and owner approval remain immutable historical evidence, while the state pointer now identifies the exact October 26 owner-approved M7 list.
