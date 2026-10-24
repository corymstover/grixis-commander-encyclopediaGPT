# Goro-Goro and Satoru M7 Rev1 — exact owner approval receipt

Date: **2026-10-24** (America/Chicago); owner: **Cory Stover**; global-restart-2026-10-13; tracker #21 (index 20), registry `Goro_Goro_and_Satoru`.

**Explicitly approved exact 100 physical cards, raw SHA-256 `36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c`.**

## Owner authorization and precise scope

Cory was presented the complete 99-line Archidekt-ready Goro-Goro and Satoru M7 Rev1 proposal with `2x Island` (100 physical cards), five additions and cuts, individual strategic merits and material costs, structural/legality checks, Bracket 4 — Optimized, three tags, and [independent engineering PR #696](https://github.com/corymstover/GrokBotMTGCompanion/pull/696) exact head `1d3c45bad93e8531d4b9e5a27edb19f1b034f61b` with [Actions run #40072138305](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40072138305), nine source-bound checks passing.

Immediately following that exact proposal on 2026-10-24, Cory replied: **“Approve.”** This is contextual, explicit approval of only the exact presented 100-card Goro M7 Rev1 list and hash; it is not a blanket approval of other decks, engineering research, or M8 certification.

- Engineering candidate source: `data/grixis/m7/independent_candidates/Goro_Goro_and_Satoru_M7_Rev1_Proposed_20261024.txt` at GitHub exact head above; re-fetched and independently hashed using `sha256sum` before canonical branch construction.
- Exact NEW approved canonical list: `refinement/decklists/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.txt` (raw `36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c`, terminal LF).
- Historical 2026-10-14 canonical approval list: `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt` (raw `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`). Preserve byte-identically; leave its historical approval receipt and decision ledger intact.
- Grok first-pass PR #669 proposed one change only and remained research-only. Engineering PR #696 added five-swap independent analysis and tested full-100 alternatives. Neither PR was blindly merged into canonical.

## Exactly five owner-approved substitutions

| Addition | Cut | Commander-specific benefit | Material opportunity cost |
|---|---|---|---|
| Bitterblossom | Mist-Syndicate Naga | Persistent new flying Faerie Rogue each upkeep; can attack with haste from Goro, Samut, Dragon Tempest, etc. | 1 life/upkeep; lose ninjutsu Ninja and post-combat self-copy; Faerie can be blocked by flyers |
| Roaming Throne | Grim Hireling | Choosing Human doubles Goro damage triggers, Hanweir's attack-token trigger, Professional Face-Breaker Treasure triggers and Satoru the Infiltrator conditional draw | Lose independent 2-treasure-per-opponent production and treasure-based creature shrink; Throne requires another Human payoff |
| Hanweir Garrison | Kaito, Bane of Nightmares | Two fresh Humans enter tapped/attacking per attack (four with Human-chosen Throne), including extra combats; Tetsuko evasion at toughness 1 | Lose Ninja planeswalker ninjutsu, surveil/combat damage draws, hexproof on own turn, emblems and stun effect; tokens can be blocked |
| Misty Rainforest | Crumbling Necropolis | Earlier untapped Island-type duals for U/B or U/R, or tapped Xander's Lounge | 1 life, sometimes two extra shock life; triome required for all three on a single land; lost no-life guaranteed UBR |
| Marsh Flats | Fabled Passage | Earlier untapped Swamp-type duals U/B or B/R (or tapped Xander's Lounge) instead of Fabled's early tapped basic | 1 life plus possible shock life, narrower typed-target selections and anti-search vulnerability |

The five-swap M7 floor is not a cap; additional alternatives including Chandra, Acolyte of Flame and a Kaito-retention control were tested/staged but not automatically selected. No poor sixth was added.

## Commander-specific restrictions

Goro triggers once per *damaged player* per combat damage step when one or more creatures that entered that turn hit. Human-chosen Roaming Throne makes each such trigger happen an additional time; it is not one Dragon per token. Hanweir's Human tokens enter tapped and attacking; they themselves never became declared attackers and generate Dragons only if they damage a player. Four freshly generated tokens hitting three different players with both enablers and Goro can produce six Dragons in one step, not a guaranteed outcome. Tokens are usually blockable without Tetsuko or evasion support.

Owner's October 14 Ninja package, Bident of Thassa, all original mana rocks including Fellwar Stone, existing extra-combat suite, Dragon Tempest, Terror of the Peaks and original historical decisions remain intact. No new official-legality exception is used.

## Verification and governance

- Independent research: [engineering PR #696](https://github.com/corymstover/GrokBotMTGCompanion/pull/696), head `1d3c45bad93e8531d4b9e5a27edb19f1b034f61b`, GitHub Actions `SUCCESS` for 9 focused source-bound tests.
- 100 physical cards in 99 rows, 99 distinct names; 2x Island is the only duplicate; 33 lands and 66 nonland library cards; exactly six Game Changers; official Commander-legal B/R/U identity.
- Oracle: 96 names sourced from October 23 frozen Scryfall 215-name collection and three manually verified Scryfall-published records on October 24. No fabricated oracle IDs and no claim of a new full-100 live Scryfall batch query.
- Bracket **4 — Optimized**; tags **Ninjas / Dragons / Extra Combats**; project exceptions none.
- Deterministic combat/fetch timing tests, not actual multiplayer game outcomes, win-rate measurements or formal complete rules-engine certification.

**Do not report CANONICALLY MERGED/LOCKED until the approval PR passes exact-head checks, is merged with expected head SHA and the merged canonical main file and registry are independently fetched and rehashed.**
