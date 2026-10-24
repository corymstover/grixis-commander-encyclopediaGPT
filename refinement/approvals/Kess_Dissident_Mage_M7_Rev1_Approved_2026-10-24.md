# Kess, Dissident Mage — M7 Rev1 explicit owner approval and canonical lock receipt

Date: **2026-10-24** (America/Chicago). Owner: **Cory Stover**. Encyclopedia: Deck **#26**, `Kess__Dissident_Mage`; cycle `global-restart-2026-10-13`.

## Exact owner instruction and scope

Cory replied **“Approve”** directly after receiving Deck #26's complete 100-card M7 Rev1 candidate, five addition/cut pairs, power level, caveats, and exact SHA-256. This authorizes canonical approval and locking of **only** that exact 100-card list:

`11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4`

Hash convention: raw UTF-8 bytes, one `1x` card per line, commander first with `[Commander]`, exactly one terminal LF, 100 distinct names.

## Explicitly approved five additions and five cuts

| Added | Removed | Material gain and cost |
|---|---|---|
| Mana Drain | Personal Tutor | Live permissioned hard counter and delayed colorless mana; loses sorcery-to-library-top setup; double blue and delayed mana can matter. |
| Grim Tutor | Demonic Counsel | Unconditional tutor and powerful once-per-own-turn Kess recast; costs three mana and three life, replacing a cheaper but delirium/Demon-conditioned spell. |
| Jeska's Will | Ledger Shredder | Commander-enabled impulse access and/or burst red mana, reusable with Kess; loses connive, graveyard stocking, and persistent flying body. Conditional resource sizes must not be assumed. |
| Cyclonic Rift | Into the Flood Maw | Versatile overload or single-target answer; loses Maw's cheaper tempo and tap-creature ceiling. Overload still costs 6U even when replayed from the graveyard. |
| Exotic Orchard | Fiery Islet | Potential black as well as blue/red fixing from opposing lands; loses guaranteed U/R and the late sacrifice-to-draw mode; Orchard's colors depend on actual opposing lands. |

These expressly revisit historical owner-selected cards. Prior October 14 consent is not imputed to the new changes; this October 24 reply authorizes them for the exact SHA above. The historical source is preserved unchanged at `refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt` (raw SHA `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`).

## Review, controls and limits

- Engineering independent five-swap review: [PR #704](https://github.com/corymstover/GrokBotMTGCompanion/pull/704). Historical Grok one-swap first-pass [PR #674](https://github.com/corymstover/GrokBotMTGCompanion/pull/674) was not the final approved candidate.
- M7 decisive packet: `data/grixis/m7/decision_reviews/Kess__Dissident_Mage_rev1.json`; the five-swap floor is a minimum, not a target or cap. Also examined six- and seven-swap fully counted challengers, rejecting their added losses.
- Source-bound Scryfall archive: `data/grixis/m6/oracle_snapshots/Kess__Dissident_Mage_M7_Scryfall_20261023.json`. Individual case fixtures are bounded, not full game simulations or empirical win-rate evidence.
- 14/14 M6-required scenario cases plus six structural/card-identity tests executed against the exact 100; the permanent transfer attestation records executable proof and actual CI URL.
- Official Commander legality: PASS for the 100 sourced Oracle records; Grixis B/R/U identity; **no project exception**. Exact 100 physical singleton cards and 27 lands.
- Commander identity: once during **each of your own turns**, one instant/sorcery from your graveyard, then exile replacement when applicable. Oracle/Consult/Pact, Intuition/Gifts, Kitten, and Breach win/recursion engines preserved.

Power Bracket **5 — fringe cEDH**. Archidekt tags: **cEDH / Spellslinger / Combo**.

This receipt is only an exact-list authorization; it makes no claim of an independent tournament win-rate uplift, no blanket M8 seal, and no approval of future deck edits.
