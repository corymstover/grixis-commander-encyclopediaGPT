# Abaddon — Step 2 Role-Based Triage of Previously Unmentioned Cards

**Baseline:** 2026-10-12 frozen TXT; SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Decklist changes:** none  
**Status:** triage complete; material interactions selected for Step 3 verification; final gate NO

## Outcome

All **61** cards that were not explicitly named in the existing interaction review have been classified by role and triaged. This is a scoping pass, not a claim that all individual Oracle interactions have already been independently re-verified. See the companion CSV for every card, role, finding, and Scryfall lookup.

### Triage summary

- **Mana base / fetchlands:** ordinary color-fixing lands need no separate interaction review. Fetchland shuffle effects matter for Brainstorm/Ponder/Mystical Tutor/Vampiric Tutor top-deck setup. Otawara and Takenuma have channel abilities; Urborg modifies land types; Ancient Tomb and self-damaging lands do not increase Abaddon's threshold.
- **Fast mana and rituals:** most are ordinary acceleration. Chrome Mox and Cabal Ritual have relevant resource/threshold constraints; Nightscape Familiar reduces actual spell costs but does not change mana value.
- **Top-deck setup:** Brainstorm, Ponder, Mystical Tutor, Imperial Seal, and Vampiric Tutor can influence the card seen by cascade or the next draw. Their ordering is conditional; do not assume a guaranteed cascade hit.
- **Free interaction:** Deadly Rollick, Deflecting Swat, Fierce Guardianship, Force of Will, and Pact of Negation have alternate-cost/commander or delayed-payment conditions. Abaddon's grant still cares about casting from hand and mana value, not the spell's paid cost.
- **Cast-from-exile:** Jeska's Will's exile-cast mode does not satisfy Abaddon's hand-only grant, but it can trigger relevant cast-from-exile payoffs. This is a material package interaction.
- **Repeated threshold enabler:** Thermo-Alchemist is material because it pings each opponent and untaps when you cast an instant or sorcery; its damage can raise the current-turn cascade threshold.
- **Board wipe:** Blasphemous Act damages creatures rather than players; it can remove the deck's own creature engines but is not itself an opponent-life-loss threshold enabler.
- **Remaining ordinary roles:** routine draw engines, tutors, basic lands, and ordinary ramp have no additional deck-specific rules issue identified in this triage pass.

## Step 3 priority list

The following items merit sourced card-text/sequence verification before being marked closed:
1. **Top-deck and cascade sequencing:** Brainstorm, Ponder, Mystical Tutor, Imperial Seal, Vampiric Tutor, plus fetchland shuffles.
2. **Abaddon + cost-reduced/alternate-cost spells:** Nightscape Familiar, Deadly Rollick, Deflecting Swat, Fierce Guardianship, Force of Will, Pact of Negation, Force of Negation.
3. **Jeska's Will and exile payoffs:** confirm which payoffs trigger on the actual spell cast and which do not trigger from copies.
4. **Thermo-Alchemist threshold loop** and interaction with instant/sorcery casts.
5. **Breach resource tension:** Cabal Ritual threshold, Chrome Mox imprint, and Underworld Breach fuel.
6. **Channel / land-type effects:** Otawara, Takenuma, Urborg, fetchlands, and Xander's Lounge; close with source-backed notes where relevant.
7. **Blasphemous Act and own-board opportunity cost**; not a deck-specific rules ambiguity, but document its interaction with the creature engine.

## Stop rule

No new candidate search, no rerun of the inconclusive Aurora Phoenix vs Mind's Desire Forge comparison, and no decklist changes. Only material interaction claims from this list move to detailed Step 3 verification.
