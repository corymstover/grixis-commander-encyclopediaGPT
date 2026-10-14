# Be'lakor deck #7 — full-list comparative audit working record

Cycle global-restart-2026-10-13. STATUS: WORKING, not approval-ready; no user approval or lock.

Frozen baseline GrixisFINALTXT60--2026.zip / Be_lakor__the_Dark_Master.txt SHA-256 9b0e16a43add999252504948aa3104666a342bf4f8c80b758a2d9f65649fe6c7; 100 cards, 94 distinct names, 36 lands, 99 noncommander card copies.

The inherited v8.1.4 card audit is **stale** for this baseline. Five names in the frozen source are missing from the inherited deck audit: Abyssal Harvester, Ancient Cellarspawn, Heartless Summoning, Demonlord Belzenlok, Reaper from the Abyss. Five names in the inherited audit are no longer in the frozen baseline: Kindred Dominance, Essence Flux, Herald's Horn, Quicksilver Amulet, Harvester of Souls. The five missing baseline cards occur in the ranked candidate research and have archived Oracle text, but archived research does not replace a current live legality check.

## Tentative three-swap shortlist (NOT FINAL)
- Raphael, Fiendish Savior -> Dream Devourer: Raphael is a Devil not Demon, while Dream Devourer is a two-mana Demon that can bank expensive cards through foretell. Foretell is delayed, incurs two mana to exile, and cannot be cast the same turn. Dream Devourer's 0 base power makes Be'lakor damage trigger minimal; the cheaper Demon deployment is the principal argument.
- Reaper from the Abyss -> Doom Whisperer: five-mana 6/6 Demon with flying, trample and repeatable life-for-surveil versus six-mana conditional end-step non-Demon removal. Surveil is valuable with reanimation, but life spending compounds Be'lakor draw loss.
- Demonlord Belzenlok -> Spark Double: four-mana copy of Be'lakor (nonlegendary) or another Demon. Copying Be'lakor creates another Demon ETB card-draw trigger, triggers original Be'lakor damage for the entering copied Demon, and adds another persistent damage-trigger source; the copy's +1/+1 counter applies. Sacrifices a high-mana Demon body and Belzenlok's high-variance draw.

## Key retained cards
Molten Echoes, Reflections of Littjara, Roaming Throne, Panharmonicon, Rite of Replication, Liliana's Contract, Sneak Attack, Patriarch's Bidding, Reanimate, Whip of Erebos, Herald of Slaanesh, Heartless Summoning, Archfiend of Despair, Bloodletter of Aclazotz, Sower of Discord, Bloodthirster, Warstorm Surge.

## Important red-team issues
- Panharmonicon doubles Be'lakor's own ETB draw/life loss; this is not free advantage when life is low.
- Molten Echoes copying legendary Demons may invoke legend rule, though ETB triggers still occur. Copies entering as Demons trigger Be'lakor; nonlegendary-copy solutions avoid legend-rule losses.
- Be'lakor's damage trigger checks the entering Demon's power as it resolves; the original Be'lakor does not damage on its own entry. Its draw ETB includes itself in Demon count.
- Liliana's Contract alternate win requires four Demons with different names at upkeep; copies of same named Demon do not meet diversity.
- Spark Double is not inherently a Demon in hand or on stack; its Demon typing comes from copying on entry. This matters to Demon cost reducers.
- Blood Speaker (candidate rank 39) is not a Demon, so its recursion/tutor merits do not improve Demon count. High-impact comparison retained.
- 36-land manabase unchanged. Need verify colored-source sufficiency and life-cost density before finalization.

## Remaining gates
Current Oracle/Commander legality/color identity verification for the full proposed 100-card list, detailed high-impact alternative closure including Dream Devourer vs Varragoth and Blood Speaker, rigorous mana/curve and consistency evaluation, final red-team, zero-new-material-improvement stop, exact list SHA and user approval request. No lock or advance without approval.

References: https://mtg.wtf/card/prm/88276/Dream-Devourer ; https://mtg.wtf/card/grn/69/Doom-Whisperer ; https://mtg.wtf/card/cmm/856/Spark-Double ; https://media.wizards.com/2023/downloads/RVR_Release_Notes_XrN0zlJaFn/EN_MTGRVR_ReleaseNotes_20231120.pdf
