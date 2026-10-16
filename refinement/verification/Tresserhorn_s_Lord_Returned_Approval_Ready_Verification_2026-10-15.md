# Tresserhorn's Lord, Returned — Approval-Ready Verification — 2026-10-15

## State and baseline
- Cycle: `global-restart-2026-10-13`.
- Tracker position: index 59 / deck 60 of 62.
- Authoritative frozen baseline: `GrixisFINALTXT60--2026.zip::Tresserhorn_s_Lord__Returned.txt`.
- Baseline: 100 cards; 34 lands; CSV/TXT reconciliation PASS in supplied project data.
- GitHub state is authoritative for current-cycle locks. Thraximundar is already APPROVED/LOCKED even though the master tracker row is stale, making Tresserhorn's Lord, Returned the next unlocked deck.

## Commander blueprint
Current Oracle text: Tresserhorn's Lord, Returned {2}{U}{B}{R}, legendary Zombie Noble, 10/4, trample, indestructible. On entry, sacrifice him unless you sacrifice three creatures, pay 3 life, and have target opponent draw three cards. Whenever you sacrifice a creature, draw a card.

Commander-first plan: deploy cheap/repeatable fodder, resolve Tresserhorn while paying the three-creature ETB requirement, convert every later sacrifice into cards, and close through aristocrats/recursive loops or the commander's 10-power combat package. The deck is intentionally distinct from the encyclopedia's Lord of Tresserhorn deck: Returned wants the ETB sacrifices; it does not suppress them with Torpor Orb/Karn-style effects.

Natural ceiling: **Power Bracket 4 — Optimized**. The commander enables deterministic sacrifice loops and very high card throughput, but a five-mana commander that requires three bodies and gives an opponent three cards is not a realistic top-tier cEDH commander.

Suggested Archidekt tags: **Aristocrats / Sacrifice / Tokens**.

## Whole-list audit
- 99/99 noncommander copies adjudicated in `Tresserhorn_s_Lord_Returned_Whole_List_Audit_2026-10-15.csv`.
- Result: 80 KEEP / 19 CUT.
- 19 one-for-one additions; candidate remains exactly 100 cards.
- Project top-100 candidate list fully adjudicated; meaningful outside-ranked challengers also reviewed.
- Second adversarial pass: ZERO NEW MATERIAL IMPROVEMENTS.

## Final proposed changes
- Arcane Denial -> Stubborn Denial
- Counterspell -> Not of This World
- Dictate of Erebos -> Diabolic Intent
- Grim Haruspex -> Yawgmoth, Thran Physician
- Izzet Signet -> Nightscape Familiar
- Liliana, Dreadhorde General -> Weaponcraft Enthusiast
- Pawn of Ulamog -> Plumb the Forbidden
- Psychosis Crawler -> My Precious // Allure of Power
- Reassembling Skeleton -> Vampiric Tutor
- Syr Konrad, the Grim -> Bastion of Remembrance
- Toxic Deluge -> Blasphemous Edict
- Dragonskull Summit -> Badlands
- Drowned Catacomb -> Underground Sea
- Shipwreck Marsh -> High Market
- Stormcarved Coast -> Shizo, Death's Storehouse
- Sulfur Falls -> Volcanic Island
- Mountain -> Kher Keep
- Swamp -> Cavern of Souls
- Swamp -> Boggart Trawler // Boggart Bog

## Rules / Oracle red-team
- Wizards' 2026-08-03 Mystery Booster Commander Edition release notes make new collector numbers 1–60 legal in Commander. Tresserhorn's Lord, Returned is collector 52, so the old project future-release exception is stale and no longer required.
- The same release notes state that if Tresserhorn is sacrificed, including to its own ETB trigger, its sacrifice-draw ability triggers; if it and other creatures are sacrificed simultaneously, it triggers for each of them.
- Paying the normal ETB requirement by sacrificing three creatures therefore creates three Tresserhorn draw triggers if Tresserhorn is on the battlefield when those sacrifices occur.
- Gravecrawler + Phyrexian Altar: Tresserhorn is a Zombie, so with Tresserhorn on the battlefield Gravecrawler can be cast from the graveyard; sacrificing Gravecrawler to the Altar makes {B} and triggers a draw, paying its recast cost. A drain payoff converts the repeatable loop into a kill.
- Gravecrawler + Pitiless Plunderer + free sacrifice outlet likewise refunds the {B} recast through Treasure and repeatedly triggers Tresserhorn.
- Warren Soultrader + Gravecrawler requires a life-neutralizing payoff (Blood Artist/Zulaport/Bastion) for an effectively unlimited loop; Marionette Apprentice alone drains opponents but does not refund Soultrader's life payment.
- The Locust God + Tresserhorn + a free sacrifice outlet loops once a creature sacrifice/draw seeds the process: draw creates an Insect, sacrificing it draws and creates the next Insect. A damage/drain outlet converts it to a win; optional sacrifice actions can be stopped to avoid self-decking.
- Plumb the Forbidden with N creatures sacrificed generates N Tresserhorn triggers plus N+1 spell/copy draws: 2N+1 cards total, with N+1 life lost from Plumb resolutions.
- Nightscape Familiar reduces only generic mana; it changes Tresserhorn from {2}{U}{B}{R} to {1}{U}{B}{R}, not lower.
- Not of This World costs {0} when countering a spell/ability that targets the 10-power commander; it does not protect against untargeted sweepers or sacrifice effects.
- My Precious grants hexproof and unblockable after the Adventure is cast/resolved and later cast as the Equipment; Allure of Power's creature sacrifice is an additional cost and triggers Tresserhorn when the commander is present.
- Blasphemous Edict's chosen creatures are sacrificed simultaneously. If fewer than thirteen are controlled, all are sacrificed. This bypasses indestructible; keep Tresserhorn out of the chosen set when enough other fodder exists.
- Infantry Shield on a 10-power Tresserhorn mobilizes 10; the resulting Warriors' delayed sacrifices create one commander draw trigger per sacrificed creature if Tresserhorn remains on the battlefield.
- Wand of Orcus plus Tresserhorn's trample/deathtouch lets only lethal damage be assigned to blockers before excess trample damage, maximizing Zombie creation on player damage.

## Legality / identity
- Commander color identity: U/B/R.
- Candidate additions are black, blue, red, colorless, or U/B/R lands only; no off-identity symbols were introduced.
- Current Wizards Commander banned list checked 2026-10-15; no candidate card appears on it.
- Current official release-note legality supersedes the stale project future-release exception for Tresserhorn's Lord, Returned.
- No project exception is required for this candidate.

## Structural verification
- Total cards: **100**.
- Commander copies: **1**.
- Distinct card-name rows: **93**.
- Repeated names: **Island x3, Mountain x3, Swamp x4 only**.
- Nonbasic singleton compliance: **PASS**.
- Land-capable slots: **34** (33 front-face lands + Boggart Trawler // Boggart Bog).
- U/B/R color identity: **PASS**.
- Official Commander legality: **PASS**.
- Relevant rules/combo review: **PASS**.
- Candidate exhaustion: **PASS**.
- Commander-necessity/differentiation: **PASS**.
- Red-team pass: **PASS**.
- Zero-new-material-improvement closure: **PASS**.

## SHA binding
Approval-candidate SHA-256 (exact UTF-8 bytes, including final newline):
`8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8`

## Status
**APPROVAL_READY — not yet approved or locked.** Explicit user approval is still required before state/tracker lock updates.
