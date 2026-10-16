# Thraximundar — approval-ready verification v2

Date: 2026-10-15
Cycle: `global-restart-2026-10-13`
Deck: #59 of 62

## Result

**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**

- Exact candidate SHA-256: `d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442`
- Cards: **100**
- Distinct names: **93**
- Lands: **36**
- Repeats: **Island x3 / Mountain x2 / Swamp x5 only**
- Singleton: **PASS**
- Commander color identity: **U/B/R — PASS**
- Authoritative FINAL CSV/TXT reconciliation: **PASS**
- Current Oracle / card identity gate: **PASS**
- Official Commander legality: **PASS**
- Project exceptions: **none**
- Rules / combo interaction attestation: **PASS**
- Whole-list audit: **99/99 noncommander baseline copies adjudicated; 86 KEEP / 13 CUT**
- Candidate exhaustion / adversarial red-team: **ZERO NEW MATERIAL IMPROVEMENTS after v2 red-team**
- Natural ceiling: **Power Bracket 4 — Optimized**
- Proposed Archidekt tags: **Sacrifice / Zombie Aristocrats / Commander Damage**

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

## Commander-first rules findings

- Thraximundar is a 6/6 Zombie Assassin with haste. Its attack trigger makes the defending player sacrifice a creature, and its last ability triggers whenever **any player** sacrifices a creature. The attack-trigger sacrifice resolves during declare attackers before blockers.
- **Winter, Tormented Loner** may sacrifice one of your creatures or planeswalkers on entry; when you do, each opponent sacrifices a creature. Every creature actually sacrificed this way is independently seen by Thraximundar.
- **Vona's Hunger** is one-sided: each opponent sacrifices a creature, or with the city's blessing each opponent sacrifices half their creatures rounded up.
- **Call to the Grave** makes each player sacrifice a non-Zombie creature on that player's upkeep. Thraximundar is a Zombie and therefore cannot be chosen for that trigger.
- **Cultist of the Absolute** gives commander creatures you own +3/+3, flying, deathtouch, ward—pay 3 life, and an upkeep sacrifice trigger. Thraximundar is therefore a 9/9 flying/deathtouch haste threat before sacrifice counters. Sacrificing another creature to the granted upkeep ability grows Thraximundar.
- **Yawgmoth, Thran Physician** converts another creature into a sacrifice trigger, a card, and up to a -1/-1 counter; its proliferate ability can add another +1/+1 counter to Thraximundar once one is present.
- **Flare of Malice** may be cast by sacrificing a nontoken black creature. That sacrifice can grow Thraximundar, then each opponent sacrifices their greatest-mana-value creature or planeswalker. Only creature sacrifices among those opponent choices trigger Thraximundar.
- **Shizo, Death's Storehouse** grants fear to a legendary creature for {B}, {T}, giving Thraximundar a low-cost commander-damage evasion line.
- **Command Beacon** moves Thraximundar from the command zone to hand. A subsequent hand-cast does not pay accumulated commander tax.
- **Rooftop Storm** remains a major commander-specific accelerator: it can replace Thraximundar's printed mana cost with {0} because Thraximundar is a Zombie; any applicable commander tax remains an additional cost.

## Combo audit

The candidate retains sacrifice loops that use the same recursive-body/outlet engines as the commander's primary plan:

- **Gravecrawler + Phyrexian Altar + another Zombie:** sacrifice Gravecrawler for {B}, then recast it for {B}. This is an unbounded cast/death/sacrifice loop. Blood Artist, Zulaport Cutthroat, Diregraf Captain, Goblin Bombardment, Mayhem Devil, or equivalent retained payoff converts it into a win.
- **Gravecrawler + Rooftop Storm + Carrion Feeder + another Zombie:** Rooftop Storm makes Gravecrawler cost {0}; Carrion Feeder repeatedly sacrifices it, producing an unbounded cast/death/sacrifice loop.
- **Gravecrawler + Pitiless Plunderer + a free sacrifice outlet + another Zombie:** each Gravecrawler death makes the Treasure needed to recast it, producing an unbounded loop with a payoff.
- **Gravecrawler + Warren Soultrader + another Zombie + Blood Artist or Zulaport Cutthroat:** Soultrader sacrifices Gravecrawler for a Treasure at the cost of 1 life; the Treasure recasts it and the drain payoff restores that life while damaging opponents.
- **Reassembling Skeleton + Pitiless Plunderer + Phyrexian Altar:** sacrificing Skeleton produces altar mana plus a Treasure; those two mana pay {1}{B} to return Skeleton tapped. This is an unbounded sacrifice/death loop. A death payoff converts it into a win.
- **Reassembling Skeleton + Pitiless Plunderer + Ashnod's Altar:** Ashnod's Altar supplies {C}{C} and Plunderer supplies a Treasure; paying {1}{B} to return Skeleton leaves one colorless mana net each cycle, producing unbounded colorless mana plus sacrifice/death triggers.

