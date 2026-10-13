# Be'lakor, the Dark Master — New-Cycle Refinement & Verification Certificate

**Deck:** #7 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** immutable October 12 source package plus `GrixisFINAL60--2026.zip` / `GrixisFINALTXT60--2026.zip`  
**Baseline raw TXT SHA-256:** `9b0e16a43add999252504948aa3104666a342bf4f8c80b758a2d9f65649fe6c7`  
**Baseline raw CSV SHA-256:** `b070c697adffdf4ad5187f390c7fe4b0ae60bfa6e12d1f160cd1991d2174cfb0`  
**Normalized baseline-list SHA-256:** `fe61e3a7d7bc5fc6d56a9c6a03b97f3986c606e3626a6a3839cdd91a7dfd9e0e`  
**Revised exact-TXT SHA-256:** `f48359f816498b386b085db60f0456576c8af9b055408685df71f0d1db448545`

## 1. Structural integrity

- Frozen baseline CSV/TXT are byte-identical between the source package and named FINAL archives.
- Baseline: 100 card copies, 94 distinct names. Revised: 100 card copies, 94 distinct names, 94 lines.
- Commander marker appears exactly once on the first line.
- Singleton/copy compliance: **PASS**. Only basic lands repeat, as in the baseline: Island x3, Mountain x2, Swamp x4. No nonbasic duplicates.
- Land count: 36, unchanged.
- CSV/TXT quantity map reconciles exactly.
- Actual list delta: +Demonic Covenant, +Ardyn, the Usurper; −Reaper from the Abyss, −Archfiend of Depravity; no other membership changes.

## 2. Commander identity and strategy

Be'lakor's current Oracle text: flying; on entry, draw X and lose X life where X is the number of Demons controlled; whenever another Demon enters under your control, it deals damage equal to its power to any target. The list is optimized around Demon density, repeatable ETB triggers, token/copy effects, reanimation, cost reduction and commander protection. The two additions do not force a new archetype.

## 3. Card identity, Oracle and legality

- All 94 baseline names are covered by the project's current Scryfall exact-printing/name metadata refresh documented in active-cycle records (generated `2026-10-13T07:03:26.694525Z`, bulk data updated `2026-10-12T21:06:24.577Z`).
- **Demonic Covenant**: current Oracle confirms Kindred Enchantment — Demon, {4}{B}{B}; current reference reports Commander legal. [Oracle and legalities](https://mtg.wtf/card/dsc/49/Demonic-Covenant).
- **Ardyn, the Usurper**: current Oracle confirms color identity B and its Demon keyword grant / graveyard-token ability; current reference reports Commander legal. [Oracle and legalities](https://mtg.wtf/card/fin/444/Ardyn-the-Usurper).
- **Reaper from the Abyss** and **Archfiend of Depravity**: current Oracle/type and Commander legalities checked. [Reaper](https://mtg.wtf/card/c14/159/Reaper-from-the-Abyss); [Archfiend](https://mtg.wtf/card/scd/67/Archfiend-of-Depravity).
- Official Commander banned-list checkpoint: checked 2026-10-13. The [October 12, 2026 Wizards announcement](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026) applied to Competitive Brawl only; it did not change tabletop Commander. No final-list card is newly banned; no project exception applies.

## 4. Rules interactions

- **Demonic Covenant as a Demon:** Be'lakor counts it as a Demon permanent for the ETB draw count. Be'lakor's other-Demon trigger also triggers when Covenant enters, but a noncreature permanent has no power; under CR 107.2 an undefined numeric value is treated as 0, so Covenant's own entry deals 0 damage through this ability. Its end-step 5/5 Demon token is a creature and will produce a 5-damage Be'lakor trigger if Be'lakor remains on the battlefield. Covenant's draw ability triggers once for each player you attack with one or more Demons. Its sacrifice clause applies only when the two cards milled share the exact same combination of card types.
- **Ardyn:** Ardyn itself is not a Demon, so it does not add to Be'lakor's Demon count. Its beginning-of-combat ability can create a token copy of a creature card from any graveyard, modified to be a 5/5 black Demon. Copiable ETB abilities are retained and trigger when the token enters; the token also triggers Be'lakor's damage ability. Menace, lifelink and haste apply to Demons you control.
- No deterministic infinite combo is added or claimed.

## 5. Candidate and performance gates

- 16 candidates reviewed: two additions implemented, two baseline cards retained, twelve rejected with reasons.
- Candidate ranking / EDHREC fields are from the October 12 project snapshot and used as discovery evidence only.
- No qualified matched-start multiplayer simulator or representative game sample was available. No win-rate or empirical superiority claim is made.

## 6. Verification gates

| Gate | Outcome | Evidence / limits |
|---|---|---|
| Frozen baseline integrity | **PASS** | Source-package and archive bytes match; hashes recorded. |
| Count and singleton | **PASS** | 100 copies; 94 distinct names; commander first; only basics repeat. |
| CSV/TXT reconciliation | **PASS** | Quantity maps match exactly. |
| Identity / Oracle / legality | **PASS** | Baseline metadata refresh plus direct checks for both additions and cuts. |
| Official Commander ban-list checkpoint | **PASS** | Checked 2026-10-13; latest Wizards changes affected Competitive Brawl only. |
| Commander-first blueprint | **PASS** | Demon ETB damage/draw, token engines, cost reductions and reanimation retained. |
| Candidate decision coverage | **PASS** | 16 candidates; 2 accepted, 2 retained, 12 rejected with reasons. |
| Rules interactions | **PASS** | Kindred subtype/no-power interaction and Ardyn token-copy interaction verified. |
| Multiplayer performance | **NOT AVAILABLE** | No qualified matched-start sample; no win-rate claim. |
| Hash / change record | **PASS** | Exact TXT hash, decision ledger, change rows and certificate recorded separately from baseline. |
| Automatic finalization | **PASS** | Mandatory technical gates pass; no separate user-approval gate in this cycle. |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This status applies only to the exact revised TXT bytes with SHA-256 `f48359f816498b386b085db60f0456576c8af9b055408685df71f0d1db448545`.