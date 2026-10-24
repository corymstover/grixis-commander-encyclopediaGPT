# Fire Lord Azula M7 Rev2 — Cory's exact owner approval and canonical receipt

Date **2026-10-24** (America/Chicago), owner **Cory Stover**. Cycle `global-restart-2026-10-13`. Deck #19, tracker index 18, registry `Fire_Lord_Azula`.

**APPROVED exact 100-card RAW SHA-256: `77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`.**

## Explicit authorization and immutable source

After seeing the entire copy/paste 100-card Fire Lord Azula M7 Rev2 list, the five paired swaps with commander-specific reasoning and losses, 100 unique/26 land faces/20 Game Changers, Bracket 5 cEDH and three tags, exact raw SHA, plus independent [engineering PR #694](https://github.com/corymstover/GrokBotMTGCompanion/pull/694), **Cory explicitly replied "Approve" on 2026-10-24**. This approves only those bytes, not future changes or any other deck.

- Newly locked exact list: `refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt` — **`77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`**.
- Prior Oct14 approved list, **left untouched**: `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt` — **`b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`**.
- Independent engineering PR #694 exact head `f795c9f932346152b4a7f79c5839d45203a17786`; [focused GitHub Actions job #120792752616](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40067171128/job/120792752616) **SUCCESS**. Grok first-pass research PR #667 was reviewed, not treated as owner approval.
- Frozen Oct23 live Scryfall 205-card Oracle source narrowed to candidate's 100 cards in `refinement/verification/Fire_Lord_Azula_M7_Rev2_Scryfall_Selected_2026-10-23.json`. The archival source is explicitly **not** described as a new Oct24 real-time pull.
- Canonical exact-head workflow plus regression of **18 previously re-locked M7 decks** required before release. This receipt does not preemptively assert CI or main merge success.

## Five owner-approved substitutions

| Add | Cut | Strategic improvement | Explicit sacrifice |
|---|---|---|---|
| Turnabout | Samut, Tyrant of Naktamun | Narset's Reversal/Turnabout combat copy loop; Samut split-second prevention of our own responsive casts | Loss of split-second protection |
| Sink into Stupor // Soporific Springs | Exotic Orchard | Combat-spell/land flexibility and two copied bounce effects | 3 life untapped, extra Ad Nauseam MV3, loss of flexible mana |
| Samut, Hazoret's Champion | Vivi Ornitier | Fourth haste source in 99-card library, earlier Azula attacking | Loss of Vivi mana/ping scaling |
| Flashback | Repeal | Can target two graveyard spells with Azula copy; replay rituals/tutors/interaction | Lose Repeal cantrip bounce; flashback pays mana |
| Electrodominance | Redirect Lightning | Azula copies damage/free-hand-spell casts and newly cast spells retrigger Azula | Lose 1-red redirection/protection; target must stay legal |

Electrodominance was **previously cut by Cory in Oct14** for its mana floor. The independent M7 review explicitly re-evaluated that choice: with Azula attacking, firebending RR pays the red portion of XRR; Azula copies Electro; each resolving instance may cast eligible hand spells during its own resolution regardless of card-type timing; those *new casts* may trigger Azula again if she remains attacking. The free casts are **conditional**, require legal Electro targets at resolution and cards of MV<=X in hand, and are **not an unconditional infinite combo**. A spell copy itself is not cast. Wizards source: https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes and https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes.

The M7 reviewer corrected an earlier erroneous Big Score/Unexpected Windfall mana claim (both need two additional mana after RR), protected **Swan Song and Gemstone Caverns** from Grok's proposed cuts, and tested a sixth `+Mistrise Village/-Wooded Foothills` which was **rejected** because its extra blue-only / sometimes-tapped mana burden was not demonstrably positive in the 26-land three-color cEDH mana base. Five is a reasoned limit, not the permitted maximum.

## Verified scope and transparency

- **100 physical cards, 100 distinct names, first card commander, color identity UBR, official Commander legality PASS in archival Oct23 Scryfall, 26 land faces including Sink MDFC, 20 Game Changers, no project exceptions.**
- Current source explains Samut split-second/self-Reversal conflict, Turnabout combo's conditional lands/mana requirement, Flashback costs/exile, and Electro legal targets/eligible hand-spell timing.
- The bounded Azula turn-four castability proxy (.4920 baseline vs .4900 final with MDFC as a land; .4626 if never as land) **is not a match win rate** and omits important fast mana, board, haste and interaction factors. No generalized exhaustive full-suite success or mathematical perfection claimed.
- Power Bracket **5 — cEDH**, tags **Combat-Flash / Spell Copy / Combo**.
- New canonical authority updates only `Fire_Lord_Azula`; retains the previous 18 M7 raw sources, hashes and locks unchanged. Owner may reopen by explicit new decision only.

**MERGE AND LOCK GATE:** exact-head GitHub Actions PASS, expected-head merge, refetch merged main, independently rehash the exact approved .txt to `77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`, verify Fire Lord state+tracker and all previous 18 SHA-bound locks. Record result in PR merge history.
