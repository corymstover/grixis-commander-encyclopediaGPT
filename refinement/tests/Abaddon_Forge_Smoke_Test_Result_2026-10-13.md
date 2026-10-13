# Abaddon Forge Smoke-Test Result — 2026-10-13

**Purpose:** verify pinned Forge source-card coverage, prepare the exact baseline and one-card variant, and prove that both files load into a Commander-mode simulation. This is not a performance comparison.

## Verdict

**Smoke-test pass, with explicit limitations.** GitHub Actions run [38338464845](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338464845) completed successfully on commit [33ac3a2](https://github.com/corymstover/grixis-commander-encyclopediaGPT/commit/33ac3a29b403889bdeb64ecf91767f0e6f6a0d0c).

- Pinned Forge release archive SHA-256 check and extraction: **PASS**.
- Forge desktop JAR starts on OpenJDK 17.0.20.1 and reports Forge 2.0.15-SNAPSHOT-09.28: **PASS**.
- Pinned card-script source commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`: **PASS**.
- Card-script presence and nonempty Oracle-field scan: **95/95 names matched; 0 missing or invalid**. This covers the test variant's 94 unique names plus Mind's Desire from the frozen baseline, with all required control cards matched.
- Frozen Abaddon baseline was extracted only after its recorded SHA-256 verified; baseline and variant were converted to Forge `.dck` files; both were 100 cards with 99 in Main and Abaddon in Commander; the declared difference remained exactly Mind's Desire OUT / Aurora Phoenix IN: **PASS**.
- Forge CLI entered Commander simulation and instantiated the baseline-vs-variant match: **PASS as a deck-load/runtime smoke check**.

## What happened in the smoke match

The bounded CLI command used a **10-second per-game clock**. Forge logged that it stopped the slow match as a draw after approximately nine seconds. It then emitted contradictory outcome lines (each player reported as having won) and a match score naming the variant. The log also emitted repeated `Steam Vents Did not have activator set in SpellAbility_Condition.checkConditions()` warnings.

**Do not count this as a win, gameplay result, or evidence that Aurora Phoenix is better.** The explicit draw and contradictory output make it unsuitable for comparing the two lists. The warnings are recorded for investigation; this smoke run did not establish whether they affect actual card behavior.

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
