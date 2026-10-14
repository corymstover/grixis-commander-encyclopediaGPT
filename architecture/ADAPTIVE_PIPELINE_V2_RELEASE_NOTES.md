# Adaptive Pipeline v2 — release notes

## Status
Release candidate for the 62-deck refinement cycle. Freeze only after both repository and adaptive CI gates pass on the same final branch head.

## Improvements
- canonical current-cycle state separates live approval state from historical tracker evidence;
- deterministic content-addressed stage caching and atomic checkpoints;
- dependency-aware invalidation for decklist, Oracle, legality, strategy, and project-exception changes;
- generic staged runner with resume-by-cache behavior;
- bounded transient retry with exponential backoff and fail-closed permanent errors;
- bounded multi-deck concurrency with per-deck failure isolation;
- telemetry summaries for median/p95 runtime, cache reuse, retries, blocker rates, and hotspot detection;
- commander-first variant comparator that refuses identity, legality, or combo-integrity regressions;
- explicit operating contract and optimization stopping rules;
- CI regression gates preserving frozen baseline verification and existing project tests.

## Expected effect
The system should spend less time repeating unchanged analysis, recover cleanly from interruptions, isolate failures rather than stalling all 62 decks, and direct deep analysis toward changed or uncertain conclusions. Final deck approval remains a human decision after full verification.

## Known limits
No scoring model can prove a deck is globally optimal across all Magic cards, metagames, or future printings. Candidate ranking and numeric quality scores remain evidence, not authority. Rules/Oracle verification, strategic judgment, and playtest evidence remain required.
