# Marchesa, the Black Rose — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Exact candidate SHA-256: `627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Authoritative baseline reconciliation

- Authoritative source: current FINAL CSV/TXT exports (`GrixisFINAL60--2026.zip` / `GrixisFINALTXT60--2026.zip`).
- Baseline card count: **100**.
- Raw FINAL TXT SHA-256: `d292b21d373085ebe83ddea091bc7f51cf8f59048c987deca5fee2395205cdc9`.
- Normalized current-cycle baseline SHA-256: `2e8a3fec0749abe153cc2be45ca89f65a6f9634376f7740a9ff63633a15d3ab7`.
- Inherited `deck_card_audit.csv` membership is stale for this commander; it was not allowed to override the current FINAL exports.

Result: **PASS**.

## 2. Exact structural verification

Exact SHA-bound candidate:
- Total cards including commander: **100**.
- Lands: **34**.
- Distinct card names: **98**.
- Repeated names: **Island x2; Swamp x2 only**.
- Nonbasic singleton compliance: **PASS**.
- Commander count: **1**.
- Commander: **Marchesa, the Black Rose**.

Result: **PASS**.

## 3. Color identity

Marchesa's color identity is **U/B/R**. The final candidate was checked against current/project Scryfall-derived identity metadata, including the new additions and lands. No card introduces a color identity outside U/B/R.

Result: **PASS**.

## 4. Current Oracle / legality checkpoint

Marchesa's current Oracle text and current Commander legality were rechecked. The official Commander banned-card checkpoint was rechecked on 2026-10-15. The baseline already carried a current 2026-10-12 legality/identity refresh; every newly introduced card was independently checked against current Oracle/legality evidence before admission.

New-card checks covered:
- Agatha's Soul Cauldron
- Altar of Dementia
- Badlands
- City of Brass
- Danny Pink
- Flare of Denial
- Flooded Strand
- Forge of Heroes
- Gev, Scaled Scorch
- Imperial Recruiter
- Mana Confluence
- Misty Rainforest
- Sage of Fables
- Satoru, the Infiltrator
- Sneak Attack
- Spark Double
- Twilight Diviner
- Underground Sea
- Vampiric Tutor
- Verdant Catacombs
- Volcanic Island

Unexpected banned/illegal cards: **NONE**.  
Project-specific legality exceptions required: **NONE**.

Result: **PASS**.

## 5. Rules and interaction verification

### Marchesa timing
Marchesa must see a controlled creature with a +1/+1 counter die for her ability to trigger. That trigger creates a delayed return at the beginning of the next end step. If the creature dies after the beginning of an end step has already occurred, its return waits until the following end step. This timing was specifically applied to Sneak Attack sequencing; no same-step return is assumed from Sneak Attack's own beginning-of-end-step sacrifice trigger.

### Persist / counter interaction
The deck intentionally uses +1/+1-counter placement to neutralize persist's -1/-1 counters. The +1/+1 and -1/-1 counters are removed in pairs as a state-based action, allowing persist creatures to be reused when the required pieces are present.

### Verified compact packages
- **Gev, Scaled Scorch + Murderous Redcap**: after an opponent has lost life that turn, Gev supplies the +1/+1 counter needed to reset Redcap's persist state and support a deterministic Redcap loop.
- **Spark Double + Murderous Redcap + Ashnod's Altar**: Spark Double can copy Redcap, re-enter through persist with its additional +1/+1 counter, reset the persist counter state, and support a deterministic sacrifice/mana/damage loop.
- **Sage of Fables + Glen Elendra Archmage or Puppeteer Clique + appropriate sacrifice outlet**: Sage's Wizard counter placement resets persist and enables repeatable loops; Sage also provides counter-to-card conversion.
- **Mikaeus, the Unhallowed + Yawgmoth, Thran Physician + Gray Merchant of Asphodel + another qualifying nontoken non-Human creature**: Gray Merchant is a real engine/finish component in the verified Mikaeus/Yawgmoth package and was correctly retained after red-team review.
- **Agatha's Soul Cauldron**: activated abilities are granted only from creature cards that remain exiled by the Cauldron; the list does not assume static, triggered, or spell abilities are copied.
- **Satoru, the Infiltrator**: Marchesa and persist returns enter without being cast, satisfying Satoru's relevant draw condition.
- **Twilight Diviner**: supports the deck's graveyard-return plan by copying a qualifying creature entering/cast from a graveyard subject to its once-each-turn restriction.

Result: **PASS**.

## 6. Mandatory whole-list and strategic gates

- 99 noncommander slots independently adjudicated: **99/99**.
- Whole-list result: **78 KEEP / 21 CUT**.
- Candidate-ranking review: **COMPLETE**; rankings treated as research, not mandates.
- Current optimized Marchesa evidence reviewed: **COMPLETE**.
- Commander identity test: **PASS**.
- Mana-base red team: **PASS**.
- Combo/function red team: **PASS**.
- Adversarial final pass: **COMPLETE**.
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

## 7. Power and identity classification

**Power Bracket 4 — Optimized**.

The candidate is intentionally optimized around Marchesa's own counter/sacrifice/return identity. It does not rely on a generic Grixis cEDH shell to manufacture a higher ceiling than the commander naturally supports.

Recommended Archidekt tags:
- **+1/+1 Counters**
- **Aristocrats**
- **Combo**

## Final gate

**APPROVAL_READY — PASS**

This document does not constitute user approval. Marchesa, the Black Rose remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact SHA-bound candidate.
