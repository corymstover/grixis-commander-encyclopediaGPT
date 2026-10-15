# Lynde, Cheerful Tormentor — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Tracker deck id: `Lynde__Cheerful_Tormentor`  
Authoritative TXT: `GrixisFINALTXT60--2026.zip / Lynde__Cheerful_Tormentor.txt`  
Source TXT SHA-256: `e72576fbc94bac2be7a043335397f958fa56e481908de53edbb23b5c1379a925`  
Normalized baseline SHA-256: `aa021e7915d1a2f7cfb27c14bb4c47b4788b83a67b6f4e31dbf715f869fc88ef`  
Approval candidate SHA-256: `05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166`

## Commander blueprint

**Primary identity:** Curse recycling/control. Resolve high-impact Curses on opponents, deliberately move Curses you own from the battlefield to your graveyard, use Lynde to return them attached to you at the next end step, then redeploy one on each upkeep while drawing two cards.

**Secondary identity:** extra-upkeep multiplication. Paradox Haze, Obeka, Splitter of Seconds, and The Ninth Doctor multiply Lynde upkeep opportunities and Curse of Misfortunes triggers.

**Support plan:** enchantment/constellation payoffs, Curse copying, premium Grixis interaction, tutors, and a high-quality three-color mana base. Generic combo packages are not added merely to raise the theoretical ceiling.

**Natural ceiling:** **Power Bracket 4 — Optimized.** Current optimized Lynde evidence supports a strong enchantment-control shell, but there is not sufficient commander-specific cEDH evidence to justify replacing the Curse engine with generic Grixis turbo-combo.

## Authoritative-source reconciliation

The current TXT/source package is authoritative. Historical v8.1.4 audit membership differs in several Curse slots. In particular, the old audit contained Curse of Echoes, Curse of Hospitality, Curse of Shaken Faith, Curse of Vengeance, and Curse of the Nightly Hunt where the current frozen source instead contains several other cards. Those historical differences are research evidence only; every addition below is evaluated as a new current-cycle change rather than silently restored.

## Exact proposed changes

1. `Curse of Oblivion` → `Curse of Shaken Faith`
   - Oblivion is a narrow four-mana graveyard-pressure Curse. Shaken Faith costs two and punishes the multi-spell/copy turns that define optimized Commander, making it a materially better Curse target and recursion piece.
2. `Curse of Chaos` → `Curse of Hospitality`
   - Both are political attack-incentive Curses. Hospitality gives attackers trample and converts each combat-damage connection into temporary card access, producing a substantially stronger reason for the table to pressure the cursed player.
3. `Curse of Shallow Graves` → `Curse of Echoes`
   - Shallow Graves overlaps with retained Curse of Disturbance as a combat-politics token Curse. Echoes instead attacks instant/sorcery-heavy opponents and gives every other player access to copies of the cursed player's spells.
4. `Fraying Sanity` → `Curse of Vengeance`
   - Fraying Sanity is a legitimate Curse but the list no longer has a dedicated mill plan. Vengeance is a one-mana Curse that begins accumulating value immediately and is exceptionally efficient fodder for Lynde's destroy/sacrifice-and-return engine.
5. `Crystal Chimes` → `Despotic Scepter`
   - Chimes is broad but slow enchantment recursion. Lynde already supplies bespoke Curse recursion. Scepter is a one-mana permanent that can repeatedly destroy a Curse you own, including one attached to an opponent, directly turning Lynde on at low opportunity cost.
6. `Protean Thaumaturge` → `Perilous Research`
   - Thaumaturge copies creatures rather than Curses and is the least commander-specific member of the copy package. Perilous Research draws two at instant speed and can sacrifice a Curse, causing Lynde to return it and setting up an additional Lynde draw-two on a later upkeep.
7. `Sphinx of the Second Sun` → `The Ninth Doctor`
   - Both create extra-upkeep value. The Ninth Doctor costs three rather than eight and supplies an additional upkeep after it untaps in the normal untap step, dramatically improving the rate of this commander-specific engine.
8. `Crumbling Necropolis` → `Mana Confluence`
9. `Dragonskull Summit` → `Badlands`
10. `Drowned Catacomb` → `City of Brass`
11. `Haunted Ridge` → `Marsh Flats`
12. `Shipwreck Marsh` → `Flooded Strand`
13. `Stormcarved Coast` → `Misty Rainforest`
14. `Sulfur Falls` → `Volcanic Island`
   - These seven land changes preserve the 35-land count while replacing a tapped tri-land, check/slow lands, and dependency-sensitive sources with unconditional three-color sources, original duals, and fetchlands. Xander's Lounge and Bojuka Bog remain as intentional tapped utility/fetchable sources.

