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
