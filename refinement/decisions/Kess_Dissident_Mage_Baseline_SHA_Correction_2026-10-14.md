# Kess, Dissident Mage — Baseline Artifact SHA Correction

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14

The first Kess complete-gate run correctly failed because the baseline artifact SHA recorded in the gate config did not match the repository baseline bytes.

- Baseline artifact: `refinement/decklists/Kess_Dissident_Mage_Current_Cycle_Baseline_2026-10-14.txt`
- Incorrect previously recorded artifact SHA-256: `49dd9a466452c2be53fa4143b0398276021c0bec22c5a9f9f5ce97a22ad5f7da`
- Correct repository artifact SHA-256: `a36c08b80e153c5a0708f9031f81d2cc30d26674c5b8efc510319344926514b2`
- Authoritative source CSV SHA-256 remains: `b6d42012e6c7c3f9d5143d7cdb3e3608e611ae56247f2b00d13f6e87549440c7`
- Kess approval-candidate SHA-256 remains unchanged: `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`

The gate configuration was corrected to the repository baseline SHA and rerun against the same exact candidate. The second run completed successfully with `APPROVAL_READY`, 100 cards, 100 distinct names, B/R/U color identity, rules PASS, official Commander legality PASS, zero project exceptions, and zero errors.

This correction changes no card in either the baseline or candidate. The earlier hash string in `Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md` should be read as superseded by this correction artifact.
