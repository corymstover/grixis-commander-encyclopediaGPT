# Abaddon Forge Smoke-Test Result — 2026-10-13

**Purpose:** verify the pinned Forge source-card coverage, exact baseline/test-variant import, basic Commander-mode runtime, and whether repeated seeded smoke runs yield reproducible match-event logs. This is not a performance comparison.

## Current verdict — smoke gates passed; comparative testing still unqualified

The latest corrected replay workflow [run 38338912312](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338912312) completed successfully on the active refinement branch.

- Pinned Forge release checksum/extraction and Forge CLI startup: **PASS**.
- Pinned source commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`: **PASS**.
- Card-script identity and nonempty Oracle-field scan: **95/95 names matched; zero missing/invalid** (94 variant names plus baseline-only Mind's Desire). This proves script presence and name mapping only, not faithful rules execution for every card.
- Frozen baseline TXT hash and exact 100-card DCK conversion/import: **PASS**. The test variant differs by exactly Aurora Phoenix IN / Mind's Desire OUT, with all other main-deck input positions aligned.
- A 20-second-clock exploratory Commander smoke match completed and produced interpretable log lines for ordinary Abaddon-granted cascade resolutions and an Imperial Seal cast through Underworld Breach. It did not cast Aurora Phoenix, show its graveyard-return trigger, or complete Underworld Breach + Lion's Eye Diamond + Brain Freeze.
- Two runs of the same command and seed produced identical normalized match-event sections in the corrected repeatability check. This is evidence of replay repeatability for that exact smoke case, not proof of identical baseline/variant starting hands or comparative performance.
- Three additional seeded Aurora-specific exploration runs have been registered in the active workflow; their outcomes are a separate pending gate until the workflow report completes.

**No gameplay result has been counted toward the registered pilot/confirmatory test, and no card change is approved.** Forge remains unqualified for deciding Aurora Phoenix versus Mind's Desire until the relevant Aurora events are observed reliably and the test metrics/controls are shown to be suitable.

## Earlier 10-second smoke attempt (historical; not used as current verdict)

The first bounded CLI run used a **10-second per-game clock**. Forge stopped the match as a draw after approximately nine seconds, then emitted contradictory winner lines (both players reported as having won) and repeated `Steam Vents Did not have activator set in SpellAbility_Condition.checkConditions()` warnings. This run is retained as a diagnostic artifact only and is not interpreted as a win or as card-comparison evidence.

## Remaining gates

| Gate | Current result |
|---|---|
| Pinned script identity / nonempty Oracle field | PASS for the 95 checked names |
| Frozen baseline and isolated variant integrity | PASS |
| Forge CLI startup | PASS |
| Exact .dck generation and Commander-mode loading | PASS as a smoke test |
| Abaddon threshold/cascade event observed and checked against expected rules | NOT TESTED |
| Aurora Phoenix graveyard-return trigger observed and checked | NOT TESTED |
| Storm copies vs cast-trigger behavior / Breach escape sequence | NOT TESTED |
| Stable RNG seed, matched starting library orders, structured zone/trigger logs | NOT DEMONSTRATED |
| Valid baseline-vs-variant comparative games | 0 |
| Approved card changes | 0 |

## Decision and next step

Forge has cleared only the *source-presence, input-preparation, and simulation-launch* smoke gate. It is **not qualified for a confirmatory comparison** of Abaddon's six-mana slot. Forge's own AI documentation says the AI performs poorly with most combo decks, and this one-game smoke result demonstrates why the match result must not be used as evidence.

Next, investigate whether the pinned engine can run deterministic, controlled scenario tests with inspectable logs for the specific rule interactions the deck relies on. In parallel, finish the deck-wide interaction audit and candidate ledger using current Oracle text and documented rules sources. If Forge cannot provide reproducible starts and trustworthy event observations, mark statistical comparison infeasible with this engine and close the slot based on commander-specific strategic evidence, with uncertainty explicitly recorded. Keep the Aurora Phoenix variant separate and unapproved. Do not modify the frozen baseline.

Artifact: [Forge smoke-run logs and reports](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338464845).
