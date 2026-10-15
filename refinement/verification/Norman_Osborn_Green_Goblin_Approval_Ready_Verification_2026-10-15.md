# Norman Osborn // Green Goblin — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #43 of 62  
Exact candidate SHA-256: `23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **42 APPROVED / LOCKED decks** through Nicol Bolas, the Ravager // Nicol Bolas, the Arisen. The reconciled tracker identifies **Norman Osborn // Green Goblin** as the next unlocked deck (tracker index 42 / deck 43 of 62).

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: current October 12 FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Goben__Gene_Splice_Savant.txt`
- Raw FINAL TXT SHA-256: `6e17c60ce8a9e9956ef66d10fe62f19afd250f0d39bcfde3eb6888dd65bc21ae`
- FINAL CSV: `GrixisFINAL60--2026.zip / Goben__Gene_Splice_Savant.csv`
- Raw FINAL CSV SHA-256: `086e00f63ecdf8299bf852d8312c5f8ba88e7953673d70192f7aae40e662ba58`
- Baseline total: **100 cards**
- Baseline distinct names: **100**
- Baseline lands: **22**
- Repeated names: **none**
- CSV/TXT membership reconciliation: **PASS**

The October 11 tracker and historical ranking materials are evidence only; the October 12 FINAL exports control membership.

Result: **PASS**.

## 3. Natural power ceiling / contemporary competitive evidence

Project research previously ranked Norman Osborn // Green Goblin **#7 overall** at approximately **855.1** and classified the deck as **Bracket 5 — cEDH**. Project tournament evidence recorded **121 entries**, with a moderate/high sample classification.

Contemporary 2026 Norman tournament evidence was also reviewed. Current cEDH Norman shells consistently use compact Oracle/Consultation and Underworld Breach packages alongside commander-specific discard/graveyard infrastructure, and recent tournament records include high finishes. This supports preserving a true cEDH ceiling rather than artificially constraining the deck to Bracket 4.

The commander-first constraint is therefore not to avoid generic cEDH cards; it is to ensure the discard → graveyard → Mayhem/cast-from-graveyard engine remains a material reason the deck functions.

Result: **PASS — Power Bracket 5 / cEDH**.

## 4. Exact structural verification

SHA-bound candidate file: `refinement/decklists/Norman_Osborn_Green_Goblin_Approval_Ready_2026-10-15.txt`

- Total cards including commander: **100**
- Commander: **1x Norman Osborn // Green Goblin**
- Lands: **23**
- Distinct names: **100**
- Repeated names: **none**
- Singleton violations: **0**
- Baseline delta: **29 cuts / 29 additions**
- Whole-list adjudication: **70 KEEP / 29 CUT across all 99 noncommander copies**
- Strategic nonland changes: **20 cuts / 19 additions**
- Land changes: **9 cuts / 10 additions**
- Land count: **22 → 23**

The candidate's fully distinct card names also preserve a clean Tainted Pact construction with no duplicate-name stopping point introduced by deckbuilding.

Result: **PASS**.

## 5. Commander Oracle / color identity / transformation

Current Norman Osborn front face:

- mana cost `{1}{U}`
- legendary Human Scientist Villain
- cannot be blocked
- when it deals combat damage to a player, connive
- `{1}{U}{B}{R}: Transform Norman Osborn. Activate only as a sorcery.`

Current Green Goblin back face:

- Goblin Human Villain
- flying, menace
- spells you cast from your graveyard cost `{2}` less to cast
- each nonland card in your graveyard has mayhem; its mayhem cost is equal to its mana cost

Mayhem allows a card discarded during the current turn to be cast from the graveyard for its mayhem cost. It does **not** override normal timing permissions. Green Goblin's cost reduction reduces only generic mana and does not itself grant permission to cast cards from the graveyard.

Color identity is determined using both faces and is **U/B/R**. Every candidate card is within U/B/R color identity or colorless.

Result: **PASS**.

## 6. Commander-specific cost compression

