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

## Step 3 priority list and disposition

1. **Top-deck/cascade sequencing — CHECKED:** Brainstorm, Ponder, Mystical Tutor, Imperial Seal, Vampiric Tutor and fetchland shuffles. Mana-value-1 setup spells cannot cascade into a lower mana-value card.
2. **Alternate/free-cost spells — CHECKED FOR NAMED MATERIAL CASES:** Deadly Rollick, Deflecting Swat, Fierce Guardianship, Force of Will, Force of Negation and Pact of Negation. Nightscape Familiar's cost reduction was separately role-triaged; costs paid do not change mana value.
3. **Jeska's Will/exile payoffs — CHECKED:** actual spells cast from exile can trigger relevant payoffs but do not receive Abaddon's hand-only cascade grant. Copies are not casts.
4. **Thermo-Alchemist — CHECKED:** its damage can raise the threshold only before the spell whose cascade eligibility depends on that damage is cast.
5. **Breach resource tension — WORKED SEQUENCE RECORDED:** the Breach/LED/Brain Freeze line is rules-coherent from its documented starting state and fuel assumptions, not an unconditional infinite. Cabal Ritual and Chrome Mox constraints are role-triaged.
6. **Channel/land-type effects — ROLE-TRIAGED:** Otawara, Takenuma, Urborg, fetchlands and Xander's Lounge have relevant functional notes; reopen only for a concrete contradiction.
7. **Blasphemous Act — CHECKED:** creature-only damage, own-engine loss, mana-value-9/cost reduction, and Abaddon cascade timing are documented in [Step 5 note](Abaddon_Step_5_Blasphemous_Act_Interaction_Check_2026-10-13.md).
8. **Harnfel face and Bituminous Blast — CHECKED:** see [Abaddon Step 4 Context Check](Abaddon_Step_4_Context_Check_2026-10-13.md).

These dispositions record bounded checks, not the final 94-name live Oracle/identity certificate.

## Stop rule

No new candidate search, no rerun of the inconclusive Aurora Phoenix vs Mind's Desire Forge comparison, and no decklist changes. Only material interaction claims from this list move to detailed Step 3 verification.


## Step 5 result

Blasphemous Act's deck-specific context check is complete. No swap was justified by rules review alone. The next bounded gate is a fresh exact-list Oracle text and color-identity refresh for the frozen 94-name Abaddon list, keeping legality and final approval as separate checks.
