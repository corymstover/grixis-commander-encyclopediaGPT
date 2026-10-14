# Edea, Possessed Sorceress — Current-Cycle Refinement Decisions

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Deck:** #16 — Edea, Possessed Sorceress  
**Status:** candidate frozen; explicit approval not yet granted  
**Authoritative standardized baseline SHA-256:** `8caaf9d1d62204627139b88e8f440ed3d3739a64e45bb1f97497590dc9df939a`  
**Approval-candidate SHA-256:** `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`

## Commander-first blueprint

Edea is a Grixis 2/5 Human Warlock with ward {2}. At the beginning of combat on your turn she temporarily gains control of an opponent's creature, untaps it, and gives it haste. Whenever a creature you control but do not own dies, Edea returns it to its owner's battlefield and draws you a card.

The deck therefore wants four tightly linked classes of effects:

1. **Additional theft** — borrow more opposing creatures so the commander is not the only source of non-owned bodies.
2. **Sacrifice conversion** — turn temporary control into mana, cards, damage, tutors, or board pressure before the control effect expires.
3. **Trigger/combat multiplication** — copy Edea or her beginning-of-combat trigger, or create additional combat phases, so she steals more than one creature per turn.
4. **Retention/replacement theft** — exploit effects such as Thassa, Nightmare Shepherd, Chaos Shrine's Black Crystal, Saw in Half, and Impostor Syndrome so a borrowed opposing card can become lasting value rather than simply return at cleanup.

Natural ceiling: **Bracket 4 — Optimized**. Edea is a five-mana board-dependent commander whose strongest commander-first lines are powerful multiplayer value/tempo engines rather than a naturally compact cEDH win package.

## Authoritative source reconciliation

The authoritative CSV and TXT exports agree exactly at **100 cards / 94 distinct names**, with only Island, Mountain, and Swamp repeated at three copies each. No project exception applies.

The supporting `deck_card_audit.csv` is stale relative to those matching exports. The authoritative exports contain:

- Corrupted Conviction
- Evereth, Viceroy of Plunder
- Grim Haruspex
- Morbid Opportunist
- Skullclamp

The audit snapshot instead contains:

- Captivating Crew
- Cunning Rhetoric
- Domineering Will
- Nasty End
- Thassa, Deep-Dwelling

