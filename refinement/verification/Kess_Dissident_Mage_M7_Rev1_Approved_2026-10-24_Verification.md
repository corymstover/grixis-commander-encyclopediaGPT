# Deck #26 Kess M7 Rev1 — whole-100 verification and evidence scope

**Owner-approved exact raw SHA-256:** `11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4`. Approval “Approve” from Cory Stover on 2026-10-24 immediately follows the full 100-card five-swap Rev1 presentation; no inferred approval.

## Physical and historical controls

- New file: `refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt`; exact 100 `1x` lines, trailing single LF; all 100 distinct, no repeated nonbasic/basic names. Kess first as `[Commander]`.
- October 14 source preserved: `refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt` — raw `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`.
- Physical diff exact five-for-five: +Mana Drain, Grim Tutor, Jeska's Will, Cyclonic Rift, Exotic Orchard; −Personal Tutor, Demonic Counsel, Ledger Shredder, Into the Flood Maw, Fiery Islet. 27 lands before/after; incumbent subtractions and replacement names are singleton verified.
- Color identity within U/B/R, source-proven official Commander legal for all names with no exceptions; selected 100-card Oracle audit `refinement/verification/Kess_Dissident_Mage_M7_Rev1_Oracle_Identity_Index_2026-10-24.json`, drawn from the frozen Scryfall archive taken 2026-10-23.

## Decisive commander-first review

Kess grants a graveyard instant/sorcery **cast** on each of her controller's turns, not a generic flash permission. That spell still requires timing, legal targets, mana and payment, and receives an exile replacement if it would go to the graveyard. The exact list retains Consultation/Pact with Thassa's Oracle, Entomb/Reanimate and Intuition/Gifts decision splits, Displacer Kitten's commander-object reset on noncreature casts, and Underworld Breach with Lion's Eye Diamond, Brain Freeze and Grinding Station.

Mana Drain's delayed mana cannot be assumed to generate Kess's needed colored pips; Grim Tutor takes three life; Jeska's Will yields resources only according to its resolved effects and hand/commander preconditions; Rift's overload does not become free through Kess; Orchard's color palette is opposing-land-dependent. Removed Ledger Shredder/Personal Tutor/Maw/Islet/Counsel all have distinct lost utility. Six- and seven-swap full-100 versions were rejected after the original five; the swap floor was not used as a stopping rule.

## Executed evidence and honest limits

- Engineering: [PR #704](https://github.com/corymstover/GrokBotMTGCompanion/pull/704), first-pass [#674](https://github.com/corymstover/GrokBotMTGCompanion/pull/674); M7 gate packet at `data/grixis/m7/decision_reviews/Kess__Dissident_Mage_rev1.json`, exact head and CI documented by separate transfer attestation.
- Mechanical plan provenance: `data/grixis/m6/test_blueprints/Kess__Dissident_Mage.json`, blob `760769aa9320e8c3440b7f64904bc0d7e2c8edc8`. The old I/J receipt tested a *different* Grok scope, and is not misrepresented as automatic proof of this final revision.
- Exact-source 14 cases C1, K1–K5, E1–E2, W1–W3, F1–F3 executed with both normal and adversarial branches by `tests/test_m6_kess_rev1_case_transfer.py`; six separately checked exact raw, swap, Oracle legality, rules and source preservation by `tests/test_m7_kess_chatgpt_rev1.py`. These are finite authored fixtures, not a general multiplayer engine, statistical sample or measured cEDH performance.
- Canonical PR exact-head checks must include `python scripts/verify_m7_certification_transfer.py --check` and its regression tests; do not merge without passing.

Natural ceiling: **Power Bracket 5 — fringe cEDH**. Tags: **cEDH / Spellslinger / Combo**. Project exceptions: **none**.

Historical and other 61 deck SHA locks remain untouched; no M8 final encyclopedia certification implied.
