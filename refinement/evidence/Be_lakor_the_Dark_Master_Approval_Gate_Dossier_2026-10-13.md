# Be'lakor, the Dark Master — Approval Gate Dossier (2026-10-13)

**Cycle:** global-restart-2026-10-13. **State:** APPROVAL_REQUESTED — NOT APPROVED — NOT LOCKED. Prior historical auto-approved/locked file is superseded as a proposal, not a user authorization. Decks #1–6 remain preserved.

## Authoritative baseline and proposed list
- Frozen baseline: GrixisFINALTXT60--2026.zip / Be_lakor__the_Dark_Master.txt, SHA-256 9b0e16a43add999252504948aa3104666a342bf4f8c80b758a2d9f65649fe6c7.
- Proposed list: refinement/decklists/Be_lakor_the_Dark_Master_Approval_Proposal_2026-10-13.txt, exactly 100 cards including commander, 94 distinct names, 36 lands; repeated basic lands only (Island 3, Mountain 2, Swamp 4).
- Three changes: Raphael, Fiendish Savior -> Dream Devourer; Reaper from the Abyss -> Doom Whisperer; Demonlord Belzenlok -> Spark Double.
- The previous artifact refinement/decklists/Be_lakor_the_Dark_Master_Final_2026-10-13.txt contains an unapproved historical Ardyn swap and must NOT be treated as current-cycle approved.

## Strategic rationale and costs
1. Raphael -> Dream Devourer: Raphael is a Devil (not Demon) and its anthem/recursion is less direct; Dream Devourer is a two-mana Demon and foretell staging engine for expensive spells. Dream Devourer has zero base power, so entering normally contributes zero damage to Be'lakor until pumped; foretell costs 2 mana to stage and cannot be cast that turn. Accept the tradeoff for curve and Demon density.
2. Reaper from the Abyss -> Doom Whisperer: **Reaper IS a Demon**, 6/6 for 3BBB with conditional morbid destroy at end step. Doom Whisperer is 6/6 Demon for 3BB, with flying, trample, pay 2 life to surveil 2, providing earlier same-power commander ETB damage and graveyard setup. Life payments are dangerous alongside Be'lakor and Vilis; surveil is optional.
3. Demonlord Belzenlok -> Spark Double: Belzenlok is a six-mana 6/6 Demon with potentially uncontrolled topdeck-exile card advantage and damage to controller. Spark Double is a four-mana non-Demon creature in hand, but as it enters copying Be'lakor becomes a nonlegendary Demon with a +1/+1 counter, triggers original Be'lakor's damage ability and its own ETB draw/life loss, and creates a second permanent Be'lakor damage engine. It is less effective if commander is absent.

## Commander and key rules red-team
- Be'lakor: 3UBR 6/5 Demon Noble; ETB draws X and loses X life where X is number of Demons controlled as trigger resolves (including Be'lakor). Whenever **another** Demon you control enters, **that entering Demon** deals damage equal to its power to any target. Original Be'lakor entering does not trigger its own Lord of Torment.
- Ancient Cellarspawn is a **Horror**, NOT Demon; retained as cost reducer and discounted-spell life-loss engine. It does not directly cause Be'lakor ETB damage.
- Abyssal Harvester is a 3-mana Demon and its token retains the original creature's Demon type only if the copied creature was a Demon; it adds Nightmare, and exiles other Nightmare tokens.
- Panharmonicon can double Be'lakor's own ETB draw AND life loss. Roaming Throne naming Demon doubles triggered abilities of Demon permanents. Molten Echoes and Reflections of Littjara create Demon copies and may involve legend-rule deaths, but ETB triggers still occur.
- Liliana's Contract requires four Demons with different names at upkeep; multiple copies of same named Demon are insufficient.
- Heartless Summoning gives creatures -1/-1, reduces Be'lakor's power-damage output, and can kill 1/1 Demon tokens. Retained because the deck's high creature costs justify reduction, but this is a real nonbo.
- Spark Double's copy is nonlegendary, so no legend-rule sacrifice of Be'lakor. Its own ETB triggers as the copied creature enters, and the original Be'lakor sees another Demon entering.
- Bloodletter of Aclazotz and Archfiend of Despair multiply life pressure, but timing and damage versus life loss must be respected.

## Research, legality, and performance
- Reviewed all 99 noncommander card copies (93 noncommander card-name rows, with basic-land multiplicities) and screened all 100 ranked candidates, with rationale and a high-impact shortlist. Key rejected alternatives: Varragoth (attack/boast timing), Blood Speaker (not Demon, delayed tutor), Ardyn (eight-mana non-Demon), Bloodcrusher (combat dependence), Razaketh (eight mana), Animate Dead (redundancy), Thassa/Closet (non-Demon setup), Nightmare Shepherd (1/1 copies lose Be'lakor damage).
- Project v8.1.4 inherited audit was stale relative to frozen baseline: baseline-only Abyssal Harvester, Ancient Cellarspawn, Heartless Summoning, Demonlord Belzenlok, Reaper from the Abyss. Legacy-only Kindred Dominance, Essence Flux, Herald's Horn, Quicksilver Amulet, Harvester of Souls. Do not silently swap lists. Archived card-level audit covers 88/93 noncommander distinct names; targeted current card-reference checks support the five missing baseline names and all three additions. This is not a claim of individual live Scryfall API checks on every card.
- Current reference pages confirm Be'lakor, Dream Devourer, Doom Whisperer, Spark Double, Reaper, Belzenlok, Ancient Cellarspawn and Abyssal Harvester as Commander-legal, and their relevant Oracle text. The 2026-10-12 banned/restricted announcement makes no Commander format changes. No unexpected ban or color-identity conflict found in baseline archive or additions. No project-specific exceptions needed.
- Lands: 36 of 99 noncommander copies. Hypergeometric, before mulligans or ramp: P(0–1 lands in opening 7) = 20.15%; P(0–1 lands in first 10 cards) = 6.29%. These are structural calculations, NOT multiplayer win-rate estimates. Lands and ramp preserved across swaps.
- No matched-start simulator or representative multiplayer testing conducted; no claimed empirical win-rate improvement. The zero-material-improvement stopping rule is qualitative: after 100 ranked-candidate review, no remaining candidate demonstrated a clear commander-specific gain without displacing higher-leverage slots. This does not prove global optimality.

## Evidence and sources
- https://mtg.wtf/card/40k/6/Be-lakor-the-Dark-Master
- https://mtg.wtf/card/pkhm/90p/Dream-Devourer
- https://mtg.wtf/card/grn/69/Doom-Whisperer
- https://mtg.wtf/card/war/68/Spark-Double
- https://mtg.wtf/card/j25/480/Reaper-from-the-Abyss
- https://mtg.wtf/card/dsc/16/Ancient-Cellarspawn
- https://mtg.wtf/card/fdn/54/Abyssal-Harvester
- https://mtg.wtf/card/dom/86/Demonlord-Belzenlok
- https://edhrec.com/commanders/belakor-the-dark-master/demons

## Approval request
The 100-card list and three changes are proposed for the user's **explicit approval**. Do not lock or advance to deck #8 until approval is granted. Preserve the six already approved decks.