This also explains why the candidate-ranking table incorrectly presents several real baseline cards as candidates (Evereth #2, Morbid Opportunist #4, Grim Haruspex #5, Corrupted Conviction #6, Skullclamp #19) while omitting audit-only cards from ranked discovery. Per project policy, the matching CSV/TXT exports remain authoritative. All five audit-only names were nevertheless challenged manually: Captivating Crew and Thassa earned slots; Cunning Rhetoric, Domineering Will, and Nasty End did not.

## Mandatory 99-slot whole-list audit

Every noncommander slot was challenged. Repeated basics are listed with their quantities; this section accounts for all 99 noncommander cards.

### Retained — interaction / protection

- An Offer You Can't Refuse — efficient stack interaction.
- Arcane Denial — broad two-mana counter; retained over adding another generic free counter because the shell already has premium interaction and commander-first slots are more valuable.
- Blasphemous Act — efficient creature reset when theft engines cannot stabilize the board.
- Chaos Warp — flexible answer to permanent types Grixis otherwise struggles with.
- Deadly Rollick — premium creature interaction with commander online.
- Deflecting Swat — protects Edea/engines and redirects hostile interaction.
- Fierce Guardianship — premium noncreature protection with Edea online.
- Grave Pact — one death-conversion payoff retained; sacrificing borrowed creatures can force real losses elsewhere while Edea returns the borrowed body.
- Mana Drain — premium universal counter and acceleration.
- Mayhem Devil — converts all sacrifice events, including Treasures and stolen bodies, into board control/damage.
- Saw in Half — particularly strong on borrowed creatures: Edea can draw from the original death while the spell's controller creates the copy tokens.
- Swan Song — efficient protection.
- Toxic Deluge — scalable reset.
- Vandalblast — efficient artifact interaction.

### Retained — mana / sacrifice infrastructure

- Arcane Signet
- Ashnod's Altar — free sacrifice outlet plus mana.
- Fellwar Stone
- Illuminor Szeras — turns a borrowed creature into black mana.
- Phyrexian Altar — free outlet plus colored mana.
- Pitiless Plunderer — converts creature deaths into Treasure.
- Sol Ring
- Talisman of Creativity
- Talisman of Dominance
- Talisman of Indulgence
- Evereth, Viceroy of Plunder — authoritative-baseline card; repeatable sorcery-speed outlet in second main, scales into a table-damage finisher.
- Goblin Bombardment — free outlet and damage conversion.
- Kethek, Crucible Goliath — end-step outlet while Edea's temporary control still applies; converts high-MV borrowed creatures into deck material.
- Viscera Seer — one-mana free outlet.
- Warren Soultrader — free outlet that creates Treasure for one life.

### Retained — sacrifice/draw/value engines

- Braids, Arisen Nightmare — end-step outlet and multiplayer draw/pressure.
- Corrupted Conviction — one-mana instant outlet that draws two; more efficient as a generic stolen-creature converter than Nasty End when the borrowed creature is not legendary.
- Deadly Dispute — instant outlet, cards, and Treasure.
- Disciple of Bolas — turns borrowed power into cards/life, with Edea adding another card if the sacrificed creature is not owned.
- Grim Haruspex — uncapped per-creature death draw for nontoken bodies; retained over Morbid Opportunist.
- Industrial Advancement — end-step sacrifice conversion into a creature from the library.
- Rakdos, the Muscle — sacrifices bodies and converts their mana value into playable opposing-library cards.
- Seize the Spotlight — either steals opposing creatures or yields cards/Treasures; every mode advances the plan.
- Skullclamp — authoritative-baseline card; cheap sacrifice/draw conversion and excellent with small bodies.
- Village Rites — one-mana instant outlet and draw.

### Retained — commander multipliers / theft / retention

- Ayara, Widow of the Realm // Ayara, Furnace Queen — sacrifice outlet whose front face converts stolen mana value into damage/life; back face is additional combat-step recursion.
- Chaos Shrine's Black Crystal — if its death trigger resolves before Edea's, it can exile a borrowed nontoken creature and later put that card onto the battlefield under your control; Edea still draws even if the return instruction can no longer move the card.
- Dominus of Fealty — repeatable upkeep theft of any permanent.
- Don Andres, the Renegade — makes borrowed creatures much more threatening in combat without stopping sacrifice.
- Gogo, Master of Mimicry — copies Edea's triggered ability for `{2}` at X=1 and can scale higher.
- Impostor Syndrome — expensive but highly commander-specific: a borrowed attacker that connects can leave behind a nonlegendary token copy you own.
- Insurrection — top-end theft finisher; stolen board can attack and/or be sacrificed before control expires.
- Irma, Part-Time Mutant — retained with timing caveat: she does not retroactively create an Edea trigger during the first combat in which she becomes Edea, but the copy effect persists, so later combats/turns begin with her already carrying Edea's triggers.
- Karlach, Fury of Avernus — an extra combat means another Edea theft trigger and reuses creatures already borrowed that turn.
- Mob Rule — mass theft and sacrifice finisher.
- Nightmare Shepherd — can exile a borrowed nontoken creature before Edea returns it, leaving you a token copy while Edea still draws.
- Reanimate — can target an opponent's graveyard, producing a creature you control but do not own and therefore a continuing Edea payoff.
- Roaming Throne — naming Warlock makes Edea's combat and death triggers trigger an additional time.
- Sakashima of a Thousand Faces — Edea copy that also suppresses the legend rule for your permanents.
- Spark Double — nonlegendary Edea copy.
- Victimize — self-recursion retained because a borrowed creature can pay the sacrifice cost while Edea draws and two engine creatures return.
- Zara, Renegade Recruiter — steals from an opponent's hand for combat; a stolen creature can be sacrificed before the delayed return.

### Retained — protection / tutors

- Lightning Greaves — commander protection remains important for a five-mana engine commander.
- Demonic Tutor — flexible tutor.
- Diabolic Intent — tutor whose sacrifice cost is synergistic rather than incidental.

### Retained — lands (26 nonbasic/basic names; 31 slots after repeated basics)

- Badlands
- Blood Crypt
- Bloodstained Mire
- Command Tower
- Exotic Orchard
- Haunted Ridge
- High Market — land-based sacrifice outlet.
- Island x3
- Luxury Suite
- Morphic Pool
- Mountain x3
- Otawara, Soaring City
- Phyrexian Tower — land-based sacrifice outlet and acceleration.
- Polluted Delta
- Scalding Tarn
- Shipwreck Marsh
- Steam Vents
- Stormcarved Coast
- Swamp x3
- Training Center
- Underground Sea
- Urborg, Tomb of Yawgmoth
- Volcanic Island
- Watery Grave
- Xander's Lounge

### Cuts after challenge

1. **Garland, Royal Kidnapper** — the static clause saying creatures you control but do not own cannot be sacrificed directly shuts off Edea's primary conversion engine for every borrowed creature, not merely Garland's own theft target.
2. **The Beast, Deathless Prince** — mostly a four-mana one-shot temporary theft spell attached to a body that enters with six stun counters; it loses badly to a multiplayer theft spell in this commander.
3. **Coercive Recruiter** — the baseline has too few natural Pirate-entry events to justify five mana. Don Andres making a borrowed creature a Pirate does not make that creature enter the battlefield, so it does not retrigger Recruiter.
4. **Morbid Opportunist** — capped at one trigger each turn; Edea and Grim Haruspex already reward the same death event more efficiently for this deck's burst-sacrifice turns.
5. **Dictate of Erebos** — strong but redundant with Grave Pact and expensive at five mana. The final slot is more valuable as an effect that multiplies Edea's unique combat trigger rather than as a second generic edict engine.
6. **Reliquary Tower** — colorless mana and no-maximum-hand-size utility are less important than making Edea's targeted theft work through hexproof/shroud.
7. **Dragonskull Summit** — avoidable conditional untapped land.
8. **Drowned Catacomb** — avoidable conditional untapped land.
9. **Sulfur Falls** — avoidable conditional untapped land.

## Final proposed swaps

1. `Garland, Royal Kidnapper` -> `Thassa, Deep-Dwelling`
   - Thassa's end-step blink can target the creature Edea borrowed that turn while you still control it, then returns that card to the battlefield **under your control** as a new object. Edea's temporary-control duration no longer governs that new object, converting a one-turn borrow into lasting control.
2. `The Beast, Deathless Prince` -> `Mass Mutiny`
   - In a normal four-player game, Mass Mutiny can borrow up to three creatures for five mana, multiplying Edea-compatible attack/sacrifice material much more efficiently than Beast's single cast trigger.
3. `Coercive Recruiter` -> `Captivating Crew`
   - Crew is a repeatable mana sink that can steal a creature in precombat main and leave Edea free to steal another at beginning of combat. It does not depend on a sparse Pirate-entry package.
4. `Morbid Opportunist` -> `Strionic Resonator`
   - Resonator can copy Edea's beginning-of-combat theft trigger or her death/draw trigger and remains useful with many other triggers in the deck. This is direct commander multiplication rather than redundant capped draw.
5. `Dictate of Erebos` -> `Full Throttle`
   - Full Throttle inserts two additional combat phases. Edea triggers at the beginning of each, so one spell can generate two extra theft events while also untapping prior attackers between combats.
6. `Reliquary Tower` -> `Arcane Lighthouse`
   - Lighthouse removes hexproof and shroud from opposing creatures for the turn, directly solving a failure mode of Edea's targeted combat trigger.
7. `Dragonskull Summit` -> `City of Brass`
8. `Drowned Catacomb` -> `Mana Confluence`
9. `Sulfur Falls` -> `Ancient Tomb`
   - These three land upgrades improve untapped fixing/acceleration. Ancient Tomb is especially valuable for a five-mana commander and the deck's four-to-six-mana engines.

The five nonland additions and five nonland cuts have the **same combined mana value (21)**, so the nonland curve does not increase. Land count remains **35**.

## Candidate exhaustion / adversarial review

High-impact ranked, stale-audit, EDHREC, and current outside challengers were explicitly tested:

- **Marchesa, the Black Rose (#1 ranked)** — rejected as an Oracle-term false positive. Edea's mandatory death trigger returns a borrowed creature to its owner; whichever order the Marchesa and Edea triggers resolve, the borrowed card changes zones before Marchesa's delayed return can reclaim that same object for you. Marchesa remains good generic aristocrats value, but it is not the best commander-specific slot.
- **Evereth / Morbid Opportunist / Grim Haruspex / Corrupted Conviction / Skullclamp** — ranking appearances are artifacts of the stale audit snapshot; all were evaluated as actual baseline cards. Only Morbid was cut.
- **Domineering Will** — capable of borrowing multiple blockers at instant speed, but its combat-condition text is less reliable than Mass Mutiny/Crew and it lost the exact-slot test.
- **Nasty End** — can draw three when the sacrificed creature is legendary, but costs one more mana than Corrupted Conviction and the stolen target is not reliably legendary.
- **Cunning Rhetoric** — reactive card access without theft/sacrifice linkage; not commander-first enough.
- **Conjurer's Closet** — powerful Edea retention engine and the closest omitted card. Thassa performs the same crucial end-step retention job one mana cheaper, is indestructible, and leaves the deck less saturated with five-mana setup pieces.
- **Chameleon, Master of Disguise** — valid distinct-name Edea copy, but the deck already retains Gogo, Irma, Roaming Throne, Sakashima, Spark Double, and now Resonator. Another four-mana clone had lower marginal value than theft density or extra combats.
- **Irenicus's Vile Duplication / Quantum Misalignment** — same redundancy conclusion as Chameleon.
- **Éomer, Marshal of Rohan** — extra combat is conditional on an attacking legendary creature dying; Full Throttle guarantees two additional combats without needing an opponent to supply a suitable legend.
- **Breath of Fury** — high ceiling but needs a reliable chain of connecting creatures and is less deterministic in this build than Full Throttle.
- **Sothera, the Supervoid** — excellent death-control engine, but it removes creatures Edea might otherwise borrow and competes with the retained Grave Pact control slot. It did not beat the more commander-specific Full Throttle slot.
- **Helm of Possession** — strong sacrifice/theft hybrid, but requires six mana before the first activation and staying tapped to preserve control; Thassa/Crew were cleaner engines.
- **Altar of Dementia / Yawgmoth, Thran Physician / Carrion Feeder / Umbral Collar Zealot** — no sacrifice-outlet shortage remains; existing free outlets plus lands and spell-cost outlets are sufficient.
- **Come Back Wrong** — flavorful permanent theft/removal, but narrower as interaction than the retained flexible removal package.
- **Jhoira, Weatherlight Corsair** — current and legal, but six mana and historic-permanent variance make it less Edea-specific than the chosen engines.
- **Jabs, Mistress of Mockery** — not released until 2026-11-09 as of this 2026-10-14 review, and Edea has no project future-release exception; therefore ineligible for this approval candidate.
- **Generic staples such as Rhystic Study, Vampiric Tutor, Force of Will, and The One Ring** — individually powerful but did not justify displacing a commander-specific theft/sacrifice/multiplication slot at Edea's natural Bracket-4 ceiling.

## Second serious pass

After reopening the strongest rejected alternatives against the nine exact swaps, the second pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

The approval candidate is therefore frozen at SHA-256 `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`, pending fresh Oracle/rules/legality verification and the fail-closed complete gate.
