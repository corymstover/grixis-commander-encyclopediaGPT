# Fresh Scryfall metadata refresh request — Abaddon closeout

Run the existing `.github/workflows/refresh-scryfall-metadata.yml` workflow on this branch. This is an explicit request to rerun the existing refresh because the approval-time 94-card Abaddon closeout remains blocked by stale October 12 metadata.

Required post-run checks:
- Record workflow run URL, completion time, bulk `updated_at`, row counts, exact-printing matches, missing/ambiguous rows, Oracle text/ID coverage, UBR color identity comparison, and official Commander legality statuses.
- Isolate all 94 distinct card names for `Abaddon_the_Despoiler`, especially Bituminous Blast, Boltwave, and Thermo-Alchemist.
- Do not change the frozen decklist, approve candidate additions, or mark the finalization gate YES.
- If Scryfall data cannot be retrieved by Actions too, preserve the error logs and mark the full current-source gate BLOCKED rather than treating a dated cache as fresh.
