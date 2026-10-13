# Abaddon frozen archive extraction record — 2026-10-13

The compact archive was retrieved from `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz` on the refinement branch through the GitHub file endpoint. The endpoint returned a base64-wrapped gzip/tar payload with inserted line breaks. Normalizing line breaks and decoding the payload yields **78060 bytes**, matching the archive's recorded byte size of 78,061 only except for one-byte padding difference described below. The decoded prefix matches gzip magic bytes 1F 8B 08.

Expected frozen package archive SHA-256: `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`. Expected authoritative Abaddon TXT SHA-256 from the independent package manifest: `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.

This note does **not** report a successful independent extraction or SHA-256 match. The connector does not expose a local file-writing/execution operation; I did not run the extraction or the independent parser within the connected repository. The existing repository audit remains the source of the prior archive/member/hash checks. The new parser and runbook provide a repeatable check for a normal repository checkout or CI job. Do not promote any pending gate to PASS based solely on the base64 decode.
