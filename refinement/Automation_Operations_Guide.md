# Grixis Commander Encyclopedia — Automation Guide

## What's automatic

- Weekly full metadata refresh: download Scryfall's default-cards bulk once, stream it, and match it against all 62 frozen CSV/TXT lists. One shared scan is more efficient than repeated per-card HTTP requests.
- Immediate/manual refresh: update the exact file refinement/metadata_audit/REFRESH_REQUEST.md on a refinement/** branch, or use Actions → Refresh current Scryfall card metadata → Run workflow. Similarly named files do not trigger the path-filtered workflow.
- Fail-closed verification: accept the output as fresh only if its summary was generated after the current workflow run started (a recent cached snapshot from a previous failed run is rejected), the summary is at most 2 hours old, Scryfall's bulk timestamp is within 72 hours, all 62 decks/5,964 rows match exactly, and no unresolved names, Oracle IDs/text, identity mismatches, or unexpected official-illegal rows remain.
- Abaddon-specific closeout audit: after the global refresh, require a successful exact 94-name join to the frozen deck and verify Oracle identifiers/text, printing identifiers, color identity, and Commander legality fields.
- Fast CI: PRs run unit tests, workflow trigger/path checks, tracker CSV schema/approval metadata validation (62 unique deck rows, no malformed columns or duplicate IDs, approvals require hash+date), and frozen-baseline integrity checks. The metadata-network refresh is separate so documentation edits do not redownload a large bulk file.
- Auditable artifacts: every refresh uploads the summary and validator report, including failure diagnostics. If the refresh step itself fails, the validator is skipped (so it cannot pass on an old cache); the job summary says no validator report was produced.

## Evidence boundaries

Metadata verification does not prove every rules interaction or strategy choice. Official legality stays separate from project-authorized exceptions. The 100-card/singleton baseline check and explicit user approval remain independent finalization gates. A FAIL/blocked result must not be rewritten as a pass; retry via the supported workflow or preserve the blocker in the tracker.

## Maintenance controls

The refresh workflow uses a repository-wide concurrency group so parallel pushes do not trigger redundant bulk downloads. The validator is chained to the current run start timestamp and executes only after successful metadata generation, preventing a recent-but-old summary from satisfying the gate. Network retry logic applies only to transient errors (timeouts, 429, and 5xx); a permanent 403 fails quickly and visibly. Stable Current_* artifacts are canonical; prior date-suffixed files are written as compatibility aliases for existing references.