Green Goblin reduces by `{2}` the generic component of spells cast from the graveyard, including spells being cast through mayhem.

Verified rate examples:

- **Big Score:** mayhem cost `{3}{R}` becomes `{1}{R}` with Green Goblin. Its additional discard cost remains mandatory. If Artist's Talent is level 2, the remaining `{1}` generic can also be reduced, leaving `{R}`.
- **Dark Deal:** mayhem cost `{2}{B}` becomes `{B}`.
- **Unstable Experiment:** mayhem cost `{1}{U}` becomes `{U}`.
- **Brain Freeze:** when cast from the graveyard, Green Goblin can reduce its generic component as applicable.

These rate changes are why several commander-specific cards were retained despite lower broad cEDH inclusion.

Result: **PASS**.

## 7. Artist's Talent

Artist's Talent is a Class enchantment whose first ability lets the controller discard a card and then draw a card whenever a noncreature spell is cast. At level 2, noncreature spells cost `{1}` less to cast.

This supplies both:

1. a repeatable discard outlet that turns cards in hand into Mayhem candidates; and
2. an additional generic cost reduction that stacks with Green Goblin's `{2}` graveyard-spell reduction.

The reductions cannot reduce colored mana symbols.

Result: **PASS**.

## 8. Attunement / Breakthrough

**Attunement** can return itself to hand as the cost of its activated ability, then draw three cards and discard four. This is a repeatable batch-discard engine that can place several nonland cards into the graveyard in one action for Mayhem access.

**Breakthrough** for `X=0` costs `{U}`, draws four cards, then causes the player to discard their hand. This is an unusually efficient hand-conversion spell in a commander whose back face can immediately turn same-turn discards into graveyard-cast resources, subject to normal timing.

Result: **PASS**.

## 9. Mayhem timing / Borne Upon a Wind / Valley Floodcaller

Mayhem changes where and for what alternative cost a card may be cast; it does not itself let a sorcery be cast at instant speed.

**Borne Upon a Wind** allows spells to be cast that turn as though they had flash.

**Valley Floodcaller** allows noncreature spells to be cast as though they had flash, including noncreature cards another effect permits the player to cast from a non-hand zone.

Accordingly, these cards materially expand off-turn Mayhem use. Without such an effect, a sorcery discarded during an opponent's turn is normally not castable through Mayhem merely because it was discarded that turn.

Result: **PASS**.

## 10. Necropotence interaction — corrected

Necropotence is deliberately **not** restored despite its generic cEDH power.

Its relevant ability is triggered, not a discard replacement effect: whenever its controller discards a card, Necropotence triggers and attempts to exile that card from the graveyard when the trigger resolves.

Consequences:

- the discarded card does reach the graveyard;
- the Necropotence trigger then goes on the stack;
- because Mayhem still obeys timing rules, a sorcery-speed Mayhem card normally cannot be cast while that trigger is waiting on the stack;
- an instant-speed Mayhem card, or a card made castable at flash timing by Borne Upon a Wind / Valley Floodcaller, can sometimes be cast in response before the exile trigger resolves.

Thus Necropotence does not absolutely shut off Mayhem, but it systematically fights the deck's intended discard → graveyard → cast workflow. The commander-first build therefore rejects it despite its abstract power.

Result: **PASS**.

## 11. Yawgmoth's Will tension

Yawgmoth's Will remains as a separate graveyard-replay engine. During its turn, cards that would be put into the controller's graveyard from anywhere are exiled instead.

Therefore, Yawgmoth's Will is **not** treated as a same-turn Mayhem discard engine. New cards discarded while its replacement effect applies will not normally remain available in the graveyard for Green Goblin's Mayhem plan. It is retained for its powerful ability to replay resources already present in the graveyard before the Will turn.

Result: **PASS**.

## 12. Reckless Handling

Reckless Handling searches for an artifact, places it into hand, shuffles, then causes a random discard. No action is taken between putting the artifact into hand and the random discard.

