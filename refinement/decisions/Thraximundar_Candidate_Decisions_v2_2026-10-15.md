# Thraximundar — Candidate Decisions v2

Date: 2026-10-15
Cycle: `global-restart-2026-10-13`
Candidate SHA-256: `d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442`

Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## Commander-first blueprint

Thraximundar is a seven-mana hasty Zombie Assassin whose attack trigger forces the defending player to sacrifice a creature and whose growth trigger rewards creature sacrifices by any player. The optimized shell is therefore **sacrifice control / Zombie aristocrats / commander damage**. It should force sacrifices across the table, turn recursive bodies into resources, protect and accelerate Thraximundar, and use the Zombie subtype where it directly improves the commander's game plan.

Natural ceiling: **Power Bracket 4 — Optimized**. The shell supports deterministic sacrifice loops, but replacing the commander's engine with a generic Oracle/Consult cEDH package would violate the project mission.

## Final proposed delta

1. Force of Will -> Mana Vault
2. Demon's Disciple -> Winter, Tormented Loner
3. Damnation -> Vona's Hunger
4. Blasphemous Act -> Call to the Grave
5. Grave Titan -> Cultist of the Absolute
6. Deadly Dispute -> Diabolic Intent
7. Deathbringer Thoctar -> Yawgmoth, Thran Physician
8. Terminate -> Flare of Malice
9. Crumbling Necropolis -> Mana Confluence
10. Rogue's Passage -> Swamp
11. Swamp -> Cabal Coffers
12. Swamp -> Shizo, Death's Storehouse
13. Mountain -> Command Beacon

## Accepted changes

- **Mana Vault:** direct acceleration for a seven-mana commander. Force of Will had only eight other blue nonland cards in the inherited baseline as realistic pitch material, making it far less reliable here than in a blue-dense shell.
- **Winter, Tormented Loner:** converts one optional self-sacrifice into one creature sacrifice from every opponent. It is a cleaner multiplayer upgrade over Demon's Disciple while staying exactly on Thraximundar's axis.
- **Vona's Hunger:** instant-speed and one-sided. City's blessing scales the effect from one creature per opponent to half of every opposing creature board rounded up.
- **Call to the Grave:** repeatable upkeep sacrifice pressure that explicitly spares Zombies, including Thraximundar.
- **Cultist of the Absolute:** turns Thraximundar into a 9/9 flying/deathtouch, ward—pay 3 life haste attacker before counters, while its upkeep sacrifice requirement itself feeds the commander's growth trigger.
- **Diabolic Intent:** sacrifices a creature as an additional cost and converts that resource into exact access to the deck's best outlet, recursive body, payoff, protection piece, or Grave Pact engine.
- **Yawgmoth, Thran Physician:** promoted during the v2 red-team. It is cheaper and more immediately useful than Deathbringer Thoctar: repeatable sacrifice outlet, card draw, creature suppression, and proliferate for Thraximundar's +1/+1 counters.
- **Flare of Malice:** promoted during the v2 red-team. Its alternate cost can itself trigger Thraximundar, and the spell then forces every opponent to sacrifice their highest-mana-value creature or planeswalker. It is substantially more commander-specific than Terminate while remaining high-grade interaction.
- **Mana Confluence:** untapped unconditional U/B/R fixing over Crumbling Necropolis.
- **Swamp over Rogue's Passage:** Cultist and Shizo already give cheaper evasion. The basic improves black reliability and the Coffers package.
- **Cabal Coffers:** high-ceiling mana engine for the expensive commander; v2 has ten naturally Swamp-typed lands before Urborg effects.
- **Shizo, Death's Storehouse:** black-producing land with a one-mana fear activation for the legendary commander.
- **Command Beacon:** directly addresses the failure mode of repeated removal on a seven-mana commander by bypassing accumulated command-zone tax on the next hand-cast.

## Cuts

- **Force of Will:** raw power is high, but the blue pitch pool is too thin and the seven-mana commander benefits more from fast mana.
- **Demon's Disciple:** on-axis but lower multiplayer output than Winter.
- **Damnation:** symmetric destruction does not trigger Thraximundar; Vona's Hunger does and is one-sided.
- **Blasphemous Act:** generic destruction. Toxic Deluge remains as emergency mass removal, while Call to the Grave is repeatable and commander-specific.
- **Grave Titan:** strong generic value but less important than direct commander evasion/protection and sacrifice synergy.
- **Deadly Dispute:** efficient, but the list retains Black Market Connections, Braids, Rhystic Study, Skullclamp, Liliana, Wilhelt, and Yawgmoth as draw engines. Diabolic Intent turns the sacrifice into exact selection.
- **Deathbringer Thoctar:** synergistic Zombie payoff, but six mana is inefficient relative to Yawgmoth's four-mana sacrifice/draw/removal engine.
- **Terminate:** excellent selected spot removal, but Flare's free mode and table-wide sacrifice pressure produce more value in this specific commander shell.
- **Crumbling Necropolis:** guaranteed tapped land.
- **Rogue's Passage:** four-mana evasion activation is too expensive once Cultist and Shizo are present.
- **Swamp x2 / Mountain x1:** converted into Coffers, Shizo, and Command Beacon while maintaining 36 lands; Rogue's Passage -> Swamp restores one basic Swamp, leaving five total.

## Retained commander-specific core