No combo is claimed without the stated Zombie condition, recursion permission, mana/life loop, sacrifice outlet, or payoff.

## Mana / curve findings

- Land count remains **36**.
- Mana Vault materially improves deployment of a seven-mana commander and is currently Commander-legal.
- Mana Confluence replaces the always-tapped Crumbling Necropolis with unconditional untapped three-color fixing.
- Rogue's Passage is removed because Cultist and Shizo already provide materially cheaper commander evasion; replacing it with a Swamp improves colored consistency and Cabal Coffers.
- The candidate contains **10 naturally Swamp-typed lands** before Urborg effects: five basic Swamps plus Badlands, Blood Crypt, Underground Sea, Watery Grave, and Xander's Lounge. Urborg, Tomb of Yawgmoth raises Coffers' ceiling further.
- Dragonskull Summit, Drowned Catacomb, and Sulfur Falls were red-teamed rather than automatically replaced. The current list has deep Swamp/Island/Mountain-type coverage, so their untapped condition is well supported; replacing them was not judged a material commander-specific improvement.
- Command Beacon is colorless, but the deck's black-heavy source base, three signets, three talismans, Arcane Signet, premium duals, and Mana Confluence preserve the U/B/R casting requirements.

## Source reconciliation

The October 12 FINAL CSV/TXT exports are authoritative and reconcile at exactly 100 cards. The inherited `deck_card_audit.csv` is stale for five Thraximundar slots: FINAL contains Deadly Dispute, Deathbringer Thoctar, Demon's Disciple, Innocent Blood, and Necrotic Hex while the inherited audit instead contains Counterspell, Soul Shatter, Undead Warchief, Village Rites, and Vona's Hunger. FINAL membership controls.

The stale audit was used only where membership matched FINAL. Vona's Hunger and other suppressed challengers were manually restored to consideration rather than being excluded by the stale membership map.

## Candidate exhaustion / red-team closeout

The v2 red-team specifically reconsidered Yawgmoth, Flare of Malice, Ophiomancer, Lagomos, Hand of Hatred, Soul Shatter, Make an Example, Blasphemous Edict, The Ozolith, Geralf, Visionary Stitcher, Butcher of Malakir, Gisa, Glorious Resurrector, Tarrian's Soulcleaver, generic Zombie-lord packages, additional generic tutors, and additional fetchland/checkland substitutions.

Yawgmoth and Flare were promoted into v2 because they materially improve both raw power and the commander's sacrifice axis. Ophiomancer and Lagomos remain strong but do not displace a retained recursive combo body, draw engine, opponent-sacrifice engine, protection slot, or differentiated payoff. No further change cleared the project's material-improvement threshold.

## Current legality / Oracle checkpoint

The current Wizards Commander banned list was checked on 2026-10-15. None of the candidate's cards are on the Commander banned list. Mana Vault remains legal in Commander; Mana Crypt is banned and is not in this list. Current public card records confirm the relevant new/additional pieces, including Winter, Tormented Loner (Reality Fracture, released 2026-10-02), Flare of Malice, Yawgmoth, Thran Physician, Cultist of the Absolute, Vona's Hunger, Call to the Grave, Diabolic Intent, Cabal Coffers, Shizo, Mana Confluence, and Command Beacon, as Commander-legal.

## Approval boundary

This artifact is **not** an approval record and does **not** lock the deck. Lock only after explicit user approval of exact SHA-256 `d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442`.
