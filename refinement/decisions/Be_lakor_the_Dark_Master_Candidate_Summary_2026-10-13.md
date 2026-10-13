# Be'lakor, the Dark Master — Candidate Decision Summary

**Deck:** #7 of 62  
**Snapshot:** October 12 frozen baseline; decisions verified October 13, 2026  
**Baseline normalized SHA-256:** `fe61e3a7d7bc5fc6d56a9c6a03b97f3986c606e3626a6a3839cdd91a7dfd9e0e`  
**Revised exact TXT SHA-256:** `f48359f816498b386b085db60f0456576c8af9b055408685df71f0d1db448545`

## Commander-first plan

Be'lakor is a six-mana Demon Noble whose ETB draws cards and costs life equal to the number of Demons controlled (including Be'lakor if still present when the trigger resolves). Whenever another Demon enters, that Demon deals damage equal to its power to any target. The deck's core is therefore Demon density, repeatable Demon ETBs, token/copy effects, cost reduction, reanimation, and protection for its high-value commander. The existing list already has substantial support in Molten Echoes, Reflections of Littjara, Roaming Throne, Panharmonicon, Ghostly Flicker, Sneak Attack, Heartless Summoning, Urza's Incubator, and multiple Demon tutors.

## Accepted changes

1. **Add Demonic Covenant; cut Reaper from the Abyss.** Covenant is a Kindred Enchantment — Demon, so it counts as a Demon permanent for Be'lakor's ETB draw count. Its own entry causes Be'lakor's other-Demon trigger to trigger, but the enchantment has no power as a noncreature permanent, so that damage amount is 0. Its repeatable value is the end-step 5/5 flying Demon token (which can produce a 5-damage Be'lakor trigger) and card draw for each player attacked by one or more Demons. The self-sacrifice condition checks whether the two milled cards have the exact same combination of card types, not merely a shared subtype.
2. **Add Ardyn, the Usurper; cut Archfiend of Depravity.** Ardyn is not itself a Demon, but grants all Demons menace, lifelink and haste, and creates a 5/5 black Demon token copy of a creature card in a graveyard at the beginning of combat. The token can create a Be'lakor damage trigger and preserve copied ETB abilities. Eight mana is a real cost; Heartless Summoning, Urza's Incubator, Rakdos, Lord of Riots and Sneak Attack help mitigate it. This trades the Archfiend's potent opponent creature cap for a more proactive token/keyword engine.

## Candidate triage

- 16 candidates documented: **2 accepted**, **2 existing core candidates retained**, **12 rejected** with card-specific reasons.
- Candidate rankings and EDHREC-derived inclusion/lift fields come from the October 12 project snapshot. They inform discovery, not automatic inclusion.
- No qualified matched-start multiplayer sample or before/after win-rate data was available. No empirical performance claim is made.

See [candidate decisions](Be_lakor_the_Dark_Master_Candidate_Decisions_2026-10-13.csv), [actual change rows](Be_lakor_the_Dark_Master_Change_Ledger_Rows_2026-10-13.csv), and [verification certificate](Be_lakor_the_Dark_Master_Verification_2026-10-13.md).