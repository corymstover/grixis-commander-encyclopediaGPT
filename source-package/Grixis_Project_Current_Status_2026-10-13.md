# Grixis Commander Encyclopedia — Current Status

**Status snapshot:** 2026-10-13 UTC  
**Scope:** 62 commander-first Grixis decks  
**Frozen authoritative list snapshot:** 2026-10-12  
**Active work branch:** `refinement/campaign-2026-10-12`  
**Baseline branch:** `baseline/freeze-2026-10-12`

## Executive status

The 2026-10-12 baseline remains frozen and structurally verified. All 62 CSV/TXT deck pairs reconcile; each list has exactly 100 main-deck-plus-commander cards and passes singleton/copy-rule checks. The verified compact archive contains all 124 lists byte-for-byte. Current Scryfall refresh matched 5,964/5,964 decklist rows to exact printing/name records with no unresolved identities, Oracle IDs/text, commander color-identity mismatches, or unexpected official Commander-illegal rows outside registered project exceptions.

The active refinement branch now has a reproducible, CI-verified exact draw-density analysis for Abaddon. Forge test infrastructure has advanced beyond the original source-only probe: its pinned release and 95 card-script name mappings were verified, the exact baseline and isolated test variant loaded in Commander mode, and a bounded 3+3 fixed-opponent pilot completed. However, the candidate comparison was **INCONCLUSIVE** because neither Mind's Desire nor Aurora Phoenix was cast in any of the six registered games. Do not reuse those games as card-performance evidence or rerun the same AI comparison. The relevant workflow is now manual-dispatch only.

**No baseline decklist has been changed, no approved deck has been reopened, and no new deck has been finalized.** The Abaddon finalization gate remains NO.

## Verified baseline and source integrity

