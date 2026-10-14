# Retrospective verification #1–8 — execution checkpoint (2026-10-14)

**Status: BLOCKED on mandatory fresh Oracle/legality gate. No approvals revoked and no approved decklists changed.**

## Implemented
- Local verifier `verify_grixis_fresh.py` parses 100-card lists and companion markers, checks count/singleton, requests each card's current Scryfall canonical identity, Oracle text, color identity, Commander legality, and records per-card evidence and SHA-256. Fails closed on missing live data and reserves manual rules and official banned-list signoff.
- Local preflight `retroaudit_inventory.py` compared frozen TXT inventories for eight decks with inherited v8.1.4 card audit, and used exact approved Ashnod list when locally available.
- Eight preflight baselines show 100 cards and no nonbasic duplicates, but **frozen TXT is not authoritative for current approved #1–5, #7–8**. Fetch exact approved GitHub list/override before certifying.
- Archived v8.1.4 card audit differs from each frozen baseline by 4–7 names. This reinforces why inherited audits cannot substitute for live per-card checks.
- Scryfall direct network lookup from the execution container fails DNS resolution; Ashnod per-card attempt yielded 95 UNVERIFIED card names, **not a PASS**.

## Next required steps
1. Make a live Scryfall card-data source available to the verifier, or provide an equally current authoritative Oracle dataset with fetch timestamps and IDs. Do not turn off fail-closed behavior.
2. Resolve exact approved decklists #1–8 from GitHub state and approved files; preserve companion outside-deck distinction and project exception registry.
3. Run per-card checks on each list, generate CSV evidence, check latest official Commander banned list, and independently sign off combo rules. Record PASS/PROJECT_EXCEPTION/FAIL/UNVERIFIED individually.
4. Only when all eight pass may current-cycle Cormela #9 verification resume; do not request approval prematurely.

**No claim of completion of the fresh gate is made.**
