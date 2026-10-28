# Wick, the Whorled Mind — M7 Rev1 owner-approved source verification

Scope: the exact new 100-card Rev1 approved by Cory (SHA-256 `1aea08a53b983ee9ce083c1e9c95b366a3abc478a43b75517714d6280b484c48`), staged for canonical main after all required checks. All original October 15 approval files stay immutable.

## Original source to new list

- Original approved October 15 raw hash `f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98` verified against live canonical state before revision; separate unchanged original file is preserved.
- Proposed approved source `refinement/decklists/Wick_the_Whorled_Mind_M7_Rev1_Approved_2026-10-27.txt` exactly matches raw bytes of engineering `data/grixis/m7/candidate_lists/Wick__the_Whorled_Mind_M7_Rev1.txt` at PR #746 tested head `d6ca6d87c7174fbef0de888bd75bd9b21ad88e6f`.
- One commander, 99 library copies, 99 distinct card names including Wick, only Island ×2 repeated; nine physical one-for-one additions and cuts, 36 land-capable cards.
- All card identities and Commander-legal/Grixis flags match the 2026-10-27 source-bound Scryfall snapshot `data/grixis/m7/wick_rev1/Wick_M7_Rev1_Scryfall_snapshot.json` (111 unique names across three portfolios and baseline). This remains a dated verification, not a promise about future ban-list updates.

## Mechanical and structural evidence

- Original deck-specific M6 plan: `data/grixis/m6/test_blueprints/Wick__the_Whorled_Mind.json`, immutable Git blob `f1c22505ea4afed4914167c0fb83ae14cc13b884`: 5 P0 (C1,K1,K2,K3,F1) and 9 P1 (K4,K5,E1,E2,W1,W2,W3,F2,F3).
- Actual exact-source M7 suite `data/grixis/m7/wick_rev1/verify.py` executes 18 deterministic tests: one complete source/legality check, twelve modeled methods covering every one of the original 14 named case IDs (two paired methods), and five distinct swap/Oracle checks. These are scoped rules/cost/stack fixtures, not complete gameplay simulations.
- [Dedicated exact-head success](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40621910172) verifies canonical October 15 baseline hash and 9-/11-/12-swap complete candidate hashes, official-source snapshots, error preconditions, UBR mana restrictions, Rat/Snail loop, infect source, Ozolith delayed counter transfer, damage/draw, Yawgmoth life cost, Massacre and Malakir front/back Oracle.
- [Global M7 contract success](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40621910756) and `data/grixis/m7/decision_reviews/Wick__the_Whorled_Mind_rev1.json`: nine substantive swaps, twelve material judgments, whole-99 CSV and complete 11/12 alternatives. The unrelated Lord Xander schema-checksum CI failures are disclosed, not falsely treated as Wick failures.
- Exact documented M7 P0/P1 mapping and known limits: `data/grixis/m7/wick_rev1/Wick_M7_Rev1_Verification_Receipt_2026-10-27.md`.
- Historical M6 I/J `data/grixis/m6/ij/input_receipts/wick-the-whorled-mind.json` was only input-attested, downstream Phase B not replayed. New M7 case mapping is not a retroactive independent M6 certificate.

## Required canonical gate

The canonical repository now requires a per-exact-SHA `refinement/verification/m7_certification_transfer/Wick__the_Whorled_Mind_1aea08a53b983ee9.json`, with fourteen explicit executed case records and the M7 CI URLs. This verification must be accompanied by that attestation and by exact-head canonical `scripts/verify_m7_certification_transfer.py --check` plus the existing approval tests. An unrelated previously missing transfer attestation may block the repository-wide gate; do not merge while any required checker is failing or amend another locked deck without separate authorization.
