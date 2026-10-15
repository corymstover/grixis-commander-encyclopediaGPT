# Marchesa, the Black Rose — Current-Cycle Decision Closeout

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## Source reconciliation

The authoritative current FINAL CSV/TXT exports reconcile at exactly 100 cards. Raw FINAL TXT source SHA-256: `d292b21d373085ebe83ddea091bc7f51cf8f59048c987deca5fee2395205cdc9`. Normalized current-cycle project-format baseline SHA-256: `2e8a3fec0749abe153cc2be45ca89f65a6f9634376f7740a9ff63633a15d3ab7`.

The inherited `deck_card_audit.csv` has stale membership for this commander, so the current FINAL exports control membership. Audit metadata was reused only where card names reconcile.

## Commander blueprint and natural ceiling

Marchesa is a +1/+1-counter, sacrifice, death/ETB recursion engine. The optimized plan is to place counters through dethrone and dedicated counter engines; sacrifice creatures for mana/cards/interaction; exploit Marchesa's delayed return trigger; use +1/+1 counters to reset persist creatures; and close through compact commander-native loops rather than a generic Grixis combo shell.

Natural ceiling: **Power Bracket 4 — Optimized**.

## Exact proposed changes

### Nonland
1. Animate Dead -> Sneak Attack
2. Arcane Denial -> Flare of Denial
3. Black Market Connections -> Agatha's Soul Cauldron
4. Bloodghast -> Twilight Diviner
5. Cauldron of Souls -> Sage of Fables
6. Drana, Liberator of Malakir -> Spark Double
7. Herald of Secret Streams -> Danny Pink
8. Juri, Master of the Revue -> Imperial Recruiter
9. Midnight Reaper -> Satoru, the Infiltrator
10. Pawn of Ulamog -> Gev, Scaled Scorch
11. Reassembling Skeleton -> Altar of Dementia
12. Village Rites -> Vampiric Tutor

### Mana base
13. Crumbling Necropolis -> Badlands
14. Drowned Catacomb -> Flooded Strand
15. Fabled Passage -> City of Brass
16. Haunted Ridge -> Mana Confluence
17. Shipwreck Marsh -> Misty Rainforest
18. Smoldering Marsh -> Underground Sea
19. Sulfur Falls -> Verdant Catacombs
20. Sunken Hollow -> Volcanic Island
21. Swamp (3 -> 2) -> Forge of Heroes

## Material decisions

- **Gray Merchant of Asphodel stays.** Red-team verification identified its real deterministic/near-deterministic engine role with Mikaeus, the Unhallowed + Yawgmoth, Thran Physician plus another qualifying nontoken non-Human body. Cutting it for generic copy value would weaken an existing compact creature-combo package.
- **The Ozolith stays.** It remains one of the cleanest ways to conserve +1/+1-counter equity when Marchesa creatures die and therefore supports the commander's defining resource rather than merely adding generic value.
- **Sage of Fables** is a high-value persist/counter piece: it gives Wizard creatures +1/+1 counters, resets Glen Elendra Archmage / Puppeteer Clique persist states, and converts counters into cards.
- **Gev, Scaled Scorch** turns opponent life loss into +1/+1 counters on entering creatures and directly supports a Murderous Redcap persist loop.
- **Spark Double** is flexible copy redundancy and participates in a Murderous Redcap + Ashnod's Altar loop while naturally entering with a +1/+1 counter when copying a creature.
- **Satoru, the Infiltrator** turns Marchesa/persist returns into card draw because those creatures enter without being cast.
- **Twilight Diviner** directly amplifies graveyard returns by copying a qualifying creature entering from a graveyard once each turn.
- **Danny Pink** turns routine +1/+1 counter placement into card draw and adds another counter-placement vector through mentor.
- **Agatha's Soul Cauldron** provides instant-speed counters, graveyard interaction, and activated-ability reuse; it is more commander-specific than Black Market Connections.
- **Altar of Dementia** adds another free sacrifice outlet and gives deterministic creature loops a noncombat mill finish.
- **Imperial Recruiter** improves access to a large share of the engine and combo creature suite.
- **Sneak Attack** is more Marchesa-specific than Animate Dead: it provides haste, immediate dethrone access, ETB deployment, and exploitable sacrifice sequencing.
- **Flare of Denial** keeps premium countermagic while its alternate cost can sacrifice a blue nontoken creature that Marchesa may later return.
- **Vampiric Tutor** is generic power, but at this deck's optimized ceiling it materially improves assembly of commander-native engines rather than replacing the strategy.
- **Forge of Heroes** gives a newly entered commander an immediate +1/+1 counter, creating commander-specific recursion insurance. The land upgrade package otherwise increases fetch density and untapped colored access while preserving one fetchable Grixis tri-land in Xander's Lounge.

## Rules / combo red-team

Verified functional packages include:
- Gev + Murderous Redcap after an opponent has lost life that turn.
- Spark Double copying Murderous Redcap + Ashnod's Altar.
- Sage of Fables + Glen Elendra Archmage or Puppeteer Clique + an appropriate sacrifice outlet.
- Mikaeus + Yawgmoth + Gray Merchant plus another qualifying nontoken non-Human creature.

Marchesa's trigger was checked carefully: when a creature with a +1/+1 counter dies while Marchesa's ability can trigger, it creates a delayed return for the beginning of the next end step. A creature sacrificed after the beginning of an end step will therefore wait until the following end step; Sneak Attack's beginning-of-end-step sacrifice should not be described as an immediate same-step Marchesa return.

## Mana-base red team

The candidate remains at **34 lands**. Premium duals, five-color lands, and three additional fetchlands replace slower conditional/tapped sources. Forge of Heroes replaces one basic Swamp as a commander-specific utility land. Xander's Lounge remains as a fetchable three-color source.

## Closure

- Current FINAL membership reconciliation: **COMPLETE**
- Mandatory 99-slot whole-list audit: **COMPLETE — 78 KEEP / 21 CUT**
- Candidate exhaustion: **COMPLETE**
- Commander-identity review: **PASS**
- Adversarial red-team: **COMPLETE**
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**
- Exact structure: **100 cards / 34 lands / 98 distinct names; only basic lands repeat**
- Singleton compliance: **PASS**
- Commander color identity: **PASS — U/B/R only**
- Current Oracle/rules/combo verification: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE**

The exact SHA-bound candidate is approval-ready. No approval or lock may be written until the user explicitly approves it.
