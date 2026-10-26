# OWNER APPROVAL — Deck #38 Missy — M7 Rev1

Date: October 26, 2026 (America/Chicago).

Cory was shown the complete Archidekt-ready Missy M7 Rev1 100-physical-card list, 12 proposed additions/cuts, the exact raw SHA-256 `f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d`, current Oracle/rules checks, Power Bracket 4 — Optimized and tags Cybermen / Morph Recursion / Aristocrats Combo. Cory replied **“Approved”** directly after presentation. **That is the sole necessary owner approval; no second approval is requested or implied.**

**Approved exact raw SHA-256:** `f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d`  
**Current approved list:** `refinement/decklists/Missy_M7_Rev1_Approved_2026-10-26.txt`  
**Preserved prior approved list:** `refinement/decklists/Missy_Approved_2026-10-15.txt`, raw SHA-256 `9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed`.

## Twelve approved replacements

1. +Altar of the Brood / −Aphetto Runecaster
2. +Yawgmoth, Thran Physician / −Ashad, the Lone Cyberman
3. +Gift of Doom / −Bane of the Living
4. +Grim Monolith / −Cybermen Squadron
5. +Goblin Sharpshooter / −Cybership
6. +Carrion Feeder / −Doomsday Confluence
7. +Chrome Mox / −Etrata, Deadly Fugitive
8. +Fierce Guardianship / −Their Name Is Death
9. +Deflecting Swat / −Ugin's Mastery
10. +Marsh Flats / −Dragonskull Summit
11. +Misty Rainforest / −Drowned Catacomb
12. +Cavern of Souls / −Inventors' Fair

## Exact scope and verification

- Engineering PR [#719](https://github.com/corymstover/GrokBotMTGCompanion/pull/719) merged on October 26, 2026 as `d63a00b183f7119f590fbb85b1ac7fd8d758614b`; tested head `0afd9afc474880769c28fbe6cbc461d35d56f930`.
- [M7 contract CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40395748220) SUCCESS; exact focused candidate tests are in `tests/test_m7_missy_rev1.py` and Scryfall snapshot `data/grixis/m7/oracle_snapshots/Missy_Rev1_Scryfall_20261026.json`.
- 100 physical cards / 97 distinct names / 35 lands; Island twice and Swamp three times, all other names once; 97/97 current Scryfall names and Commander-legal Grixis identities; no project exceptions.
- Commander-first nonartifact-death-to-Cyberman conversion, reusable face-up morph creatures, sacrifice-trigger/drain engine, and villainous choices retained. Generic non-Missy consultation/breach lines not added.
- Six exact-candidate finite test methods PASS. The historical M6 blueprint was originally **design-only**. Five required P0 cases now have bounded positive/adversarial source-mapped tests under the exact owner-approved SHA; 11 P1 source scenarios are explicitly deferred in the transfer artifact. This is **not** a broad independent I/J game-state suite or a simulated win-rate claim.
- **Power Bracket 4 — Optimized**; Archidekt tags **Cybermen / Morph Recursion / Aristocrats Combo**.

Supersede only Missy's current October 15 canonical pointer while preserving its historic list, approvals and reviews byte-for-byte. Do not infer a blanket approval for any other deck or milestone.
