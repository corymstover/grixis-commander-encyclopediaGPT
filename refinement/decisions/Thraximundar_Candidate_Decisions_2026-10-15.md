# Thraximundar — Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `5adcc8b9f3b0bff9eae89e30b4c7a14970242363a1964265e80c52d8987e884c`

Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## Commander-first blueprint

Thraximundar is a seven-mana hasty Zombie Assassin whose attack trigger forces a sacrifice and whose growth trigger rewards every creature sacrifice by any player. The optimized shell is therefore sacrifice / Zombie aristocrats with commander-damage pressure, not generic Grixis control. It forces sacrifices across the table, turns recursive bodies into resources, and retains compact sacrifice loops that arise naturally from the same engine.

Natural ceiling: **Power Bracket 4 — Optimized**. The deck has deterministic combo support, but converting a seven-mana sacrifice commander into a generic Oracle/Consult cEDH shell would violate the commander-first objective.

## Final proposed delta

1. Force of Will -> Mana Vault
2. Demon's Disciple -> Winter, Tormented Loner
3. Damnation -> Vona's Hunger
4. Blasphemous Act -> Call to the Grave
5. Grave Titan -> Cultist of the Absolute
6. Deadly Dispute -> Diabolic Intent
7. Crumbling Necropolis -> Mana Confluence
8. Swamp -> Cabal Coffers
9. Swamp -> Shizo, Death's Storehouse
10. Mountain -> Command Beacon

## Accepted changes

- **Mana Vault:** Thraximundar costs seven. The baseline had only eight other blue nonland cards available to pitch to Force of Will, making Force materially less reliable than in a blue-dense shell. Mana Vault is direct commander acceleration.
- **Winter, Tormented Loner:** an on-axis upgrade to Demon's Disciple. Its optional self-sacrifice then makes every opponent sacrifice a creature, creating multiple Thraximundar triggers.
- **Vona's Hunger:** instant-speed, one-sided sacrifice. With the city's blessing it scales to half of each opponent's creature board rounded up.
- **Call to the Grave:** one of the highest-lift local candidates and a literal commander engine. It forces a sacrifice during each player's upkeep and excludes Zombies, so Thraximundar is never a legal choice for that trigger.
- **Cultist of the Absolute:** makes Thraximundar a 9/9 flying, deathtouch, ward—pay 3 life threat before sacrifice counters. Its upkeep sacrifice also triggers Thraximundar when a creature is sacrificed.
- **Diabolic Intent:** preserves a sacrifice action while turning the slot into exact access to the missing outlet, recursive creature, payoff, protection, or Grave Pact engine.
- **Mana Confluence:** untapped unconditional U/B/R fixing over Crumbling Necropolis.
- **Cabal Coffers:** high-ceiling mana engine for a seven-mana commander, supported by four basic Swamps, five naturally Swamp-typed dual/tri lands, and Urborg.
- **Shizo, Death's Storehouse:** black-producing functional land that gives the legendary commander fear for commander-damage pressure.
- **Command Beacon:** directly mitigates accumulated commander tax by moving Thraximundar to hand.

## Cuts

- **Force of Will:** generically excellent but poorly supported by the deck's thin blue pitch pool; Mana Vault more reliably advances the deck's core seven-mana commander plan.
- **Demon's Disciple:** on-plan, but Winter creates a stronger asymmetrical sacrifice pattern.
- **Damnation:** clean reset, but Vona's Hunger is asymmetric and produces commander growth triggers.
- **Blasphemous Act:** powerful generic sweeper; Toxic Deluge remains, while Call to the Grave is substantially more commander-specific and repeatable.
- **Grave Titan:** strong generic top-end value, but Cultist more directly converts Thraximundar into a protected/evasive commander-damage clock.
- **Deadly Dispute:** efficient, but the remaining draw suite is substantial; Diabolic Intent converts the same sacrificial resource into exact engine selection.
- **Crumbling Necropolis:** guaranteed tapped land.
- **Swamp x2 / Mountain x1:** converted into Coffers, Shizo, and Command Beacon while keeping 36 lands.

## Retained commander-specific core

