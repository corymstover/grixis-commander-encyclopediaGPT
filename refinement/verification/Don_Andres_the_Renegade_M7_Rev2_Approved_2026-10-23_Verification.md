# Don Andres M7 Rev2 canonical verification — owner-approved exact 100

**Result intended:** exact owner-approved candidate, awaiting canonical PR exact-head CI and main post-merge rehash.  
**Owner reply:** `Approve` after complete seven-swap Don Andres M7 Rev2 list, exact raw SHA and passing engineering PR.  
**Exact approved raw SHA-256:** `59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f`.  
**Canonical new artifact:** `refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt`.  
**Historical Oct14 approved source:** `refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt`, raw `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`; preserve unchanged.

## Deterministic tests

| Gate | Exact evidence |
|---|---|
| 100 physical | One commander, 99 library cards; 99 distinct; 2x Island only repeat |
| Color identity | All named card identities subset of U/B/R; no project exceptions |
| Commander legality | 99/99 official legal according to Oct23 Scryfall archived/direct Oracle; no exception |
| Oracle exact source | 98 selected Grok Oct23 Scryfall archived + one direct Scryfall Passionate Archaeologist plus adversarial old land records |
| Mana and role | 35 lands and 9 rocks; red RRR Insurrection limitation acknowledged |
| Game Changers | Five: Ancient Tomb, Cyclonic Rift, Fierce Guardianship, Opposition Agent, Vampiric Tutor |
| Bracket/tags | Bracket 4 — Optimized; Theft / Pirates / Treasure |
| Whole-deck delta | Exactly 7 substitutions against Oct14 approved baseline, not five-swap cap |
| Ownership | Don controls but does not own, so stolen creatures get +2/+2 menace deathtouch Pirate; created copies/tokens owned by us do not |
| Cast/timing | Opponent-owned noncreature cast makes two **tapped** Treasures; copied spells aren't cast; Background damages on exile cast |
| Background | Red enchantment in 99 legal even without choose a Background per Wizards |
| Land conditions | Shipwreck Marsh: two **other** lands; Smoldering Marsh: two **basic** lands; Gloomlake/Blazemire colored mana restrictions verified |
| Treachery | Untap up to five only if Aura resolves and enters; Aura removal ends theft |
| Simulation | No measured multiplayer win-rate, no invented infinite and no independently re-run Pass C |

## Selected bounded scenario

- Three opponent-owned spells cast from exile with MV2 noncreature, MV4 creature, MV6 noncreature: Don yields 4 **tapped** Treasures (two noncreature casts) and Passionate Archaeologist yields 12 noncombat damage in chosen targets (2+4+6), assuming Don/Background survive and spells actually can be cast. That is a conditional source-bound trace, **not a simulated game result**.
- If no opponent casts their first spell on a turn, Mind's Dilation creates no free cast; Stolen Strategy would instead exile cards on our upkeep, though would require us to pay for casting. The swap has a disclosed seven-mana timing/hand-draw tradeoff.
- Gloomlake Verge does not automatically replace Shipwreck's late black access; corrected land text and six-swap keep-Shipwreck alternate source verified. Blazemire may reduce fetchable Swamp/Mountain and conditional red access, no fictitious RRR certainty.

## Canonical approval checklist

1. Independently fetch engineering PR #689 exact head `3fc6011ec261e6ecc4f9365b503633b7559a7ab1`, confirm `40058523937 SUCCESS`, rehash 100 exact bytes.
2. Verify canonical main remains historical `a6022...` before update and preserve 13 earlier M7 locks.
3. Commit new approved 100, 99 selected Oracle records, approval receipt, this verification, only Don registry/tracker, and targeted tests/workflow.
4. Run new approval test and all 13 prior M7 regressions plus any repository-required workflows, exact-head PASS.
5. Merge canonical PR, refetch main approved list and independently SHA-256 hash; compare registry/tracker to prepared byte-exact content.

