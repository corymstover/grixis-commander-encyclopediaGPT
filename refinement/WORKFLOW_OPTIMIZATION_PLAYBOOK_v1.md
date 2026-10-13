# Grixis Commander Encyclopedia — Workflow Optimization Playbook v1

**Created:** 2026-10-13 UTC  
**Applies to:** the 62-deck Commander-first refinement campaign  
**Pilot:** Abaddon the Despoiler  
**Status:** working standard; improve only from recorded evidence

## Objective

Reduce repeated work and elapsed time while preserving commander identity, realistic optimization, legality, rules accuracy, source traceability, frozen-baseline protection, and explicit user approval. Faster work is not a reason to weaken final verification.

## Lessons from the Abaddon pilot so far

1. **Keep a frozen baseline and a separate refinement branch.** Never edit approved lists just because a new cycle starts.
2. **Do not treat inventory as analysis.** The first pass found 94 names; the improved role triage distinguished routine cards from material interactions. Future decks should classify first and only research meaningful dependencies.
3. **Separate gates that answer different questions.** Structural integrity, dated Oracle metadata, current Oracle refresh, current official legality, rules interactions, strategic quality, final hash, and user approval are not interchangeable.
4. **Do not repeat inconclusive tests.** The Aurora Phoenix vs. Mind's Desire Forge pilot cast neither candidate. Record it as inconclusive and do not rerun the same setup.
5. **Use a written stopping rule.** Stop broad research when no material, commander-specific unresolved interaction or plausible upgrade remains; do not pursue a separate rules essay for every ordinary land or routine spell.
6. **Commit as work happens.** Each bounded step should update the step note, source review, triage ledger, status report, and deck tracker as applicable. Fetch latest content and SHA immediately before each write; avoid parallel writes to the same file; re-fetch to verify the commit.
7. **If a write fails, troubleshoot instead of abandoning the update.** Try a minimal new-file checkpoint or a single-file append/update, verify it, then synchronize the remaining ledgers. Never claim an update was made until it is re-fetched.
8. **Do not let tool failure create duplicate analysis.** Preserve completed findings locally in the current task and write them once the API path works. Do not rerun the rules research merely because recording failed.
9. **Keep candidate discovery bounded.** Rankings are leads, not instructions. Screen the relevant candidate subset once, log reasons, and reopen only when new evidence supports a plausible material improvement.
10. **Keep performance claims proportional to evidence.** Static probability reports are descriptive; an unqualified Forge workflow is not a Commander win-rate model.

## Standard per-deck pipeline

### A. Intake / baseline (one-time)
- Resolve exact commander and frozen CSV/TXT list.
- Verify baseline hashes, 100-card count including commander, singleton/copy rules, and commander identity.
- Load existing commander blueprint, profile, candidate ledger, exceptions, prior approval/lock status.
- Never reopen a locked deck unless explicitly requested.

### B. Candidate screen (bounded)
- Use commander-specific rankings and current candidate research.
- Screen plausible cards for identity fit, synergy, power ceiling, and likely cut.
- Record include/reject/hold decisions and rationale.
- No automatic substitutions and no broad repeat search without a concrete evidence gap.

### C. Interaction triage (single pass)
Assign each unique card/package one disposition:
- **MATERIAL CHECK** — relevant zone, timing, replacement, copy/cast distinction, cost, target, combo, commander trigger, or own-board dependency.
- **ROUTINE ROLE** — no special commander-specific rules dependency; check text/role once, no essay.
- **CLOSED** — sourced, exact relevant interaction reviewed.
- **OPEN** — specific question and evidence needed named.
- **NOT APPLICABLE** — reason recorded.
A package-level note may close multiple cards when the same rule applies, but the ledger must point to the note and retain per-card status.

### D. Resolve only material opens
- Prioritize by consequence and uncertainty.
- Verify current Oracle text and relevant Comprehensive Rules.
- Write exact conditions, zone, timing, mana value, target, and failure points.
- Do not re-audit closed packages unless new evidence contradicts them.
- Do not repeat failed/inconclusive simulation setups.

### E. Current data / legality closeout
- Refresh Oracle text, color identity, names/printing mapping, and legality for the exact frozen or explicitly proposed list.
- Treat official Commander banned-list status separately from metadata provider status.
- Record project-authorized exceptions accurately; never describe exceptions as officially legal.
- Do not call a dated snapshot a live refresh.

### F. Final integrity and approval
- Independently count 100 cards including commander, singleton/copy rules, color identity, hash and export reconciliation.
- Recheck material interactions and combo function for the exact final list.
- Present all proposed swaps with cuts and rationale before changing the list.
- User approval is required before marking final gate YES and locking the deck.

## Required progress updates

At each bounded step:
1. State the single step and completion criterion.
2. Do only that step.
3. Update the relevant detailed note plus triage/coverage plan, current status, and deck tracker in the same work unit.
4. Verify writes by fetching the files from the active branch.
5. Report: findings, files changed, remaining gates, next one step.
6. Never report a commit as verified until fetch confirms its contents.

## Optimization metrics to track

For each deck, record:
- Unique card names and number classified.
- Material checks opened/closed.
- Candidate decisions screened/logged.
- Number of repeat research passes (target: zero without new evidence).
- Tool/test outcomes: useful, inconclusive, failed, or not applicable.
- Baseline changes (target: none before approval).
- Current gate and next concrete blocker.

Across decks, review where time is being spent. If the same rules question recurs across decks, create a reusable sourced rules note and link it rather than rewrite the same analysis. Shared notes must be generic enough to apply but each deck still needs a short commander-specific application.

## Pilot-specific current position

Abaddon Steps 1–5 are documented as bounded interaction work: inventory/triage, cascade and alternate-cost sequencing, Harnfel and Bituminous Blast, and Blasphemous Act. The frozen list remains unchanged. Next planned bounded gate: current Oracle text and color-identity refresh for the exact 94 distinct names. Finalization remains NO until all gates and explicit user approval are complete.

## Reusable rule

**Research once, record once, reuse with a commander-specific check, and verify every write.** Optimize the workflow, never by skipping the checks that prevent a bad decklist.
