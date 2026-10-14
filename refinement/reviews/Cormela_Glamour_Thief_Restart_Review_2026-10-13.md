# Cormela, Glamour Thief — Fresh Restart Review

**Deck:** #9 of 62  
**Baseline:** Immutable October 12 archives  
**Raw baseline CSV SHA-256:** `0780ccdcace7e54df75ddf15d02e9d4368e3d102ef7a1eb3c7123d9bb9479703`  
**Raw baseline TXT SHA-256:** `10639176c36a7a55853cd1c65f22ac31e22b99dd15d7e95607b1d03acb74babd`  
**Normalized baseline hash:** `949ad1d40e2af9af6c17d487f05c046c67232dd2b347e1670ce9f6e020521615`  
**Proposed list SHA-256:** `cb81718ff186d28f97bc17ce1c9ce880e02a8a90e96df8c539cfbc05beb2fe75`

## Status
**TECHNICAL REVIEW COMPLETE — PROPOSED CHANGE AWAITS USER APPROVAL.** Earlier refinement status was not treated as approval. The proposal is Galvanic Iteration for Grapeshot; this deck remains unapproved and unlocked pending explicit approval.

## Commander-first plan
Cormela is a hasty creature that taps for UBR restricted to instant/sorcery spells and returns an instant or sorcery from graveyard to hand when she dies. This list's natural ceiling is cEDH / Bracket 5: fast mana, premium tutors, free/cheap interaction, and compact graveyard/sacrifice combo. Underworld Breach, Lion's Eye Diamond, Brain Freeze and the commander death trigger form an important engine group. Brain Freeze is the mill/storm route; Tendrils of Agony is the life-loss storm route.

## Proposed swap
**Add Galvanic Iteration; cut Grapeshot.** Galvanic Iteration costs {U}{R}, copies the next instant or sorcery cast that turn, and has flashback {1}{U}{R}. It can copy Brain Freeze or a key ritual/tutor. The copy is not cast and does **not** increase storm count. Flashback exiles the card after it leaves the stack; Cormela can return it only if it is still in the graveyard when her death trigger resolves.

Grapeshot is the chosen cut because Brain Freeze and Tendrils remain distinct finishers. This loses a one-mana direct-damage spell that can remove utility creatures or convert storm into damage. The swap is a strategic trade-off, not an empirically proven upgrade.

## Candidate triage
Sixteen commander-specific candidates were reviewed. Galvanic Iteration is the proposed addition; fifteen alternatives were rejected with reasons. The October 12 rankings/Lift values are discovery evidence only. Current EDHREC Cormela cEDH data were used as adoption context, not as proof of card strength. High-cost value spells do not fit the compact curve; Cursed Recording risks self-damage in a storm deck; Silundi Vision has a tapped-land face and slow selection.

## Audit
- Proposed list: 100 cards, 100 distinct names, commander first, 30 lands, no duplicates.
- Full-list matrix covers all 100 names. The 99 retained baseline cards are in the current metadata refresh; Galvanic Iteration was checked directly.
- UBR identity and Commander legality pass; official Commander banned list checked 2026-10-13, no final-list card is banned; no project exception applies.
- Galvanic Iteration copy-not-cast/storm interaction, flashback exile and Cormela death-trigger timing checked. No infinite combo is asserted from Galvanic Iteration alone.
- No qualified matched-seed multiplayer sample; no win-rate claim.

## Sources
[EDHREC Cormela cEDH combo](https://edhrec.com/commanders/cormela-glamour-thief/cedh/combo) · [Cormela](https://scryfall.com/card/snc/301/cormela-glamour-thief) · [Galvanic Iteration](https://scryfall.com/card/msc/184/galvanic-iteration) · [Grapeshot](https://scryfall.com/card/msc/803/grapeshot) · [Official Commander ban list](https://mtgcommander.net/index.php/banned-list/)

## Artifacts
- Proposed list: `refinement/decklists/Cormela_Glamour_Thief_Restart_2026-10-13.txt`
- Matching CSV: `refinement/decklists/Cormela_Glamour_Thief_Restart_2026-10-13.csv`
- Matrix: `refinement/reviews/Cormela_Glamour_Thief_Full_List_Review_2026-10-13.csv`
- Candidate ledger: `refinement/decisions/Cormela_Glamour_Thief_Restart_Candidate_Decisions_2026-10-13.csv`
- Change ledger: `refinement/changes/Cormela_Glamour_Thief_Restart_Change_Ledger_2026-10-13.csv`
- Verification: `refinement/verification/Cormela_Glamour_Thief_Restart_Verification_2026-10-13.md`
