# Davros, Dalek Creator M7 Rev2 — nine-swap exact owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Owner: **Cory Stover**  
Cycle: `global-restart-2026-10-13`  
Decision: **APPROVED / LOCKED**, Deck #12/index 11, raw SHA-256 `96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc`.

## Exact owner authorization

After seeing the entire independently reviewed nine-swap 100-card list in the assistant response, nine additions/cuts, exact raw SHA-256 `96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc`, [engineering PR #687](https://github.com/corymstover/GrokBotMTGCompanion/pull/687), and final exact-head CI success, Cory expressly replied:

> Approve

Cory approved **only this exact 100-card raw list**. The approval does not authorize any change to Deck #13 Doctor Doom or any prior locked deck.

Source: `refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt`, UTF-8, 100 physical cards, 95 named entries, trailing newline, exact SHA-256 `96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc`.

The prior historically owner-approved source `refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt` remains byte-exact at `aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc`. The old October 13 tracker `5c1d4a49…` referenced the *older proposed* list; it is historical, **not** the approved October 14 source.

## Nine exact approved substitutions

| Added | Removed | Reason |
|---|---|---|
| Bloodletter of Aclazotz | Death in Heaven | During our turn turns 2 opponent life loss into 4; Saga needs delayed graveyard setup. |
| Tergrid, God of Fright | The Cyber-Controller | Turn discarded permanent cards and nontoken sacrifices into battlefield theft; variable X-mill Cyberman engine removed. |
| Purphoros, God of the Forge | Blasphemous Act | Indestructible while often noncreature; each new Dalek/clone causes 2 damage to every opponent. Lose cheap 13-damage artifact-creature sweep, retain Toxic Deluge and Their Name Is Death. |
| Fiery Confluence | This Is How It Ends | Untargeted choose 2-damage-to-each-opponent three times = 6/table. The single-target shuffle villainous choice may be circumvented. |
| Flame Rift | Cyberman Patrol | `{1}{R}` gives a guaranteed 4 damage to each opponent before end step if it resolves; also deals 4 **to us**. Patrol's afflict 3 depends on blocking and combat. |
| Spark Double | Cybermen Squadron | A permanent 4-mana nonlegendary Davros copy gives another end-step trigger; 7-mana myriad engine cut. |
| Irenicus's Vile Duplication | Weeping Angel | Permanent flying nonlegendary Davros token; defensive flash body cut. |
| Quantum Misalignment | Ashad, the Lone Cyberman | Nonlegendary Davros token plus another via rebound at next upkeep when cast from hand; casualty-dependent artifact duplicator cut. |
| Mechanized Warfare | Labyrinth Raptor | Adds +1 to red or artifact source damage to opponents, including Purphoros 2→3 per Dalek and each Fiery 2→3. Combat-menace support cut. |

Explicitly **retained**: Swan Song, Vandalblast, Sycorax Commander, 34-land mana architecture, complete Dalek/villainous choice payoff engine.

## Exact mechanical and identity verification

- 100 physical cards = 1 original Davros commander plus 99 library. **95 distinct names**, repeat only Island 2, Mountain 3, Swamp 3. **34 lands**, **7 mana rocks**.
- All 95 current Oracle identities/text, color identities, quantities and official Commander legality verified in selected records, U/B/R only, **no project-specific exceptions**.
- Six Game Changers: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Tergrid, God of Fright. **Power Bracket 4 — Optimized**. Archidekt tags **Daleks / Villainous Choice / Group Slug**.
- Davros is a legendary **artifact Alien Scientist (not a Dalek)**. Condition `opponent lost 3+ life this turn` is checked on each end-step ability **resolution**. A clone's individual end-step ability does not happen unless a player passes through the beginning of that end step with the clone present.
- Spark Double, Irenicus's Vile Duplication, and Quantum Misalignment make **nonlegendary** permanent Davros copies; no legend-rule elimination of originals. Quantum's second token appears on rebound at next upkeep, not retroactively at the current end step.
- Purphoros triggered by a Dalek from one Davros resolution is put on the stack only after that Davros ability resolves; its damage can qualify other opponents **for later pending Davros triggers**, not the triggering ability that created that Dalek. With Mechanized, Purphoros's red 2→3 damage can qualify previously unqualified opponents before the next Davros resolves.
- The Valeyard doubles each opponent's villainous choice, **not Dalek production**; empty-handed opponent can choose to discard an impossible card. Dauthi Voidwalker exile replacement can prevent Tergrid from retrieving the discarded/sacrificed permanent from a graveyard while both remain.
- Fiery Confluence `2/2/2` has no target; if a chosen artifact mode gives the spell its only target and that target becomes illegal, the spell fails to resolve at all. Bloodletter turns opponent life loss into twice the amount only during our turn, no infinite.
- All candidate-testing is bounded and source-bound. **No measured multiplayer win-rate, automatic loop, or third-model independence claim.**

## Source provenance and tests

- Independent engineering [PR #687](https://github.com/corymstover/GrokBotMTGCompanion/pull/687), exact head `f9608321853a1a90cd0f4882d1227a255301355a`. Candidate-specific exact-head workflow run **`40056636170` SUCCESS**. Proposed exact SHA was refetched from that head and independently rehashed before owner presentation.
- Source: Grok firstpass [#660](https://github.com/corymstover/GrokBotMTGCompanion/pull/660) October 23 archived live Scryfall 177-name Oracle snapshot; Cult October 23 archived selected Scryfall for Spark Double, Irenicus, Quantum; official Wizards [The Brothers' War release notes](https://magic.wizards.com/en/news/feature/the-brothers-war-release-notes) for Mechanized Warfare and independently cross-referenced `oracle_id`.
- Grok firstpass **six** and its M6 I/J remain intact and **were not re-sealed** for this ChatGPT **nine**. Source artifacts and prior locked canonical decks are not to be modified.
- This canonical PR creates only Davros exact approval artifacts and regression tests; must pass exact-head CI, merge, re-fetch canonical main and independently check raw SHA plus the other 61 registry entries before claiming completion.

## Governance

Do not reopen or replace Davros after owner-approved M7 lock except Cory explicitly requests it. Once merged, proceed to independent Deck #13 Doctor Doom research **without** interpreting this approval as owner approval of Doctor Doom.
