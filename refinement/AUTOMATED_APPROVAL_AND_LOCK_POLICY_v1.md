# Automated Approval and Lock Policy v1
**Effective:** 2026-10-13  
**Scope:** 62-deck Grixis Commander Encyclopedia refinement cycle  
**Authority:** User-delegated autonomous deckbuilding and finalization

## Policy change

The user explicitly delegates final approval and lock decisions to the assistant based on informed, commander-specific judgment. The assistant no longer needs to present a deck for separate user approval once all mandatory verification gates pass. This replaces the prior explicit-user-approval gate for the current refinement cycle.

This delegation authorizes the assistant to select defensible additions/cuts, decide that zero changes are best, finalize a list, approve it, and mark it locked. It does not authorize ignoring an unresolved correctness issue or claiming unsupported verification.

## Mandatory gates before auto-approval

A deck may be auto-approved/locked only when the record shows all of the following:

1. **Baseline integrity:** The authoritative current CSV/TXT pair is identified, reconciled, and preserved; source and revised list hashes are recorded.
2. **Commander-first strategy:** A commander-specific blueprint states the core plan, win conditions, key packages, vulnerabilities, and natural power ceiling.
3. **Candidate decisions:** Material candidates have been considered against plausible cuts. The decision ledger records accepted/rejected/deferred decisions and reasons. Rankings are leads, not mandates.
4. **Exact-list identity and rules:** Current Oracle text, exact card identity/printing as relevant, color identity, and material rules/interaction/combo dependencies are checked against the exact revised list.
5. **Legality and exceptions:** Official Commander legality is checked at finalization time. Each permitted project exception is separately recorded and never mislabeled as officially legal.
6. **Deck construction:** Exactly 100 cards including commander (and documented companion handling where applicable), singleton/copy rules, commander/color identity, and list export/hash all pass independently.
7. **Strategic coherence and power:** Mana, consistency, interaction, engines, closing lines, and commander synergy receive a reasoned final review. No automated rank or structural audit substitutes for this judgment.
8. **Evidence and reproducibility:** A verification certificate, final decklist, hash, decision ledger/summary, and tracker/status update are present and cross-consistent. Automated checks pass where applicable.
9. **No unresolved material blocker:** Unknown Oracle identity, unexpected legality concern, card-count discrepancy, unresolved high-impact rules interaction, or a materially inconclusive required test blocks approval until resolved or explicitly dispositioned with a defensible evidence-backed rationale.

## Automatic decision

- If all mandatory gates pass, the assistant may finalize, approve, and lock the deck without another user confirmation.
- If any hard gate fails or required evidence is missing, keep that deck unapproved/unlocked, record the blocker, and continue bounded remediation.
- A test may be marked inconclusive where appropriate; it must not be misrepresented as positive evidence. Do not rerun an inconclusive test unchanged without a material improvement in method or evidence.
- No change is a valid outcome when the strongest defensible decision is to retain the list.
- Use targeted, risk-based review to avoid needless work, while never skipping mandatory checks.
- Approval is based on documented evidence and informed judgment, not a claim of mathematically perfect deck construction.

## Project state and preservation

The active refinement cycle supersedes historical approval labels; source archives, frozen baselines, and historical records remain immutable. Update only the active campaign records and final deck artifacts. Preserve approved decks and do not reopen them absent a material correctness issue or explicit user request.

The current campaign proceeds in authoritative tracker order. Each deck is assessed individually and retains its own natural strategy and power ceiling.

## Audit labels

Use consistent statuses:
- `UNAPPROVED / UNLOCKED`: work remains or a required gate is unresolved.
- `READY FOR AUTO-APPROVAL`: all mandatory gates and artifacts are complete; final review has not yet been recorded.
- `APPROVED / LOCKED`: all mandatory gates passed, assistant decision and rationale recorded, final hash/certificate/tracker cross-checked.
- `BLOCKED`: a material discrepancy or required gate failure prevents approval; include owner/action/evidence needed to clear it.

Each auto-approval entry must record the date, exact final-list hash, verification certificate path, key accepted/rejected changes (or reason for zero changes), gate outcomes, and any bounded residual uncertainty.


## Full-strength refinement standard — 2026-10-13

The user's instruction is to **not be conservative about deck adjustments**. Review each deck thoroughly and make as many or as few changes as the evidence warrants. Do not preserve cards merely because they were in the baseline, and do not optimize for a low change count.

For every deck, the assistant must:
1. Reassess the entire list in commander-specific context, not merely the top-ranked candidates or obvious weak cards.
2. Review every card's role, synergy, efficiency, curve/mana requirements, redundancy, interaction, resilience, and contribution to a win condition. Identify low-impact, replaceable, off-plan, or actively conflicting cards.
3. Build a broad enough commander-specific candidate pool to challenge the baseline, using ranked candidates as discovery leads and targeted current source research where it can change a decision.
4. Consider multiple plausible cuts and additions rather than stopping at the first acceptable swap. Evaluate packages and structural changes when the commander's strategy benefits from them.
5. Make all justified improvements, whether that means many swaps, a small set of swaps, or no changes. The count is an outcome, not a target. Do not manufacture changes for the appearance of activity.
6. Record clear decisions for meaningful candidates: accepted, rejected, or deferred—with the strategic reason and any material evidence gap. Explain the opportunity cost of important inclusions and cuts.
7. Re-evaluate the deck as a whole after swaps. Recheck mana curve and land/ramp balance, engine density, interaction coverage, redundancy, card advantage, win-condition density, and commander synergy.
8. Perform the full mandatory technical gates in this policy before automatic approval and locking. Thorough optimization is not permission to waive verification.

A candidate is not rejected solely because it is unfamiliar, outside inherited rankings, or requires broader structural revision. A candidate is not included solely because it is highly ranked, popular, expensive, or powerful in generic Grixis. Judge it against the deck's commander-specific plan and natural power ceiling.

The final review should explicitly state whether the baseline was meaningfully challenged, the strongest alternatives considered, the changes made (or why no changes were justified), the resulting strategic trade-offs, and any bounded unresolved uncertainty that is material to confidence. When a required hard correctness check remains unresolved, the deck stays unapproved/unlocked until it is cleared.
