# Abaddon the Despoiler — Baseline Consistency Analysis

**Snapshot:** 2026-10-13 UTC  
**Status:** DESCRIPTIVE BASELINE ONLY — not a gameplay simulation or finalization gate  
**Frozen baseline TXT SHA-256:** 2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf

## Verified deck composition

- Main deck plus commander: **100 cards**.
- Library after setting commander aside: **99 cards**.
- Lands: **34**.
- Cards tagged Ramp in the source list: **19**.
- Explicit early-acceleration set: **12 cards**.

The early-acceleration set is Arcane Signet, Cabal Ritual, Chrome Mox, Dark Ritual, Lion's Eye Diamond, Lotus Petal, Mana Vault, Rite of Flame, Sol Ring, and the three Talismans. This is a transparent classification for a first-pass density check, not a claim that all twelve are equally reliable or always usable.

## Exact draw-density probabilities

These probabilities sample cards without replacement from the 99-card library. Seven cards means the un-mulliganed opening hand; ten cards means opening seven plus three draw steps; twelve means opening seven plus five draw steps. Extra draw, tutors, mulligans, sequencing, and mana colors are not modeled.

| Cards seen | At least 2 lands | At least 3 lands | At least 1 early accelerator | At least 2 lands + 1 accelerator | At least 3 lands + 1 accelerator | At least 4 lands + 1 accelerator |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 76.46% | 45.33% | 60.75% | 43.49% | 23.17% | 7.73% |
| 10 | 91.87% | 73.70% | 74.32% | 67.29% | 52.30% | 31.48% |
| 12 | 96.27% | 85.41% | 80.81% | 77.39% | 67.71% | 49.89% |

## Opening-hand land distribution

| Lands in opening seven | Exact probability |
|---:|---:|
| 0 lands | 4.68% |
| 1 lands | 18.86% |
| 2 lands | 31.13% |
| 3 lands | 27.21% |
| 4 lands | 13.61% |
| 5 or more lands | 4.51% |

## Interpretation

- The raw opening seven has at least two lands **76.46%** of the time and at least three lands **45.33%** of the time.
- The opening seven contains at least two lands and at least one card from the declared early-acceleration set **43.49%** of the time.
- By ten cards seen, the probability of at least three lands and at least one declared early accelerator is **52.30%**.
- These are card-density probabilities, not the probability of casting Abaddon on a particular turn. The latter depends on colored sources, tapped lands, mulligans, sequencing, and the actual function of each accelerator.

## Decision use

Use this as a frozen-baseline reference for later deck-specific comparisons. Do not infer that the deck fails a target, that more lands are required, or that a candidate is an upgrade without a predeclared metric and a commander-specific reason. No decklist change is implied by this report.

## Limitations

- No mulligan policy or keep decisions modeled.
- No mana-color, tapped-land, sequencing, cost-reduction, or acceleration usability model.
- No tutors, extra draw, or card-specific draw triggers modeled.
- Early acceleration is a declared 12-card set; Cabal Ritual is conditional on available mana/graveyard state and Chrome Mox/Lion's Eye Diamond have meaningful costs.
- This is a descriptive baseline consistency benchmark, not a deck-quality score, gameplay result, or pass/fail threshold.

## Reproducibility

Run python scripts/analyze_abaddon_baseline_consistency.py --report-output refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md in the repository. In archive mode, the script verifies the pinned compact-archive SHA-256 and the exact Abaddon TXT SHA-256 before calculating the probabilities.
