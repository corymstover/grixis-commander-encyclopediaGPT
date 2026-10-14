# Be'lakor, the Dark Master — Full Restart Review

**Deck #7 of 62 · Review date: 2026-10-13 · Active status: TECHNICAL REVIEW COMPLETE; final hash/tracker gate pending independently verified digest.**

Frozen normalized baseline hash in source certificate: `fe61e3a7d7bc5fc6d56a9c6a03b97f3986c606e3626a6a3839cdd91a7dfd9e0e`. The preserved current candidate build contains 100 copies, 94 unique names and 36 lands, with only basic lands repeating. Prior-cycle certification was treated as evidence, not new-cycle approval.

## Commander-first strategy

Be'lakor draws and loses life equal to Demon count on entry, then each other Demon entry deals damage equal to that creature's power to any target. The list prioritizes dense Demon bodies, repeated Demon ETBs, token copies, blink effects, reanimation and cost-cheating. It does not force the deck into generic Grixis goodstuff or a spellslinger shell.

## Fresh restart decisions

The two previous swaps are retained after full re-evaluation:
- **Demonic Covenant for Reaper from the Abyss.** Covenant is a Kindred Enchantment — Demon, contributes to Be'lakor's Demon count, creates a 5/5 flying Demon at each end step, and draws for each player you attack with Demons. Its own noncreature entry triggers Be'lakor but deals 0 because it has no power; its generated creature token can deal 5 if Be'lakor remains.
- **Ardyn, the Usurper for Archfiend of Depravity.** Ardyn gives Demons menace, lifelink and haste, then at beginning of combat can create a 5/5 black Demon token copy of a creature card in any graveyard. It is not itself a Demon. Its cost of eight mana is real, but the list has Heartless Summoning, Urza's Incubator, Rakdos, Lord of Riots and Sneak Attack to mitigate deployment.

The cuts are genuine trade-offs: Reaper's conditional end-step removal and Archfiend's opponent-creature suppression are powerful effects. Covenant and Ardyn instead emphasize recurring Demon entries, card flow and proactive board pressure.

## Rules and interaction checks

- Be'lakor's ETB draw count includes Demons already on the battlefield as it enters, including Demonic Covenant as a Demon permanent. It loses that much life as part of the same ability.
- A noncreature permanent has no power; Be'lakor's “deals damage equal to its power” trigger for Demonic Covenant's own entry deals zero. The token Covenant creates is a 5/5 creature and deals 5 to a target through Be'lakor.
- Ardyn's ability creates a token copy of a creature card in a graveyard, modified to a 5/5 black Demon. Copiable ETB abilities are retained; if the copied card has an ETB ability it triggers on the token's entry. This also creates a Be'lakor damage trigger.
- Ardyn is not a Demon, so it doesn't increment Be'lakor's Demon count or trigger the “another Demon” ability when Ardyn itself enters.
- Kindred Discovery, Panharmonicon, Roaming Throne, Molten Echoes and Reflections of Littjara affect different kinds of triggers/copies; they are not universally interchangeable. Legendary-token restrictions and the exact source of the trigger matter.
- Demon ETB damage triggers require Be'lakor to remain on the battlefield as appropriate for the trigger's source/condition; removal and stack ordering still matter.
- No deterministic infinite combo is added or claimed. High-end sequences depend on cost reducers, Sneak Attack, reanimation, token copies and sufficient board/graveyard resources.

## Candidate review

The inherited candidate ledger assessed 16 candidates: two accepted swaps (Demonic Covenant and Ardyn), two baseline core cards retained (Heartless Summoning, Ancient Cellarspawn), and twelve rejected options. The rankings are supporting discovery data only.

- **Varragoth, Bloodsky Sire rejected:** redundant tutor package; boast requires attacking and places the card on top.
- **Dream Devourer rejected:** foretell setup is slower than existing cost reducers/Sneak Attack and it is not a Demon.
- **Bloodcrusher of Khorne rejected:** marginal evasion improvement and no ETB/card advantage.
- **Plague Drone rejected:** narrow lifegain hate and only a 3/3 trigger payoff.
- **Ob Nixilis, Unshackled rejected:** meta-dependent search punishment without an ETB/card-advantage payoff.
- **Bloodgift Demon rejected:** redundant, slower draw compared with Be'lakor ETBs, Vilis, Rakdos, Patron of Chaos, Unholy Annex and Kindred Discovery.
- **Lord Xander, the Collector rejected:** another expensive top-end threat but less cleanly aligned to Demon engine density.
- **Aspiring Champion rejected:** combat-dependent, random creature result.
- **Venomcrawler rejected:** four-mana body with no immediate ETB, protection or card flow.
- **Exalted Flamer of Tzeentch rejected:** pulls toward spellslinger and inconsistent graveyard recursion, away from Demon ETBs.
- **Séance Board rejected:** delayed creature-death setup and restricted mana.
- **Lord of the Void rejected:** seven-mana combat-damage-dependent payoff.
- **Heartless Summoning retained:** core creature cost reduction; the -1/-1 drawback is monitored for small utility bodies/tokens.
- **Ancient Cellarspawn retained:** synergizes with cost reducers and remains a targeted opponent life-loss trigger, not an all-opponent trigger.

## Legality, identity and integrity

The prior active-cycle certificate documents current Scryfall name/Oracle/identity metadata refresh for all 94 baseline names and direct checks for both additions and cuts. Both additions and both cuts are Commander-legal and fit UBR. The official Commander banned-list checkpoint in the source certificate is dated 2026-10-13; no project exception applies.

## Final structural gate

The decklist has 100 copies including commander, 94 unique names, and 36 lands. The only repeated names are Island ×3, Mountain ×2 and Swamp ×4. Singleton/copy and commander-first marker pass. The frozen baseline is preserved and the current final revision is a separate dated artifact. No matched-start multiplayer simulator or representative before/after game sample was available, so no win-rate claim is made.

**Technical review disposition:** all substantive card, strategy, rules and legality review sections pass; close only after re-fetching the exact restart TXT and confirming its content hash in the certificate and tracker.