# Crosis, the Purger M7 Rev2 — exact owner-approved source verification

**Approved raw SHA-256:** `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a` (100-card UTF-8 text, trailing LF).  
**Historical Oct14 approved raw SHA-256:** `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1` (preserved).  
**Owner:** Cory explicitly replied **“Approve”** to the full nine-swap Rev2 100 and its exact SHA on 2026-10-23 America/Chicago.  
**Sources:** engineering independent [PR #685](https://github.com/corymstover/GrokBotMTGCompanion/pull/685), head `6bc6ff135e90db1237c0dd9881017aaf36e249fe` (four exact-head workflows SUCCESS). Crosis 197-name October23 archived live Scryfall plus Cecily October23 selected live Scryfall for channel lands; no fresh research pipeline.

## Certified exact 100

- 100 physical (one Crosis commander, 99 in library), 95 distinct names, only 3 Island, 2 Mountain, 3 Swamp repeat.
- 36 lands; the three added channel lands are untapped U/B/R respectively. 12 acceleration artifacts (Izzet Signet kept). 14 Game Changers, Power Bracket 4 — Optimized. Three Archidekt tags Discard / Dragons / Extra Combats.
- All 95 names resolved by actual `oracle_id` and `oracle_text`, official Commander `legal`, color identity subset U/B/R. Zero project exceptions; no split errors, color violations, missing names or illegal cards.
- Nine one-for-one substitutions match original approved Oct14 source, computed by physical multiset delta.
- Core intact: Painter's Servant, Crosis, Sword of Feast and Famine, Brotherhood Regalia, Lightning Greaves, Dark Deal, Izzet Signet, Tergrid and the Tinybones suite.
- Crosis is {3}{U}{B}{R} and his combat-damage ability optionally costs **{2}{B}**; Painter makes all cards in a hand the chosen color. Megrim deals 2 damage per discarded card, Caress and Raiders' Wake cause loss of 2 life per discard; active Bloodchief adds life loss/gain per opponent card into graveyard but requires three quest counters from qualifying end steps. Sword+Aggravated Assault is conditional on connecting and five colored mana per extra combat; for an additional Crosis purge it needs a further {2}{B} on resolution, so at least eight usable mana with applicable pips to pay both.
- No source claims statistical simulation or deterministic win. Archived research is Oct23, not independently rerun live on canonical commit. A previous first-pass five-swap M6 J remains **not** re-sealed for Rev2.

## Preserved evidence and checks

- Previous approved October14 source `refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt`, raw `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1` unchanged. Original tracker note incorrectly suggests swapping Regalia for Blizzard; bound source contains both; retain provenance discrepancy.
- Other nine M7 approved/locked deck hashes checked unchanged in regression.
- M6 J original Grok source seal restored exact; all four engineering PR #685 exact-head workflows PASS.
- This canonical PR must pass its own workflow(s), then be merged and **main refetched and raw independently rehashed**. A proposal CI PASS alone is not owner approval, which was explicitly provided for this SHA.
