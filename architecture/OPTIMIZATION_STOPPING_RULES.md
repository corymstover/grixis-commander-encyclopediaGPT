# Adaptive Pipeline v2 — optimization stopping rules

Architecture optimization continues only while a proposed change can improve at least one measured dimension without weakening a hard gate.

Measured dimensions:
1. correctness defects caught before lock;
2. duplicate/redundant computation;
3. median and p95 stage runtime;
4. cache hit rate on unchanged inputs;
5. recovery after interruption;
6. blocked/retry rate;
7. CI minutes per finalized deck;
8. manual state synchronization;
9. stale-source incidents;
10. commander-specific analysis coverage.

A change is retained only when tests and hard-gate equivalence pass and its benchmark shows a material benefit or removes a demonstrated correctness risk.

Stop architecture iteration when the prioritized backlog contains no demonstrated correctness risk and three consecutive candidate optimizations fail acceptance. At that point freeze the pipeline version, document remaining limitations, and direct optimization effort to deck quality. Reopen architecture only for a regression, new capability, source-format change, or measured bottleneck.

Never optimize by weakening final verification, legality, singleton/color-identity checks, project-exception accounting, commander-first strategy review, or explicit user approval/lock requirements.
