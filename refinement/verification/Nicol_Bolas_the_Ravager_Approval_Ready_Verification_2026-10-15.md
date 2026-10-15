# Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #42 of 62  
Exact candidate SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **41 APPROVED / LOCKED decks** through original Nicol Bolas. The reconciled tracker identifies **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen** as the next unlocked deck (tracker index 41 / deck 42 of 62).

Original Nicol Bolas (#41) is frozen under a distinct Discard / Commander Damage / Control identity. This deck is intentionally differentiated around Ravager ETB discard, transformation, planeswalkers, proliferate, copied loyalty abilities, and graveyard recursion.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: current FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Nicol_Bolas__the_Ravager.txt`
- Raw FINAL TXT SHA-256: `61555ac47ff9be33805cacb19ba7aadd35a6b262c510fdd9ea2a91ca633c20e2`
- FINAL CSV: `GrixisFINAL60--2026.zip / Nicol_Bolas__the_Ravager.csv`
- Raw FINAL CSV SHA-256: `71e4b6797d31db559d888b88d9a0e2048d1ece4aeb65ed7440eeb1474a6c798e`
- Baseline total: **100 cards**
- Baseline distinct names: **96**
- Baseline lands: **34**
- Repeated baseline names: **Island x3, Swamp x3 only**
- CSV/TXT membership reconciliation: **PASS**

Historical October 11 update records were treated as evidence only, not authoritative membership or mandatory decisions.

Result: **PASS**.

## 3. Exact candidate structural verification

SHA-bound candidate file: `refinement/decklists/Nicol_Bolas_the_Ravager_Approval_Ready_2026-10-15.txt`

Independent byte/hash recount:

- SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`
- Total cards including commander: **100**
- Commander: **1x Nicol Bolas, the Ravager // Nicol Bolas, the Arisen**
- Lands: **34**
- Distinct names: **98**
- Repeated names: **Island x2, Swamp x2 only**
- Nonbasic / nonbasic-card singleton violations: **0**
- Baseline delta: **16 cuts / 16 additions**
- Mandatory whole-list adjudication: **83 KEEP / 16 CUT across all 99 noncommander copies**

Result: **PASS**.

## 4. Commander Oracle / color identity / current legality

Current front face:
- `{1}{U}{B}{R}`
- Legendary Creature — Elder Dragon
- Flying
- When Nicol Bolas enters, each opponent discards a card.
- `{4}{U}{B}{R}`: Exile Nicol Bolas, then return him transformed under his owner's control. Activate only as a sorcery.
- 4/4

Current back face, Nicol Bolas, the Arisen:
- Legendary Planeswalker — Bolas
- 7 starting loyalty
- `+2`: draw two cards
- `-3`: Nicol Bolas deals 10 damage to target creature or planeswalker
- `-4`: put target creature or planeswalker card from a graveyard onto the battlefield under your control
- `-12`: exile all but the bottom card of target player's library

Color identity is **U/B/R**. Every candidate card is within U/B/R color identity or colorless.

Current Wizards Commander banned-list checkpoint reviewed 2026-10-15: no card in the exact candidate is Commander-banned. Nicol Bolas, the Ravager is currently Commander-legal. Project-specific exception required: **NONE**.

Result: **PASS**.

## 5. Transform rules / immediate loyalty activation

The commander's activated ability exiles the front face and returns the same double-faced card transformed. If Ravager leaves the battlefield before that activated ability resolves, it cannot be exiled from the battlefield and returned by that resolving ability.

A transforming double-faced card normally enters front face up unless an effect explicitly instructs it to enter transformed. The Ravager activation explicitly instructs the return transformed, so it returns as the Arisen.

Once the Arisen has entered transformed, it is a new permanent and may activate a loyalty ability that turn if normal timing and activation restrictions are satisfied; it is not subject to creature summoning-sickness restrictions for loyalty abilities.

Result: **PASS**.

## 6. Training Grounds

Training Grounds says activated abilities of creatures you control cost `{2}` less to activate, without reducing the total mana component below one mana.

Ravager's transform ability is an activated ability of a creature while he is on the front face. Training Grounds reduces `{4}{U}{B}{R}` to **`{2}{U}{B}{R}`**. It does not remove colored mana symbols.

This is one of the strongest direct commander-specific upgrades in the candidate because it moves the transform from seven mana to five mana while preserving the exact game action the commander is designed to perform.

Result: **PASS**.

## 7. Displacer Kitten / double-faced reset

Displacer Kitten blinks a target nonland permanent you control whenever you cast a noncreature spell.

- Blinking **front-face Ravager** returns the card as a new front-face Ravager and retriggers the each-opponent discard ETB.
- Blinking **transformed Arisen** does **not** return the planeswalker face. Because Kitten does not instruct the card to enter transformed, the double-faced card returns front face up as Ravager, retriggering the ETB discard.
- The returned card is a new object; counters from its previous existence are gone.

The line is therefore an intentional commander reset / ETB reuse engine, not planeswalker flicker protection that preserves the back face.

Result: **PASS**.

## 8. Deliver Unto Evil

Deliver Unto Evil targets up to four cards in your graveyard. If you control a **Bolas planeswalker**, all legal targets return to your hand; otherwise an opponent chooses two to remain in the graveyard and the rest return.

The transformed commander is a planeswalker with subtype **Bolas**, so controlling the Arisen satisfies the enhanced condition. This makes Deliver Unto Evil directly commander-dependent recursion after transformation.

Result: **PASS**.

## 9. Rowan's Talent / Rings of Brighthearth / copied loyalty abilities

Rowan's Talent triggers whenever a loyalty ability of the enchanted planeswalker is activated and copies that ability. Rings of Brighthearth may copy any activated nonmana ability for `{2}` when its trigger resolves, including planeswalker loyalty abilities.

A copied loyalty ability does **not** repeat its loyalty cost. The loyalty counters are added or removed only for the original activation. Consequently:

- Arisen `+2` can draw four total cards when copied once without adding four loyalty.
- `-3` can create two 10-damage ability instances while removing only three loyalty for the original activation.
- `-4` can reanimate two targets when copied once while removing only four loyalty.
- `-12` can be copied if the original can legally be activated; only the original activation removes twelve loyalty.

Result: **PASS**.

## 10. The Chain Veil / Rings / Teferi, Temporal Archmage engine

The Chain Veil's `{4}, {T}` ability is a nonmana activated ability. Rings of Brighthearth can therefore copy it for `{2}`.

Official Chain Veil rules state that each additional time its last ability resolves allows another loyalty activation for each planeswalker that turn. Therefore one Chain Veil activation copied by Rings gives **two Chain Veil resolutions**, adding two extra loyalty-activation permissions beyond the normal once-per-turn activation.

With:
- Teferi, Temporal Archmage,
- The Chain Veil,
- Rings of Brighthearth,
- and mana permanents Teferi can untap that collectively produce at least six mana (the candidate can assemble this with combinations such as Mana Vault + Sol Ring + another mana permanent),

the following repeatable engine is rules-valid:

1. Spend six total mana to activate The Chain Veil and pay for Rings to copy it.
2. Resolve two Chain Veil abilities, creating two additional planeswalker activations.
3. Use one Teferi activation on `-1` to untap The Chain Veil and enough mana permanents to reproduce six mana.
4. Use another Teferi activation on `+1`, restoring the loyalty spent on `-1`.
5. Re-activate and copy The Chain Veil.

Each iteration consumes two Teferi activations but creates two new activation permissions, while Teferi's loyalty can remain stable from alternating `-1` and `+1`. The engine can therefore generate arbitrarily many Chain Veil resolutions / loyalty-activation permissions while the required permanents remain in place.

This is documented as a multi-card combo engine. The verification does **not** claim that any two pieces alone form an infinite combo.

Result: **PASS**.

## 11. Tezzeret the Seeker

Tezzeret's `+1` untaps up to two artifacts, which can refresh The Chain Veil and/or mana artifacts. His `-X` searches for an artifact with mana value X or less and puts it directly onto the battlefield.

Relevant targets include:
- The Chain Veil at X=4,
- Rings of Brighthearth at X=3,
- Ichormoon Gauntlet at X=3,
- Mana Vault at X=1,
- Sol Ring at X=1,
- Mox Opal / Chrome Mox at X=0.

This makes Tezzeret an engine tutor/untapper rather than generic five-mana value.

Result: **PASS**.

## 12. Sanctum Lurker

Sanctum Lurker states that planeswalkers you control aren't put into their owners' graveyards for having 0 loyalty, and grants each planeswalker you control `[+2]: This planeswalker deals 1 damage to each opponent and you gain 1 life.`

A planeswalker that reaches exactly 0 loyalty can therefore remain on the battlefield while Lurker's effect applies. On a later legal loyalty activation, its granted `+2` can be activated and the two loyalty counters are added as the activation cost.

The protection is specifically from the state-based action for 0 loyalty; it does not make planeswalkers indestructible or prevent other removal.

Result: **PASS**.

## 13. Ripples of Potential

Ripples proliferates, then lets the controller phase out any number of permanents they control that received counters from that proliferate action.

This means a planeswalker can receive an additional loyalty counter and then phase out. Phasing does not remove its counters. It phases back in normally during its controller's next untap step.

Ripples therefore combines loyalty growth with temporary protection without sacrificing the counter gained.

Result: **PASS**.

## 14. Dreamtide Whale

Dreamtide Whale has vanishing 2 and triggers whenever a player casts their second spell each turn, causing proliferate.

The trigger can increase loyalty counters on selected planeswalkers. Because the Whale itself has time counters, the controller may also choose it during proliferate to add a time counter, extending its vanishing clock rather than accelerating its disappearance.

Result: **PASS**.

## 15. Spark Double

Spark Double may enter as a copy of a creature or planeswalker you control, except it is not legendary and enters with an additional loyalty counter if it is a planeswalker.

It may copy the **currently transformed Arisen** because the Arisen is a planeswalker you control. Spark Double is not itself a transforming double-faced card; it simply enters with the copiable characteristics of the chosen planeswalker face, nonlegendary, and with one additional loyalty counter.

This is distinct from attempting to copy front-face Ravager and use the copied transform ability: a non-double-faced copy of Ravager can be exiled by that ability but cannot return transformed.

Result: **PASS**.

## 16. Dark Intimations

Dark Intimations remains a commander/flavor-specific support spell: each opponent sacrifices a creature or planeswalker and discards a card, while you recover a creature or planeswalker and draw.

Its graveyard rider triggers when you **cast a Bolas planeswalker spell** and causes that planeswalker to enter with an additional loyalty counter. Transforming Ravager through his activated ability does **not** cast a planeswalker spell, so Dark Intimations does not add a loyalty counter to the Arisen merely because the commander transforms.

Result: **PASS**.

## 17. Mana-base red team

Candidate land count remains **34**, exactly equal to the authoritative baseline.

Final lands include:
- **nine fetchlands:** Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills;
- original duals Badlands, Underground Sea, Volcanic Island;
- shocks Blood Crypt, Steam Vents, Watery Grave;
- Xander's Lounge;
- City of Brass, Mana Confluence, Command Tower, Reflecting Pool;
- Luxury Suite, Morphic Pool, Training Center;
- utility lands Ancient Tomb, Cavern of Souls, Karn's Bastion, Otawara, Takenuma, Urborg;
- basics Island x2, Mountain x1, Swamp x2.

The deck also retains a high density of nonland mana: Chrome Mox, Lotus Petal, Mana Vault, Mox Diamond, Mox Opal, Sol Ring, Arcane Signet, three Signets, Fellwar Stone, three Talismans, and Jeska's Will.

The red team rejected lowering the land count because the deck wants Ravager on curve and still wants to reach five mana with Training Grounds or seven mana naturally for transformation. It also rejected weaker planeswalker-themed lands that would reduce no-budget color quality.

Result: **PASS**.

## 18. Candidate exhaustion / encyclopedia differentiation

Project candidate rankings, historical October 11 decisions, current optimized Ravager evidence, contemporary 2026 cards, planeswalker engines, proliferate pieces, loyalty-copy effects, graveyard recursion, transform-cost support, premium interaction, fast mana, and mana-base challengers were all reviewed.

Notable rejected packages:
- Cruel Ultimatum: flavorful but inefficient relative to current commander/planeswalker engines.
- Ugin, the Spirit Dragon: generically powerful but expensive and not needed at the already dense top end.
- Dack Fayden: efficient but not superior to the finalized walker/engine roles.
- Ashiok, Dream Render: graveyard exile conflicts with the Arisen's `-4` and Deliver Unto Evil.
- Thrummingbird / Experimental Augury: proliferate density is already sufficient after Dreamtide Whale and Ripples.
- Teferi's Talent: slower than Rowan's Talent for direct loyalty multiplication.
- Interplanar Beacon / Turbulent Wetlands: do not beat premium no-budget fixing.
- additional wheel package: rejected to avoid overlap with Nekusar/Gwendlyn and because Ravager's discard is not intended to repeatedly refill opponents.
- generic Oracle/Consultation / unrelated Breach wins: rejected as commander-irrelevant homogenization.

Commander-necessity test: Training Grounds accelerates Ravager's unique transform; Displacer Kitten reuses Ravager's ETB; Deliver Unto Evil is fully enabled by the Arisen; Rowan's Talent and Rings multiply the Arisen's abilities; proliferate engines accelerate the transformed commander's loyalty; the Chain Veil package makes the Arisen one of the primary beneficiaries rather than an incidental commander.

Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

Result: **PASS**.

## 19. Mandatory gate summary

- Current repository state recovered: **PASS**
- Locked decks before Ravager approval: **41/62**
- Correct next unlocked deck: **PASS**
- Authoritative FINAL baseline reconciled: **PASS**
- Mandatory 99-slot audit: **99/99 PASS**
- Whole-list result: **83 KEEP / 16 CUT**
- Candidate structural count: **100 cards — PASS**
- Distinct names: **98**
- Land count: **34**
- Singleton compliance: **PASS**
- U/B/R color identity: **PASS**
- Current official Commander legality: **PASS**
- Project exceptions: **NONE REQUIRED**
- Commander Oracle / transform rules: **PASS**
- Training Grounds transform reduction: **PASS**
- Displacer Kitten DFC reset: **PASS**
- Deliver Unto Evil Bolas condition: **PASS**
- Rowan's Talent / Rings loyalty copies: **PASS**
- Chain Veil / Rings / Teferi engine: **PASS**
- Sanctum Lurker 0-loyalty interaction: **PASS**
- Ripples / Dreamtide proliferate interactions: **PASS**
- Spark Double interaction: **PASS**
- Dark Intimations cast-vs-transform distinction: **PASS**
- Mana-base red team: **PASS**
- Candidate exhaustion: **PASS**
- Adjacent-deck differentiation from original Nicol Bolas: **PASS**
- Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**
- Natural ceiling: **Power Bracket 4 — Optimized**

Recommended Archidekt tags: **Superfriends / Transform / Proliferate**.

## Final gate

**APPROVAL_READY — PASS**

Exact approval-ready candidate SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`.

This record is working verification evidence only. Nicol Bolas, the Ravager // Nicol Bolas, the Arisen remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact candidate.
