# Abaddon archive payload verification — 2026-10-13

The compact archive's repository audit already records SHA-256 `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`, 124 expected members, and byte-for-byte agreement with the verified source ZIP. The archive is retrievable through GitHub's file tool as a base64-wrapped text response; that response contains line breaks which must be removed to decode correctly. The current chat's GitHub integration does not provide a local execution environment or Actions workflow-dispatch action, so the newly committed parser cannot be run inside the repository from this tool session.

Do not treat the parser files as successful executed tests. Use a normal repository checkout/CI run to run `Abaddon_Independent_Final_Decklist_Check_2026-10-13.py`; then record the exact output. Until this occurs, rely only on the previously committed baseline audit/hash manifest for structure, and keep the approval gate NO.
