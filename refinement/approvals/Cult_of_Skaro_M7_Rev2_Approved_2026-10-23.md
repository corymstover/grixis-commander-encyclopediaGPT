# Cult of Skaro M7 Rev2 — nine-swap owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Owner: **Cory Stover**  
Cycle: `global-restart-2026-10-13`  
Decision: **APPROVED / LOCKED**, Deck #11/index 10, raw SHA-256 `e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d`.

## Exact owner authorization

After seeing the full nine-swap 100-card list, its strategic and rules comparisons, [engineering PR #686](https://github.com/corymstover/GrokBotMTGCompanion/pull/686), four exact-head PASS checks and full raw SHA, Cory expressly replied:

> Approve

This approves **only** `e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d`, exact UTF-8 100-card list with trailing LF at `refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt`. It is **not a blanket approval** for Deck #12 Davros or any later deck. The original approved October14 baseline `refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt` (misleading "candidate" basename) remains byte-exact at `4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b`. The old tracker cites an Oct13 SHA cc2f7a54… and a lone Skorpekh→Ashad swap, both incomplete for the bound Oct14 source. The discrepancy is retained as evidence, not silently repaired.

## Nine expressly approved substitutions

| Added | Removed | Why |
|---|---|---|
| Karlach, Fury of Avernus | Cybermen Squadron | Every-turn extra combat for more Cult attack triggers, trades 7-mana global myriad ceiling for faster reliability. |
| Kindred Discovery | Canoptek Spyder | Draw for Dalek enters and declarations incl. tokens, versus Spyder's nontoken restriction; mandatory draw and UU noted. |
| Hammer of Purphoros | Adaptive Omnitool | Global haste for Cult and copies, versus expensive equip dig. |
| Shaun, Father of Synths | Thopter Spy Network | Nonlegendary Cult Synth copies; **The Master, Multiplied is retained** to prevent own Shaun-triggered Synth exile and preserve myriad tokens for future attack declarations while present. |
| Quantum Misalignment | Anrakyr the Traveller | Two Cult nonlegendary copies through cast/rebound vs life-costly narrow artifact cheat. |
| Skorpekh Lord | Baleful Strix | Artifact team power+menace; **Etherium Sculptor retained** as a third artifact spell cost reducer; lost cheap deathtouch flyer/cantrip disclosed. |
| Reverse the Polarity | Desynchronization | 1UU response to counter other spells or grant unblockable alpha strike vs four-mana asymmetrical resolved-permanent bounce. |
| Otawara, Soaring City | 1 Island | Untapped blue source with channel bounce, slight nonbasic hate exposure. |
| Takenuma, Abandoned Mire | 1 Swamp | Untapped black source with channel creature recovery, slight nonbasic hate exposure. |

## Verified exact 100 and bounded mechanics

- 100 physical cards; 1 commander, 99 library; 96 distinct rows. Only basics repeat: Island 2, Mountain 3, Swamp 2. 34 lands, 9 mana rocks, 3 artifact reducers, 3 Game Changers. Grixis U/B/R singleton and official Commander legality source-bound PASS. Zero project exceptions.
- Cult random attack triggers **only when declared an attacker**. Myriad/Shaun tokens entering attacking do not retro-trigger Cult. If The Master static effect remains while our token-exile triggers resolve, Synth and myriad token copies are not exiled by **our** triggered abilities, and can trigger Cult on later declared attacks. The Master does not prevent opponent exile spells or resolve problems after it leaves.
- Shaun's newly created Synth cannot be declared during Karlach's additional combat unless haste (Hammer or Dalek Emperor); Karlach untapping alone is insufficient. Kindred Discovery chosen type Dalek draws on entry and declared attack. Strionic Resonator/Scientist Supreme ability copies keep chosen mode; separate Roaming Throne triggers choose independently. Sword + Aggravated Assault remains conditional on connecting and enough red mana.
- Bracket **4 — Optimized**, Archidekt tags **Artifacts / Extra Combats / Copies**. No simulated win rates or unconditional infinite claims.
- All 96 selected card Oracle IDs/text/legalities bound from 2026-10-23 Grok 210-name archived Cult snapshot and exact canonical Crosis Oct23 live Scryfall selected records for Otawara/Takenuma. No additional paid Grok use or pipeline rerun.
- Engineering [PR #686](https://github.com/corymstover/GrokBotMTGCompanion/pull/686) exact head `426d8afcd76924ee1c036d91a91dc33abd1d79f7`, all four exact-head runs PASS: `40055304492`, `40055304455`, `40055304478`, `40055304482`. Grok first-pass #659 six-swap formal M6 I/J was **not** re-sealed for this nine-swap candidate. Historic seals/source untouched.
- This canonical PR adds the exact owner approval only; it must pass its own exact-head checks, be merged and re-fetched from main to independently rehash. Preserve all ten previous M7 owner locks and 62 registry entries.

## Lock governance

No canonical edits to Cult after this lock without Cory's explicit request. Proceed to Deck #12 Davros only after post-merge verification, and **do not imply Davros is M7 owner approved**.
