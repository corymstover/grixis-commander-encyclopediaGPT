# Deck #37 — Mishra, Eminent One M7 Rev1 — exact owner-approved verification

Date: October 26, 2026, America/Chicago.

## Exact identity and Commander rules gate

- Approved physical raw SHA-256 **`0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0`**.
- Commander on first line; **100 physical lines / 100 distinct names / 99 singleton noncommanders / 34 lands**. No companion.
- Current October 26 Scryfall cards/collection snapshot resolves **100/100** names; **100/100 officially Commander legal**, **100/100 Grixis/colorless identity valid**, no project exceptions, no unresolved or split errors.
- Six one-for-one changes only from preserved October 15 approved source raw SHA `ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0`.
- Commander Warform copies an owned noncreature artifact as a 4/4 hasty artifact creature and keeps copied mana value. Beginning-of-combat targeting, legend rule, ETB triggers and next-end-step sacrifice were checked against current Oracle.
- **Panharmonicon** doubles triggers caused by Warform ETBs, not the combat trigger. **Roaming Throne** doubles Mishra's trigger with Human/Artificer choice. Heart energy arithmetic verified with exact-positive/negative source-bound fixtures.
- **Idol of Oblivion** may tap on the Warform copy's entry turn because the Warform has haste, but only after a token was actually created. **Simulacrum Synthesizer** retains copied artifact's mana value for qualifying triggers.
- **Grinding Station** artifact entrance untaps and its activated ability requires tap and sacrifice; no invented zero-cost action. **Marionette Apprentice** one qualifying death equals one trigger; no double counting. Lightning Greaves equips for zero and protects one creature with shroud, whereas removed Padeem protected artifacts differently.
- Original October 15 verified Determined Iteration/Heart, Helm/Urza/Elixir, and artifact-recursion interaction documentation preserved. Historic M6 blueprint cases were design-only; see scoped transfer instead of claiming a complete independent I/J test of M7.

## Engineering proof and owner receipt

- [Engineering PR #718](https://github.com/corymstover/GrokBotMTGCompanion/pull/718) merged `27b30297a7c7753a6a6ad889460c114813ef42ab`; tested head `670f0cecf0812583a880d02135752c1aee40e19b`.
- [Exact engineering candidate tests](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40312936555) **SUCCESS**, seven focused finite test methods. The canonical branch additionally implements five source-mapped finite P0 tests in `tests/test_deck37_m7_p0_source_cases.py` with positive and adverse preconditions (C1, K1, K2, K3, F1). They are bounded predicates, not a complete Magic simulation.
- [Global M7 decision gate](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40312936783) **SUCCESS**.
- Evidence: `data/grixis/m7/oracle_snapshots/Mishra__Eminent_One_Rev1_Scryfall_20261026.json`, `data/grixis/m7/decision_reviews/Mishra__Eminent_One_rev1.json`, `tests/test_m7_mishra_eminent_rev1.py`.
- Owner replied **“Approve”** to the fully displayed exact Deck #37 list on October 26; one approval, not a second confirmation. Receipt `refinement/approvals/Mishra_Eminent_One_M7_Rev1_Approved_2026-10-26.md`.
- Canonical M6 transfer: P0 5/5 bounded finite PASS; P1 2/10 bounded PASS (K5 and W1), 8/10 source-specific **DEFERRED** (K4, K6, E1, E2, W2, W3, F2, F3). These include unsimulated full turn-control, token-chain, win-loop and artifact-hate/speed game-state scenarios, not hidden failures or simulated win-rate evidence. A fresh whole-engine I/J rerun is NOT claimed. The exact P1 deferrals are disclosed as limitations in owner receipt and attestation.

**Power Bracket 4 — Optimized. Tags: Artifacts / Warform Tokens / Combo.**

Postmerge requirement: independently read the new canonical main deck file and SHA, approval record, transfer attestation, and the one-deck registry edit before reporting LOCKED.
