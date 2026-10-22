# Abaddon the Despoiler — M7 exact-source final approval verification

Date: 2026-10-22. Scope: **one deck and one expressly approved M7 version**, never all 62.

## Source chain

1. Frozen previous approved list: `refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt` with raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; file remains immutable.
2. Owner-presentable, strict candidate-bound M7 100 in engineering `data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt`, PRs #578–#582, final M7 decision packet `data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev2.json`.
3. Exactly copied original raw UTF-8 LF bytes into canonical `refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt`. Required SHA-256: `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`. The current `state/current_deck_overrides.json` and tracker must both reference precisely this digest.
4. Cory replied “Approve” after receiving this **specific** proposed 100 and SHA, recorded in `refinement/approvals/Abaddon_the_Despoiler_M7_Approved_2026-10-22.md`.

## Verified properties and evidence

- Physical 100 cards including single commander; first line `1x Abaddon the Despoiler [Commander]`.
- 34 lands; Island, Mountain and Swamp quantities 3 each; no illegal nonbasic repeats.
- Current Oct22 2026 Scryfall Oracle snapshots cover all 100 required names across the candidate and two other full-100 alternatives, Grixis color identity and official Commander legality. No Abaddon project-specific exception.
- Exactly six additions and corresponding six removals; comprehensive 99-slot audit, 13 material judgments, 10 challenged incumbents, two physically complete five-swap alternatives.
- Decision-scoped Abaddon M6 I tested-pool local-optimum and J source-hashed reproducibility sidecars revalidated for **this six-swap result**, with 104 previously executed P0 + 14 existing residual P1 + 12 revision-specific bounded physical mechanics cases. The model is not an exhaustive gameplay win-rate simulator.
- [PR #582 exact-head Actions 39836471622](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39836471622) concluded **success**; previous [PR #581 exact-head](https://github.com/corymstover/GrokBotMTGCompanion/pull/581) passed.
- Correct Pass C provenance: GPT-6 owner-equivalent via authorized waiver, **0 technically independent third-model executions**.
- Power Bracket 4 — Optimized; Archidekt tags Cascade, Exile Cast, 40K Chaos.

## Approval and preservation gates

- Cory's current M7 Abaddon approval: **COMPLETE**.
- Canonical new exact approved list: **LOCKED** once this transaction lands in `main`.
- Other 61 existing approved and locked deck entries: **unchanged** in this transaction.
- Old approved Abaddon list, its approval SHA, and prior two-swap withdrawn research: **preserved as historical artifacts**.
- Overall M6.10 milestone certification/acceptance and M8 acceptance: **NOT AUTOMATICALLY DECLARED**.
