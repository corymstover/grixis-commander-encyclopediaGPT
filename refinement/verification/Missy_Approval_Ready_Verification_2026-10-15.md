# Missy — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #38 of 62  
Exact candidate SHA-256: `9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

The current-cycle repository state contains 37 APPROVED/LOCKED decks through Mishra, Eminent One. The reconciled tracker names Missy as the next unlocked deck. No prior current-cycle Missy blueprint, candidate decision, approval-ready list, or verification record existed before this audit.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: current FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Missy.txt`
- Raw FINAL TXT SHA-256: `31775ecbab42edc930e05965101d980d79947612d2605c20f82f0e39b2e10eb5`
- FINAL CSV: `GrixisFINAL60--2026.zip / Missy.csv`
- Raw FINAL CSV SHA-256: `3055aa2c9a8b318fe58c3f3d8aa86fb729e25d57214979de69f5f6ad386ddd5c`
- Baseline total: **100 cards**
- Baseline distinct names: **96**
- Baseline lands: **35**

The older card-audit membership snapshot differs by five cards and was not allowed to override the current FINAL export. Candidate rankings were used as discovery evidence only.

Result: **PASS**.

## 3. Exact structural verification

SHA-bound candidate file: `refinement/decklists/Missy_Approval_Ready_2026-10-15.txt`

- Total cards including commander: **100**
- Commander: **1x Missy**
- Lands: **35**
- Distinct names: **97**
- Repeated names: **Island x2, Swamp x3** only
- Nonbasic/nonbasic-card singleton violations: **0**
- Baseline delta: **16 cuts / 16 additions**
- Whole-list adjudication: **83 KEEP / 16 CUT across all 99 noncommander slots**

Result: **PASS**.

## 4. Commander Oracle / color identity / legality

Current Missy text verified on 2026-10-15:

> Whenever another nonartifact creature dies, return it to the battlefield under your control face down and tapped. It's a 2/2 Cyberman artifact creature.
>
> At the beginning of your end step, each opponent faces a villainous choice — Each artifact creature you control deals 1 damage to that opponent, or you draw a card and chaos ensues.

Missy's color identity is **U/B/R**. All additions are colorless, B, U, R, UB, UR, BR, or lands with no identity outside U/B/R. No incoming card introduces a color-identity violation.

Current Commander legality checkpoint:
- Missy: legal.
- Incoming interaction-dependent cards Ruthless Ripper, Dragon's Eye Savants, Horde Ambusher, Boltbender, Bane of the Living, Cybership, and Panoptic Projektor: Commander-legal at current public checkpoints.
- Retained/new artifacts and lands are within color identity; Mana Vault is not on the current tabletop Commander banned list.
- Wizards' 2026-10-12 B&R announcement made Competitive Brawl changes but no tabletop Commander change affecting this candidate.
- No candidate name appears on the current tabletop Commander banned list.
- Project-specific exception required: **NONE**.

Result: **PASS**.

## 5. Missy face-down rules

Current Doctor Who rulings establish:

1. A creature returned by Missy is a face-down 2/2 Cyberman artifact creature with no name and no color.
2. If that face-down card has morph, its controller may turn it face up by paying/revealing its morph cost.
3. When the face-down creature turns face up, Missy's effect making it a Cyberman ends and its printed characteristics resume.
4. Turning a face-down permanent face up does not cause it to leave and re-enter the battlefield.

This is the rules foundation for the selected zero-mana reveal-cost creatures.

Result: **PASS**.

## 6. Commander-native loop verification

### Ruthless Ripper

Ruthless Ripper has morph—reveal a black card and drains a target player for 2 when turned face up. With Missy and a free sacrifice outlet, the loop is:

face-up Ripper is sacrificed → Missy returns it face down as a Cyberman artifact → reveal a black card to turn it face up for no mana → Ripper drains 2 → repeat.

Verified deterministic variants in the candidate include:
- Goblin Bombardment: infinite damage plus Ripper life loss.
- Phyrexian Altar: infinite colored mana plus Ripper life loss.
- Ashnod's Altar: infinite colorless mana plus Ripper life loss.
- Viscera Seer: infinite scry/death triggers plus Ripper life loss.
- Altar of Dementia: Ripper has power 1 face up, so each loop mills 1 and drains 2.

### Dragon's Eye Savants

Morph—reveal a blue card is mana-free. Missy plus Savants plus Ashnod's Altar produces infinite colorless mana/death/ETB/LTB/sacrifice triggers; Phyrexian Altar produces the corresponding colored-mana loop. **Red-team caveat:** Savants has printed power 0, so Altar of Dementia alone does not mill cards in the Savants loop without a power boost. No such unsupported mill claim is used.

### Horde Ambusher

Morph—reveal a red card is mana-free. Missy plus Horde Ambusher plus Goblin Bombardment is a deterministic infinite-damage/death/ETB/LTB/sacrifice loop. Positive printed power also makes Altar of Dementia a mill outlet for this loop.

