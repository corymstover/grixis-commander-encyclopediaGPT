# Be'lakor M7 Rev2 — post-owner approval exact-source verification

**Exact candidate raw SHA-256:** `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`  
**Original approved raw:** `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`  
**Owner approval:** Cory's explicit reply "Approve" immediately after complete 100-card Rev2 list, eight swaps and exact hash, 2026-10-23 America/Chicago. The reply is not a general authorization to approve other decks.

## Source-bound recount
- 100 physical cards, 94 unique names: 94 rows, Island ×3 / Mountain ×2 / Swamp ×4, singleton elsewhere. Exactly one `Be'lakor, the Dark Master [Commander]`.
- 36 physical lands. Seven static rocks: Sol Ring, Arcane Signet, Rakdos Signet, Talismans of Creativity/Dominance/Indulgence, Cursed Mirror. Dark Ritual is not a reusable rock.
- 25 printed Demon cards, 5 Game Changers (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor), Bracket 4. All selected cards have archived live Oct23 Scryfall Oracle ID/text, Commander `legal` and U/B/R subset color identity. No exceptions.
- Engineering PR #682 exact head `bcf3e8fc40f1084c0a612c368b1ecba5899be884`, Actions run #40050434686 success: 7 new Rev2 and 4 inherited GrokBot regression tests. Independent raw candidate SHA verified against exact remote file and canonical proposed bytes.
- Source selected Oracle copied unchanged from `data/grixis/m6/oracle_snapshots/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Selected_20261023.json` on PR head.

## Relevant interaction gates
- Be'lakor Lord of Torment triggers only on *another* Demon entering and uses that entering Demon's power, including token/copy/reanimation ETBs.
- Cursed Mirror copies as it enters for temporary ETB damage/benefits; copying a legendary Demon still invokes the legend rule, and copying a creature temporarily removes its ordinary red mana ability. It costs {2}{R}, one more than the old Fellwar Stone.
- Curse-Marred Demon searches any card then discards **one at random**. Shadowgrange forces each opponent to sacrifice a highest-power creature and gains life equal to the greatest power **among all sacrificed**, not cumulative; it has a single black pip.
- Rite of Replication kicked Be'lakor line: 5+5×4 = 25 finite Lord triggers with simultaneous legendary tokens before state-based legend rule; stacking Prince below Lord may avoid self-loss, but Prince life loss remains real and doublers can increase it.
- Previous mechanical bundle for five-swap first pass remains historical, not a formal certificate of this revised exact candidate. No fresh full Spellbook combo search or multiplayer playtest claimed.

## Governance
Canonical approval PR updates only Be'lakor key and tracker row, adds immutable exact 100-card artifact, receipt, source evidence and regression tests. Other 6 new-cycle locks, historical Be'lakor October13 file, project exceptions, and aggregate milestone authority are preserved. Post-merge main must be refetched and rehashed.
