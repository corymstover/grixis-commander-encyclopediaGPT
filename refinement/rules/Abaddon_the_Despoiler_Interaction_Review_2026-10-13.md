# Abaddon the Despoiler — Interaction Review v1

**Review date:** 2026-10-13  
**Baseline snapshot:** 2026-10-12  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Decklist changes:** None.  
**Comparative playtests:** None completed; exploratory Forge runtime/replay smoke checks exist but are not performance evidence. This interaction review must not be treated as comparative test evidence.

## 1. Aurora Phoenix ↔ Mind's Desire: rules findings

### Relevant current card text and facts

- **Abaddon the Despoiler** costs {2}{U}{B}{R}. During your turn, spells you cast from your hand with mana value no greater than the total amount of life your opponents have lost this turn have cascade. This is a current-turn aggregate life-loss threshold; it is not an opponent's current life total or damage dealt by a single source.
- **Aurora Phoenix** costs {4}{R}{R}, has printed cascade, and says: “Whenever you cast a spell with cascade, return this card from your graveyard to your hand.” It is red identity and listed as Commander-legal.
- **Mind's Desire** costs {4}{U}{U}, has storm, and is listed as Commander-legal. When it is cast from your hand during your turn, it also meets Abaddon's threshold and gains cascade if the opponents' aggregate life loss this turn is at least six. Storm remains active.