Result: **PASS**.

## 7. Ixidron red-team correction

Ixidron says, "As this creature enters, turn all other nontoken creatures face down." Missy is another nontoken creature relative to Ixidron, so Ixidron turns Missy face down and removes access to the commander's engine until Missy is turned face up again by another effect.

Therefore Ixidron is **CUT**, not retained as generic face-down synergy.

Result: **PASS**.

## 8. The Valeyard retention

The Valeyard says that if an opponent would face a villainous choice, they face that choice an additional time. Missy's end-step ability instructs each opponent to face a villainous choice, so The Valeyard directly doubles the commander-specific choice event for each opponent.

The red-team pass therefore reversed the temptation to cut The Valeyard as an expensive side-theme card. It is retained.

Result: **PASS**.

## 9. Ugin's Mastery retention

Ugin's Mastery triggers whenever you cast a colorless creature spell. Morph/disguise cards cast face down are colorless creature spells on the stack, so casting them face down triggers Mastery. Its attack trigger also turns a face-down creature you control face up when the attacking power threshold is met.

This makes the card materially more commander-specific than a superficial reading suggests. It is retained.

Result: **PASS**.

## 10. Panoptic Projektor

Panoptic Projektor:
- can tap to make the next face-down creature spell cast that turn cost {3} less; and
- causes a triggered ability caused by turning a face-down permanent face up to trigger an additional time.

The first ability helps morph/disguise creatures cast from hand face down. It does **not** pay for turning Missy-returned permanents face up. The second ability doubles triggered face-up payoffs such as Ruthless Ripper, Bane of the Living, Pyrotechnic Performer, and Aphetto Runecaster triggers as applicable.

Result: **PASS**.

## 11. Cybership

Cybership's combat-damage trigger puts the top two cards of the damaged player's library onto the battlefield face down under your control as 2/2 Cyberman artifact creatures. Its rulings mirror Missy's relevant face-down treatment: cards with morph may be turned face up for their morph cost, and when a face-down card turns face up the effect making it a Cyberman ends.

Cybership is therefore a direct commander-identity theft/Cyberman engine rather than a generic six-drop.

Result: **PASS**.

## 12. Mana and curve red team

Candidate remains at **35 lands** while replacing three lower-tempo lands with Mana Confluence, City of Brass, and Phyrexian Tower, and converting one of two Mountains into Inventors' Fair. The mana base retains fetches, original duals, shocks, multiplayer duals, check/slow lands, Xander's Lounge, basics, Command Tower, and Exotic Orchard.

All three Signets become corresponding Talismans, and Mana Vault is added. This improves early acceleration and materially helps deploy/protect a six-mana commander without reducing land count.

The refined nonland curve is lower than the baseline because the seven-mana Dalek Emperor, multiple five/six-mana engines, and slower four-mana Dalek value are replaced by more one/two/four-mana infrastructure.

Result: **PASS**.

## 13. Candidate exhaustion / commander necessity / strategic coherence

The project top-100 candidates, current Missy EDHREC core/optimized evidence, stale-baseline omissions such as Boltbender/Cybership, generic Grixis staples, alternative sacrifice outlets, turn-face-up engines, high-cost morphs, and mana-base challengers were reviewed.

Key reject conclusions include Biotransference (anti-synergy because it makes creatures artifacts and suppresses Missy's nonartifact-death trigger), redundant outlets after the finalized package, slow four-plus-mana ramp, and generic exile interaction that prevents opposing creature deaths from becoming Missy resources.

Commander-necessity test: the candidate's primary deterministic loops, theft conversion, face-down recursion, asymmetric wipes, and villainous-choice scaling materially degrade or disappear without Missy. The list is not a generic Grixis shell wearing Missy as commander.

Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

Result: **PASS**.

## 14. Mandatory gate summary

- Current state recovered from authoritative repository: **PASS**
- Current-cycle locked decks before Missy approval: **37/62**
- Next unlocked deck correctly identified as Missy: **PASS**
- Authoritative FINAL baseline reconciled: **PASS**
- Mandatory 99-slot audit: **99/99 PASS**
- Candidate-ranking exhaustion: **PASS**
- Outside meaningful alternatives reviewed: **PASS**
- Commander Oracle text: **PASS**
- Color identity: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE REQUIRED**
- Relevant rules/combos: **PASS**
- Red-team pass: **PASS**
- Mana/curve review: **PASS**
- Commander-first coherence: **PASS**
- Natural power ceiling: **Power Bracket 4 — Optimized**
- Exact 100-card count: **PASS**
- Singleton compliance: **PASS**
- Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**

Recommended Archidekt tags: **Cybermen / Morph / Aristocrats**.

## Final gate

**APPROVAL_READY — PASS**

Exact approval-ready candidate SHA-256: `9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed`.

This record is a working verification artifact only. Missy remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact candidate.
