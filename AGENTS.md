# Grixis Commander Encyclopedia — canonical M7 approval safety

This repository stores Cory Stover's exact 62 owner-approved Commander decks. The engineering and test repository is `corymstover/GrokBotMTGCompanion`. Before any new M6/M7 authored work, read its `AGENTS.md`, the M6 single-deck review standard, the decisive optimization/test-economy standard, and the current commander-specific M6 P0/P1 blueprint and I/J receipts.

## Mandatory final revision rule

**The original Abaddon M6/M6.1–M6.x system and later I/J/M7 gates are required, not optional.** GrokBot research is additional evidence, never a replacement for executed mechanical cases or the established decision schema.

Before asking Cory to approve an M7 candidate, or creating a canonical approval PR:

1. Recover live canonical raw SHA and original owner decisions, Grok first-pass research, frozen Oracle, EDHREC inclusion/high-lift discoveries, exact M6 case plan, completed P0/P1 runs, scoped I/J receipts, and prior 100-card alternatives. No new simulation if old evidence decides the question.
2. Compare the **exact final 100** with the Grok/I/J-tested 100. Reuse old cases only with source-bound proof that their cards, costs, rules conditions and adversarial assertions remain valid. Run invalidated or unexecuted mandatory P0 and relevant P1, recording the execution and exact-head CI evidence. An unexecuted plan or a structural unittest is not mechanical certification.
3. Run the actual engineering `scripts/grixis_m7_decision_gate.py --check` against a conforming final-revision packet. Record post-floor full-100 and alternate-package judgments. Five swaps are the ordinary owner-presentation minimum, never the target or cap; only an explicit deck-specific waiver changes that eligibility requirement.
4. Ask Cory to approve the **whole exact final list and raw SHA-256**. A routine "Proceed" never approves a list. Never alter an earlier lock because new evidence is incomplete.
5. Include `refinement/verification/m7_certification_transfer/<deck_id>_<raw_sha_first_16>.json` in the narrow canonical PR, using `refinement/verification/m7_certification_transfer/M7_EVIDENCE_TRANSFER_CONTRACT.md`. It must account for the authoritative P0/P1 IDs, I/J candidate scope, M7 decision-gate execution, exact Oracle/source, and actual owner approval.
6. Run `python scripts/verify_m7_certification_transfer.py --check` and all exact-head approval checks; merge only after PASS, then refetch main and independently verify exact bytes and approval registry. Never treat CI PASS as owner consent.

The frozen October 24 snapshot preserves 24 newly M7-approved raw SHA locks. The retrospective gap ledger identifies 20 revisions needing explicit original-to-final certification-scope reconciliation. **Those are engineering evidence gaps, not revocations of Cory's approvals.** Reconcile and record them without altering canonical lists or historical proof.

**Owner resolution 2026-10-27:** Cory explicitly confirmed, “Goben IS Green Goblin, theyre the same CARD.” Preserve the historical registry ID `Goben__Gene_Splice_Savant`, preserve the exact owner-approved Norman Osborn // Green Goblin 100-card artifact and its SHA, and use the specific engineering plan `Norman_Osborn_Green_Goblin` only for this SHA-bound, receipt-verified alias. `scripts/verify_m7_certification_transfer.py` must enforce this one-to-one identity crosswalk and reject any other alias or changed list. Neither pinned historical file is to be rewritten. The source decision is documented in `refinement/verification/m7_certification_transfer/Goben_Norman_Owner_Identity_Resolution_2026-10-27.md`; never silently generalize this equivalence to other commander IDs.

No prompt or future chat may waive this contract through omission. Any policy change requires Cory's explicit authorization and a documented code/CI update.