Sources checked:
- [Current Magic Comprehensive Rules (effective September 25, 2026)](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt), especially rules 113.10, 603.2, 702.40 (storm), and 702.85 (cascade).
- [Official Magic rules landing page](https://magic.wizards.com/en/rules).
- [Abaddon Oracle text and Commander legality](https://www.mtg.wtf/card/40k/171/Abaddon-the-Despoiler).
- [Aurora Phoenix text, format legality and official rulings](https://www.metamox.com/cards/aurora-phoenix).
- [Mind's Desire text, format legality and rulings](https://www.mtg.wtf/card/c21/123/Minds-Desire).

### Confirmed interaction

**Abaddon-granted cascade does trigger Aurora Phoenix's graveyard ability.** Abaddon itself costs five mana ({2}{U}{B}{R}; mana value 5), not six. Abaddon's static ability grants cascade to qualifying spells cast from hand. Cascade triggers when the spell is cast (CR 702.85a); Aurora Phoenix's trigger condition is that a spell with cascade was cast (CR 603.2). Therefore, if Aurora Phoenix is in its owner's graveyard immediately after a qualifying hand-cast spell is finished being cast, its return ability triggers even when that spell received cascade from Abaddon rather than printing cascade.

The Aurora Phoenix ruling states that its return ability triggers only if Aurora Phoenix is in the graveyard immediately after casting finishes, and that the cascade ability and Aurora return trigger can be put on the stack in either order. This matters for decision-making:
- Put Aurora Phoenix's return trigger above the cascade trigger to return the Phoenix before revealing/casting a cascade hit.
- Put the cascade trigger above the Phoenix return trigger to resolve cascade first. Aurora can return later if it is still in the graveyard when its return trigger resolves.
- If the Phoenix is not in the graveyard immediately after the spell is cast, the return ability does not trigger for that cast.

Aurora's printed cascade works when Aurora itself is cast from hand or another zone. If Aurora is cast from hand during your turn and the threshold is at least six, Abaddon grants it a second instance of cascade in addition to its printed instance; CR 702.85c says multiple instances trigger separately. Thus Aurora can generate two cascade triggers on that cast, while its graveyard-return ability triggers only once for that one cast event if Aurora was in the graveyard immediately after casting. If Aurora is cast from exile by a cascade effect, Abaddon's hand-cast condition does not grant it another instance.

### What is actually lost by cutting Mind's Desire

The proposed swap is not a free upgrade:
- Both cards have mana value six.
- Aurora increases recursive cascade density and supplies a reusable threat/value card if the deck repeatedly casts cascade spells while Aurora can be returned. When cast from hand at a threshold of six or more, its printed cascade plus Abaddon's granted instance produce two cascade triggers.
- Mind's Desire supplies a potentially explosive storm spell and can itself gain one Abaddon-granted cascade when cast from hand after at least six aggregate opponent life loss this turn; its storm copies are not cast and therefore do not trigger cascade.
- Consequently, replacing Mind's Desire reduces a high-ceiling draw payoff that can combine storm and cascade on a qualifying turn. This cost must be included in testing; cascade synergy alone does not establish that Aurora is the stronger card.

**Candidate status:** Rules interaction confirmed; **proposed for testing, not accepted**.

## 2. Abaddon threshold and timing guardrails

1. The life-loss threshold is reset by the turn boundary; prior-turn life loss does not count.
2. Only spells cast from the controller's hand receive cascade from Abaddon. Spells cast from exile through a cascade resolution or from the graveyard through escape do not get Abaddon-granted cascade.
3. Abaddon's static ability functions while Abaddon is on the battlefield. Casting Abaddon from the command zone does not give Abaddon cascade from its own ability.
4. Abaddon checks the threshold as each spell is cast. Life loss caused by that spell after it has been cast cannot retroactively give that spell cascade.
5. Cascade's hit must have mana value less than the spell with cascade; a card whose alternate cost is reduced does not thereby have reduced mana value (CR 702.85a).

## 3. Existing Underworld Breach + Lion's Eye Diamond + Brain Freeze line

The baseline list contains all three pieces: **Underworld Breach**, **Lion's Eye Diamond**, and **Brain Freeze**. The list also retains tutors and graveyard/card-velocity tools that can find or assemble pieces.

The established line is a graveyard/escape engine with these core conditions:
- Underworld Breach and Lion's Eye Diamond on the battlefield.
- Brain Freeze in the graveyard.
- Sufficient expendable cards in hand/graveyard to pay the escape costs (a commonly documented starting line uses at least six other cards between hand and graveyard; do not count combo pieces or reserved finishing resources as fuel).

Functional outline:
1. Sacrifice Lion's Eye Diamond, discarding the hand and adding three mana of one color.
2. Escape Lion's Eye Diamond from the graveyard by exiling three other graveyard cards.
3. Escape Brain Freeze by paying {1}{U} and exiling three cards.
4. Brain Freeze's storm trigger copies the spell for each other spell cast before it this turn. Allocate mill to fuel further escapes and mill opponents as required.
5. Repeat while sufficient library/graveyard resources remain.

The line is **rules-coherent as a known combo**, but it is not a free or resource-less loop: graveyard fuel, mana sequencing, card-zone setup, and the hand-discard cost on Lion's Eye Diamond matter. The Abaddon ability does not add cascade to the escape casts because they are cast from the graveyard, not from hand.

References:
- [EDHREC combo record: Underworld Breach + Lion's Eye Diamond + Brain Freeze](https://edhrec.com/combos/izzet/1368-3518-4856)
- [Current Comprehensive Rules: cascade and storm](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt)

## 4. What remains open

This review closes the first candidate's specific Abaddon/Aurora cascade-grant question and records a rules-coherent summary of the Breach line. It does **not** close the entire Abaddon deck rules audit. The following remain:
- Audit each relied-upon nontrivial interaction/package in the list.
- Complete a real, controlled comparison of baseline versus Aurora variant, or explicitly document that test data cannot be collected with available tools.
- Do not infer performance from card popularity, rules synergy, or a scripted model that does not faithfully implement Magic's rules.
- Present a final exact list only if a swap is justified, independently recount and reverify it, and wait for explicit user approval before considering it finalized.



## 5. Commander-specific package interaction review — expanded 2026-10-13

This section follows the current source-package Oracle text for the Abaddon list and the current Scryfall metadata refresh. It records the important trigger and zone interactions rather than treating every card as an isolated inclusion. This is still a focused interaction review, not proof that every conceivable game state has been tested.

### Cascade and same-turn life-loss engine

| Package/card | Verified interaction | Guardrail |
|---|---|---|
| **Bloodletter of Aclazotz + Solphim, Mayhem Dominus + damage spells** | On your turn, Bloodletter doubles life loss an opponent would take. Solphim separately doubles noncombat damage dealt to opponents. Where both apply to a damage event, a base 1 damage ping can become 2 damage from Solphim, then 4 life lost after Bloodletter. These are replacement effects acting on different parts of damage/life loss. | This only applies to opponent life loss during your turn. Solphim does not double pure life-loss effects such as Loyal Subordinate or The Ruinous Powers trigger. |
| **Boltwave / Flame Rift** | With both Solphim and Bloodletter on your turn, Boltwave's 3 damage becomes 6 damage to each opponent and then 12 life lost per opponent; Flame Rift's 4 damage becomes 8 damage to each opponent and then 16 life lost per opponent. The life lost is aggregated across opponents for Abaddon's threshold. | Flame Rift also deals its printed 4 damage to you; Solphim and Bloodletter's opponent-only effects do not double your own life loss. Do not count self-damage from lands or mana sources toward Abaddon's threshold. |
| **Loyal Subordinate + Bloodletter** | Loyal Subordinate's lieutenant trigger makes each opponent lose 3 life at the beginning of combat. Bloodletter doubles that to 6 per opponent on your turn (18 total at a normal three-opponent table), without needing combat damage. | This is life loss, not damage, so Solphim does not amplify it. It requires control of your commander at the beginning of combat, not that your commander attack. |
| **Neheb, the Eternal** | At the beginning of each postcombat main phase, Neheb adds red mana equal to the total life opponents have lost this turn. This can convert Abaddon's damage/life-loss setup into mana for a postcombat cascade turn. | It counts life lost this turn; it does not carry the prior turn's loss forward. Mana is generated at the postcombat main phase trigger only. |
| **Rakdos, Lord of Riots** | He cannot be cast unless an opponent has lost life this turn, and the cost reduction for creature spells is {1} for each life opponents have lost this turn. Abaddon's damage setup assists both conditions. | This is a separate life-loss check/reduction; it does not itself grant cascade to spells cast from zones other than hand. |

The doubling sequence can make a low-mana spell open a large Abaddon threshold. For instance, Boltwave is mana value one; if Solphim and Bloodletter are both present on your turn, the resulting 12 life loss per opponent is enough to satisfy Abaddon's mana-value threshold for much of the deck. The engine is conditional on those permanents and the damage resolving, so this is a high-ceiling line, not a baseline guarantee.

### Cast-from-exile value and damage

| Package/card | Verified interaction | Guardrail |
|---|---|---|
| **Passionate Archaeologist** | Abaddon is a commander creature you own, so the Background gives Abaddon an ability that triggers when you cast a spell from exile. It deals damage equal to that spell's mana value to a target opponent. Cascade hits, spells cast from The Ruinous Powers, and suspend casts from exile can all trigger it. | A card copy created by Nalfeshnee or Storm is not cast; it does not trigger Passionate Archaeologist. If Abaddon is not on the battlefield when the exile spell is cast, Abaddon cannot deal this damage. |
| **Keeper of Secrets** | Whenever you cast a spell from anywhere other than your hand, Keeper deals damage equal to that spell's mana value to a target opponent. This includes cascade hits cast from exile and escape casts from the graveyard. | Copies of a spell are not cast, so they do not trigger Keeper of Secrets. |
| **Nalfeshnee** | Casting a spell from exile triggers Nalfeshnee, which can copy that spell. A copied permanent spell becomes a token permanent with haste and an end-step sacrifice ability; a copied instant/sorcery spell is copied on the stack. | Nalfeshnee's copy is not cast. It does not create a second cascade trigger, does not trigger Passionate Archaeologist/Keeper/Prosper's cast-from-exile text, and does not count as a spell cast for Storm. It **does** count as a copied instant/sorcery for Storm-Kiln Artist's magecraft ability. |
| **Prosper, Tome-Bound** | Each card you play from exile creates a Treasure. This includes a card cast from cascade or The Ruinous Powers and a land played from exile when a land play is permitted. | A spell copy is not a card played from exile. It doesn't trigger Prosper. Track the normal land-play limit and the duration of each exile permission. |
| **The Lost and the Damned** | Each spell you cast from a zone other than your hand creates a 3/3 Spawn token; a land entering under your control from other than your hand also triggers it. This covers cascade/suspend casts from exile and escape casts from the graveyard, as well as lands played from exile. | It triggers on the actual cast/land-entry event, not on storm or Nalfeshnee copies. It is not limited to only one spell per turn. |
| **The Ruinous Powers** | At your upkeep, it randomly selects an opponent and exiles that player's top card for play until end of turn. If you cast a spell this way, that spell's owner loses life equal to its mana value. If the owner is an opponent, this life loss increases Abaddon's threshold for subsequent spells from hand during your turn; Bloodletter doubles that life loss on your turn. | The spell cast from The Ruinous Powers is from exile, not your hand, so Abaddon does not grant cascade to that spell. The loss-of-life trigger resolves after the spell has been cast and cannot retroactively grant that same spell cascade. A land played from exile is not a spell and does not cause this life-loss trigger. |
| **Wild-Magic Sorcerer** | The first spell you cast from exile each turn has cascade. For example, if an Abaddon cascade hit is your first spell cast from exile that turn, Wild-Magic Sorcerer grants that hit cascade as well. Spells cast from exile later in that same turn do not each receive this Wild-Magic Sorcerer grant; later chain links cascade only if they have their own cascade ability or another effect grants it. If that first spell already has printed cascade, its instances trigger separately. | The extra cascade is limited to the first spell cast from exile each turn; do not assign it to every cascade hit. |
| **Delayed Blast Fireball** | When cascade casts it from exile, the exile condition applies: it deals 5 damage to each opponent and their creatures, rather than 2. Solphim and Bloodletter can amplify its opponent life-loss component on your turn. | The exile clause depends on how it was cast. A normal cast from hand doesn't receive the 5-damage version just because Abaddon granted cascade to the spell that found it. |

### Spell-copy, storm, and damage-trigger interactions

- **Exalted Flamer of Tzeentch** deals 1 damage to each opponent whenever you cast an instant or sorcery, including spells cast from exile or escaped from the graveyard. It doesn't trigger just because an instant/sorcery is copied.
- **Kessig Flamebreather** and **Vivi Ornitier** trigger when you cast a noncreature spell. Each real cast in a cascade chain can trigger them; a copy is not cast. Vivi's counter and damage trigger happen from the same noncreature cast.
- **Storm-Kiln Artist** triggers when you cast or copy an instant or sorcery. Unlike the effects above that require a cast, it can make Treasures from the copies created by Brain Freeze's storm ability or Nalfeshnee's copy ability.
- **Birgi, God of Storytelling** triggers for spells actually cast, including from exile or the graveyard; it doesn't trigger from spell copies. This list does not contain Grinning Ignus, so do not claim the known Birgi + Grinning Ignus infinite loop is present.
- **Noise Marine** has printed cascade and an enters-the-battlefield ability dealing damage equal to the number of spells cast that turn. Spells cast while its own cascade triggers resolve before Noise Marine resolves can increase that later damage number.
- **Call Forth the Tempest** has two printed instances of cascade and mana value 11 ({8}{R}{R}{R}). When cast from hand during your turn after opponents have lost at least eleven total life that turn, Abaddon grants an additional cascade instance, for three separate cascade triggers. Its damage to opposing creatures is based on the total mana value of other spells cast that turn; actual cascade-hit spells count as casts, while storm/Nalfeshnee spell copies do not.
- **Ancestral Vision, Inevitable Betrayal, and Profane Tutor** have mana value zero and can be hit by cascade effects that allow casting them without paying their mana cost. When cast from exile this way they are normal spell casts, not suspend casts. They do not get cascade from Abaddon because they were cast from exile rather than the controller's hand.

### Breach / Brain Freeze finish and practical conditions

The baseline's Underworld Breach + Lion's Eye Diamond + Brain Freeze package is listed by EDHREC/Commander Spellbook as a high-ceiling three-card combo with these starting prerequisites: Brain Freeze in the graveyard; Breach and LED on the battlefield; at least six other cards across hand and graveyard. The exact sequence depends on the starting zones, fuel, available mana, spell/escape timing, and how many cards are available to keep the engine moving.

1. Sacrifice LED to discard your hand and add three mana of one color.
2. Escape LED by exiling three other graveyard cards.
3. Escape Brain Freeze for {1}{U}, exiling three cards.
4. Use Brain Freeze's storm copies to mill yourself for continuing escape fuel and opponents for a potential finish; repeated casts raise storm count.
5. If using **Wheel of Fortune** or **Windfall** to make opponents with empty libraries attempt to draw and lose, retain enough of your own library to survive those draw instructions. Milling an opponent's library alone does not make them lose immediately.

With Storm-Kiln Artist in play, Brain Freeze casts **and their storm copies** can create Treasures; Exalted Flamer triggers for each actual instant/sorcery cast, while Nalfeshnee and the cast-from-exile payoffs trigger only for spells actually cast from exile. Those trigger distinctions matter when sequencing and estimating mana or damage.

This is a resource-dependent finite-game combo sequence, not a resource-free mathematical infinite. Opponents can interact between steps, and graveyard hate, counters, and insufficient fuel can stop it. Official combo discovery/reference: [EDHREC's Underworld Breach + LED + Brain Freeze record](https://edhrec.com/combos/izzet/1368-3518-4856); Abaddon-specific known combo listing: [EDHREC Abaddon combo list](https://edhrec.com/combos/abaddon-the-despoiler).

## 6. Updated result and open gates

**Closed by this review:** the Abaddon mana-value fact (5, not 6); the proposed Aurora/Phoenix granted-cascade interaction; the primary same-turn opponent-life-loss threshold interactions; major cast-from-exile trigger boundaries; and the core Breach/LED/Brain Freeze package prerequisites and copy/cast guardrails.

**Still open:** verify remaining individual interactions not covered above; review card-by-card current Oracle text for any later changes after the recorded Scryfall snapshot; a validated test engine and actual baseline-vs-variant gameplay results; the test decision; any final-list recount and hash; and explicit user approval before any proposed final change. This review does not justify marking the deck final.


### Rules references for the expanded review

- [Official Magic Comprehensive Rules, effective September 25, 2026](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt): rules 702.85a and 702.85c (cascade and multiple instances); 702.40a (storm); 603.2 (trigger conditions); 113.10 (granted abilities); 707.10 (spell copies are not cast); 120.3a (damage to a player causes life loss); and 121.4 (a player attempting to draw from an empty library loses the game the next time priority would be received).
- [Current Scryfall Abaddon printing](https://scryfall.com/card/40k/171/abaddon-the-despoiler); [Aurora Phoenix](https://scryfall.com/card/cmr/161/aurora-phoenix); [Bloodletter of Aclazotz](https://scryfall.com/card/lci/92/bloodletter-of-aclazotz); [Solphim, Mayhem Dominus](https://scryfall.com/card/one/150/solphim-mayhem-dominus); [The Ruinous Powers](https://scryfall.com/card/40k/139/the-ruinous-powers); [The Lost and the Damned](https://scryfall.com/card/40k/129/the-lost-and-the-damned); [Keeper of Secrets](https://scryfall.com/card/40k/78/keeper-of-secrets); [Nalfeshnee](https://scryfall.com/card/clb/678/nalfeshnee); [Passionate Archaeologist](https://scryfall.com/card/clb/656/passionate-archaeologist); [Prosper, Tome-Bound](https://scryfall.com/card/afc/2/prosper-tome-bound); [Wild-Magic Sorcerer](https://scryfall.com/card/clb/816/wild-magic-sorcerer); [Exalted Flamer of Tzeentch](https://scryfall.com/card/40k/119/exalted-flamer-of-tzeentch); [Delayed Blast Fireball](https://scryfall.com/card/clb/676/delayed-blast-fireball); [Call Forth the Tempest](https://scryfall.com/card/hoc/22/call-forth-the-tempest); [Noise Marine](https://scryfall.com/card/40k/82/noise-marine).
- [EDHREC/Commander Spellbook-style combo record for Underworld Breach + Lion's Eye Diamond + Brain Freeze](https://edhrec.com/combos/izzet/1368-3518-4856) lists the starting state and six-card hand/graveyard fuel prerequisite. This is combo-discovery evidence; the steps still require applying current Oracle text and the Comprehensive Rules.

## 7. Bounded closeout checklist — current evidence

This table makes the remaining work explicit and prevents already-settled questions from being repeatedly reopened.

| Check | Status | Evidence / consequence |
|---|---|---|
| Abaddon mana cost and mana value | CLOSED | `{2}{U}{B}{R}`, mana value 5; confirmed in current Oracle data. |
| Same-turn opponent life-loss threshold | CLOSED | The threshold counts aggregate opponents' life loss during the current turn; prior-turn loss and self-life-loss do not count. |
| Granted/printed cascade stacking | CLOSED for documented interactions | Multiple cascade instances trigger separately. Aurora Phoenix and Call Forth the Tempest cases are recorded above. |
| Aurora Phoenix graveyard return from a cascade spell | RULES-CLOSED; PERFORMANCE INCONCLUSIVE | Rules interaction is supported; Forge pilot never cast either candidate and is not valid swap evidence. Keep baseline Mind's Desire. |
| Damage replacement / life-loss amplification | REVIEWED | Solphim amplifies noncombat damage to opponents; Bloodletter doubles opponents' life loss on your turn. Do not conflate damage with direct life loss. |
| Cast from exile vs cast from hand vs cast from graveyard | REVIEWED | Abaddon's grant is hand-only; exile/graveyard casts can still trigger the specific payoffs that refer to those zones. |
| Spell copies vs casts / Storm | REVIEWED | Ordinary cast-trigger payoffs do not trigger from copies; Storm-Kiln Artist's cast-or-copy wording is the exception called out above. |
| Breach + LED + Brain Freeze route | RULES-COHERENT; FINAL SEQUENCE AUDIT OPEN | Prerequisites and resource dependence recorded, but do not call it a resource-free infinite or imply it has been fully runtime-validated. |
| All remaining 100-card membership and every other interaction | OPEN | Must finish the independent exact-list audit; this document is not yet the final card-by-card certificate. |
| Exact final list hash / approval | OPEN | Frozen baseline unchanged; finalization gate NO pending final audit and explicit user approval. |

### Scope boundary and stop rule for this review

The completed items above are closed unless current Oracle/rules sources materially change or a concrete contradictory interaction is found. Do not reopen Aurora-versus-Mind's Desire for the same uninformative Forge AI comparison. The remaining work is a bounded card-specific audit of the frozen list, not another general search for possible upgrades. Candidate ledger decisions remain proposals/rejections/inconclusive records, not authorized card changes.

## 8. Step 2 — role-based triage of the 61 previously unmentioned names (2026-10-13 UTC)

**Scope:** Frozen baseline only. No cards added, removed or reclassified. This closes the first-pass triage for the 61 names not explicitly mentioned in the prior narrative; it does not by itself certify all 94 card names or all game-state interactions.

### Lands (28 copies / basic duplicates noted)

All 28 land copies are mana infrastructure. Fetchlands, shocklands, rainbow lands and duals need a mana-base/color-source audit but no special cascade/cast-copy interactions. Otawara and Takenuma have channel abilities that function from hand by paying their channel costs; they are not spells, do not trigger cast payoffs, and do not receive Abaddon cascade. Urborg changes Swamp land types for all lands on the battlefield, potentially broadening black production, but does not change color identity. Ancient Tomb costs 2 life to activate; self-life-loss does not increase Abaddon's opponent-life-loss threshold.

### Ordinary tutors

Demonic Tutor, Imperial Seal, Mystical Tutor and Vampiric Tutor are normal search effects with no special Abaddon interaction. Gamble's random discard occurs after searching; if a chosen card is discarded, it can seed Underworld Breach or other graveyard uses, but this is contingent and not a guarantee. Tutors must be sequenced before the intended cascade turn if their mana cost exceeds the current Abaddon threshold; because they are cast from hand, the tutor itself may receive cascade if Abaddon is out and the threshold is met.

### Free/conditional interaction

Deadly Rollick and Fierce Guardianship can be cast for zero mana with their commander-on-battlefield alternate conditions; Abaddon still sees their printed mana values for its threshold and cascade's mana value comparison, not their alternate costs. Deflecting Swat's free mode likewise does not lower mana value. Force of Will and Force of Negation alternate costs involve exiling a blue card and paying life for Force of Will; that life is paid by you and does not increase Abaddon's threshold. Force of Negation's free mode is restricted to an opponent's turn, so it does not serve as a free cascade spell during your own turn. Pact of Negation's delayed upkeep payment is a separate risk: after casting it, you must pay {3}{U}{U} at the next upkeep or lose. Flusterstorm copies itself for each spell cast before it that turn; these copies are not cast and do not trigger ordinary cast triggers, but Storm-Kiln Artist sees copies of an instant/sorcery and can trigger magecraft for them. Pyroblast can target a blue spell/permanent and can be cast targeting any spell even if that spell is not blue, but its resolution only affects the target if it's blue; Swan Song counters enchantment, instant, or sorcery spells, with the created Bird token on resolution. None of these interaction spells changes the frozen card list; exact targeting legality and stack states are game-dependent.

### Rituals / acceleration

Arcane Signet and the Talismans are routine mana rocks. Sol Ring and Mana Vault make colorless mana and cannot pay colored pips without another effect. Chrome Mox requires exiling a nonartifact, nonland card from hand as it enters and has imprint; Lotus Petal sacrifices itself for one mana. Dark Ritual and Rite of Flame are one-shot black/red rituals; Rite of Flame scales with prior Rite of Flame cards in graveyards. Cabal Ritual adds {B}{B}{B}, or {B}{B}{B}{B}{B} with threshold (seven or more cards in your graveyard), so it is a conditional rather than guaranteed burst. Jeska's Will has modes chosen on cast: a mana mode based on opponents' hand size, or exile the top three cards and allow them to be played until end of turn, or both if you control a commander; if cast with Abaddon present from hand at threshold, the spell can gain cascade. Nightscape Familiar reduces blue/red spell costs by {1} and can regenerate itself for {B}; cost reduction does not change mana value for Abaddon's threshold or cascade. The reduction applies to generic portions of blue/red spells, and does not reduce colored pips.

### Draw / cantrips

Brainstorm draws three then puts two cards from hand on top of library, so it can protect/reposition cards but may put valuable cascade hits back into the library. Ponder looks at the top three and can shuffle; its value with cascade depends on timing and top-deck setup. Mystic Remora and Rhystic Study are upkeep/conditional draw engines, not cast-trigger engines; their upkeep costs tax resources but do not interact specially with cascade. Their card advantage improves ability to build a cascade turn but does not lower mana value.

### Thermo-Alchemist

Thermo-Alchemist triggers on casting an instant or sorcery by untapping; it taps to deal 1 damage to each opponent. If activated during your turn before casting a qualifying spell, the opponent life loss from its damage can raise Abaddon's threshold after damage resolves. It does not have haste inherently; timing of its first activation matters. Damage is life loss only after damage is dealt and state-based actions/trigger ordering are processed; do not count projected damage before it occurs.


### Result and what remains

- Land role: 28 card copies, reviewed as mana-base infrastructure; nonbasic color-production and utility-land activations are documented above.
- Ritual/mana acceleration role: 13 names, reviewed for alternate-cost/setup requirements and relevant mana-value guardrails.
- Draw/cantrips role: 4 names reviewed.
- Tutor role: 5 names reviewed.
- Free/conditional interaction and counters: 10 names reviewed.
- Thermo-Alchemist: reviewed as a threshold enabler.
- The “not explicitly mentioned” category has therefore been triaged by role. The most material special conditions found are: Ancient Tomb self-payment is not opponent life loss; fetchlands/shocks have life costs that do not raise Abaddon's threshold; alternative/free casting costs do not reduce printed mana value; Force of Negation's free mode is opponent-turn restricted; Pact of Negation has delayed failure condition; Cabal Ritual depends on graveyard threshold; Chrome Mox depends on an imprint card; Nightscape Familiar reduces generic cost but not mana value; and Gamble can contingently seed graveyard cards.
- This triage is a rules-oriented summary and has not tested every possible stack/game state. It does not substitute for the official fresh legality refresh and final list-level audit.
- **Remaining card-level coverage gap:** The 33 names already explicitly mentioned in the prior review still need their coverage statuses reviewed in context; the full 94-card audit certificate is not complete. Next bounded step should verify high-impact listed interactions and the Breach sequence with current Oracle/rules sources, rather than repeating basic-card explanations.

## 9. Step 2 closeout boundaries and priority interactions for the remaining review

The role-based triage above is a first-pass coverage screen. The following items remain important enough to require explicit current Oracle/rules confirmation before Abaddon can pass its interaction gate:

| Priority | Card/package | Verification required | Status |
|---|---|---|---|
| P1 | Underworld Breach + Lion's Eye Diamond + Brain Freeze | Work through a concrete legal starting state and every escape cost, LED discard/mana sequence, Brain Freeze storm count, fuel count, and termination condition. Distinguish an engine that can repeat with sufficient fuel from a deterministic infinite combo. Check how opposing interaction can break the line. | OPEN |
| P1 | Force of Will / Force of Negation / Fierce Guardianship / Deadly Rollick / Pact of Negation | Verify alternate-cost restrictions and their mana values independently of cost paid; distinguish free modes legal only on an opponent's turn; record Pact's delayed upkeep consequence. | COVERED IN ROLE TRIAGE; current-source spot-check remains |
| P1 | Cascade hit legality / zero-mana-value cards | Confirm the cascade comparison uses mana value rather than alternate cost and how suspend cards cast without paying mana cost behave when hit by cascade. | REVIEWED ABOVE; current-source spot-check remains |
| P2 | Fetchlands, shocklands, Ancient Tomb, rainbow lands, channel lands, Urborg | Verify life-payment does not count toward Abaddon's opponent-life-loss threshold; verify channel activations are abilities, not casts; verify Urborg affects land types, not color identity. | COVERED IN ROLE TRIAGE; only material contradications reopen |
| P2 | Chrome Mox / Cabal Ritual / Nightscape Familiar / Jeska's Will | Verify imprint requirement, threshold condition, cost reduction scope, mode selection, and exile-cast triggers in their relevant setup states. | COVERED IN ROLE TRIAGE |
| P2 | Gamble / tutors / cantrips | Verify timing and contingent discard/top-of-library effects when used to assemble a cascade turn or Breach package. | COVERED IN ROLE TRIAGE |
| P2 | Interaction suite | Confirm alternate-cost conditions and target restrictions. These are ordinary role checks unless they create a specific Abaddon/cascade dependency. | COVERED IN ROLE TRIAGE |

### Audit stopping rule

Do not require an individual rules essay for every land or routine spell. An entry can close as **NO SPECIAL INTERACTION** when current Oracle text has been checked and no commander-specific or nontrivial dependency exists. Keep that result distinct from **NOT CHECKED**. A package can close as **RULES-COHERENT** only after the sequence is written out with explicit zone/mana/fuel requirements and failure points.

The final gate remains NO until all 94 names have an explicit per-card disposition (covered, no special interaction, or open), the material open interactions are resolved, fresh official legality is verified, the final list/hash is independently checked, and the user explicitly approves the exact list.

## 10. Step 3 — Breach package sequence audit (2026-10-13 UTC)

A bounded standalone review is committed at [Abaddon Breach Sequence Audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md). It records the required starting zones, LED's discard/mana costs, the three-card escape cost for each spell, storm-copy distinctions, resource/fuel accounting, finish constraints, and common interruption points.

**Disposition: PARTIALLY VERIFIED.** The project source names this combo but does not contain a fully itemized fuel-and-mana ledger proving a specific repeatable starting state. No unconditional infinite or deterministic kill is claimed. Close only after a concrete starting inventory and every iteration's mana/fuel accounting are independently checked. No decklist changes; final gate remains NO.

### Current-source confirmation — 2026-10-13 UTC

The official Comprehensive Rules page identifies the current rules edition as effective September 25, 2026. A bounded review has been recorded at [Abaddon Breach Package Audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md). The rules-level conclusions are supported: escape consumes three other graveyard cards per escape cast; LED sacrifices itself and discards the hand as activation costs; storm copies are not cast and don't raise storm count; Abaddon's grant applies to hand-cast spells; an empty library alone is not a loss.

The combo remains **PARTIALLY VERIFIED**, not because the core rules are unknown, but because the repository lacks a fully itemized worked state/fuel ledger proving the exact loop/finish from a defined starting inventory. Do not downgrade or upgrade that claim without such a ledger.

## 11. Step 6 — worked Breach line closes the specific-sequence proof gap (2026-10-13 UTC)

The latest [Abaddon Breach Package Audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md) now includes a worked uninterrupted line with an exact starting zone inventory, ten escape cycles, LED mana, storm counts, six-card fuel replacement, opponent-mill allocation, and a Wheel of Fortune finish. This supersedes earlier statements in Sections 3, 7 and 10 that no worked starting state had been recorded.

**Updated disposition:** RULES-COHERENT WITH SPECIFIC CONDITIONS — worked uninterrupted example provided. This proves one line from its stated starting state assuming no opponent interaction. It does not establish an unconditional infinite, a guaranteed win from arbitrary resources, or that the list reliably assembles the combo. No gameplay-performance inference is made.

The 94-card review gate remains open overall: this closes the specific worked-sequence gap, not the full live Oracle refresh, exhaustive per-card disposition, or explicit user approval.


## Step 7 — material sequencing spot-check: cascade setup, free interaction, exile casts, Thermo-Alchemist (2026-10-13 UTC)

**Scope:** a bounded current-text/rules review of the four material interaction groups identified by the role triage. No decklist changes were made. This is not the final 94-name current-Oracle refresh or final approval certificate.

### Top-deck setup and cascade ordering

- Abaddon's grant checks the spell's **mana value** and requires that the spell be cast from its controller's hand during their turn. The amount paid, including an alternate or reduced cost, does not change mana value.
- Brainstorm, Ponder, Mystical Tutor, Imperial Seal and Vampiric Tutor each have mana value 1. If cast from hand during your turn while Abaddon is on the battlefield and opponents have lost at least 1 life this turn, each receives Abaddon-granted cascade. This list has six other mana-value-0 nonlands that can be potential hits (Ancestral Vision, Chrome Mox, Inevitable Betrayal, Lion's Eye Diamond, Lotus Petal and Profane Tutor), if revealed. These hits are possible, not guaranteed. Cascade resolves before its source spell, so the cantrip/tutor cannot set up the top card for its own already-triggered cascade; its draw or top-deck effect resolves after cascade.
- A tutor that puts a card on top can therefore set up a later, higher-mana-value cascade spell. Cascade only casts the revealed card if its mana value is less than the spell whose cascade ability is resolving; it does not compare the hit against Abaddon's life-loss threshold.
- A fetchland activation can shuffle away a deliberately arranged top card if activated before the relevant cascade trigger resolves. Sequence fetches before arranging the top, or avoid a later shuffle when preserving the setup matters.
- These are sequencing opportunities, not guaranteed hits: the next cascade spell's mana value, the top card's mana value, intervening shuffles, and any other cascade triggers still matter.

### Free/alternate-cost interaction

| Card | Mana value | Abaddon-specific finding |
|---|---:|---|
| Deadly Rollick | 4 | If cast from hand during your turn with Abaddon present and the threshold is at least 4, it gets cascade even if its commander-dependent alternative cost is used. Its target must still be a creature. |
| Deflecting Swat | 3 | If cast from hand during your turn and the threshold is at least 3, its alternative cost does not prevent Abaddon from granting cascade. It still requires a spell or ability with a target that can legally be changed to a legal new target. |
| Fierce Guardianship | 3 | If cast from hand during your turn and the threshold is at least 3, its free cast does not prevent cascade. It counters only a target noncreature spell. |
| Force of Will | 5 | If cast from hand during your turn and the threshold is at least 5, its alternate cost does not prevent cascade. The alternative cost still requires exiling a blue card from hand and paying 1 life; paying life yourself does not add to Abaddon's threshold. |
| Force of Negation | 3 | Its free alternative is restricted to an opponent's turn, so that free mode does not produce Abaddon-granted cascade (which applies only during your turn). If legally cast from hand during your own turn by paying its normal cost, it can receive cascade at threshold 3; it counters only a noncreature spell. |
| Pact of Negation | 0 | A hand-cast Pact during your turn qualifies for Abaddon's grant at any nonnegative threshold, but cascade cannot find a card with mana value less than 0. It therefore gains no useful cascade hit. Its next-upkeep payment requirement remains a separate consequence. |

The general rule is that **alternate cost changes what is paid, not mana value or the hand-cast zone condition**. Abaddon is not a general permission to cast these spells at times when their own rules do not allow them.

### Jeska's Will and exile casts

Jeska's Will has mana value 3 and lets its controller choose both modes if they control a commander as they cast it. Its exile mode gives permission to play the three exiled cards until end of turn. Those cards are cast/played from exile, not from hand: actual spells cast this way can trigger Keeper of Secrets, Passionate Archaeologist (if Abaddon is on the battlefield), Prosper, Tome-Bound and The Lost and the Damned as applicable, but do **not** receive cascade from Abaddon's hand-only grant. A land played from exile is a land play, not a spell cast, and does not receive cascade or trigger spell-cast payoffs. The mana-producing mode itself does not cause opponent life loss; mana gained is not Abaddon's threshold.

### Thermo-Alchemist and threshold sequencing

Thermo-Alchemist's tap ability deals 1 damage to each opponent; casting an instant or sorcery untaps it. Each resolved damage event that causes opponents to lose life during your turn adds that life loss to Abaddon's aggregate threshold. To repeat the ping, the controller must have priority and be able to activate the tap ability while Thermo-Alchemist is untapped; the untap trigger from an instant/sorcery cast uses the stack and does not retroactively change the cascade eligibility of the spell that was already cast. Thus, use a Thermo-Alchemist ping **before** casting a spell whose cascade eligibility depends on that additional life loss, rather than expecting damage after the cast to grant cascade to the same spell. Damage prevention or replacement effects can alter the actual life lost, so count life loss that actually occurs.

### Evidence and limits

The conclusions above follow Abaddon's Oracle condition and the current Magic Comprehensive Rules cascade, mana-value, casting, and triggered-ability framework (rules reference: [official Magic rules page](https://magic.wizards.com/en/rules); [Comprehensive Rules effective September 25, 2026](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt)). Card-text spot checks include [Abaddon the Despoiler](https://scryfall.com/card/40k/171/abaddon-the-despoiler), [Jeska's Will](https://scryfall.com/card/cmr/187/jeskas-will), [Thermo-Alchemist](https://scryfall.com/search?q=%21%22Thermo-Alchemist%22), and [Fierce Guardianship](https://scryfall.com/search?q=%21%22Fierce+Guardianship%22). This closes only these contextual questions; other material card entries and the fresh exact-list Oracle/identity check remain open. Final gate remains NO.


## Step 8 — Harnfel and Bituminous Blast contextual checks (2026-10-13 UTC)

**Scope:** close the two named gaps from the per-card triage. No list changes.

### Birgi // Harnfel reverse face

Harnfel, Horn of Bounty has the activated ability “Discard a card: Exile the top two cards of your library. You may play those cards this turn.” The discarded card is a cost and is not one of the two cards exiled by the ability. The permission lasts for the turn even if Harnfel leaves the battlefield. Cards played this way follow their normal costs and timing restrictions. Each actual spell cast from exile can trigger the list's applicable cast-from-exile payoffs (including Keeper of Secrets, Passionate Archaeologist if Abaddon is on the battlefield, Prosper, Tome-Bound, and The Lost and the Damned); the spell does not receive Abaddon's cascade grant because it was not cast from hand. A land played this way is a land play, not a spell cast. This is card advantage/velocity with a discard cost, not a free cast engine by itself.

### Bituminous Blast

Bituminous Blast is a {3}{B}{R} instant with mana value 5, printed cascade, and “Bituminous Blast deals 4 damage to target creature.” It has two relevant roles: instant-speed creature removal and a cascade value spell. If cast from hand during its controller's turn while Abaddon is on the battlefield and opponents have lost at least five total life that turn, Abaddon grants a second cascade instance. The printed and granted cascade abilities trigger separately and resolve separately; each uses the spell's mana value 5 as the comparison point, and each may cast a qualifying card with mana value less than 5. The revealed/cast cascade spell resolves above Bituminous Blast, so the removal damage from Bituminous Blast itself has not yet resolved while its cascade chain is happening. Its target must be a creature when cast and must remain legal for the damage spell to resolve. If Bituminous Blast is cast from exile or another non-hand zone, its printed cascade still functions, but Abaddon does not grant another instance.

**Disposition:** both previously flagged context questions are now checked against current card text and the current Comprehensive Rules cascade definition. This closes these two triage items only; it does not certify all remaining explicit-review entries or the full exact-list Oracle/identity gate.

References: [Birgi // Harnfel official Wizards release notes](https://media.wizards.com/2021/downloads/KHM_Release_Notes/EN_MTGKHM_ReleaseNotes_20210113.pdf); [Bituminous Blast card text/rulings](https://www.mtg.wtf/card/c16/182/Bituminous-Blast); [Comprehensive Rules effective September 25, 2026](https://blogs.magicjudges.org/rules/comprehensive-rules/).


## Step 8 result — contextual gaps closed (2026-10-13 UTC)

The detailed Harnfel reverse-face and Bituminous Blast check is recorded in [Abaddon Step 4 Context Check](../tests/Abaddon_Step_4_Context_Check_2026-10-13.md). In brief: Harnfel's exile-play permissions allow normal-cost plays that can trigger applicable cast-from-exile payoffs but do not qualify those spells for Abaddon's hand-only cascade grant. Bituminous Blast has mana value 5 and printed cascade; under Abaddon's hand-cast/turn/threshold conditions it can gain an additional cascade instance, resolving above the Blast before its creature damage resolves.

These two items are closed only. Remaining exact-list Oracle/identity, full per-card interaction, final integrity, legality-at-approval, and user-approval gates remain open. No decklist changes; final gate NO.


## Step 9 — Blasphemous Act context check (2026-10-13 UTC)

See [Abaddon Step 5 Blasphemous Act Interaction Check](../tests/Abaddon_Step_5_Blasphemous_Act_Interaction_Check_2026-10-13.md). Oracle text and the deck-specific interaction are now documented: mana value 9 despite cost reduction; damage to creatures only; the wipe can destroy Abaddon's own creature engines; and, when the hand-cast/turn/threshold conditions are met, Abaddon grants cascade before the sorcery resolves. A creature cast from that cascade is exposed to the pending wipe. The card remains in the frozen baseline; no cut is justified by rules review alone. Full list gate remains NO.



## Step 10 — remainder of the 94-name coverage triage (2026-10-13 UTC)

The companion triage CSV now has zero names left in the literal “NOT EXPLICITLY MENTIONED — triage required” status. The 19 outstanding rows from the previous pass were classified below as contextual checks or role-triaged. This closes the **triage queue**, not the exhaustive card-by-card Oracle audit or the final approval gates.

| Card | Disposition / deck-specific constraint |
|---|---|
| Brainstorm | Can reorder the library before later cascade reveals, but does not guarantee a useful hit. Cascade still reveals until a nonland card with mana value less than the cascade spell is found. |
| Deadly Rollick | Its alternate cost requires a commander on the battlefield and does not change mana value 4. Abaddon’s grant still requires a hand-cast spell during your turn and a life-loss threshold of at least four. |
| Deflecting Swat | Its alternate cost requires a commander you control. Alternate cost does not change mana value 3; retargeting itself does not increase Abaddon’s threshold. |
| Demonic Tutor | Ordinary library-to-hand tutor; no special Abaddon rules interaction beyond setup. It does not itself supply life loss or guarantee a cascade hit. |
| Fierce Guardianship | Its free mode requires a commander on the battlefield. Mana value remains 3. If cast from hand during your turn at threshold 3, its Abaddon-granted cascade can hit any revealed nonland with mana value 0–2 in this deck, including a mana-value-0 nonland; the cascade trigger is not guaranteed to find a desirable hit. |
| Flusterstorm | Storm copies are copies, not casts, so they do not trigger cast-only payoffs. At mana value 1, a qualifying hand-cast can receive Abaddon-granted cascade and can hit a mana-value-0 nonland if revealed. |
| Force of Negation | Its alternate-cost mode is limited to an opponent’s turn, so that mode does not meet Abaddon’s during-your-turn requirement. Alternate cost does not change mana value. |
| Force of Will | Exiling a blue card and paying 1 life is an alternate cost; mana value stays 5. A qualifying hand-cast on your turn can technically receive cascade at threshold 5 despite not paying its printed cost. |
| Gamble | Searches then randomly discards; this can assemble or incidentally seed the graveyard but may discard the tutored card. At mana value 1, a qualifying hand-cast can hit a mana-value-0 nonland with Abaddon-granted cascade if revealed. |
| Imperial Seal | Puts a chosen card on top, not in hand. Later draw/cascade order and intervening library changes govern access; its own cascade resolves before Imperial Seal's top-deck effect. At mana value 1, a qualifying hand-cast can hit a mana-value-0 nonland if revealed. |
| Mystic Remora | Its upkeep and draw triggers are not casts and do not increase Abaddon's threshold. If cast from hand during your turn with sufficient threshold, its mana-value-1 cascade can hit a mana-value-0 nonland if revealed. |
| Mystical Tutor | Sets an instant or sorcery on top for later access; it does not guarantee a later cascade hit if intervening library manipulation occurs. Its own mana-value-1 cascade resolves before the tutor sets up the top card and may hit a mana-value-0 nonland if revealed. |
| Pact of Negation | Mana value 0 means no legal nonland card has a lower mana value for cascade to find. If Pact resolves, the next-upkeep payment remains a separate consequence. |
| Ponder | Looking, shuffling and drawing can arrange the library but cannot guarantee a later cascade hit. Its own mana-value-1 cascade resolves before Ponder's library/draw effect and may hit a mana-value-0 nonland if revealed. |
| Pyroblast | Can target a blue spell or blue permanent; if that target is not blue on resolution, it is illegal. At mana value 1, a qualifying hand-cast can also receive cascade and hit a mana-value-0 nonland if revealed. |
| Rhystic Study | Triggers on opponents casting spells; its tax/draw effect does not itself cause life loss or increase Abaddon's threshold. At mana value 3, a qualifying hand-cast can hit any revealed nonland of mana value 0–2, but the cascade hit is not guaranteed. |
| Swan Song | Counters only an enchantment, instant or sorcery and creates a Bird token on resolution. At mana value 1, a qualifying hand-cast can hit a mana-value-0 nonland with Abaddon-granted cascade if revealed. |
| Thermo-Alchemist | Its damage must resolve before the relevant spell is cast to contribute to that spell’s cascade threshold. Its cast-triggered untap does not retroactively change the spell already on the stack. |
| Vampiric Tutor | Instant-speed top-deck setup is powerful but later library changes can alter the result. Its own mana-value-1 cascade resolves before the tutor sets up the top card and may hit a mana-value-0 nonland if revealed. |

The precise statements above describe these cards’ ordinary Oracle functions and their relevance to Abaddon. They do not replace the source/date-bound metadata overlay, nor do they claim exhaustive testing of every possible opponent effect or game state.

**Triage disposition:** 94/94 distinct names inventoried; prior contextual items recorded; remaining triage queue empty. Cards retained unchanged. The next gate is final closeout verification, including freshly checking exact current Oracle/color identity/official Commander legality, independently recounting the frozen list and hash, and then presenting the exact list for approval. The list is not finalized until the user explicitly approves it.


## Step 11 — cascade hit audit correction and public card-reference refresh (2026-10-13)

**No decklist changes.** This section corrects a substantive false statement in the earlier role/context triage. Some mana-value-1 spells were described as having no lower-mana-value nonland hit, and a mana-value-3 spell was described as having no lower-MV hit. That was too categorical for this exact list: it contains mana-value-0 nonland cards, including Ancestral Vision, Chrome Mox, Inevitable Betrayal, Lion's Eye Diamond, Lotus Petal and Profane Tutor. Pact of Negation is the seventh MV-0 nonland but cannot be a lower-MV cascade hit itself. Therefore, a mana-value-1 spell with Abaddon-granted cascade can hit a qualifying mana-value-0 nonland if one is revealed. A mana-value-3 spell can hit mana-value-0, 1 or 2 nonlands if revealed. Cascade remains probabilistic and is constrained by the actual reveal sequence and the specific cascade spell's mana value. Pact of Negation remains different: its mana value is 0, so no card can have lower mana value than it; its cascade instance cannot find a legal card to cast.

The card-level triage CSV has been corrected accordingly for the affected claims involving Fierce Guardianship, Flusterstorm, Gamble, Imperial Seal, Mystic Remora, Mystical Tutor, Ponder, Pyroblast, Rhystic Study, Swan Song and Vampiric Tutor. This correction supersedes the conflicting lower-MV statements in Step 7 and Step 10. It does not claim that every hit is useful or guaranteed.

### Public card-reference refresh (2026-10-13, UTC)
- **Bituminous Blast** — `{3}{B}{R}`, instant, mana value 5; printed cascade; deals 4 damage to target creature. Public card reference reports Commander legal. A hand-cast during your turn with at least 5 aggregate opponent life lost that turn also receives Abaddon's cascade. These are separate cascade triggers; they resolve before the Blast spell resolves, and each compares hits against mana value 5. Source: https://www.mtg.wtf/card/c16/182/Bituminous-Blast
- **Boltwave** — `{R}`, sorcery, mana value 1; deals 3 damage to each opponent. Public card reference reports Commander legal. Red identity is a subset of Abaddon's UBR identity. Source: https://www.mtg.wtf/card/fdn/79/Boltwave
- **Thermo-Alchemist** — `{1}{R}`, 0/3 Human Shaman with defender; tap to deal 1 damage to each opponent; untaps whenever you cast an instant or sorcery. Public card reference reports Commander legal. Red identity is a subset of UBR. The tap ability must resolve before the relevant spell is cast to contribute its actual life loss to that spell's Abaddon cascade threshold. Source: https://www.mtg.wtf/card/j22/83/Thermo-Alchemist
- The official Commander banned list was rechecked via https://mtgcommander.net/index.php/banned-list/; none of these three cards is banned. This specific claim is grounded in the official named banned list and public card references, not a direct Scryfall API card-object fetch.

### Current Oracle / identity / legality gate — honest status
A direct current Scryfall named-card or bulk endpoint refresh could not be obtained in this session; Scryfall's API endpoint returned access/403 errors. Thus the above named-card facts have been independently cross-checked against up-to-date public card-reference pages, and the official Commander ban list was checked, but this cannot honestly be labeled a fresh Scryfall object refresh across all 94 unique cards. The prior 2026-10-12 bulk snapshot remains dated evidence for the complete 94-name dataset. The remaining full-list gate requires retrieving a fresh authoritative bulk/card-object source and comparing all 94 names' Oracle text, color identity, and commander legality. No card is known from the current evidence to fail the gate, but don't substitute that for verification.

### Interaction and combo closeout
The review's material rules checks remain rules findings, not multiplayer performance evidence: Abaddon's threshold is aggregate opponent life actually lost during your turn; alternate costs do not alter mana value; Abaddon's grant requires a spell cast from hand while Abaddon is on the battlefield; cast-from-exile payoffs only see actual spells cast from exile; copies do not count as casts; printed cascade and Abaddon-granted cascade are separate triggers; and the worked Breach/LED/Brain Freeze + Wheel sequence is coherent only from its explicitly stated starting state with no interaction. It is not an unconditional infinite or evidence of reliable assembly. This bounded interaction review is substantial, not exhaustive proof of every game state.

**Disposition — current closeout:** the Scryfall refresh summary generated at `2026-10-13T06:44:29.581734+00:00` reports a global metadata pass across 5,964/5,964 exact printing/name rows; the Abaddon exact-list audit passed for all 94 names, including Oracle IDs/text, UBR identity, and Commander legality. Structural checks pass and the frozen list is unchanged. The finalization gate remains NO solely because explicit approval of the exact list has not yet been recorded.

## Step 12 — current Scryfall closeout and automation verification (2026-10-13 UTC)

The current refresh workflow completed successfully after the exact watched request path was updated. Refresh summary generated at `2026-10-13T06:44:29.581734+00:00`; Scryfall default-cards bulk last updated at `2026-10-12T21:06:24.577+00:00`. The global metadata gate reports 62 decks, 5,964 rows, 5,964 exact set/collector/name matches, zero missing or ambiguous printings, zero name-variant reviews, zero missing Oracle text/IDs, zero color-identity mismatches, zero unresolved exceptions and zero unexpected official-illegal rows. The Abaddon-specific gate passed 94/94 exact names, Oracle IDs/text, UBR color identity, and Commander legality.

This is metadata/identity/legality evidence from one shared current bulk scan and exact printing map. It is not proof that every individual board state was tested. The card interaction review remains substantial but bounded; the Breach/LED/Brain Freeze + Wheel line assumes its written starting state and no opponent interaction. Aurora Phoenix vs Mind's Desire remains inconclusive as a performance test; retain Mind's Desire and do not claim a win-rate result.

The automation fixes merged to main include a weekly/manual refresh, exact watched request path, serialized bulk jobs, transient-only retry logic, stable Current_* output names with legacy aliases, fail-closed freshness/completeness validation, an Abaddon exact-name audit in the refresh job, diagnostic artifacts, and fast CI for unit tests/workflow contracts/frozen-baseline integrity. The first quality-gate run passed. This closes the current metadata blocker; it does not bypass the user's explicit final-list approval requirement.