The candidate deliberately retains Accursed Marauder, Fleshbag Marauder, Innocent Blood, Plaguecrafter, Sheoldred's Edict, Necrotic Hex, Archfiend of Depravity, Grave Pact, Dictate of Erebos, Tergrid, Mayhem Devil, Carrion Feeder, Goblin Bombardment, Altar of Dementia, Ashnod's Altar, Phyrexian Altar, Warren Soultrader, Gravecrawler, Reassembling Skeleton, Rooftop Storm, Wilhelt, Diregraf Captain, Blood Artist, Zulaport Cutthroat, Mahadi, Pitiless Plunderer, Grimgrin, Sheoldred, Braids, Liliana, and Skullclamp because they either force sacrifices, exploit deaths/sacrifices, recur sacrificial bodies, create deterministic loops, or reinforce Thraximundar's Zombie identity.

## Material challengers rejected after v2 red-team

- **Ophiomancer:** excellent repeatable fodder, especially with Grave Pact/Dictate. Reassembling Skeleton is retained because it is a reusable nontoken black body and participates in deterministic Pitiless Plunderer loops with both Phyrexian Altar and Ashnod's Altar. Fodder production is not the current bottleneck.
- **Lagomos, Hand of Hatred:** on-theme and capable of tutoring after five deaths, but its once-per-own-turn Elemental is less productive than the retained recursive engines; the conditional tutor does not displace Demonic Tutor, Vampiric Tutor, or Diabolic Intent.
- **Soul Shatter:** very strong one-sided edict, but Vona's Hunger and Flare of Malice scale better across multiplayer boards and the list already has deep edict density.
- **Make an Example:** powerful mass sacrifice, but Vona's Hunger is cheaper, instant-speed, and can produce comparable board compression with city's blessing.
- **Blasphemous Edict:** explosive when thirteen creatures are present, but it is symmetric and can force Thraximundar itself to be sacrificed when your own board is below thirteen creatures.
- **Tarrian's Soulcleaver:** useful commander-growth equipment, but Cultist provides immediate evasion, deathtouch, ward, +3/+3, and a sacrifice trigger with no growth setup.
- **Geralf, Visionary Stitcher:** useful Zombie evasion/outlet card, but Yawgmoth and the existing free outlets are stronger; Cultist and Shizo already solve commander evasion.
- **Butcher of Malakir:** seven mana and redundant with Grave Pact / Dictate of Erebos.
- **Gisa, Glorious Resurrector:** strong attrition, but its exile replacement interferes with the deck's normal death/graveyard ecosystem and is less direct than retained sacrifice engines.
- **The Ozolith:** good counter insurance, but narrower than protection, tax mitigation, fast mana, or repeatable sacrifice engines.
- **Additional Zombie lords:** rejected because Zombie tribal is a supporting subengine, not the deck's primary identity.
- **Additional generic tutors / Oracle-Consult packages:** rejected because they increase generic Grixis combo density without making Thraximundar more necessary.
- **Additional fetchland/checkland substitutions:** reviewed; the three retained checklands have ample basic-land-type support and no change produced a material commander-specific improvement.

## Combo / rules closeout

- Gravecrawler + Phyrexian Altar + another Zombie: unbounded sacrifice/cast/death loop.
- Rooftop Storm + Gravecrawler + Carrion Feeder + another Zombie: unbounded zero-mana recursion/sacrifice loop.
- Pitiless Plunderer + Gravecrawler + a free sacrifice outlet + another Zombie: Treasure pays the next Gravecrawler cast.
- Warren Soultrader + Gravecrawler + another Zombie + Blood Artist/Zulaport Cutthroat: Treasure pays the recast and drain recovers the life payment.
- Reassembling Skeleton + Pitiless Plunderer + Phyrexian Altar: altar mana plus Treasure pays Skeleton's {1}{B} return cost, creating an unbounded sacrifice/death loop.
- Reassembling Skeleton + Pitiless Plunderer + Ashnod's Altar: each cycle leaves one net colorless mana after paying Skeleton's return cost, producing unbounded colorless mana plus sacrifice/death triggers.
- Thraximundar sees any creature sacrifice by any player, including sacrifices to Diabolic Intent, Yawgmoth, Flare's alternate cost, Cultist's upkeep ability, Vona's Hunger, Call to the Grave, and its own attack trigger.

## Whole-list audit and source discrepancy

All **99/99 noncommander baseline copies** were adjudicated: **86 KEEP / 13 CUT** in the gross one-for-one swap ledger.

The authoritative FINAL baseline contains Deadly Dispute, Deathbringer Thoctar, Demon's Disciple, Innocent Blood, and Necrotic Hex where inherited `deck_card_audit.csv` instead contains Counterspell, Soul Shatter, Undead Warchief, Village Rites, and Vona's Hunger. FINAL controls. Vona's Hunger and other suppressed candidates were manually restored for consideration.

## Closeout

- **100 cards / 93 distinct names / 36 lands**
- Repeated names: **Island x3 / Mountain x2 / Swamp x5 only**
- Singleton: **PASS**
- U/B/R color identity: **PASS**
- Official Commander legality: **PASS**
- Project exceptions: **none**
- Candidate exhaustion / red-team: **ZERO NEW MATERIAL IMPROVEMENTS after v2**
- Natural ceiling: **Power Bracket 4 — Optimized**
- Proposed Archidekt tags: **Sacrifice / Zombie Aristocrats / Commander Damage**

The candidate remains unlocked until explicit user approval of SHA-256 `d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442`.
