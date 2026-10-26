# Deck #41 — Nicol Bolas — M7 Rev1 approved verification

Date: 2026-10-26
Cycle: global-restart-2026-10-13
Status: OWNER-APPROVED EXACT LIST; CANONICAL LOCK ELIGIBLE
Commander: Nicol Bolas (original Elder Dragon)
Power Bracket: 4 — Optimized
Archidekt tags: Discard / Commander Damage / Control

## Exact artifact identity

- Canonical path: `refinement/decklists/Nicol_Bolas_M7_Rev1_Approved_2026-10-26.txt`
- Exact raw SHA-256: `a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6`
- Previously approved October 15 artifact retained: `refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt`
- Prior approved raw SHA-256: `e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617`
- Engineering source: `corymstover/GrokBotMTGCompanion/data/grixis/m7/candidate_lists/Nicol_Bolas_chatgpt_rev1.txt`
- Engineering approval review: `data/grixis/m7/decision_reviews/Nicol_Bolas_chatgpt_rev1_review.md`
- Engineering PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/723
- Merged engineering commit: `5a0463d11b66711257506cc1a035af669bf86871`
- Tested engineering head: `35f4740298b61723ed8b859c5bdb84e3c22f2f5c`
- GitHub Actions successful verification run (same exact list): https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40411851701
- Prior successful independently displayed verification run: https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40411457402

## Structural and external metadata gate

- Total physical cards including Nicol Bolas: **100**.
- Exactly one designated commander: **1x Nicol Bolas**.
- Physical text rows: **99** because **2x Island** is represented as one row.
- Distinct names: **99**.
- Copies repeated: Island x2 only; no nonbasic singleton violations.
- Lands: **37**.
- Commander identity: **U/B/R**. All noncommander identities are included within it.
- Official Commander legality: **PASS** using live Scryfall Commander legality for 99/99 unique names in CI on 2026-10-26.
- Project exceptions: **none**.
- Exact 10 removals / 10 additions relative to the October 15 canonical baseline.
- Seven SHA-bound finite tests: **7/7 PASS**.
- Fourteen strategic Oracle witnesses: **PASS** on the identified cards at the time of the check.
- Candidate raw SHA, source baseline SHA, required inclusions, 37-land structure and singleton compliance: **PASS**.

## Commander-first / rules decisions

- Nicol Bolas discards an opponent's entire hand whenever Nicol deals damage to that opponent, including noncombat damage.
- Dragon Tempest, Ingris Stingerquill, Kediss, Chandra's Ignition, Pain for All and Quicksilver Dagger retain exact commander-sourced damage pathways.
- Sarkhan, Soul Aflame can copy Nicol Bolas with the distinct name Sarkhan; it remains legendary and is not automatically destroyed by the legend rule because names differ.
- Ophidian Eye and Curiosity are separate per-damage-event draw triggers; neither requires the damage to be combat damage.
- Rivaz provides red/black mana for Dragon spells, not for Nicol's upkeep payment. Casting Nicol from a graveyard requires that Nicol was left in that zone, not returned to the command zone.
- Dream Halls allows alternative costs for any player, retains commander tax and does not remove Nicol's UBR upkeep requirement. Treat the symmetrical benefit as a strategic risk.
- Minamo untaps legendary Nicol Bolas to enable an additional noncombat tap ability (Quicksilver Dagger), not an additional combat phase.
- Reanimate costs life equal to Nicol's mana value if Nicol is returned; it cannot target the commander in the command zone.
- Removed Bojuka Bog reduces graveyard interaction; removed No Mercy reduces attack deterrence; both are conscious role tradeoffs.
- Aggravated Assault + Sword of Feast and Famine requires a successful Sword hit and enough mana from untapped lands to pay the next Assault activation.

## Owner-level closure

The user responded **“Approve”** on October 26, 2026, directly to Deck #41 Nicol Bolas M7 Rev1, containing the full Archidekt-ready candidate, ten additions/cuts and exact raw SHA-256 `a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6`.

This is the single explicit approval and authorizes replacement of the previously locked October 15 Nicol Bolas list with this exact M7 Rev1, while retaining prior artifacts for provenance. No repeated owner-approval request is required. This document makes no claim of measured gameplay win rates or of broader milestone acceptance.
