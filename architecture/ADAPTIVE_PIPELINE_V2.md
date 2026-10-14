# Adaptive Pipeline v2 — Architecture and Safety Contract

**Date:** 2026-10-13
**Status:** implementation baseline
**Scope:** research, verification, CI orchestration, trackers, and project maintenance. Decklist strategy remains commander-first and human/audit governed.

## Goals
1. Eliminate repeated work by caching immutable/freshness-scoped results.
2. Make every long operation resumable and idempotent.
3. Prevent infinite retry/research loops with explicit budgets and circuit breakers.
4. Replace deck-specific automation with parameterized deck jobs.
5. Maintain one canonical machine-readable project state and derive trackers/reports from it.
6. Measure runtime, failure, cache-hit, retry, and evidence-reuse rates.
7. Permit self-optimization only inside a bounded propose → benchmark → accept/rollback loop.

## Canonical state machine
Each deck moves through:
UNREFINED -> INTAKE -> BLUEPRINT -> CANDIDATE_TRIAGE -> RULES_REVIEW -> VERIFY -> TEST -> FINALIZE -> LOCKED
with BLOCKED as a side state carrying blocker_code, evidence_needed, retry_after, and attempt_count.

A stage may run only when its declared inputs exist and their hashes/freshness satisfy its contract. A stage writes an atomic checkpoint before the next stage begins.

## Content-addressed cache
Cache key = SHA256(stage_version + normalized input hashes + source snapshot IDs + relevant configuration).

Recommended cache classes:
- baseline structural audit: immutable until decklist hash changes;
- Oracle/card metadata: shared project-wide snapshot;
- official legality checkpoint: shared dated snapshot;
- rules notes: keyed by Oracle IDs + rules-note version;
- commander candidate evidence: commander + source snapshot + ranking method version;
- simulation/test result: exact deck hash + engine version + test config + seed set.

No stage repeats a successful cached computation unless its invalidation condition is true.

## Bounded execution
Every external or expensive stage declares:
- timeout;
- max_attempts;
- exponential backoff ceiling;
- retryable error classes;
- non-retryable error classes;
- circuit_breaker threshold;
- checkpoint frequency.

Default: max_attempts=3. A repeated deterministic failure becomes BLOCKED, not an automatic rerun.

## Research stop rules
A research stage closes when:
- all high-impact candidates are ACCEPT/REJECT/HOLD with reasons;
- no unresolved material rules question remains;
- any HOLD has a named evidence gap;
- broad discovery budget is exhausted without a new material candidate.

Never restart broad research solely because a recording/API write failed.

## Single-writer project state
Create one canonical state document/database containing deck_id, deck_hash, stage, gate statuses, source snapshot IDs, current revision, blocker, last successful checkpoint, metrics, and artifact references.
CSV trackers and Markdown status pages are generated views. They are not independent authorities.

Use optimistic concurrency (expected state version/SHA). Conflicts must re-read and reconcile rather than overwrite.

## Parameterized deck runner
Replace commander-specific CI scripts/workflows with a generic runner:
`python -m grixis_pipeline run --deck-id <id> --through <stage>`

Deck-specific behavior belongs in data/config (commander blueprint, exceptions, test profile), not copied workflow logic.

## Telemetry
Each stage emits JSONL:
run_id, deck_id, stage, stage_version, input_hash, cache_hit, started_at, duration_s, result, retry_count, external_calls, bytes_downloaded, artifact_hashes, blocker_code.

Campaign KPIs:
- median and p95 stage duration;
- cache hit rate;
- retry rate;
- blocked-run rate;
- duplicate-research rate;
- CI minutes per finalized deck;
- manual-write count per deck;
- stale-source incidents;
- rollback count;
- verification defects caught before lock.

## Adaptive optimization loop
The system may autonomously optimize execution policy, not deck strategy or legality truth.

1. DETECT: telemetry identifies a regression or repeated cost.
2. PROPOSE: generate a narrowly scoped change with expected metric effect.
3. BENCHMARK: replay a fixed representative fixture set.
4. SAFETY GATES: baseline hashes, legality/identity outputs, decision outputs, and verification semantics must remain equivalent unless the change explicitly and correctly fixes a defect.
5. ACCEPT only if the target metric materially improves and no safety metric regresses.
6. ROLLBACK automatically on regression.
7. LOG the change, benchmark, rationale, and version bump.

Never self-modify:
- frozen baseline decklists;
- project exceptions;
- commander strategy decisions;
- approval/lock status;
- source hierarchy;
- hard verification gates.

## Immediate migration order
P0: canonical state + stage contracts + telemetry + retry/circuit-breaker library.
P0: generic baseline/metadata verification keyed by deck hash.
P1: generic deck runner and matrix CI; retire Abaddon-only verification jobs after parity tests.
P1: derived tracker/report generation from canonical state.
P1: shared rules-note cache and candidate-evidence cache.
P2: benchmark harness and adaptive optimizer for safe execution parameters.
P2: incremental invalidation so a card swap rechecks only affected deck/hash-dependent stages plus final hard gates.

## Acceptance criteria
- Re-running an unchanged completed stage performs no expensive work.
- Killing a run mid-stage can resume from the last valid checkpoint.
- No automatic loop can exceed its retry/research budget.
- A deterministic failure surfaces as BLOCKED with one actionable cause.
- Tracker/status views cannot disagree with canonical state.
- Generic runner processes at least three strategically different commanders without code changes.
- Benchmark suite proves optimization changes preserve all hard-gate outcomes.
