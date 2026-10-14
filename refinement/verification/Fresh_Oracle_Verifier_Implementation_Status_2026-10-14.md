# Fresh Oracle verifier — execution and evidence contract

The protocol's Section 11 is a hard gate. The local `verify_grixis_fresh.py` preflight exists but must not be treated as a complete production verifier: its execution environment lacked Scryfall network access, and manual official banned-list and combo-rule review remains mandatory.

**Current status:** retrospective #1–8 BLOCKED, not passed. No approved decklist altered.

Implementation requirements: exact approved-list source; fresh Oracle ID and full card-face text for every name; live Commander legality; official banned-list reconciliation; companion and documented exceptions; separate manual rules attestation; reproducible per-card CSV with timestamps and hashes. The script must fail closed if any source cannot be reached or if manual attestation is missing.

This checkpoint is intentionally not a success claim. See `refinement/verification/Retrospective_1_to_8_Fresh_Oracle_Gate_Checkpoint_2026-10-14.md`.
