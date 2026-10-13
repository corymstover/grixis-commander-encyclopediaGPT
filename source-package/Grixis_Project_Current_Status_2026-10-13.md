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

## Latest Abaddon independent static metadata audit — 2026-10-13 UTC

The audit is implemented in `scripts/audit_abaddon_baseline_metadata.py`, with helper tests and workflow `.github/workflows/verify-abaddon-baseline-audit.yml`. The latest successful CI run is [38345446231](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38345446231), and its machine-readable output is [artifact 11787549914](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38345446231/artifacts/11787549914).

**Observed output:** 100 total cards including commander; 94 unique card names; one Abaddon commander marker/copy; zero nonbasic singleton violations; all 94 unique names join exactly once to the deck-scoped row in the 2026-10-12 Scryfall overlay; zero missing/ambiguous rows; zero required metadata-field issues; all recorded printing status values are exact; all metadata color-identity checks pass. This is a dated metadata/static membership pass, not a fresh official ban-list check at approval time and not an exhaustive interaction/strategic optimality certification.

The audit code uses the overlay's actual schema and scopes every join by both deck ID and exported card name. Earlier failed runs exposed two defects (wrong card-name column assumptions, then project-wide name-only joins that collided across decks). Those runs were kept as CI history; they are superseded by the current deck-scoped passing run. Keep the failed history rather than pretending the first implementation was correct.

### Current Abaddon audit checklist

- [x] Frozen compact archive hash verified.
- [x] Baseline TXT hash verified.
- [x] Exactly 100 total cards and one Abaddon commander marker.
- [x] Singleton/copy rules checked.
- [x] 94/94 exact deck-scoped metadata matches.
- [x] Oracle ID and Oracle text present for all 94 names.
- [x] Scryfall identity-check field is PASS for all 94 names; blank color identity is correctly accepted for colorless cards.
- [x] Current stored Commander legality fields are present and no overlay metadata join issues remain.
- [ ] Re-run fresh official Commander legality/banned-list validation immediately before approval.
- [ ] Finish the full card-specific interaction audit and source each nontrivial rules claim.
- [ ] Independently compare any proposed final list/hash against the frozen baseline and verify current copy-paste export.
- [ ] Present exact list for explicit user approval. Final gate remains NO until approval.

No decklist was changed in this audit.

## Stepwise continuation — interaction audit coverage control

The next bounded step is recorded at [Abaddon Interaction Audit Coverage Plan](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Interaction_Audit_Coverage_Plan_2026-10-13.md). It formalizes an inventory of all 94 unique names in the frozen deck and maps each to existing rules/interaction coverage before researching only uncovered material dependencies.

The current interaction review is extensive, but its own section 7 still marks all-card interaction closeout and the exact final-list certificate OPEN. The new plan therefore does not claim the audit is complete. It preserves existing closed findings and the inconclusive Aurora Phoenix comparison, forbids baseline changes during the audit, and separates the dated metadata pass from the fresh official legality check required at approval time.

**Current step:** coverage-control plan committed; card-by-card mapping and remaining interaction review are the next work unit. The frozen list, finalization gate NO, and historic approvals remain unchanged.

### Step 1 completed — Abaddon interaction coverage inventory (2026-10-13 UTC)

The frozen 100-card Abaddon TXT has been inventoried into [Abaddon Interaction Coverage Inventory](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Interaction_Coverage_Inventory_2026-10-13.csv). All 94 unique card names are represented. The existing review explicitly mentions 33 names; 61 are not explicitly mentioned and have been queued for role-based triage. Explicit mention is not itself a certification, and absence from the narrative review is not automatically a defect. Step 2 is to assess the 61 names by role and open rule-level reviews only for material interactions/dependencies. No decklist changes were made; final gate remains NO.

### Step 2 completed — role-based triage of remaining Abaddon names (2026-10-13 UTC)