Accursed Marauder, Fleshbag Marauder, Innocent Blood, Plaguecrafter, Sheoldred's Edict, Necrotic Hex, Archfiend of Depravity, Grave Pact, Dictate of Erebos, Tergrid, Mayhem Devil, Deathbringer Thoctar, Carrion Feeder, Goblin Bombardment, Altar of Dementia, Ashnod's Altar, Phyrexian Altar, Warren Soultrader, Gravecrawler, Reassembling Skeleton, Rooftop Storm, Wilhelt, Diregraf Captain, Blood Artist, Zulaport Cutthroat, Mahadi, Pitiless Plunderer, Grimgrin, and Sheoldred remain because they create sacrifices, exploit deaths/sacrifices, recur sacrificial bodies, or reinforce the Zombie subengine.

## Material challengers rejected

- **Soul Shatter:** manually reconsidered because stale audit membership suppressed it. Vona's Hunger is more explosive in multiplayer and scales harder with city's blessing.
- **Tarrian's Soulcleaver:** excellent growth equipment, but Cultist supplies immediate +3/+3, flying, deathtouch, ward, and a sacrifice trigger without setup counters.
- **Geralf, Visionary Stitcher:** useful Zombie flying/outlet piece, but outlet density is already high and Cultist/Shizo solve commander evasion more directly.
- **Butcher of Malakir:** seven mana and redundant with Grave Pact / Dictate.
- **Gisa, Glorious Resurrector:** strong attrition, but its exile replacement pulls against the deck's death/recursion web.
- **Legate Lanius:** on-plan but less efficient than Winter and Vona's Hunger after the existing edict density is considered.
- **Viscera Seer / High Market:** more outlets are not the current bottleneck.
- **The Ozolith:** counter preservation is narrower than direct protection, evasion, acceleration, or tax mitigation.
- **Nightscape Familiar / Wayfarer's Bauble / Burnished Hart:** useful ramp, but Mana Vault plus the existing signet/talisman/ritual package is stronger at this ceiling.
- **Undead Warchief / Death Baron / Endless Ranks of the Dead:** Zombie tribal is secondary; this is sacrifice-first.
- **Thassa's Oracle / Demonic Consultation:** rejected as forced cEDH homogenization that would reduce the commander's necessity.

## Combo / rules closeout

- **Gravecrawler + Phyrexian Altar + another Zombie:** unbounded sacrifice/cast/death loop because the Altar produces the black mana needed to recast Gravecrawler.
- **Rooftop Storm + Gravecrawler + Carrion Feeder + another Zombie:** unbounded zero-mana recursion/sacrifice loop.
- **Pitiless Plunderer + Gravecrawler + free sacrifice outlet + another Zombie:** each death supplies the Treasure needed to recast Gravecrawler.
- **Warren Soultrader + Gravecrawler + another Zombie + Blood Artist or Zulaport Cutthroat:** Soultrader's 1-life cost is restored by the drain payoff while the Treasure pays for the next Gravecrawler cast, creating a deterministic win.
- Thraximundar sees sacrifices by any player, including sacrifices used to cast Diabolic Intent, activate outlets, pay Cultist's upkeep trigger, resolve Vona's Hunger / Call to the Grave, or satisfy its own attack trigger.

## Whole-list audit and source discrepancy

All **99/99 noncommander baseline copies** were adjudicated: **89 KEEP / 10 CUT**.

The authoritative FINAL baseline contains Deadly Dispute, Deathbringer Thoctar, Demon's Disciple, Innocent Blood, and Necrotic Hex where the inherited `deck_card_audit.csv` instead contains Counterspell, Soul Shatter, Undead Warchief, Village Rites, and Vona's Hunger. FINAL controls. Stale membership was not allowed to overwrite the current list, and the suppressed Vona's Hunger / Soul Shatter candidates were manually reconsidered.

## Closeout

- **100 cards / 94 distinct names / 36 lands**
- Singleton: **PASS — basics only repeated**
- U/B/R color identity: **PASS**
- Official Commander legality: **PASS**
- Project exceptions: **none**
- Candidate exhaustion / red-team: **ZERO NEW MATERIAL IMPROVEMENTS**
- Natural ceiling: **Power Bracket 4 — Optimized**
- Proposed Archidekt tags: **Sacrifice / Zombie Aristocrats / Commander Damage**

The candidate remains unlocked until explicit user approval of SHA-256 `5adcc8b9f3b0bff9eae89e30b4c7a14970242363a1964265e80c52d8987e884c`.
