# Be'lakor, the Dark Master — M7 Rev2 owner approval and canonical locking

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED** for tracker deck #7, exactly the eight-swap candidate with raw SHA-256 `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`.

## Exact owner authorization
Cory responded immediately after ChatGPT displayed the complete M7 Rev2 100-card decklist, all eight one-for-one swaps, Power Bracket 4, three Archidekt tags, exact raw SHA-256 `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`, and engineering PR #682:

> Approve

The preceding assistant message asked for owner approval of *this exact eight-swap M7 Rev2 list* and stated that any canonical lock would require the owner's response. The word "Approve" refers only to this identified deck/list/SHA, not a blanket delegation, not a general "Proceed", and not a waiver of technical checks or an acceptance of aggregate M6.10/M7/M8 milestones.

## Historical and canonical source preservation
- New approved artifact: `refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt`, exact raw `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`.
- Historical October 13 Be'lakor approved list remains at `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt` with SHA `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`. Preserve its bytes.
- The tracker ID is `Be_lakor__the_Dark_Master` (double underscore). The canonical registry key is `Be_lakor_the_Dark_Master` (single underscore). These are historically different and must remain distinguished.
- Independent engineering review: [PR #682](https://github.com/corymstover/GrokBotMTGCompanion/pull/682), exact head `bcf3e8fc40f1084c0a612c368b1ecba5899be884`, stacked on preserved unmerged first-pass PR #655. First-pass proposal SHA `62a96b4f39584fa38947843bea352de923b29d7b266b57fce5918802a79b57bf` is research only.
- GitHub Actions exact-head [run #40050434686](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40050434686): **SUCCESS**, seven new source-bound Rev2 tests and four first-pass candidate regressions.

## Eight owner-approved one-for-one changes

| Add | Remove | Source-bound commander-first reasoning |
| --- | --- | --- |
| Desecration Demon | Dream Devourer | Six-power Lord ETB instead of zero; combat tap risk acknowledged. |
| Kindred Dominance | Blasphemous Act | Demons survive the one-sided wipe; seven-mana cost vs cheap symmetric reset acknowledged. |
| Demonlord Belzenlok | Rakdos, Patron of Chaos | Copyable ETB card draw; variable yield and self damage acknowledged. |
| Shadowgrange Archfiend | Bloodthirster | Immediate eight-power Lord hit; opponents sacrifice their strongest creature and gain life equal to the greatest power among sacrifices, not the sum; loses extra-combat ceiling. |
| Cursed Mirror | Fellwar Stone | Seven mana rocks retained. Three-mana red rock can temporarily copy a Demon with ETB/legend rule caveats. |
| Curse-Marred Demon | Balor | Four-mana copyable tutor-then-random-discard Demon; searched card can be discarded. |
| City of Brass | Crumbling Necropolis | Untapped reliable colors; life-payment/damage risk. |
| Mana Confluence | Foreboding Ruins | Untapped reliable colors without revealing a type; paid life each use. |

## Verification and explicit limitations
- **Exactly 100 physical cards** across **94 card names**, all nonbasics singleton; Island ×3, Mountain ×2, Swamp ×4.
- **One commander Be'lakor**, Grixis U/B/R identity; **36 lands, 25 printed Demons, seven reusable mana rocks**; Dark Ritual is one-shot.
- All 94 selected names source-bound to current 2026-10-23 live Scryfall Oracle records archived in first-pass #655 and contemporaneous canonical Ashnod land receipts; official Commander `legal`, color identity U/B/R subset, Oracle IDs/text captured; **no project exceptions**.
- Five unchanged Game Changers: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor. **Power Bracket 4 — Optimized**; **Demon Tribal / ETB Damage / Reanimator**.
- Known kicked Rite of Replication on Be'lakor has 25 finite Lord triggers before doublers, not an infinite loop. Roaming Throne and Panharmonicon can also multiply dangerous draw/life-loss Prince triggers. Cursed Mirror copying a legendary Demon does not override the legend rule.
- The first-pass scoped M6 I/J sealed bundle describes the earlier five-swap proposal, **not** the owner-approved eight-swap Rev2; it is not relabeled or silently inherited. Rev2's separate selected-Oracle snapshot, rule/strategy judgment and focused exact-source tests provide bounded candidate-specific verification. No updated Commander Spellbook exhaustive full-list lookup, full multiplayer playtest, statistical ranking, or new formal M6 I/J seal is claimed.
- Pass C owner-equivalent review is expressly **non-independent**, under Cory's existing waiver. Earlier M7 locked decks remain unchanged.
