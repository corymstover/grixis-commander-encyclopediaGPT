# Nekusar, the Mindrazer — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #40 of 62  
Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

## Final 17-card delta from authoritative FINAL baseline

| Cut | Add | Decision basis |
|---|---|---|
| Psychosis Crawler | Wizard's Staff | Crawler is a five-mana payoff for the controller's own draws. Staff costs two, equips Nekusar for {1} because he is a Wizard, and adds an instance of both Nekusar triggered abilities. This is a direct commander-identity upgrade. |
| The Locust God | Toxic Deluge | The Locust God is a six-mana self-draw token engine. Deluge gives the deck a true three-mana creature sweeper so it can clear pressure and rebuild its five-mana commander/engines efficiently. |
| Megrim | Curiosity | Megrim is a three-mana discard-only damage effect overlapping the cheaper Liliana's Caress. Curiosity is one mana, turns every Nekusar damage event into optional card draw for the controller, and also forms an optional draw/damage loop with retained Niv-Mizzet, Parun. |
| Dictate of Kruphix | Winds of Change | Dictate is a three-mana recurring symmetrical draw resource. Winds of Change is a one-mana hand redraw that produces a large controlled burst of actual draws for Nekusar and the punishment suite. |
| Font of Mythos | Molten Psyche | Font is a four-mana delayed group-hug engine. Molten Psyche is a three-mana wheel; with metalcraft it adds damage equal to cards each opponent has drawn that turn. The candidate retains well over three artifacts. |
| Solphim, Mayhem Dominus | Krang, the All-Powerful | Solphim changes Nekusar's 1 damage to 2, preventing Ghyrson Starn from triggering on that event. Krang instead adds instances of draw-caused triggered abilities across Nekusar, Fate Unraveler, Sheoldred, Underworld Dreams, Spiteful Visions, Phyrexian Tyranny, Kederekt Parasite and other punishers without breaking Ghyrson. |
| Crumbling Necropolis | Mana Confluence | Always-tapped tri-land becomes untapped perfect fixing. |
| Dragonskull Summit | Arid Mesa | Conditional checkland becomes a fetch for Badlands, Blood Crypt, Steam Vents, Volcanic Island, Xander's Lounge or a Mountain as appropriate. |
| Drowned Catacomb | Flooded Strand | Conditional checkland becomes an Island-typed fetch for Underground Sea, Watery Grave, Steam Vents, Volcanic Island, Xander's Lounge or Island. |
| Shipwreck Marsh | Marsh Flats | Slowland becomes a Swamp-typed fetch for Badlands, Blood Crypt, Underground Sea, Watery Grave, Xander's Lounge or Swamp. |
| Shivan Reef | Volcanic Island | Painland becomes an untapped fetchable U/R dual. |
| Stormcarved Coast | Misty Rainforest | Slowland becomes a fetch for Island-typed UBR lands/basics. |
| Sulfur Falls | Verdant Catacombs | Checkland becomes a fetch for Swamp-typed UBR lands/basics. |
| Sulfurous Springs | Underground Sea | Painland becomes an untapped fetchable U/B dual. |
| Underground River | Wooded Foothills | Painland becomes a fetch for Mountain-typed UBR lands/basics. |
| Island (one of three) | City of Brass | Keeps two Islands while adding untapped three-color fixing for Nekusar and Niv-Mizzet's demanding pips. |
| Swamp (one of three) | Mikokoro, Center of the Sea | Keeps two Swamps while turning a land slot into repeatable each-player card draw that directly triggers Nekusar's punishment engine. |

Net structural effect: land count remains **35**. The candidate has nine useful fetchlands, both remaining original duals plus newly added Underground Sea/Volcanic Island, shocks, Xander's Lounge, City of Brass, Mana Confluence, multiplayer duals, and six basics.

## Historical P-006 correction

The inherited proposal was `Krang, the All-Powerful → Fate Unraveler`. That proposal is **REJECTED AS WRITTEN**.

Fate Unraveler remains a four-mana standalone draw punisher and is one of the strongest independent redundancies when Nekusar is answered. Krang is good enough to add, but the whole-list audit found a materially weaker cut: **Solphim, Mayhem Dominus**. Solphim's damage replacement effect interferes with Ghyrson Starn's exact-1 trigger, while Krang increases the number of draw-triggered punishment instances without modifying the underlying damage event.

## Trigger-multiplier rules correction

The current Nekusar-specific article informally compares Krang to Wizard's Staff, but the cards are not rules-identical.

