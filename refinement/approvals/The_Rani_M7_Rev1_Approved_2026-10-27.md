# Owner approval — Deck #57 The Rani M7 Rev1

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

## Single owner authorization

> Approve Deck #57 The Rani M7 Rev1, exact raw SHA-256 924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27. Proceed with engineering merge, canonical locking, and post-merge verification without bypassing any required certification gate.

- **Approved raw 100 SHA-256:** `924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27`.
- **Approved file:** `refinement/decklists/The_Rani_M7_Rev1_Approved_2026-10-27.txt`.
- **Preserved prior approval:** `refinement/decklists/The_Rani_Approved_2026-10-15.txt` with raw SHA `7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c`.
- **Structure:** exactly 100 cards, commander first, 94 distinct names; Islands ×3, Mountains ×3, Swamps ×3 are the only repeats.
- **Commander identity:** U/B/R; 33 lands; Bracket 4 — Optimized; tags Goad / Clue Tokens / Artifact Drain.
- **Official legality:** all cards currently legal in Commander, and all identities within Grixis; no project-specific legality exception used.

## Exact eight commander-first changes

| Cut | Addition |
|---|---|
| Death Kiss | Frenzied Gorespawn |
| Maestros Confluence | Curse of Verbosity |
| Grenzo, Havoc Raiser | Mirkwood Bats |
| Tangletrove Kelp | Cyberdrive Awakener |
| Mocking Doppelganger | Alexios, Deimos of Kosmos |
| Reanimate | Marionette Apprentice |
| Five Hundred Year Diary | Tamiyo's Journal |
| Hateful Eidolon | Roaming Throne |

This retains The Rani's unique **Mark → goaded combat damage → investigate** plan while improving forced attacks, repeatable draw, clue/artifact token payoffs, and typed trigger doubling. These are not a generic Grixis combo conversion. Time Sieve requires five sacrificed artifacts and is **not** assumed to be an unconditional infinite loop. Roaming Throne requires Time Lord as its creature type to double Rani's triggers; separate trigger resolution must retain legal target(s).

## Evidence and mandatory hold

- Engineering M7 PR [#741](https://github.com/corymstover/GrokBotMTGCompanion/pull/741) merged at `1b37673f3856583affa2f4c29f71ecfa7c4cc2da` from exact reviewed head `e4e18415dde7eae5fc06b0ef257a167cfa0bcb98`.
- [Exact-head Deck 57 CI #40602646406](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40602646406) and [M7 contract #40602646407](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40602646407) both succeeded.
- Follow-up [engineering PR #742](https://github.com/corymstover/GrokBotMTGCompanion/pull/742) executes the five original M6 blueprint P0 scenarios against the exact same 100; no list changed. Its dedicated exact-head CI receipt is in the separate per-case attestation.
- Nine P1 source-plan cases are explicitly **DEFERRED**, preserving their owner-visible coverage gap. Historical M6 I/J inputs were accepted, but Phase B was incomplete; bounded finite M7 assertions do not substitute for a complete game-rules simulation.
- **Canonical transition is contingent on the pre-existing, mandatory whole-registry `verify_m7_certification_transfer.py --check` gate.** A staged draft PR is not a completed canonical lock until all required checks pass and the PR merges. Do not waive the gate, rewrite the frozen provenance snapshots, or invent historic receipts.

This owner approval is final for the listed raw SHA; do not request a second approval. Its publication/lock execution must respect certification gates.
