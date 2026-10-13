# Abaddon frozen archive extraction record — 2026-10-13

The compact archive was retrieved from `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz` on the refinement branch through the GitHub file endpoint. After removing the endpoint's inserted line breaks, the response contains a base64 string of 104,084 characters, which decodes to 78,062 bytes if padded/decoded as a complete base64 payload; the committed archive manifest records 78,061 bytes. The leading bytes match gzip magic `1F 8B 08`, but the connector payload normalization does not permit a trusted digest comparison here.

Expected frozen package archive SHA-256: `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`. Expected authoritative Abaddon TXT SHA-256 from the independent package manifest: `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.

This note does **not** report a successful independent extraction or SHA-256 match. The connected GitHub actions do not expose a local shell or workflow-dispatch operation, so I did not run the extraction or independent parser within the repository. The existing repository audit remains the source of the prior archive/member/hash checks. The committed parser and runbook provide a repeatable check for a normal repository checkout or CI job. Do not promote any pending gate to PASS based solely on this endpoint payload.