- **Wizard's Staff:** if a triggered ability of equipped Nekusar triggers, it triggers an additional time. This applies to both Nekusar's beginning-of-draw-step trigger and his opponent-draw damage trigger.
- **Harmonic Prodigy:** because Nekusar is another Wizard, his triggered abilities trigger an additional time. This likewise applies to both abilities.
- **Krang:** applies only when a player drawing a card causes a triggered ability of a permanent you control to trigger. It applies to Nekusar's damage trigger and draw-triggered punishment permanents, but not to Nekusar's beginning-of-draw-step trigger because that trigger is caused by the draw step beginning, not by a card being drawn.

These additional-trigger effects are **additive**, not a multiplicative doubling chain.

Example with Nekusar equipped with Wizard's Staff plus Harmonic Prodigy plus Krang:
- beginning-of-draw-step ability: base + Staff + Prodigy = three instances;
- each opponent draw causing Nekusar's damage ability: base + Staff + Prodigy + Krang = four instances.

Krang's official release notes explicitly state that it does not copy the triggered ability; it causes the ability to trigger an additional time and choices are made separately.

## Important retained-card decisions

- **Fate Unraveler — KEEP.** Independent punishment density is more valuable than treating the old Krang proposal as mandatory.
- **Ghyrson Starn, Kelermorph — KEEP.** With Nekusar's original 1-damage events intact, each event can trigger Ghyrson for 2 additional damage. Cutting Solphim restores this engine's reliability.
- **Harmonic Prodigy — KEEP.** Two mana for another Nekusar Wizard-trigger instance is one of the most commander-specific effects in the list.
- **Niv-Mizzet, Parun — KEEP.** Demanding pips are now better supported by the mana base; it remains a draw/damage engine and Curiosity gives it a compact optional loop.
- **Consecrated Sphinx — KEEP.** Expensive but scales directly from the extra draws the deck gives opponents and provides the controller resources for subsequent wheel turns.
- **Anvil of Bogardan — KEEP.** At two mana, its extra draw plus discard advances both draw-punishment and discard-punishment engines while removing maximum hand size.
- **Kami of the Crescent Moon / Fevered Visions / Stormfist Crusader — KEEP.** These are cheaper ongoing draw sources; Dictate and Font are the slower redundant pieces cut first.
- **Premium free/cheap interaction — KEEP.** Nekusar is five mana and attracts removal; interaction density is justified at Bracket 4 rather than converting those slots into more group-hug effects.

## Candidate exhaustion — notable rejected alternatives

- **Master of the Feast / Seizan, Perverter of Truth / Prosperity / Vision Skeins / Temple Bell — REJECT.** More forced draw is available, but the candidate already has sufficient draw density; none beats a retained slot after speed, reciprocity, and setup costs are compared.
- **Naktamun Lorespinner // Wheel of Fate — REJECT.** Current Nekusar-specific research flags its front face as unreliable because the deck itself keeps opponents' hands stocked, making the transformation condition awkward.
- **The Master of Lake-town — REJECT.** Strong life-loss-to-mill conversion but feeds opposing graveyards and pulls the list toward a mill subtheme rather than improving the wheel/draw-kill engine.
- **Tomik, Izzet Sparkmage / Ojer Axonil, Deepest Might — REJECT in this build.** Damage replacement/increase effects that turn Nekusar's original 1 into 2+ prevent Ghyrson from triggering on that event; the Ghyrson line is more efficient and commander-native here.
- **Narset, Parter of Veils / Notion Thief — REJECT.** Locking opponents out of the cards drawn by wheels is powerful but suppresses the repeated actual draw events this deck wants to punish and homogenizes the list toward generic Grixis wheel-lock play.
- **Phyresis / Tainted Strike — REJECT.** Infect is a shortcut kill package rather than the strongest expression of Nekusar's natural draw-punishment ceiling.
- **Mindcrank — REJECT.** It completes a Bloodchief Ascension loop but converts the deck toward a commander-independent mill combo; Bloodchief remains useful without forcing that package.
- **Additional cEDH Oracle/Consultation or deterministic Breach packages — REJECT.** They can raise abstract power but reduce commander necessity and change the deck's identity.
- **Lightning Greaves — REJECT at final cut stage.** Protection is useful, but the list already has a dense free/one-mana protection suite and Greaves does not protect Nekusar from board wipes or multiply draw output.
- **Memory Jar / Time Spiral / Time Reversal — REJECT.** Strong additional wheel effects, but the candidate has enough wheel density and the retained low-cost wheels are more mana-efficient.

## Final red-team result

The final serious pass challenged every proposed spell swap, the entire 11-land mana-base delta, trigger stacking, the Ghyrson/Solphim interaction, the Curiosity/Niv line, wheel density, protection density, and commander-independent alternative wins.

No challenger produced a material improvement without a larger opportunity cost in mana, commander dependence, internal synergy, or strategic identity.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`
- Exact approved artifact: `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**
- Next unlocked deck in tracker order: **Nicol Bolas (index 40 / deck 41 of 62)**.
