# Davros M7 Rev2 canonical verification — owner-approved exact 100

**Result intended: APPROVED EXACT SOURCE, pending canonical PR exact-head CI and post-merge re-fetch.**  
**Owner reply:** `Approve` to full independently verified 100-card nine-swap Davros M7 Rev2 list and exact raw SHA on 2026-10-23 America/Chicago.  
**Expected raw SHA-256:** `96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc`.  
**Canonical artifact:** `refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt`.  
**Historical approved source:** `refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt` → `aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc`. Preserve both; older tracker Oct13 SHA 5c1d4a49 is an unapproved prior proposal.

## Deterministic structural gate

| Verification | Bound evidence / result |
|---|---|
| 100 physical | Exactly 100 = 1 Davros commander + 99 library |
| 95 distinct named entries | Exactly 95; only basic Island 2 / Mountain 3 / Swamp 3 repeat |
| Grixis color identity | All selected card color identities subset of U/B/R, PASS |
| Current Oracle names/text | 95/95 selected records with oracle_id/text; PASS |
| Commander legality | 95/95 Commander legal as of 2026-10-23 source; PASS |
| Project exceptions | None |
| Normal mana | 34 lands, 7 mana rocks, Enthusiastic Mechanaut artifact reducer |
| Game Changers | Six: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Tergrid |
| Power | Bracket 4 — Optimized |
| Archidekt tags | Daleks / Villainous Choice / Group Slug |
| Nine additions and nine cuts | Exactly nine one-for-one substitutions relative to historical approved Oct14 bytes |
| Source provenance | Grok Oct23 archived 177-name Scryfall + Cult Oct23 selected Scryfall clone names + Wizards official Mechanized Warfare BRO release notes |
| Engineering verification | PR #687 exact head f9608321853a1a90cd0f4882d1227a255301355a, workflow 40056636170 SUCCESS |
| Simulation | No matched-start multiplayer games, **no invented win rate** |

## Independent finite rules tests

Davros is an artifact **Alien Scientist, not Dalek**. Beginning end-step condition is checked on resolution, not intervening-if at trigger generation. Persistent nonlegendary Davros clones from Spark Double, Irenicus's Vile Duplication, Quantum Misalignment survive the legend rule and each trigger at beginning of end step when present. Quantum rebound creates another token on later upkeep. With Purphoros and 2 waiting Davros triggers, first token's Purphoros red entry damage is stacked after the first Davros ability and before the second; only the *second* trigger can benefit. B/C starting at zero see 2 (Purphoros alone), 3 (with Mechanized) or 4 (with Bloodletter on our turn); only the latter two qualify before second Davros. The first Davros qualification cannot be retroactively changed. Mechanized applies +1 to actual red/artifact **damage events**, including each Fiery mode, but not Wound Reflection life loss. Tergrid and Dauthi replacement tension, impossible empty-hand discard option, and target-dependent Fiery failure are documented.

**No deterministic infinite or measured multiplayer win-rate claim.** The original Grok six-swap M6 I/J was **not** re-sealed for ChatGPT nine swaps. Preserve its firstpass evidence and all 11 previous M7 canonical locks.

## Canonical lock execution checklist

1. Independently hash fetched exact PR #687 candidate and compare `96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc`. Check selected Oracle full 95 names, 100 physical, singleton, UBR legality, exceptional project choices none.
2. Update only `decks.Davros__Dalek_Creator` registry record, exactly one tracker row (index 11), preserve historical approved source, add the exact bytes, selected Oracle, approval receipt and this verification.
3. Run a Davros-specific exact-head canonical unittest/workflow plus regression of all 11 earlier M7 approved locks. Distinguish PASS of scoped tests from exhaustive game simulation.
4. Merge owner-approved canonical PR only after exact-head SUCCESS. Fetch main again and verify raw SHA, only Davros registry entry changed, all other 61 registry records and historical source unchanged.
5. Record PR number and post-merge SHA in handoff; move next to Deck #13 Doctor Doom independent M7 review without canonical write until its own owner approval.
