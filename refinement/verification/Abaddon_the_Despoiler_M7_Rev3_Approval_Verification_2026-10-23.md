# Abaddon Rev3 — canonical exact-source lock verification

Date: 2026-10-23. Scope: exactly one newly owner-approved M7 version, **not** wholesale M6/M7/M8 acceptance.

## Source chain and immutable history

1. Historical Oct13 Abaddon approved source retained: `refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt` SHA256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.
2. Rev2 Abaddon previously approved on Oct22, retained unchanged: `refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt` SHA256 `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`.
3. Rev3 exact M7 candidate from engineering `data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev3.txt`, raw SHA256 `5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24`. `data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json` marks exact 100 **owner-ready**, source-bound by source-checked Rev2 hash/git blob, Oracle logical hash, candidate tests, and approval-required state.
4. This session's explicit owner message authorizes superseding Rev2 **only** with that exact digest, and the new list is now at `refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt`.
5. `state/current_deck_overrides.json` Abaddon entry and only the Abaddon row in `refinement/Deck_Refinement_Tracker_2026-10-12.csv` update to Rev3 date/hash/artifacts. Other 61 deck records and tracker rows must compare byte-identical to the repository's pre-merge `main`.

## Structural and Oracle certification scope

- Exactly 100 cards including commander, 95 card names, 34 lands, repeats only basic 3 Island / 2 Mountain / 3 Swamp.
- Six genuine substitutions against immutable approved Rev2; six adds/six cuts.
- Commander identity Abaddon Grixis U/B/R. Each of 95 distinct names official Commander legal and within identity according to archived source snapshots, including selected new cards; no project exception.
- Rules checks include 14 actual changed-card deterministic paid source/stack/trigger cases; 104 historical P0 cases split 27 removed-card-only comparators, 77 retained rule facts; 14 historical P1 split 3 excluded comparator cases / 11 retained facts. Historical tests are *not claimed re-executed as the new physical list*.
- Scoped M6 I local optimum among four fully specified physical stage13 portfolios and M6 J source-hash bounded reproducibility PASS per Stage20; neither implies measured multiplayer win rates or automatically accepts project-wide M6.10.
- Exact-head engineering [PR #645 Actions](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39911935249) success (93 steps); [PR #648 Actions](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39913153403) success (93 steps); corrected printed Call Forth `{5}{R}{R}{R}` in documentation.
- Official power bracket **4 — Optimized**; Archidekt tags **Cascade / Exile Cast / 40K Chaos**.

## Approval and lock rule

One-deck **EXPLICIT OWNER APPROVAL** is recorded in `refinement/approvals/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.md`. Canonical lock supersedes but **does not erase** historical Rev2. Admiral and other 60 approved/locked records remain unchanged. Aggregate milestone acceptance is not inferred. Continue encyclopedia work with deck #3 only when directed by project workflow and current owner instructions.