## Important retained packages

- `Claws of Gix`, `Braids, Arisen Nightmare`, and `Demon of Fate's Design` remain direct ways to put your own Curse from the battlefield into your graveyard and trigger Lynde.
- `Curse of Misfortunes` is the central Curse tutor and becomes stronger with extra upkeep steps.
- `Paradox Haze`, `Obeka, Splitter of Seconds`, and the added `The Ninth Doctor` form the extra-upkeep package.
- `Curse of Bloodletting` is retained because it amplifies all damage to the cursed player and can increase the amount of combat damage Obeka actually deals, which increases Obeka's additional-upkeep count.
- `Curse of Obsession` plus `Curse of Fool's Wisdom` is retained as a punishing draw-step pairing.
- `Copy Enchantment`, `Mirrormade`, `Estrid's Invocation`, and `Clever Impersonator` remain because copying the best Curse or other high-impact enchantment is a distinct and scalable angle.
- `Ashiok's Reaper` and `Wicked Visitor` reward enchantments going from the battlefield to the graveyard; `Entity Tracker`, `Grim Guardian`, and `Doomwake Giant` reward the enchantment-heavy construction more broadly.
- Premium interaction and tutors are retained to protect a comparatively setup-intensive four-mana commander and prevent the identity engine from being too fragile.

## Rules-critical conclusions

- Lynde triggers only when a permanent that is a Curse moves from the battlefield to **your graveyard**. Discarding or milling a Curse card does not trigger Lynde.
- A Curse you own attached to an opponent is still a permanent you own, so Despotic Scepter can target it. Destroying it sends it to your graveyard under normal circumstances and triggers Lynde.
- Lynde's delayed return happens at the beginning of the next end step and returns that Curse attached to you. Her upkeep ability can then move one Curse attached to you to an opponent; that move does not target.
- If Curse of Misfortunes is attached to you, its upkeep trigger and Lynde's upkeep trigger can both trigger. Ordering Misfortunes above Lynde allows Misfortunes to put a Curse onto the battlefield attached to you first; Lynde can then move a Curse attached to you when her trigger resolves.
- A Curse that enters during an upkeep did not exist at the beginning of that upkeep and therefore does not retroactively generate its own beginning-of-upkeep trigger.
- Obeka's added upkeep steps and The Ninth Doctor's added upkeep step each cause beginning-of-upkeep abilities to trigger in those extra upkeeps. Obeka's added beginning phases skip untap and draw.
- Perilous Research draws two, then sacrifices a permanent. Sacrificing a Curse while Lynde is present triggers Lynde after the spell finishes resolving.

## Candidate exhaustion / rejected challengers

- `Curse of the Pierced Heart`, `Curse of Leeches`, `Curse of Stalked Prey`, `Curse of Inertia`, and `Curse of the Nightly Hunt`: valid Curse density options, but each is lower-impact than the selected four Curse upgrades.
- `Shadow of the Second Sun`: powerful extra-beginning-phase effect, but six mana is materially less efficient than The Ninth Doctor for the same upkeep-multiplication objective.
- `Strionic Resonator`: can copy Lynde or Curse triggers, but requires repeated mana and does not outperform the selected direct Curse/sacrifice engines.
- `Read the Runes`, `Infernal Tribute`, `Ice Out`, `Final Vengeance`, and `Beseech the Mirror`: all have real sacrifice/bargain synergy, but no current slot is weaker enough to justify another change after the selected Despotic Scepter and Perilous Research additions.
- `Valeria Richards, Precocious`: efficient generic noncreature support, but not more commander-specific than the retained enchantment engines.
- `Archnemesis`: an Aura but not a Curse, so Lynde does not recur or move it as a Curse.
- `The Unluckiest Planeswalker` and `Jabs, Mistress of Mockery`: not used; current release timing is after this refinement date and no Lynde-specific project exception authorizes them.
- Generic Thassa's Oracle/Consultation or Breach packages: rejected as commander-independent homogenization.

After the whole-list audit, source reconciliation, current optimized comparison, October 2026 card review, Curse-density review, sacrifice-engine review, mana review, extra-upkeep rules review, and adversarial candidate pass, **ZERO NEW MATERIAL IMPROVEMENTS** remain beyond the fourteen swaps above.

## Structural state

- Candidate: **100 cards**
- Distinct names: **93**
- Repeated names: `Island x4`, `Mountain x3`, `Swamp x3` only
- Lands: **35**
- Commander identity: **U/B/R**
- Expected project exceptions: **none**
- Proposed ceiling: **Power Bracket 4 — Optimized**
- Approval state: **NOT APPROVED** pending fresh SHA-bound complete gate and explicit user approval.