The 61 names absent from the prior narrative review have now been triaged in [the expanded interaction review, Section 8](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md). The review documents relevant conditions for mana-base lands, channel abilities, alternative/free costs, mana-value invariance, Force of Negation/Pact of Negation limitations, Cabal Ritual threshold, Chrome Mox imprint, Nightscape Familiar cost reduction, Gamble discard contingency, cantrip/draw timing, and Thermo-Alchemist threshold setup.

This closes the **first-pass role-based triage** of the 61 names, not the entire 94-card interaction certificate. The 33 names already mentioned in the prior review still require context-level confirmation; the high-impact Breach sequence and remaining rules claims still require a dedicated final check. No cards changed; finalization gate remains NO.

### Step 3 bounded audit — Underworld Breach package (2026-10-13 UTC)

The standalone [Abaddon Breach Sequence Audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md) now records the package's necessary starting zones, costs, fuel accounting, storm/copy distinctions, finish conditions and interruption points. Its disposition is **PARTIALLY VERIFIED** because no exact inventory/iteration fuel ledger was available to certify a repeatable loop from a specific starting state. This avoids calling the package an unconditional infinite. No list changes; final gate remains NO.

### Step 3 current-source spot-check logged

The Breach/LED/Brain Freeze bounded audit was checked against the current Magic Comprehensive Rules (effective September 25, 2026) and current card reference pages. The rules concepts are supported, but the package remains **PARTIALLY VERIFIED** because no exact starting-zone inventory and iteration-by-iteration mana/fuel ledger has been proven. The next task is not further generic combo research: verify the 33 previously mentioned card entries in context and then determine whether a worked combo state can responsibly be provided from the actual frozen list resources. Current official Commander legality, final list/hash checks, and user approval remain outstanding.

### Step 4 — explicit per-card triage record (2026-10-13 UTC)

A more detailed [Abaddon Interaction Triage CSV](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Interaction_Triage_Updated_2026-10-13.csv) now assigns per-name notes to the 94 distinct card names, keeping routine-role cards distinct from material interactions. It tightens coverage labels for two names where the first inventory overcalled explicit coverage: Birgi // Harnfel (the old review discussed Birgi but did not analyze the Harnfel face) and Bituminous Blast (listed in the blueprint, but not substantively explained in the interaction review). These are now flagged for a brief context check rather than counted as fully closed.

The triage CSV remains a working coverage tool, not an independently validated final certificate. Several notes are source/Oracle spot-check targets rather than a claim that every exact interaction has been exhaustively checked. No cards changed; final gate remains NO.

### Detailed card-level triage corrections

The [updated triage CSV](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Interaction_Triage_Updated_2026-10-13.csv) distinguishes names that were only mentioned in a summary from those with an actual rules discussion. In particular, Birgi // Harnfel had been counted as explicit coverage even though only Birgi was discussed; Bituminous Blast was present in a package list but lacked a detailed interaction analysis. Both are now flagged for a contextual check. The coverage inventory remains a work-in-progress aid, not a completion certificate.

### Fresh official Commander banned-list check — 2026-10-13 UTC

