# Retrospective certification — approved decks #1–8

**Date:** 2026-10-14  
**Cycle:** global-restart-2026-10-13  
**Final retrospective status:** **PASS — 8/8 CERTIFIED UNDER THE 2026-10-14 FRESH ORACLE / LEGALITY / RULES GATE**

This certification closes the retroactive verification required after the project adopted the mandatory fresh per-card Oracle and legality gate. It does **not** reopen, replace, or change any of the eight user-approved decklists.

## Evidence chain

### 1. Fresh authoritative card-data layer — PASS

GitHub Actions now acts as the project's network boundary for current card truth. The successful current-cycle cache reports:

- generated UTC: `2026-10-14T05:25:45.050588+00:00`
- represented Scryfall bulk update: `2026-10-13T21:05:51.771+00:00`
- current-cycle distinct names requested: **516**
- records written: **516**
- validated bulk-overlay hits: **498**
- targeted live exact-name lookups: **18**
- unresolved: **0**
- cache SHA-256: `b3850fc70fce8de18c2b362a6f0e83779e01b32166f58cece7d62c1a0fc4b053`
- cache result: **PASS**

Primary records:
- `refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json`
- `refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl`
- `architecture/ORACLE_DATA_ACCESS_V1.md`

### 2. Exact-list / count / singleton / identity / per-card Oracle / Commander-legality machine gate — PASS 8/8

The hardened retrospective workflow successfully verified the exact approved current-cycle list sources and generated row-per-card evidence. Every approved deck passed:

- exactly 100 cards in the Commander deck, including commander(s);
- singleton compliance with basic-land / legitimate copy-rule treatment;
- current canonical card resolution;
- current Oracle record availability;
- UBR color-identity compatibility;
- current Commander-legality field reconciliation;
- no unresolved names or ambiguous identities;
- documented exception handling rather than silently treating an exception as officially legal.

For deck #8, Lutri is outside the 100-card Commander deck and the starting-deck companion condition independently passes.

Primary records:
- `refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.json`
- `refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.md`
- eight `Card_Verification_*_2026-10-14.csv` files
- eight `Verification_Gate_*_2026-10-14.md` files

### 3. Official Commander legality checkpoint — PASS / registered exceptions preserved

The 2026-10-14 official Commander banned-list checkpoint found no unexpected legality blocker in decks #1–7. Deck #8 retains exactly the three already authorized project exceptions:

1. `Lutri, the Spellchaser` — officially banned as companion; project-authorized companion.
2. `Trade Secrets` — officially banned; project-authorized in this designated main deck.
3. `Yawgmoth's Bargain` — officially banned; project-authorized in this designated main deck.

These remain labeled as official illegality plus separate project authorization. Deck #8 is **not** described as officially Commander-legal without qualification.

Primary record:
- `refinement/verification/Retrospective_1_to_8_Official_Banlist_Checkpoint_2026-10-14.md`

### 4. Material rules-interaction gate — PASS 8/8

The material commander, combo, copy, sacrifice-cost, finality-counter, companion, and triggered-ability interactions relied upon by the eight approved lists were re-attested against current Oracle records and the current Wizards Comprehensive Rules checkpoint.

Primary record:
- `refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`

The fresh rules pass found **one stale historical documentation error** in Ashnod the Uncaring: older records incorrectly described Ashnod as once-per-turn and as requiring a nontoken permanent. Current Oracle text has neither restriction. The correction strengthens the approved list's qualifying sacrifice-activation interactions and does not require a deck change.

Correction record:
- `refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md`

## Per-deck retrospective result

| # | Approved deck | 100 / singleton | Fresh Oracle / CI / legality | Rules | Final retrospective |
|---:|---|---|---|---|---|
| 1 | Abaddon the Despoiler | PASS | PASS | PASS | **CERTIFIED** |
| 2 | Admiral Beckett Brass | PASS | PASS | PASS | **CERTIFIED** |
| 3 | Admiral Brass, Unsinkable | PASS | PASS | PASS | **CERTIFIED** |
| 4 | Anhelo, the Painter | PASS | PASS | PASS | **CERTIFIED** |
| 5 | Ashad, the Lone Cyberman | PASS | PASS | PASS | **CERTIFIED** |
| 6 | Ashnod the Uncaring | PASS | PASS | PASS, historical wording corrected | **CERTIFIED** |
| 7 | Be'lakor, the Dark Master | PASS | PASS | PASS | **CERTIFIED** |
| 8 | Bjorna // Cecily + Lutri | PASS | PASS / 3 registered exceptions | PASS / PROJECT_EXCEPTION | **CERTIFIED UNDER PROJECT RULES** |

## Approved-list preservation

No decklist mutation was made during this retrospective. The eight decks remain approved and locked exactly as previously authorized. Certification validates the approved lists under the stronger gate; it does not constitute a new optimization pass or permission to revise them.

## Hash note for decks #3 and #4

The retrospective machine report records both the source-file raw-byte SHA and the pre-existing central-state approved hash. Those values differ for Admiral Brass, Unsinkable and Anhelo because the earlier central state used a different list-hash / normalization representation. The exact approved source paths and user-approval evidence are unchanged, and the machine gate found no card-membership discrepancy. Do not overwrite the historical central-state hashes merely to force raw-byte equality; preserve the hash-method distinction.

## Closure

All mandatory retrospective hard gates are now closed:

- current card-data acquisition: **PASS**
- exact approved-list provenance: **PASS**
- 100-card count / singleton: **PASS**
- per-card canonical Oracle resolution: **PASS**
- color identity: **PASS**
- official legality / project exception reconciliation: **PASS**
- material rules interactions: **PASS**
- user approvals preserved: **PASS**

# RETROSPECTIVE #1–8: COMPLETE

The project may resume at **deck #9 — Cormela, Glamour Thief**, which must itself pass the same fresh per-card and rules gate before any approval request.
