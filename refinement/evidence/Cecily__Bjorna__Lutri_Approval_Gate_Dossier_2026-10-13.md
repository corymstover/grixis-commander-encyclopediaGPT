# Deck #8 — Bjorna // Cecily + Lutri — Approval Gate Dossier

**Current-cycle status:** APPROVAL_REQUESTED, NOT APPROVED, NOT LOCKED. All prior seven approved decks preserved.

## Source and deck count
Frozen TXT: GrixisFINALTXT60--2026.zip / Cecily__Bjorna__Lutri.txt. Source-member SHA-256: 4e10f9fcc2e8ec230cf7627d9f32eb4693b45c1af7a5a104d14f878e39f99a2f.

The frozen TXT has 100 distinct name rows and **101 physical cards**: 2 commanders + 98 library cards (including one extra Island) + 1 Lutri companion outside the game. This is **exactly 100 in the Commander deck**, plus companion outside the deck; the companion must not be incorrectly counted as a 101st deck card. Commander pair is Bjorna, Nightfall Alchemist and Cecily, Haunted Mage (Friends forever). Main-deck singleton compliance passes, only Island x2. Companion's starting-deck restriction (nonland names unique) passes. All 33 lands preserved.

## One recommended change
- CUT Reckless Fireweaver
- ADD Robe of the Archmagi

Reckless Fireweaver converts artifact-token arrivals to table-wide damage but is a secondary payoff, not a direct way to attain Cecily's 11-card attack trigger. Robe of the Archmagi costs 2U and equips **Cecily (Human Wizard)** for 1 mana, giving draw equal to combat damage dealt to a player. It also equips non-Wizards for 4. Cecily triggers **on attack**, not combat damage; Robe's combat-damage draw happens **after** Cecily's attack trigger resolves and cannot make the 11-card condition true on that same attack. It builds hand size for subsequent attacks. Robe does not make Cecily unblockable and is vulnerable to artifact removal. Cutting Fireweaver reduces passive token-burn output; Academy Manufactor, Sai, Third Path Iconoclast, Oni-Cult Anvil, Bjorna sacrifice fodder and Treasure synergies remain.

## Commander rules and interactions
- **Bjorna** is a 1/3 Human, not Wizard, with {T}, sacrifice an artifact as cost to deal 1 damage to a creature and goad it. Target must be a creature; it does not target players. Academy Manufactor increases Treasure/Clue/Food resources for sacrifice. Robe does not have the cheap Wizard equip rate for Bjorna.
- **Cecily** is a Human Wizard with maximum hand size 11. On attack she draws one card, loses one life, then checks **11 or more cards in hand** to allow casting an instant or sorcery **from hand** without paying its mana cost. The draw happens before checking the threshold. An eleven-card maximum is not a requirement to discard immediately; normal cleanup rules apply.
- Cecily free-casts **Apex of Power from hand**; Apex's own 'if cast from your hand' clause is satisfied even though mana cost is waived, producing ten mana of one color. 'Cast without paying its mana cost' disallows alternate casting costs but allows additional costs.
- Lutri's companion condition checks **starting deck**, not the outside-the-game companion. Lutri is banned **as a companion** in official Commander, but expressly authorized as a project exception. To put Lutri from outside the game into hand, pay {3} at sorcery speed; then pay its normal mana cost to cast it. Its ETB spell-copy ability requires Lutri to have been cast, and a target instant/sorcery spell you control on stack.
- Trade Secrets and Yawgmoth's Bargain are officially banned in Commander but are explicit project-authorized exceptions for this deck. Do not describe the deck as officially legal without qualifications.
- Harmonic Prodigy can copy relevant Wizard/Shaman triggered abilities, including Cecily's attack trigger if it is a Wizard triggered ability; additional Cecily attack triggers resolve individually and may produce multiple free casts if hand thresholds are met.
- The One Ring, Trade Secrets, Bargain, Windfall, Wheels, and Rhystic Study help build the eleven-card threshold; Wheel effects also replace hand and can reduce it. The deck is not just generic spellstorm: its commander pair's artifact-goad control and hand-size attack engine remain the strategic center.

## Candidate exhaustion and review
All 98 noncommander main-deck card copies, plus the one outside-deck companion, reviewed; all 100 ranked candidates screened. Notable alternatives considered: Whispersilk Cloak (attack trigger needs no combat damage); Wizard Class (hand-size support, but slower to draw than the Robe's successful connection); Double Vision, Mizzix's Mastery, Thousand-Year Storm (high synergy but compete for expensive spell and payoff slots); Ponder, Preordain, Flame of Anor, An Offer You Can't Refuse (efficient but lack a decisive weakest cut). No other candidate demonstrated a clearly stronger slot-specific upgrade under identity-first constraints.

## Structural / legal verification
- Proposed list: 100 deck cards including 2 commanders, 98 library cards; plus 1 outside-deck companion.
- 33 lands; only basic Island repeated (x2).
- Color identity UBR: inherited v8.1.4 deck audit passes all 100 original distinct names, including companion, with exactly the three authorized official-legality exceptions. Robe of the Archmagi is blue and currently Commander legal.
- Official Commander banned list and October 12, 2026 WotC announcement consulted. No unexpected format ban found. The current legality conclusion is based on archived per-card audit + targeted current check, not an individual live Scryfall API query for every card.
- Proposed decklist SHA-256 (UTF-8 LF newline): 553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28.
- Hypergeometric 33-land-only consistency (98-card library), ignoring mulligans and mana rocks: P(0–1 land in opening 7) 24.74%; P(0–1 land in first 10 cards) 8.81%. 33 lands is relatively lean, but the deck retains a dense two-mana artifact acceleration package and spell-based Treasure generation.
- No controlled multiplayer win-rate tests performed; no empirical improvement claim. The one-swap proposal is a commander-first qualitative recommendation with acknowledged combat-connectivity risk.

## Source links
- https://www.mtg.wtf/card/clb/91/Robe-of-the-Archmagi
- https://www.mtg.wtf/card?q=e%3Asld+subset%3A%22Stranger+Things%22
- https://mtgcommander.net/index.php/banned-list/
- https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026

## Approval gate
Request explicit approval for the single Reckless Fireweaver -> Robe of the Archmagi change and resulting 100-card main-deck list with outside-deck Lutri companion. **Do not lock without user approval.**
