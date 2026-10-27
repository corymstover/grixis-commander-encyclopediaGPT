# Deck #52 — Sol'kanar the Swamp King — M7 Rev1 approval verification

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

- **Candidate full raw UTF-8 SHA-256:** `2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3`.
- **Previous approved Oct15 raw SHA:** `7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106`; previous approved file and records must remain untouched.
- **Source:** complete 100-card `data/grixis/m7/candidate_lists/Sol_kanar_the_Swamp_King_M7_Rev1.txt` from merged engineering PR #733 and canonical new `refinement/decklists/Solkanar_the_Swamp_King_M7_Rev1_Approved_2026-10-27.txt`.
- **Structure:** 100 physical cards / 95 distinct names / Swamp×6 basic only repetition / one Grixis commander / no companion / 35 actual front-face land copies plus Fell the Profane // Fell Mire land back-face = 36 functional land-capable slots. No off-color name, no unregistered project exception.
- **Oracle/legality evidence:** archival Scryfall Oracle bulk 2026-10-15 all 95 names source-bound via precise Oracle IDs, source blob `c84463e9fa4708165027404d4ca54af5dcf5774b`, recorded in engineering JSON `data/grixis/m7/oracle_snapshots/Sol_kanar_the_Swamp_King_M7_Rev1_2026-10-15.json`. All 95 archived Commander legal, U/B/R or colorless. Not claimed to be a live same-day 95-card Scryfall sweep. Official Commander ban list and targeted selected rules reviewed.
- **Exact six swaps:** +Necropotence/-Alhammarret's Archive; +Orcish Bowmasters/-Underworld Dreams; +Rowan, Scion of War/-Bontu's Monument; +Hatred/-Bloodletter of Aclazotz; +Yawgmoth's Will/-Dimir Signet; +Bubbling Muck/-Talisman of Creativity.
- **Whole-list:** original 99 physical slots individually adjudicated 93 KEEP / 6 CUT. Extra Mindcrank/Rakdos Signet swap rejected after colored-mana consistency analysis. Preserve two premium colored mana rocks: Rakdos Signet and Talisman of Dominance/Indulgence.
- **Key mechanical scope:** Sol'kanar triggers for players' black spells but not its own casting; Painter Servant naming black and Horn generate separate life-gain events; Urborg/Blanket yield swampwalk; Hatred as a paid life-cost addition to 5 power needs 16 to reach 21 commander damage and remains vulnerable to response; Rowan counts total life *lost* not net loss, reduces only generic, requires sorcery tap; Bubbling Muck affects all players' Swamps; Necropotence exiles purchased cards until next end step; Yawgmoth's Will uses exile replacement.
- **Engine protected:** Painter/Grindstone, Demon's Horn, K'rrik, Rhystic/Remora/Ring, Citadel/Top/Aetherflux, Exquisite Blood/Bloodthirsty Conqueror and Vito/Enduring Tenacity/Starscape Cleric/Marauding Blight-Priest, Witch of the Moors, Coffers/Ghast/Urborg/Blanket, full anti-combo interaction and Bog/Charm graveyard defenses.
- **Engineering source:** [PR #733](https://github.com/corymstover/GrokBotMTGCompanion/pull/733) exact tested head `4e4b6c7ebbdc70b96c218d88d9fd67ec1c6e327b`, merge commit `9ad96f3cd050e94dc49333e246b278d584f8e276`.
- **Action evidence:** [focused suite #40554443034](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40554443034) SUCCESS and [M7 contract #40554443052](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40554443052) SUCCESS at exact head.
- **Owner authority:** Cory's single response **"Approve"** to the immediately preceding full Deck #52 M7 Rev1 proposal is explicit selected-candidate approval, not blanket future authorization. It authorizes engineering merge, canonical locking and post-merge re-verification.
- **Natural power ceiling/tags:** Bracket 4 — Optimized; Black Spells / Lifegain / Swamp Matters.
- **Post-merge required checks:** re-fetch both new canonical deck file and `main/state/current_deck_overrides.json#decks.Sol_kanar_the_Swamp_King`, independently confirm raw SHA and APPROVED/LOCKED, inspect tracker and preserved predecessor. Do not infer milestone completion from one deck.

**Boundary:** finite source-bound checks are not full independent-model certification, randomized four-player simulation or aggregate M6.10/M7/M8 acceptance.
