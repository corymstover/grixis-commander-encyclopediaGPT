# Admiral Brass, Unsinkable — Commander-First Refinement Blueprint v1

**Date:** 2026-10-13  
**Deck position:** 3 of 62 (tracker index 2)  
**Status:** Baseline established; first candidate proposal pending user approval  
**Frozen baseline:** `GrixisFINALTXT60--2026.zip` → `Admiral_Brass__Unsinkable.txt`  
**Baseline TXT SHA-256:** `2e3721984f38bd2a19c1377357f6e737e3588152014bed816e81ce2759392196`

## 1. Commander identity and core plan

Admiral Brass, Unsinkable mills four cards when it enters. At the beginning of combat on your turn, it may return a target Pirate creature card from your graveyard to the battlefield with a finality counter; that creature becomes base 4/4 and gains haste until end of turn. The deck should use that recurring combat trigger as its engine rather than treat the commander as generic reanimation.

**Primary plan**
- Put high-impact Pirate creatures into the graveyard through the commander’s ETB mill, looting, and targeted setup.
- Reanimate a Pirate at the beginning of combat to generate an immediate attack and/or ETB value.
- Maximize Pirate density, impactful ETB/attack triggers, and ways to use the commander’s recurring body effectively.
- Use broad tribal recursion (Living Death, Patriarch’s Bidding, Victimize) as complementary recovery/closing tools rather than the entire identity.
- Protect the commander and preserve a functional graveyard without depending on self-mill as an end in itself.

## 2. Important rules interaction: finality counters

The commander’s returned creature receives a finality counter. If that creature would die while it has that counter, it is exiled instead. Removing the finality counter before it would die allows it to die normally and become a future graveyard target again. Counter-removal effects are therefore unusually relevant: they can turn a one-use reanimation into a repeatable engine. This needs to be balanced against activation timing, summoning sickness, and the fact that the commander’s reanimation happens at the beginning of combat.

## 3. Frozen baseline assessment

The frozen source list contains 100 cards (97 lines) and remains unchanged. Its plan already has meaningful support:
- Graveyard setup: Entomb, Buried Alive, Faithless Looting, the commander’s own mill-four ETB.
- Reanimation and tribal recovery: Animate Dead, Reanimate, Victimize, Living Death, Patriarch’s Bidding.
- High-impact Pirates: Amphin Mutineer, Angrath’s Marauders, Broadside Bombardiers, Coercive Recruiter, Hostage Taker, Port Razer, Zara, Renegade Recruiter, and others.
- Tribal/combat payoff: Shared Animosity, Skeleton Crew, Wonder, Kindred Discovery.
- Interaction and protection: premium removal/counters and Siren Stormtamer, Lightning Greaves, Deflecting Swat, Fierce Guardianship.

The first refinement should be narrow. Avoid replacing this deck with generic Grixis reanimator, and do not add cards merely because they rank highly.

## 4. Candidate research — first pass

The current project ranking is discovery evidence. The leading candidate Enterprising Scallywag is already present; so are Dire Fleet Daredevil, The Indomitable, and Ghost of Ramirez DePietro. Those are not proposed additions.

Candidates warranting further consideration:
- **Power Conduit (#31; score 65.4; EDHREC inclusion 20.94%, lift 50.1):** directly removes a finality counter from a returned Pirate and converts it into a +1/+1 counter on a creature or a charge counter on an artifact. As a noncreature artifact, it can activate immediately after being cast, unlike a newly cast creature with a tap ability.
- **Soul Diviner (#37; score 62.1; inclusion 17.72%, lift 36.0):** can remove a counter from a creature and draw a card, including removing a finality counter, but summoning sickness can prevent immediate use on the turn it is cast.
- **The Grim Captain’s Locker (#7):** graveyard/escape utility, but four mana and its escape costs compete with existing recursion; no change proposed in this pass.
- **Back in Town (#54):** can return multiple outlaw creatures (including Pirates), but the deck already has Living Death, Patriarch’s Bidding, and Victimize; evaluate for redundancy before adding.
- **Arm-Mounted Anchor (#19):** potentially strong draw/loot for a Pirate, but the list already has several draw engines and its equip/combat setup needs comparison against more direct commander synergy.
- **Port of Karfell (#2) and Nephalia Drownyard (#3):** candidate ranking is high, but these utility lands have opportunity costs versus the existing premium mana base; do not add by rank alone.
- **Warkite Marauder (#6), Kitesail Larcenist (#17), and Dire Fleet Ravager (#18):** commander-compatible Pirates with distinct utility/ETB effects; review against the existing high-impact Pirate suite before any addition.

## 5. Initial proposed change — pending approval

**Add 1x Power Conduit; cut 1x Revel in Riches.**

Rationale: Power Conduit gives the deck a low-cost, commander-specific way to remove finality counters and reuse high-impact Pirates. Its tap ability is available immediately because it is not a creature, so it can remove the counter from the Pirate returned at the beginning of combat that turn. It also turns the removed counter into a +1/+1 counter on a creature or a charge counter on an artifact.

Tradeoff: Revel in Riches is an independent alternate-win condition and a Treasure engine, so cutting it reduces that secondary win path and some Treasure value. The proposed cut is based on identity and consistency: Revel in Riches does not directly enable the commander’s Pirate reanimation loop, while Power Conduit does. No swap is approved or applied until the user approves it.

**Legality/text checkpoint:** Power Conduit is a colorless artifact and is Commander-legal; current Oracle text and legality were checked against MTG.WTF. Revel in Riches is Commander-legal and has the documented Treasure/alternate-win text. No official legality exception is involved.

## 6. Verification boundaries

No decklist has been changed. The frozen 2026-10-12 source exports remain untouched. The candidate list, Oracle text, and legalities were reviewed for this proposal; full 100-card verification is required after any user-approved swap. No gameplay win-rate or multiplayer-test claim is made.
