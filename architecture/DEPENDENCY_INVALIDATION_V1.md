# Dependency-aware invalidation v1

## Purpose
Preserve verified work unless a changed input can affect it. Recompute correctness-critical conclusions whenever their dependencies change.

## Change classes
- DECKLIST: local to the changed deck; reopens structure, identity, legality, commander fit, synergy, combos, mana/curve, role density, candidate conclusions, tests and final verification.
- ORACLE_SNAPSHOT / LEGALITY_SNAPSHOT: project-wide card-fact invalidation; does not erase unrelated historical research artifacts.
- COMMANDER_STRATEGY: local strategic invalidation; preserves structural and Oracle facts.
- PROJECT_EXCEPTION: legality/final-verification invalidation for affected decks.

## Safety
Final verification is always downstream of a material change. Cache reuse is allowed only when dependency hashes match. Approval and lock state are never mutated by invalidation logic.
