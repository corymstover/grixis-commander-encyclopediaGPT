# Nekusar, the Mindrazer — Commander-First Blueprint

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #40 of 62  
Status: working refinement evidence; not user approval

## Commander identity

Nekusar is a five-mana U/B/R Zombie Wizard with two linked strategic functions:

1. At the beginning of each player's draw step, that player draws an additional card.
2. Whenever an opponent draws a card, Nekusar deals 1 damage to that player.

The deck's natural optimized identity is therefore **Wheels / Draw Punishment / Group Slug**, not generic Grixis combo-control. The best cards either force or compress many draws, punish those draws, multiply Nekusar's own triggers, or protect/accelerate the five-mana commander long enough for those effects to matter.

## Natural power ceiling

**Power Bracket 4 — Optimized.**

Nekusar can produce explosive table-wide damage through wheels and trigger multipliers, has premium Grixis interaction/tutors/fast mana, and can support compact secondary combos. The commander still requires a five-mana setup and generally wins through accumulated draw events rather than a commander-zone deterministic cEDH line. Do not force Thoracle/Breach consultation packages, Narset/Notion-Thief wheel locks, infect shortcuts, or unrelated turbo-combo shells merely to imitate Bracket 5.

## Core strategic pillars

### 1. Force many real draws
Retain efficient wheels and repeatable draw engines. Prefer one- to three-mana wheels over four-plus-mana symmetrical group-hug cards that give opponents resources before the punishment engine is established.

### 2. Convert every opponent draw into pressure
Nekusar, Fate Unraveler, Underworld Dreams, Sheoldred, Spiteful Visions, Phyrexian Tyranny, Kederekt Parasite, Razorkin Needlehead, Scrawling Crawler, Orcish Bowmasters, and Ghyrson create overlapping punishment so the deck is not commander-or-bust.

### 3. Multiply Nekusar specifically
Harmonic Prodigy and Wizard's Staff both exploit Nekusar's Wizard type. Krang multiplies draw-caused triggered abilities across a broader permanent suite. These effects are additive rather than multiplicative with one another.

Important distinction: Wizard's Staff/Harmonic Prodigy can add instances of Nekusar's draw-step ability because it is a triggered ability of Nekusar/Wizard. Krang does not add an instance of that draw-step trigger because a player drawing a card did not cause that ability to trigger; the beginning of the draw step did. Krang does add instances of Nekusar's damage ability and other abilities that trigger because a player drew.

### 4. Preserve the exact-1 damage engine
Ghyrson Starn turns each separate 1-damage event from Nekusar and several other pingers into another 2 damage. Damage replacement effects that change the original 1 into 2+ prevent Ghyrson from seeing an event of exactly 1 damage. That makes Solphim, Mayhem Dominus a real internal nonbo in this specific shell and the correct cut for Krang rather than Fate Unraveler.

### 5. Keep interaction efficient
Nekusar is expensive and visible. Free/one-mana stack interaction, flexible removal, and an efficient sweeper are more valuable than adding another slow damage enchantment. Toxic Deluge supplies a true three-mana creature reset while Cyclonic Rift remains the asymmetric emergency/reset tool.

### 6. Mana base must support triple pips
Niv-Mizzet, Parun asks for UUU/RRR while Nekusar and the rest of the deck are three colors. Premium fetches, original duals/shocks, City of Brass, Mana Confluence, and Xander's Lounge are justified. Six basics remain. Mikokoro is retained as a commander-native utility land because it converts a land slot into an instant-speed each-player draw trigger.

## Commander-necessity test

The refined list becomes materially better when Nekusar is present:
- Wizard's Staff cheaply equips a Wizard and doubles both of Nekusar's triggered abilities.
- Harmonic Prodigy adds instances of Nekusar's Wizard triggers.
- Krang adds instances of Nekusar's damage trigger and the deck's other draw-caused punishment triggers.
- Curiosity on Nekusar turns each damage event into optional card draw for the controller.
- Winds of Change and Molten Psyche convert one low-cost spell into many opponent draws for Nekusar to punish.
- Mikokoro creates a repeatable draw event from a land slot.

Removing Nekusar leaves a functioning wheel/group-slug deck, but substantially reduces the efficiency and density of its best trigger-multiplication lines. This satisfies the project's commander-first requirement.

## Deliberately rejected homogenization

- Narset, Parter of Veils / Notion Thief wheel locks: suppress opponent draws and conflict with the deck's core draw-punishment identity.
- Thassa's Oracle consultation package: powerful but commander-independent.
- Phyresis / Tainted Strike infect shortcuts: fast kill vector but not the strongest expression of Nekusar's natural strategy.
- Mindcrank package: Bloodchief Ascension combo is powerful but redirects the deck toward a commander-independent mill loop.
- Naktamun Lorespinner // Wheel of Fate: current Nekusar-specific research flags the front side as unreliable when the deck itself keeps hands stocked.

## Approval-ready target

- Exact candidate SHA-256: `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`
- 100 cards
- 97 distinct names
- 35 lands
- Six basics: Island x2 / Mountain x2 / Swamp x2
- Proposed baseline delta: 17 cuts / 17 additions
- Target bracket: **4 — Optimized**
- Recommended Archidekt tags: **Wheels / Draw Punishment / Group Slug**
