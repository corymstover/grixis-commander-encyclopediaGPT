# Thraximundar — approval-ready verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #59 of 62

## Result

**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**

- Exact candidate SHA-256: `5adcc8b9f3b0bff9eae89e30b4c7a14970242363a1964265e80c52d8987e884c`
- Cards: **100**
- Distinct names: **94**
- Lands: **36**
- Repeats: **Island x3 / Mountain x2 / Swamp x4 only**
- Singleton: **PASS**
- Commander color identity: **U/B/R — PASS**
- Authoritative FINAL CSV/TXT reconciliation: **PASS**
- Current Oracle / card identity gate: **PASS**
- Official Commander legality: **PASS**
- Project exceptions: **none**
- Rules / combo interaction attestation: **PASS**
- Whole-list audit: **99/99 noncommander copies adjudicated; 89 KEEP / 10 CUT**
- Candidate exhaustion / adversarial red-team: **ZERO NEW MATERIAL IMPROVEMENTS**
- Natural ceiling: **Power Bracket 4 — Optimized**
- Proposed Archidekt tags: **Sacrifice / Zombie Aristocrats / Commander Damage**

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

## Commander-first rules findings

- Thraximundar is a 6/6 Zombie Assassin with haste. Its attack trigger makes the defending player sacrifice a creature, and its last ability triggers whenever any player sacrifices a creature. The defending-player sacrifice resolves during declare attackers before blockers.
- Call to the Grave forces one non-Zombie sacrifice on each player's upkeep. Thraximundar is a Zombie, so it is never a legal creature to sacrifice to Call to the Grave's upkeep trigger.
- Winter, Tormented Loner may sacrifice one of your creatures or planeswalkers on entry; when you do, each opponent sacrifices a creature. Those creature sacrifices all independently trigger Thraximundar.
- Vona's Hunger makes each opponent sacrifice a creature and, with the city's blessing, instead makes each opponent sacrifice half their creatures rounded up.
- Cultist of the Absolute gives commander creatures you own +3/+3, flying, deathtouch, ward—pay 3 life, and an upkeep sacrifice requirement. Thraximundar therefore begins combat as a 9/9 evasive threat before sacrifice counters; the upkeep sacrifice can also trigger Thraximundar.
- Shizo, Death's Storehouse grants fear to a target legendary creature for {B}, {T}, directly supporting commander-damage pressure.
- Command Beacon can move Thraximundar from the command zone to hand, allowing a later hand-cast without accumulated commander tax.

## Combo audit

- **Gravecrawler + Phyrexian Altar + another Zombie:** sacrifice Gravecrawler for black mana and use that mana to recast it. This is an unbounded cast/death/sacrifice loop; Blood Artist, Zulaport Cutthroat, Diregraf Captain, Goblin Bombardment, or another retained payoff converts it into a win.
- **Gravecrawler + Rooftop Storm + Carrion Feeder + another Zombie:** Rooftop Storm makes Gravecrawler cost {0}; Carrion Feeder repeatedly sacrifices it, creating an unbounded cast/death/sacrifice loop.
- **Gravecrawler + Pitiless Plunderer + free sacrifice outlet + another Zombie:** Gravecrawler's death makes the Treasure needed to pay for the next cast, creating an unbounded loop with a payoff.
- **Gravecrawler + Warren Soultrader + another Zombie + Blood Artist or Zulaport Cutthroat:** Soultrader costs 1 life and creates the Treasure used to recast Gravecrawler; the drain payoff restores the life while damaging opponents, making the loop deterministic with the payoff present.

No combo is asserted without the required Zombie condition, mana/life loop, sacrifice outlet, or payoff.

## Mana / curve findings

Land count remains **36**. Mana Confluence replaces an always-tapped land; Mana Vault materially accelerates the seven-mana commander; Shizo remains a black source while adding evasion; and Command Beacon directly mitigates commander tax. Cabal Coffers has nine naturally Swamp-typed lands available before Urborg is considered: four basic Swamps plus Badlands, Blood Crypt, Underground Sea, Watery Grave, and Xander's Lounge. Urborg, Tomb of Yawgmoth raises that ceiling further.

The six removed nonland cards have nominal mana values 5, 3, 4, 9, 6, and 2 versus 1, 3, 3, 5, 1, and 2 for their replacements. Nominal top-end pressure is therefore materially reduced, while recognizing that Blasphemous Act commonly costs less than nine in actual games.

## Source reconciliation

The October 12 FINAL CSV/TXT exports are authoritative and reconcile at exactly 100 cards. The inherited `deck_card_audit.csv` is stale for five Thraximundar slots: FINAL contains Deadly Dispute, Deathbringer Thoctar, Demon's Disciple, Innocent Blood, and Necrotic Hex, while the inherited audit instead contains Counterspell, Soul Shatter, Undead Warchief, Village Rites, and Vona's Hunger. FINAL membership controls.

The retained FINAL-only Deathbringer Thoctar, Innocent Blood, and Necrotic Hex were separately refreshed against current public card data. Vona's Hunger was manually restored to candidate consideration rather than being suppressed by stale audit membership.

## Current legality / Oracle checkpoint

The current Wizards Commander banned list was checked on 2026-10-15. None of the candidate cards are on the Commander banned list. Current public card records were refreshed for every candidate card absent from the inherited Thraximundar audit, including newly released Winter, Tormented Loner (Reality Fracture, released 2026-10-02), which is currently Commander-legal.

Primary public checkpoints:
- https://magic.wizards.com/en/banned-restricted-list
- https://mtg.wtf/card/fra/240/Winter-Tormented-Loner
- https://mtg.wtf/card/prix/90s/Vonas-Hunger
- https://mtg.wtf/card/m12/85/Call-to-the-Grave
- https://mtg.wtf/card/pclb/123s/Cultist-of-the-Absolute
- https://mtg.wtf/card/fca/34/Diabolic-Intent
- https://mtg.wtf/card/2x2/394/Mana-Vault
- https://mtg.wtf/card/jou/163/Mana-Confluence
- https://mtg.wtf/card?q=%21cabal+coffers
- https://mtg.wtf/card/dmc/233/Shizo-Deaths-Storehouse
- https://mtg.wtf/card/c15/56/Command-Beacon
- https://mtg.wtf/card/jmp/244/Innocent-Blood
- https://mtg.wtf/card/cmr/137/Necrotic-Hex

## Approval boundary

This artifact is **not** an approval record and does **not** lock the deck. Lock only after explicit user approval of exact SHA-256 `5adcc8b9f3b0bff9eae89e30b4c7a14970242363a1964265e80c52d8987e884c`.
