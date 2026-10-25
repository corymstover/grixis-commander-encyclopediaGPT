# Deck #30 Lord Xander M7 Rev1 — decisive whole-99 review

**Owner-approved raw SHA:** `de348618961269083a44a3f3e05a7f0be7ddbd7e943da0ac82a115e5e4aeb6cd`.
**Baseline raw SHA:** `92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787`.

Lord Xander's three seven-mana trigger roles—ETB half-discard, declared-attack half-mill, and dies half-nonland sacrifice—determine card choices. The nine replacements reduce an independent Breach/LED/Brain Freeze shortcut, wheel draw-denial and some free permission in exchange for actual commander-zone access, haste, native graveyard reanimation, own-targetable protection/cloning, and mill-to-life conversion. This is a deliberate natural-Bracket-4, commander-first decision, not a claim that a generic fast-combo shell would never win earlier.

| Add | Removed incumbent | Decisive role and paid tradeoff |
| --- | --- | --- |
| Hellkite Courser | Lion's Eye Diamond | 4RR enters and puts owned Xander from command zone with haste; nonlegendary Courser is a valid retained Persist/Entomb reanimation target. Sacrifices burst mana. |
| Syr Konrad, the Grim | Brain Freeze | Opponent creature cards milled by Xander create one damage per card to each opponent. Costs 3BB; removes old Breach line. |
| Necromancy | Underworld Breach | Recurs actual legendary Xander or another creature from graveyard, replacing a commander-independent engine. Vulnerable to graveyard hate and aura removal. |
| Bloodchief Ascension | Maddening Cacophony | Life-drain on opponents' graveyard entries after the third quest counter, cooperating with Mindcrank; loses a standalone scalable mill spell. |
| Irenicus's Vile Duplication | Notion Thief | 3U makes a persistent flying nonlegendary Xander with ETB and later attack triggers; loses Wheel/draw denial. |
| Goryo's Vengeance | Orcish Bowmasters | 1B instant, legendary graveyard Xander return with haste; end-step exile is not death. Loses cheap Bowmasters draw punishment. |
| Samut, Hazoret's Champion | Pact of Negation | Two-mana global haste ensures a newly arrived Xander can actually attack; gives up emergency free stack denial. |
| Malakir Rebirth // Malakir Mire | Force of Negation | One black protects Xander against ordinary destruction by causing dies and another ETB; tapped black MDFC option. Gives up opponent-turn free noncreature permission. |
| Swiftfoot Boots | Lightning Greaves | Hexproof/haste permits one's own targeted Xander copies, equips and revival spells instead of shroud; equip costs one extra. |

Protected identity cards include Auton Soldier, Hall of Echoes, Spark Double, Sakashima, Helm of the Host, Phantasmal Image, Blade of Selves, Saw in Half, Strionic Resonator, Roaming Throne, Fraying Sanity, Bruvac, Riverchurn Monument, Altar of Dementia, Duskmantle Guildmage, Mindcrank, Persist, Bojuka Bog, Aggravated Assault, Sword of Feast and Famine and Karlach. The owner-added Hall and owner-keep Persist are explicitly honored; Persist targets *Courser*, never legendary Xander directly. Bojuka remains the only targeted land graveyard-exile slot rather than being displaced by Malakir.

## Post-nine-swap open-ended challenge

Actual 100-card alternatives are SHA-bound in engineering PR #708:

- **10 substitutions**: Waste Not for Riverchurn Monument, raw SHA `46814512c3107cd7a68017a60241e3ef3f052e2f766bcf73d57b9df85d82c92d`. Rejected: Waste Not weakens when Xander has depleted hands; Riverchurn once-only exhaust can finish a half-milled library.
- **11 substitutions**: previous plus Rite of Replication for Karlach, raw SHA `b57eae60e33e1a544ca3348f5e8e1cd68c2be78d9442b24d243a608579c7653c`. Rejected: loses native extra declared attack and asks for a nine-mana kicked copy turn.
- **12 substitutions**: previous plus Echoing Assault for Swan Song, raw SHA `3fe4c6ed1ad3a5113dc1d1594aff3c9837c2f113efdab4692b88b1ccba3d9278`. Rejected: five-mana attack-dependent engine displaces the last important single-blue cheap protection.

Other material candidates individually challenged: Displacer Kitten, Kaya's Ghostform, Phyrexian Tower, Sneak Attack with Command Beacon, Flameshadow Conjuring, Jaxis, Flesh Duplicate, Thassa, Anger, Rising of the Day, Geode Golem, The Master of Lake-town, and Panharmonicon. The whole original 99, weakest 15 slots, current Scryfall 97 selected identities and commander-specific EDHREC Clones/Reanimator inclusion, optimized niche and historical High Synergy (not fabricated High Lift) informed the review. No artificial swap cap or minimum dictated nine.

## Reproduction, source limits and safety

- Exact full M7 packet: `data/grixis/m7/decision_reviews/Lord_Xander__the_Collector_rev1.json` in [engineering PR #708](https://github.com/corymstover/GrokBotMTGCompanion/pull/708).
- Fresh Scryfall Oracle/legality index for all 97 names mirrored in `refinement/verification/Lord_Xander_the_Collector_M7_Rev1_Oracle_Identity_Index_2026-10-25.json`.
- Paid finite-case 5 P0 + 9 P1 exact source tests and all other applicable engineering gates PASS on final head `fcff8a8a4aa184c144daaaab4f12974d7ed486d4`, run https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40185256873.
- Old Pass C owner-equivalent Stage A reviewer was technically non-independent. Owner-authorized versioned SHA correction preserves the wrong original seal and actual Stage A evidence rather than silently rewriting history; related [PR #709](https://github.com/corymstover/GrokBotMTGCompanion/pull/709) was verified and merged independently.
- The October 14 old approved source and old approval receipt remain unmodified. The new lock applies only to the owner-approved exact Rev1 bytes.