If the randomly discarded card is a nonland while Green Goblin is active, that card becomes eligible for Mayhem because it was discarded that turn. It still cannot be cast until Reckless Handling has finished resolving, and its normal timing permissions still apply.

This creates commander-native overlap while serving as access to Lion's Eye Diamond, Grinding Station, Mox Amber, fast mana, or another relevant artifact.

Result: **PASS**.

## 13. Thassa's Oracle / Consultation / Tainted Pact

The candidate retains the compact cEDH package:

- Thassa's Oracle
- Demonic Consultation
- Tainted Pact

The exact approval-ready list contains **100 distinct card names**, so Tainted Pact has no duplicate-name stopping condition introduced by the decklist itself.

These wins are retained because Norman's natural ceiling is genuinely cEDH; they are not treated as the deck's sole identity.

Result: **PASS**.

## 14. Underworld Breach / LED / Brain Freeze

The classic Underworld Breach + Lion's Eye Diamond + Brain Freeze package remains a compact win engine.

Green Goblin can improve the rate of graveyard-cast spells by reducing generic mana, but the Breach package does not require the commander to function. It remains acceptable because the rest of the refined list preserves a substantial commander-native discard / Mayhem architecture.

Result: **PASS**.

## 15. Underworld Breach / Grinding Station / Mox Amber

Grinding Station can sacrifice Mox Amber to mill three cards. Underworld Breach may then allow Mox Amber to be escaped for zero mana by paying its escape exile cost; when the artifact returns, Grinding Station's artifact-entry trigger untaps the Station.

With Norman Osborn on the battlefield, Mox Amber can produce blue mana before being sacrificed because Norman is a blue legendary permanent.

This package is treated as a self-mill / mana engine that can support Breach finishes when the graveyard contains sufficient resources. The approval packet **does not** claim these three cards alone produce a resource-free deterministic win from an empty graveyard.

Result: **PASS**.

## 16. Cavern of Souls — corrected scope

Cavern of Souls naming **Human** can make the front-face Norman Osborn creature spell uncounterable while producing an appropriate colored mana for that spell.

Green Goblin is also a Human on the battlefield, but the back face is reached by transformation and is **not separately cast**. Cavern is therefore described as protecting the Norman Osborn commander spell, not as separately casting/protecting Green Goblin.

Result: **PASS**.

## 17. Mana-base / acceleration red team

The authoritative baseline contained **22 lands**. The candidate deliberately increases this to **23**, rather than shaving further in a color-intensive turbo list.

Final land package:

- Ancient Tomb
- Arid Mesa
- Badlands
- Blood Crypt
- Bloodstained Mire
- Cavern of Souls
- City of Brass
- City of Traitors
- Command Tower
- Flooded Strand
- Gemstone Caverns
- Mana Confluence
- Marsh Flats
- Misty Rainforest
- Otawara, Soaring City
- Polluted Delta
- Scalding Tarn
- Steam Vents
- Underground Sea
- Verdant Catacombs
- Volcanic Island
- Watery Grave
- Wooded Foothills

The candidate also adds **Mox Amber, Grim Monolith, and Simian Spirit Guide** while retaining the baseline's dense fast-mana package. This is a deliberate turbo-mana modernization rather than a simple land reduction.

Color sequencing for `{1}{U}` Norman, `{1}{U}{B}{R}` transformation, and U/B/R compact win pieces remains supported by nine fetchlands, three original duals, three shocks, five-color lands, Cavern, and the artifact/ramp package.

Result: **PASS**.

## 18. Candidate exhaustion / commander-necessity review

Project rankings, historical October 11 changes, current Norman cEDH tournament shells, current EDHREC cEDH evidence, commander-specific discard outlets, graveyard-cast engines, timing enablers, fast mana, compact wins, interaction, tutors, and mana-base challengers were reviewed.

Notable rejected alternatives include:

- **Necropotence:** rejected for the triggered graveyard-exile tension described above.
- **Skirge Familiar:** genuine Norman synergy, but too slow at five mana from hand / three after Green Goblin when the deck already has many cheaper outlets.
- **Kefka, Court Mage:** tournament-playable and synergistic, but five mana loses the slot competition to cheaper setup and compact infrastructure.
- **Chainer, Nightmare Adept:** commander lift acknowledged; four-mana creature-only recursion remains slower than the finalized plan.
- **Secrets of the Dead:** commander-native but three mana with no immediate effect.
- **The One Ring:** extremely strong generic card advantage, but four mana and no commander-specific discard/graveyard role; current draw engines are sufficient.
- **Mnemonic Betrayal / Diabolic Intent / Force of Negation:** individually powerful but did not clear the final opportunity-cost bar.
- **Putrid Imp / Firestorm:** additional cheap discard outlets were tested but final outlet density is already sufficient.
- **Bazaar of Baghdad:** powerful discard engine but zero mana production is too costly in a 23-land color-intensive turbo shell.
- **Cephalid Coliseum / Urza's Saga:** useful utility, but final color requirements and land tempo favor the chosen configuration.
- **Oscorp Industries:** uniquely flavorful and Mayhem-compatible, but entering tapped is too costly at the deck's natural Bracket-5 ceiling.

Commander-necessity test: the exact list contains multiple compact generic cEDH finishes, but Norman/Green Goblin materially changes the efficiency and availability of Big Score, Dark Deal, Unstable Experiment, Shadow of the Goblin, Attunement, Breakthrough, Ghostly Pilferer, Tolarian Winds, Artist's Talent, Reckless Handling, and other discard/graveyard sequences. The commander remains strategically consequential rather than ornamental.

Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

Result: **PASS**.

## 19. Current legality checkpoint

The current official Commander banned list was checked for the exact candidate. No candidate card is a named Commander-banned card. The October 12, 2026 Banned & Restricted update changed Competitive Brawl but did not create a tabletop Commander legality issue for this list.

Project-specific legality exception required: **NONE**.

Result: **PASS**.

## 20. Mandatory gate summary

- Current repository state recovered: **PASS**
- Current-cycle locked decks before Norman approval: **42/62**
- Norman correctly identified as next unlocked deck: **PASS**
- Authoritative FINAL baseline reconciled: **PASS**
- Baseline structure: **100 / 100 distinct / 22 lands**
- Mandatory 99-slot audit: **99/99 PASS**
- Whole-list result: **70 KEEP / 29 CUT**
- Candidate: **100 / 100 distinct / 23 lands**
- Singleton: **PASS**
- Tainted Pact duplicate-name construction check: **PASS**
- U/B/R color identity: **PASS**
- Current official Commander legality: **PASS**
- Project exceptions: **NONE REQUIRED**
- Norman / Green Goblin Oracle and transform review: **PASS**
- Mayhem timing review: **PASS**
- Green Goblin generic-cost reduction: **PASS**
- Artist's Talent stacking: **PASS**
- Attunement / Breakthrough discard engine: **PASS**
- Borne Upon a Wind / Valley Floodcaller timing expansion: **PASS**
- Necropotence interaction corrected and reviewed: **PASS**
- Yawgmoth's Will graveyard tension: **PASS**
- Reckless Handling timing/discard interaction: **PASS**
- Oracle / Consultation / Tainted Pact: **PASS**
- Breach / LED / Brain Freeze: **PASS**
- Breach / Grinding Station / Mox Amber: **PASS — conservatively characterized**
- Cavern of Souls scope: **PASS — front-face spell only**
- Mana-base / acceleration red team: **PASS**
- Candidate exhaustion / commander-necessity review: **PASS**
- Natural ceiling: **Power Bracket 5 — cEDH**
- Recommended Archidekt tags: **Mayhem / Graveyard Casting / Turbo Combo**
- Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**

## 21. Final status

**APPROVAL_READY — NOT APPROVED / NOT LOCKED**

The exact approval-ready candidate is bound to SHA-256:

`23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`

No state or tracker lock should be written until explicit user approval of this exact candidate is received.
