# Inalla, Archmage Ritualist M7 Rev1 — canonical source-bound whole-100 verification

**Pre-merge candidate for Cory's explicit exact-SHA approval:** `c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69`. Do not assert the candidate is locked on `main` until post-merge exact byte verification.

## Owner authority and isolation

- Date 2026-10-24 (America/Chicago); Cory replied **“Approve”** directly after the full 100-card Inalla M7 Rev1 decklist, five add/cut pairs and tradeoffs, Bracket 5 and tags, engineering PR and exact hash.
- Canonical tracker index22, ID `Inalla__Archmage_Ritualist`. Only this deck's new approved artifact, registry object, tracker row and receipt/verification/test/workflow may change in this PR.
- Historical Oct14 approved artifact must stay identical: raw `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`, **no terminal LF**. Never rewrite it.
- Regression gate rehashes all 22 prior **new M7** owner-approved exact 100s from their registered source paths. Older 39 canonically approved decks are historical and not falsely counted as new M7.
- Next deck #24 Jeleva is historical locked only; do not mistake that for new M7 approval.

## Structural facts

- Candidate: **100 physical / 100 distinct names / 100 rows**, Inalla first line labeled commander, quantity1, terminal newline.
- No basic or nonbasic duplicates; `Tainted Pact` structural uniqueness.
- **27 lands**, 19 source-bound Game Changers, correct U/B/R identity and card identity.
- Five exact swaps: Flashback/Kefka; Corpse Dance/Final Fortune; Gifts Ungiven/Wheel of Fortune; Forbidden Orchard/Exotic Orchard; Starting Town/Island. No Pyroblast substitute; it was rejected before owner proposal.
- Official Commander legal: **all 99 candidate names except Flashback in October23 204-card Scryfall live collection snapshot**, each checks Commander legal and subset UBR. Flashback is {R} instant from 2026 Secrets of Strixhaven, independently in [Wizards official SOS release notes](https://media.wizards.com/2026/downloads/SOS_Release_Notes_FwhcBWdFIE/EN_MTGSOS_ReleaseNotes_20260410.pdf), [Gatherer SOS#115](https://gatherer.wizards.com/SOS/en-us/115/flashback) and current published legality. No invented Flashback Oracle ID; source is documented independently. Current official Commander format and Game Changer reference: [Wizards](https://magic.wizards.com/en/formats/commander).
- Paired audit artifact `refinement/verification/Inalla_Archmage_Ritualist_M7_Rev1_Scryfall_Selected_2026-10-24.json` pins actual 100 source-bound texts, color/legality and source provenance.

## Rules and strategies challenged

1. **Inalla Eminence** triggers for entering **nontoken** Wizards while commander is in command zone or battlefield, costs {1}, creates hasty token until next end step. `Spellseeker` tutoring for instants/sorceries with mana value <= 2 works for original and token ETBs.
2. **Gifts Ungiven** four-card pile `Spellseeker`, `Step Through`, `Reanimate`, `Unearth`: there are exactly `C(4,2)=6` opponent-chosen 2-to-graveyard splits. Three place Spellseeker in hand (cast as usual); the other three put Spellseeker in graveyard but leave at least one of Reanimate or Unearth in hand, so the nontoken Wizard can enter from graveyard and trigger Eminence. This is **Spellseeker access**, not an uncontested game win. Preconditions: all four in library, enough mana/life, combo components usable, and no effective interaction or graveyard hate.
3. **Corpse Dance** {2}{B} instant buyback {2} reanimates the **top creature card of graveyard**. With `Scholar of the Ages` on battlefield, `Burnt Offering` and Corpse Dance in hand and sufficient mana, sacrifice Scholar to Burnt Offering for seven B/R, then Corpse Dance with buyback for five to reanimate Scholar, returning Burnt Offering plus another instant/sorcery; this generates conditional net +1 B/R per iteration after Burnt cost and repeats ETBs/spells. Requires Scholar to remain top creature card and buyback to resolve; targetless graveyard reorder/hate and disruption matter.
4. **Flashback** targets an instant/sorcery in your graveyard, grants flashback at original mana cost. Costs are payable, normal timing/targets apply, spell is exiled after flashback-cast use. It cannot cast an alternative-free spell just because it granted flashback. It is a Spellseeker-searchable spell with mana value1.
5. **Mana tradeoffs**: Forbidden Orchard colored tap creates a 1/1 for opponent; Starting Town enters untapped only if played in own turns 1–3 and pays 1 life per colored activation. Island loss reduces fetchable untapped blue/nonbasic hate resilience, and Exotic Orchard often taps for painless rainbow in cEDH pods.
6. **Losses**: removing Kefka loses Wizard card advantage, Final Fortune loses extra turn, Wheel loses fast seven-card refill and Breach graveyard fill. These were explicitly disclosed to Cory as prior Oct14 owner-added cards.

## Verification scope and milestone treatment

- Focused canonical PR exact-head tests must check candidate raw SHA, original Oct14 raw SHA, 100 source names/Oracle, 27 lands, 19 Game Changers, six Gifts splits, rules source, approval receipt, only Inalla registry/tracker edit and 22 original new M7 locks by their own raw bytes.
- Re-run most recent #22 Gwendlyn gate. GitHub Actions PASS is not by itself owner consent; approval is separately provided by Cory and recorded.
- No independent third-model gameplay review, full Magic engine simulation, or real multiplayer win-rate test claimed.
- Natural commander ceiling **5 — cEDH**, tags **Spellseeker Combo / Reanimator / Turbo**, project exceptions **none**.

After exact-head PASS, merge with expected head SHA, refetch `main`, independently hash approved Inalla artifact, verify registry APPROVED/LOCKED, tracker updated only Inalla, 22 previous new M7 lock hashes intact.
