# Adaptive Pipeline v2 — operating contract

This system accelerates the 62-deck refinement cycle without replacing expert Commander judgment.

## Automatic
- verify frozen inputs and current card metadata;
- reuse cache only when dependency hashes match;
- invalidate analyses affected by decklist, Oracle, legality, strategy, or exception changes;
- retry transient infrastructure failures with bounded exponential backoff;
- checkpoint every successful or blocked stage;
- collect runtime/cache/blocker telemetry and surface measured bottlenecks;
- compare proposed variants against the current baseline using commander-first quality dimensions.

## Never automatic
- declaring a card strategically correct from popularity/ranking alone;
- weakening legality, color identity, singleton, count, combo, or rules gates;
- approving or locking a deck;
- silently changing project exceptions;
- silently changing a commander's strategic blueprint or natural power ceiling.

## Variant acceptance
A proposed swap must preserve commander identity and all integrity gates and demonstrate a material aggregate improvement. Numeric quality scoring is decision support, not proof: Oracle/rules verification and strategic review remain mandatory.

## Recovery
Completed stages are content-addressed. Interrupted runs resume by reusing verified stage outputs. Transient failures are retried only within bounded policy; permanent/data failures stop immediately and leave a BLOCKED checkpoint.

## Self-optimization
Telemetry may propose optimizations. An optimization is retained only if regression tests and hard gates pass and measured performance/correctness improves. Three consecutive non-improving optimization candidates trigger architecture freeze under OPTIMIZATION_STOPPING_RULES.md.
