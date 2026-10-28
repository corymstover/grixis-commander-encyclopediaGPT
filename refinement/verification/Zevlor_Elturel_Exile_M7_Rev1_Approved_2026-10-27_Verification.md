# Zevlor, Elturel Exile — Deck #62 M7 Rev1 owner-approved exact-source verification

**Scope:** Only Cory's exact 100-card / six-swap raw SHA `071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f`. Canonical status is contingent on the exact-head lock PR passing and merging.

## Protected source and deckwide reconciliation

- Original Oct15 canonical raw SHA `d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9`, immutable original approved artifact and owner receipt retained.
- Proposed new approved artifact `refinement/decklists/Zevlor_Elturel_Exile_M7_Rev1_Approved_2026-10-27.txt` is byte-identical to engineering candidate at [GrokBot M7 PR #748](https://github.com/corymstover/GrokBotMTGCompanion/pull/748), head `4145603e8a13c3470486f9663c15239f247ff3d6` and final merge `ae45cb6c13797228df0c0f380a04d3dfe92f82a2`.
- Exactly 100 cards: Zevlor first, 99 other physical copies, 97 distinct card names, only Island/Mountain/Swamp ×2 repeated, 34 lands. Six additions and removals each present exactly once, no rogue deck replacement or land drift.
- Canonical `refinement/decisions/Zevlor_Elturel_Exile_M7_Rev1_Whole99_Audit_2026-10-27.csv` preserves decisions on 99/99 physical original slots; engineering has its own matching source-bound ledger.
- Current Oracle and Commander legality are bound to the dated engineering Scryfall record of 108 material names, `data/grixis/m7/zevlor_rev1/Zevlor_M7_Rev1_Scryfall_snapshot.json`; every selected identity is commander legal and within UBR. No project exception.

## Specific P0/P1 and rules verification

The original engineering M6 blueprint plan `data/grixis/m6/test_blueprints/Zevlor__Elturel_Exile.json` (pinned original Git blob `c439684d4a28eb91198e72ab400fd60ed3f7fb86`) requires exactly five P0 `C1,K1,K2,K3,F1` and eleven P1 `K4,K5,K6,K7,E1,E2,W1,W2,W3,F2,F3`.

- [Exact-head dedicated run #40629369955](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40629369955) **SUCCESS**: 23 methods in `data/grixis/m7/zevlor_rev1/verify.py` against the four physical 100-card SHA-pinned sources and frozen Scryfall Oracle text. Each historical case ID maps to a distinct source-backed positive/negative finite fixture; six other methods test the exact new effects.
- Zevlor only responds to a cast instant/sorcery with exactly one opponent or opposing permanent target; copies are not casts but do trigger actual `cast or copy` magecraft. Countering the original after the delayed trigger does not erase its referenced spell copies.
- Bracers copies an activated ability and thus produces separate watches; Twinning Staff adds an additional copy per copy event, not recursively. Targetable Swiftfoot Boots enables own Minamo/Seal untaps; shroud would disallow them. Mana costs are paid, and watches end at turn boundary.
- Gifts searches the caster's library, with up-to-four different card names per independent resolution; Rousing Refrain supplies red only and its copies do not remain suspended; Traumatic Critique at X=0 filters three times without dealing damage; Heist has no stolen-card casting permission without gift.
- Original M6 `data/grixis/m6/ij/input_receipts/zevlor-elturel-exile.json` remains `inputs_attested_downstream_incomplete`, `phase_b_replayed:false`. The new bounded M7 case tests are not retroactively completed M6 J, a full Magic engine or simulated table win percentages.

## Strategic test and canonical transfer

The exact packet `data/grixis/m7/decision_reviews/Zevlor__Elturel_Exile_rev1.json` passed the decision gate with six real selected swaps, eleven material candidate judgments, nine challenged incumbents, full 99-slot audit, and genuine complete eight-/nine-swap rejected alternatives. The same dedicated GitHub Actions job passed the repository-wide M7 gate.

Canonical PR must also include `refinement/verification/m7_certification_transfer/Zevlor__Elturel_Exile_071e9a8b9eaa0f2c.json` with the exact engineering head, CI URL, original M6 plan/receipt, 5 P0 + 11 P1 newly executed case records, actual positive/adverse assertions and approved exact SHA on each case. Required local/CI checks: `python scripts/verify_m7_certification_transfer.py --check` and `python -m unittest discover -s tests -p test_m7_certification_transfer.py -v`, plus the Deck #62 exact lock test.

No file or status of any other approved deck is changed.
