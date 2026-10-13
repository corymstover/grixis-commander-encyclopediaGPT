# Abaddon the Despoiler — Interaction Review v1

**Review date:** 2026-10-13  
**Baseline snapshot:** 2026-10-12  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Decklist changes:** None.  
**Playtests:** None run; this report must not be treated as test evidence.

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

