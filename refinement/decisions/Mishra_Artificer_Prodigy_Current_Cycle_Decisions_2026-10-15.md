# Mishra, Artificer Prodigy — Current-Cycle Decision Closeout

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d`  
Status: **APPROVED / LOCKED**

## Source reconciliation

The authoritative current FINAL CSV/TXT exports reconcile at exactly 100 cards / 100 distinct names. Raw FINAL TXT SHA-256: `33f6524ee7458a62995850fe888236fa494b59a45875ce0c8af4b6f229a3b67f`. Normalized current-cycle project-format baseline SHA-256: `98b13427fc4c901bd040baaa79b2cd06c2cdc1d4efb844326cec8da8a0e7ed34`.

The current `deck_card_audit.csv` reconciles 100/100 baseline card names with no review flags, color-identity failures, or official-legality failures. Current FINAL exports control membership.

## Commander blueprint and natural ceiling

Mishra is an artifact spell / parity-breaking stax-combo commander. The optimized strategy deliberately pairs his cast trigger with symmetrical effects that counter, redirect, or otherwise disrupt artifact spells. Because Mishra triggers when the artifact is cast, the deck can allow its own artifact spell to be countered or moved and then use Mishra's trigger to find a card with that spell's name in graveyard, hand, or library and put it directly onto the battlefield.

This makes Blood Funnel, Nether Void, Nullstone Gargoyle, Possibility Storm, and the added Chalice of the Void / Void Mirror / Vexing Bauble / Planar Chaos package commander-specific asymmetry rather than generic stax. The remainder of the list supports fast artifact mana, compact artifact combo engines, recursion, tutors, and enough stack interaction to defend the engine.

Natural ceiling: **Power Bracket 5 — cEDH (fringe / commander-centric artifact stax-combo)**.

## Exact approved changes

1. An Offer You Can't Refuse -> Swan Song
2. Biotransference -> Force of Negation
3. Buried Ruin -> Mana Confluence
4. Darksteel Forge -> Void Mirror
5. Master Transmuter -> Vexing Bauble
6. Mirrodin Besieged -> Planar Chaos
7. Padeem, Consul of Innovation -> Chalice of the Void
8. Rakdos Signet -> Grim Monolith
9. Sai, Master Thopterist -> Transmute Artifact
10. Simulacrum Synthesizer -> Force of Will
11. Vedalken Archmage -> Uthros Research Craft
12. Xander's Lounge -> City of Brass

## Material decisions

- **Void Mirror, Vexing Bauble, Chalice of the Void, and Planar Chaos** are direct Mishra parity breakers. With correct trigger ordering, a qualifying artifact spell can be countered first, then Mishra can recover that named card from the graveyard and put it onto the battlefield.
- **Possibility Storm** is retained as one of the strongest commander-identity cards. For an artifact spell cast from hand, its trigger can resolve before Mishra's, move the original card through exile to the bottom of the library, and cast a replacement. Mishra's original trigger can then find the original artifact in the library and put it onto the battlefield.
- **Vexing Bauble / Void Mirror + Possibility Storm** create a powerful spell-from-hand lock structure against opponents because the free replacement spell is normally exposed to the counter effect while opponents lack Mishra's recovery trigger. This is not represented as an unconditional lock on all spells or abilities; additional-cost mana, uncounterable effects, trigger interaction, and spells not cast from hand can matter.
- **Uthros Research Craft** is a lower-cost artifact-centric draw engine. Mishra's power 4 can station it to three or more station counters in one activation, after which its artifact-cast trigger can draw even when the artifact spell is later countered.
- **Swan Song, Force of Negation, and Force of Will** increase efficient stack protection at the natural cEDH ceiling without displacing the artifact-stax identity.
- **Transmute Artifact** is a high-efficiency artifact-specific tutor that directly assembles lock and combo pieces.
- **Grim Monolith** materially improves speed and artifact-mana density over Rakdos Signet.
- **City of Brass and Mana Confluence** improve untapped three-color access. Buried Ruin is expendable because Academy Ruins, Emry, Goblin Welder, Goblin Engineer, Scrap Trawler, Myr Retriever, and Junk Diver already provide substantial artifact-recursion redundancy.
- **Fabricate stays.** It remains a clean artifact tutor and survives the red-team pass; cutting it for Transmute Artifact would remove useful tutor density rather than upgrade a genuinely weak slot.
- **Biotransference, Darksteel Forge, Master Transmuter, Mirrodin Besieged, Padeem, Sai, Simulacrum Synthesizer, and Vedalken Archmage** are functional cards, but at this ceiling they are slower or less commander-specific than the incoming parity breakers, free interaction, tutor, and Uthros engine.

## Retained combo / lock packages

- **Mystic Forge + Sensei's Divining Top + artifact cost reducer + Aetherflux Reservoir**: repeated Top casts/draws generate Reservoir life gain and a lethal activation.
- **Bolas's Citadel + Sensei's Divining Top + Aetherflux Reservoir**: repeated Top casting from the library converts life into casts while Reservoir gains escalate toward lethal range.
- **Krark-Clan Ironworks + Scrap Trawler + Myr Retriever / Junk Diver** remains the artifact-recursion core; with appropriate cost reduction and sequencing it supports repeated casts and mana generation, with Aetherflux Reservoir as a payoff.
- **Karn, the Great Creator + Mycosynth Lattice**: Lattice makes permanents artifacts and Karn prevents opponents from activating abilities of artifacts; together this shuts off activated abilities of opposing permanents, including mana abilities of lands. The deck does not rely on Karn's outside-the-game wish ability.
- **Mycosynth Lattice + overloaded Vandalblast**: Lattice makes opposing permanents artifacts and overload destroys artifacts you do not control, leaving your permanents intact.

## Rejected challengers after red-team

Serious challengers reviewed and rejected include Ice Cave, Shimmer Myr, Liberator, Urza's Battlethopter, Mishra's Bauble, Lotus Petal, Gemstone Caverns, The Mycosynth Gardens, Darksteel Citadel, Torpor Orb, Cursed Totem, Winter Orb, Static Orb, Trinisphere, Thassa's Oracle / Consultation packages, and Underworld Breach packages. They either add insufficient commander-specific value, impose meaningful internal costs, lose to the retained slot on consistency, or push the deck toward generic Grixis cEDH homogenization without improving the commander's own strategy enough.

## Whole-list closeout

- Current FINAL membership reconciliation: **COMPLETE**
- Mandatory 99-slot whole-list audit: **COMPLETE — 87 KEEP / 12 CUT**
- Candidate-ranking review: **COMPLETE; rankings treated as research, not mandates**
- Current Mishra optimized/cEDH evidence review: **COMPLETE**
- Commander-identity review: **PASS**
- Adversarial rules/combo red-team: **COMPLETE**
- Mana-base red-team: **PASS**
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**
- Exact candidate structure: **100 cards / 100 distinct names / 29 lands**
- Singleton compliance: **PASS**
- Commander color identity: **PASS — U/B/R only**
- Current Oracle/rules/combo verification: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE**

## Approval state

The user explicitly approved this exact SHA-bound candidate on 2026-10-15. The canonical approved artifact is `refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt` and the approval record is `refinement/approvals/Mishra_Artificer_Prodigy_Approved_2026-10-15.md`.

This deck is **APPROVED / LOCKED** for the current refinement cycle and must not be revised, reopened, or replaced unless the user explicitly requests it.