- Original source ZIP: 4,193,697 bytes; SHA-256 `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`.
- ZIP integrity PASS; 165/165 expected files match the internal manifest's byte sizes and SHA-256 hashes.
- Four authoritative 2026-10-12 FINAL CSV/TXT ZIPs match the source manifest.
- Compact repository archive: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`, SHA-256 `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`; all 124 members verified byte-for-byte.
- Structural validation: 62/62 CSV/TXT reconciliations; 62/62 exact 100-card totals; 62/62 singleton/copy-rule passes; 6,200 deck card copies plus the separately tracked companion.
- The raw source package is still not fully mirrored as individual files in GitHub. Remaining raw-mirror gaps are documented in [Source Consolidation Reconciliation](Source_Consolidation_Reconciliation_2026-10-13.md). The original archives/datasets remain retained in the verified source package.

## Current card identity and legality metadata

The Scryfall refresh snapshot was updated at `2026-10-12T21:06:24.577Z`.

- Exact printing/name matches: 5,964/5,964.
- Ambiguous/unmatched names: 0.
- Missing Oracle IDs: 0.
- Blank Oracle text: 0.
- Commander color-identity mismatches: 0.
- Unresolved commanders: 0.
- Unexpected official Commander-illegal rows outside registered project exceptions: 0.

Registered exceptions remain separately documented and must not be described as officially legal: Lutri as the designated companion, Trade Secrets and Yawgmoth's Bargain in the designated Bjorna // Cecily deck, plus the future-release cards The Madcap Jester, Dragon's Smile, and Tresserhorn's Lord, Returned.

Metadata correctness is not equivalent to complete rules/interaction or strategy verification.

## Abaddon refinement

### Completed

1. Commander-first blueprint and target ceiling documented: cascade thresholds built from same-turn opponent life loss; value from spells cast from exile; amplified damage; compact Breach/LED/Brain Freeze route. The blueprint correctly records Abaddon as five mana (mana value 5).
2. Candidate discovery and targeted triage completed for 60 commander-specific candidates, including a targeted review through rank 100. Candidate rankings remain evidence for review, not automatic changes.
3. Decision ledger records alternatives with roles, proposed cuts, trade-offs and decisions. Aurora Phoenix vs Mind's Desire is closed INCONCLUSIVE with the frozen baseline preserved.
4. Expanded rules/interaction review documents key cascade threshold/timing, damage and life-loss amplification, cast-from-exile triggers, spell-copy vs cast distinctions, and core Breach/LED/Brain Freeze prerequisites.
5. Exact hypergeometric baseline consistency analysis now exists in `scripts/analyze_abaddon_baseline_consistency.py`; tests are in `tests/test_analyze_abaddon_baseline_consistency.py`; the report is `refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md`. GitHub Actions [run 38343814218](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38343814218) passed its tests, report regeneration, and committed-report consistency check. This is a descriptive draw-density benchmark, not gameplay evidence or a pass/fail deck-quality score.

### Forge evidence and test ruling

Pinned Forge release `forge-2.0.15` at commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676` has passed distribution checksum checks and runtime/source-presence checks. The active workflow found 95/95 name mappings (94 variant names plus baseline-only Mind's Desire). Both the frozen baseline and the exact one-card Aurora Phoenix variant were prepared as 100-card DCK lists and loaded in Commander mode. Smoke logs showed ordinary Abaddon-granted cascade resolutions and an Underworld Breach escape cast; repeated identical commands produced identical normalized event sections.

The registered pilot [run 38341150840](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38341150840) completed three baseline and three variant games against a fixed Ruthless Regiment opponent, same numeric seed series and seat order, but without matched starting libraries. Neither Mind's Desire nor Aurora Phoenix was cast (0/3 each); no candidate-specific storm or graveyard-return line was observed; one variant ended in a timeout draw and had a runtime warning. The output cannot answer the candidate question.

**Decision:** close the Aurora Phoenix vs Mind's Desire comparison INCONCLUSIVE for this engine/setup. Keep Mind's Desire in the baseline; keep Aurora Phoenix as a separate test artifact only. Do not spend more runs on the same AI/input method. Forge is acceptable for pinned script mapping, deck import and exploratory smoke tests, but not qualified for this comparative strength decision or an unbiased multiplayer win-rate claim.

The same-seed pilot workflow was changed to manual dispatch only to prevent expensive automatic reruns. Exact baseline consistency CI [run 38343814218](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38343814218) passed. The latest pilot run [run 38343803830](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38343803830) also completed successfully as a workflow; that success means its scripted checks and registered exploratory pilot completed, not that the candidate comparison was conclusive.

### Remaining Abaddon finalization gates

- Complete a checklist-based audit of every remaining card-specific interaction/package materially relied upon by the list; the existing interaction review is extensive but not yet certified exhaustive.
- Independently validate the exact frozen baseline list against current Oracle identity, color identity, official legality and registered exception records before any final-list certificate.
- Record a final exact-list SHA-256 and an independent count/singleton verification at closeout.
- Resolve the slot decision with the already recorded inconclusive outcome and commander-identity/opportunity-cost rationale; no replacement card is justified by the current test evidence.
- Present the exact list for explicit user approval. Do not mark Abaddon final or change the baseline before approval.

See [Abaddon expanded interaction review](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md), [candidate ledger](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-12.csv), [Forge smoke-test report](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Forge_Smoke_Test_Result_2026-10-13.md), and [baseline consistency report](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md).

## Tracker truth

- All 62 decks: baseline structural and refreshed exact-printing/Oracle/identity/legality metadata checks pass, with authorized exceptions separated.
- All 62 current refinement finalization gates: NO under the new campaign protocol. This does not revoke historical approvals; all previously approved/locked decklists remain untouched.
- Abaddon: blueprint and candidate screening complete; Aurora/Mind's Desire closed inconclusive; exact draw-density report complete and CI-verified; full remaining card-specific closeout, independent final audit/hash, and user approval pending.
- Remaining 61 decks: commander-specific rules/strategy reviews and controlled refinement for this new campaign remain outstanding.

## Efficient next sequence

1. Continue only source-preserving, hash-verified consolidation where it removes a material workflow obstacle.
2. Finish Abaddon's remaining card-specific interaction checklist and independent audit preparation; do not repeat the inconclusive Forge AI comparison.
3. Close Abaddon only after all hard gates are met, present the exact list and rationale, and wait for explicit approval.
4. After approval, write the final hash/certificate and move to the next not-yet-refined deck. Never reopen an already approved/locked deck without an explicit request or a documented material trigger.
