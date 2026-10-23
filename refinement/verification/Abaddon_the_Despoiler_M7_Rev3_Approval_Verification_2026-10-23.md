# Abaddon the Despoiler — Rev3 canonical exact-source approval verification

**Date:** October 23, 2026. **Scope:** Approved and locked one exact Rev3 100-card deck; Rev2 history preserved.

## Source chain and checks

1. Owner's explicit approval: twice issued in project conversation for exact raw SHA-256 `5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24`, specifically replacing current locked Rev2 `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`.
2. Source: `corymstover/GrokBotMTGCompanion:chatgpt-cycle76-m6-refinement/data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev3.txt`. Raw bytes independently SHA-256 checked before canonical write; Git blob SHA `13ada6e731799dc77519a907e1a3c37fc1575e6b`.
3. New canonical copy: `refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt`. The previously canonical `refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt` remains unchanged as approved history (its Git blob SHA `6ce148a6a291dd3dc349e10fe9dd1e1c29ea8aac`).
4. Exactly 100 physical cards, including commander first, 95 unique names and only repeated basic lands: Island ×3, Mountain ×2, Swamp ×3; 34 lands; exact six one-for-one swaps including a single Mountain converted to Mount Doom.
5. Fresh source bound Scryfall Oracle and Commander legality / UBR identity across all 95 unique names recorded in engineering `data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json`. No project exceptions.
6. New bounded changed-card mechanics cases: 14 passing P0 fixtures, including paid Mage Offspring, separate cascade grants under Sakashima, first-main Sanctum life loss, Sheoldred's post-Wheel (not retroactive) life-loss triggers, Mount Doom payment, and Rule of Law responses. The previous 104 P0 cases are not all transferable: 27 rely on removed/older cards; 77 potential remaining cases have qualified reused evidence only. 14 historical P1, including three nontransferable counterfactuals.
7. Engineering candidate-specific local-best / reproducibility sidecars `data/grixis/m6/ij/adjudications/Abaddon_protected_six_stage20_20261023.json`, `data/grixis/m6/ij/candidate_certificates/Abaddon_protected_six_stage20_20261023.json`, `data/grixis/m6/bundles/candidate_exact/Abaddon_protected_six_stage20_20261023.json`; Stage18 mana and adversarial reports; four full 100-card configurations including five/six/seven changes.
8. Decision gate Rev3 `data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json` in engineering [PR #645](https://github.com/corymstover/GrokBotMTGCompanion/pull/645) successfully passed [93 exact-head CI steps](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39911935249). Mana text typo corrected without changing deck in [PR #648](https://github.com/corymstover/GrokBotMTGCompanion/pull/648), [CI PASS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39913153403).
9. Owner decision now explicitly given, replacing earlier `READY_FOR_EXACT_OWNER_APPROVAL` condition for this exact candidate. Canonical state authority `state/current_deck_overrides.json`, tracker row 0, and `tests/test_current_cycle_state.py` must refer to new digest and new file.
10. Admiral Beckett Brass canonical SHA `ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000` and all 60 remaining override entries are unchanged.

## Verified scope / limits

**Commander:** Abaddon the Despoiler. **Power Bracket:** 4 — Optimized. **Archidekt tags:** Cascade / Exile Cast / 40K Chaos.

The Pass C owner waiver was an explicitly non-independent equivalent, not independent third-model output. Neither targeted source-derived game-state fixtures nor four-configuration comparative judgment support empirical multiplayer win rates. Single-deck canonical M7 approval is not approval/acceptance of the global M6.10, M7, or M8 milestones. Canonical lock is complete only after merge + exact-byte post-merge verification.