The official Wizards [Banned & Restricted list](https://magic.wizards.com/en/banned-restricted-list) was checked against all names in the frozen Abaddon baseline. No Abaddon decklist card appears on the official Commander banned list. The list labels Lutri, the Spellchaser as banned only as a companion, but Lutri is not in this Abaddon list; other project-authorized exceptions are likewise not relevant to Abaddon.

**Scope of this PASS:** current official Commander banned-list checkpoint only. It does not refresh every card's Oracle text or color identity, prove all interactions, or approve the deck. The Scryfall exact-printing/Oracle/identity overlay remains dated 2026-10-12. Abaddon's final gate remains NO.

### Step 5 — final-list integrity checkpoint recorded (2026-10-13 UTC)

The [Abaddon Final-List Integrity Checkpoint](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Final_List_Integrity_Checkpoint_2026-10-13.md) consolidates the existing successful structural audit, the pinned list hashes, and the fresh official Commander banned-list check. Its disposition is **PASS WITH OPEN RULES/CURRENT-ORACLE GATES**, not deck approval. It explicitly separates the 2026-10-12 Scryfall metadata snapshot from the official October 13 banned-list check and records no decklist changes.

Next work remains narrow: current live Oracle/identity validation for the exact 94 names, close remaining material contextual entries (including Harnfel face text), and retain the Breach combo as PARTIALLY VERIFIED unless a concrete starting inventory and mana/fuel ledger is proven. Final gate remains NO.

### Step 6 — worked Abaddon Breach sequence added (2026-10-13 UTC)

The [Breach package audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md) now includes a concrete ten-cycle line from a specified board/graveyard/library state, with resource accounting and a Wheel of Fortune finish. The combo's **specific-sequence** status is upgraded from PARTIALLY VERIFIED to **RULES-COHERENT WITH SPECIFIC CONDITIONS** for that uninterrupted state. The review explicitly does not call this an unconditional infinite or a guaranteed line through interaction.

Remaining overall gates are unchanged: live Oracle/identity refresh for the exact list, completion of all material card-level contextual checks, final export/hash/count verification, and explicit user approval. No card change has been made; final gate NO.

### Step 2 completed — role-based triage of unmentioned cards (2026-10-13 UTC)

All 61 cards absent from the existing narrative interaction review were classified in [Abaddon Unmentioned Card Role Triage](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Unmentioned_Card_Role_Triage_2026-10-13.csv), with a summary at [Abaddon Role Triage Summary](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Role_Triage_Summary_2026-10-13.md). The main material items identified for sourced follow-up are top-deck/cascade sequencing; hand-cast/alternate-cost free interaction; Jeska's Will and cast-from-exile payoffs; Thermo-Alchemist's repeated opponent damage; Underworld Breach resource constraints; channel abilities and land-type effects; and Blasphemous Act's own-board opportunity cost. Ordinary fixing lands and routine ramp/draw/tutors were not promoted to full interaction reviews without a material dependency.

This was a role-based triage pass, not a fresh card-by-card Oracle certification. No decklist changes were made; final gate remains NO.


### Step 7 completed — Abaddon material sequencing spot-check (2026-10-13 UTC)

The expanded [Abaddon interaction review](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) now records current-rule findings for top-deck/cascade sequencing, six free or alternate-cost interaction spells, Jeska's Will exile casts, and Thermo-Alchemist's repeated damage/threshold timing.

Key practical findings: mana value is not reduced by alternate costs; cascade compares the revealed card against the cascade spell's mana value, not Abaddon's threshold; mana-value-1 cantrips/tutors cannot hit a lower-mana-value card with Abaddon-granted cascade; Pact of Negation's mana value 0 yields no legal cascade hit; Force of Negation's free mode is opponent-turn-only; spells cast from Jeska's Will's exile permission do not qualify for Abaddon's hand-only grant; and Thermo-Alchemist damage must happen before the relevant spell is cast to raise that spell's eligibility threshold.

This closes those four bounded contextual groups only. It does not close all 94 card dispositions, the fresh exact-list Oracle/identity refresh, the final list/hash verification, or explicit approval. No cards changed; finalization gate remains NO. The next step is a short, sourced context check of the remaining named exceptions in triage (especially Harnfel's reverse face and Bituminous Blast), not a new candidate-ranking or Forge run.


### Step 4 logged — Harnfel and Bituminous Blast

Two contextual gaps are now documented in [Abaddon Step 4 Context Check](../refinement/tests/Abaddon_Step_4_Context_Check_2026-10-13.md) and reflected in the coverage plan. No decklist changes. The next bounded check is Blasphemous Act's creature-only damage and own-board trade-off. Full interaction closeout, current exact-list Oracle/identity refresh, final integrity checks, approval-time legality check, and explicit user approval remain open. Final gate: NO.
