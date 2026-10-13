# Abaddon Frozen-Baseline Audit Plan — 2026-10-13

## Purpose and state protection

This plan supports a bounded independent verification of the frozen Abaddon the Despoiler list. It does not propose or apply changes, and is not a finalization certificate.

- Baseline TXT SHA-256: `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`
- Compact 62-deck archive SHA-256: `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`
- Candidate alternative Aurora Phoenix remains test-only; Mind's Desire remains in the baseline.
- The Aurora/Mind's Desire Forge pilot is closed INCONCLUSIVE. Do not rerun the same AI comparison.

## Bounded work units

### A. Static baseline audit
- Extract the Abaddon TXT only from the hash-pinned 124-list archive.
- Verify exact baseline TXT hash, 100 cards including commander, one commander marker, and singleton/copy-rule compliance.
- Join exact card names to the Scryfall metadata overlay dated 2026-10-12, reporting missing/ambiguous mappings rather than guessing.
- Preserve exact per-card source name, quantity, role tag, Oracle ID, type line, color identity, Commander legality metadata, printing key, and any exception annotation.
- Distinguish a successful metadata join from a full current legality review and from rules/strategy certification.

### B. Interaction checklist
Use the expanded interaction review as a starting point. Close already-covered findings unless a concrete contradiction appears. Audit remaining material interactions in the exact list: triggers, replacement effects, zone changes, casting permissions/costs, copies versus casts, combo dependencies, graveyard requirements, and rules that can make a stated line fail. Each finding should state the exact card interaction, necessary board/zone/mana conditions, stopping points, and primary Oracle/rules reference.

### C. Reproducible artifact gate
Use the pinned baseline/archive hashes and committed scripts. The CI should run fast deterministic checks, emit a machine-readable artifact, and fail for missing or ambiguous joins. A dated overlay is not a substitute for a current official banned-list checkpoint before final approval.

## Explicit non-claims

This work does not establish the deck's multiplayer win rate, does not prove the list is optimal, does not turn draw-density probabilities into gameplay evidence, and does not authorize a card change. No final gate should be marked PASS until the final independent verification and user approval requirements in the project protocol are met.
