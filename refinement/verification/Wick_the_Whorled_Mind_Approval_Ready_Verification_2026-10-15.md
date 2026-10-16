# Wick, the Whorled Mind — Approval-Ready Verification — 2026-10-15

## State and baseline
- Cycle: `global-restart-2026-10-13`.
- Tracker position: index 60 / deck 61 of 62.
- Current locked total before approval: 60/62.
- Authoritative baseline: `GrixisFINAL2--2026.zip::Wick__the_Whorled_Mind.csv`, reconciled against `GrixisFINALTXT2--2026.zip::Wick__the_Whorled_Mind.txt` at 100 cards.
- The older v8.1.4 `deck_card_audit.csv` contains a stale five-slot configuration and is supporting evidence only; it does not supersede the later FINAL2 CSV/TXT source.
- Frozen source exports remain unchanged.

## Commander blueprint
Current Oracle text: Wick, the Whorled Mind `{3}{B}`, legendary Rat Warlock, 2/4. Whenever Wick or another Rat you control enters, create a 1/1 black Snail creature token if you do not control a Snail; otherwise put a +1/+1 counter on a Snail you control. `{U}{B}{R}, Sacrifice a Snail:` Wick deals damage equal to the sacrificed creature's power to each opponent, then you draw that many cards.

Commander-first plan: deploy cheap or multi-body Rats, accumulate power on a single Snail, preserve/amplify those counters, then convert the Snail into table-wide damage and cards. Type-changing effects that add Rat while preserving Snail create compact commander-native sacrifice loops with free outlets. The deck remains Rat/Snail-centric rather than becoming a generic Grixis Consultation/Breach shell.

Natural ceiling: **Power Bracket 4 — Optimized**.
Suggested Archidekt tags: **Rats / Snail Counters / Combo**.

## Whole-list audit
- 99/99 noncommander copies adjudicated in `refinement/decisions/Wick_the_Whorled_Mind_Whole_List_Audit_2026-10-15.csv`.
- Result: **76 KEEP / 23 CUT**.
- Project top-100 candidate pool fully adjudicated.
- Meaningful outside-ranked challengers reviewed.
- Final adversarial correction: Plague of Vermin -> Song of Totentanz.
- Subsequent complete pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

## Final proposed changes
1. Blood Artist -> Intruder Alarm
2. Counterspell -> Mana Drain
3. Dimir Signet -> Altar of Dementia
4. Endrek Sahr, Master Breeder -> Rat King, Verminister
5. Kindred Discovery -> Lich's Relic
6. Nadier's Nightblade -> Tainted Strike
7. Ogre Slumlord -> Blade of the Bloodchief
8. Rakdos Signet -> Diabolic Intent
9. Reflections of Littjara -> The Ozolith
10. Shared Animosity -> Bulk Up
11. Sling-Gang Lieutenant -> Voracious Vermin
12. Terminate -> An Offer You Can't Refuse
13. Wave of Rats -> Tangled Colony
14. Plague of Vermin -> Song of Totentanz
15. Bojuka Bog -> Boggart Trawler // Boggart Bog
16. Dragonskull Summit -> Badlands
17. Drowned Catacomb -> Underground Sea
18. Fabled Passage -> Marsh Flats
19. High Market -> Phyrexian Tower
20. Path of Ancestry -> Mana Confluence
21. Sulfur Falls -> Volcanic Island
22. Mountain -> Swarmyard
23. Swamp -> Cavern of Souls

## Oracle / rules red-team conclusions
- **Wick sacrifice resolution:** damage and cards use the sacrificed Snail's power as it last existed on the battlefield.
- **Arcane Adaptation / Leyline of Transformation / Maskwood Nexus:** these effects add Rat/every creature type without stripping Snail, allowing the Snail token to remain a Snail while also being a Rat. Rat entry therefore creates/grows the Snail and free sacrifice outlets can repeatedly exploit Wick's trigger structure.
- **Conspiracy rejected:** choosing Rat makes affected creatures the chosen type rather than preserving all existing creature types, so the Snail ceases to be a Snail. This makes it materially worse and can create undesirable mandatory-trigger behavior rather than the selected deterministic outlet structure.
- **Wick + Rat type-changer + Phyrexian Altar:** with the Snail also a Rat, sacrificing it to the Altar produces colored mana. The next Rat-entry event creates/recreates the Snail, and repeatable Rat-entry engines can convert this into arbitrarily many sacrifice/death/ETB events and mana. Payoffs such as Mirkwood Bats, Impact Tremors, Zulaport Cutthroat, Goblin Bombardment, or Altar of Dementia convert the loop into a deterministic win where the relevant preconditions are met.
- **Marrow-Gnawer + Intruder Alarm:** with at least two Rats available to tap with Marrow-Gnawer, its token-making activation creates Rats, those entries trigger Intruder Alarm and untap the team, and the increased Rat count lets the process repeat for arbitrarily many Rats.
- **Tainted Strike:** Wick, not the sacrificed Snail, is the source dealing the activated-ability damage. Giving Wick infect before the ability resolves causes that noncombat damage to players to be dealt as poison counters. A sacrificed Snail with power 10 therefore gives each opponent 10 poison counters, subject to normal prevention/replacement effects.
- **Bulk Up:** doubling the Snail's power before Wick's activation increases both the table-wide damage and card-draw payload; flashback provides a second use.
- **Blade of the Bloodchief:** every creature death can add a +1/+1 counter to the equipped Snail, making broad sacrifice turns and sweepers permanent Wick payload growth.
- **The Ozolith:** when a Snail with +1/+1 counters leaves the battlefield, those counters can be stored on The Ozolith and later moved to another creature at combat, mitigating the reset cost of Wick sacrificing its Snail.
- **Lich's Relic:** +2/+1 on the equipped Snail directly increases Wick's sacrificed-power payload; its ETB payment mode also supplies commander-independent removal utility.
- **Song of Totentanz:** `{X}{R}` creates X Rat tokens for its controller, causing X Rat-entry triggers for Wick, and gives creatures currently controlled haste until end of turn. It materially outperforms seven-mana symmetrical Plague of Vermin for this deck.
- **Cavern of Souls:** can make Wick/Rat creature spells uncounterable when Rat is chosen, but its restricted colored mana cannot pay Wick's `{U}{B}{R}` activated ability. The mana-base count therefore does not treat Cavern as unrestricted activation fixing.

## Legality / identity
- Commander color identity: U/B/R.
- Exact candidate contains only cards within U/B/R color identity.
- Current official Commander legality checked for the candidate set; no unexpected banned card identified.
- No project exception is required for Wick or any candidate card.

## Structural verification
- Total cards: **100**.
- Commander copies: **1**.
- Distinct card names: **99**.
- Repeated names: **Island x2 only**.
- Nonbasic singleton compliance: **PASS**.
- Land-capable slots: **36** (35 dedicated/front-face lands plus Boggart Trawler // Boggart Bog).
- U/B/R color identity: **PASS**.
- Official Commander legality: **PASS**.
- Relevant Oracle/rules/combo review: **PASS**.
- Commander-first strategic coherence: **PASS**.
- Candidate exhaustion: **PASS**.
- Adversarial red-team: **PASS**.
- Zero-new-material-improvement closure: **PASS**.

## SHA binding
Approval-candidate SHA-256 (exact UTF-8 bytes, including final newline):
`f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98`

Candidate artifact:
`refinement/decklists/Wick_the_Whorled_Mind_Approval_Candidate_2026-10-15.txt`

## Status
**APPROVAL_READY — not yet approved or locked.** Explicit user approval is required before changing `state/current_deck_overrides.json` or the master refinement tracker.
