# Abaddon Step 5 — Blasphemous Act Interaction Check

**Date:** 2026-10-13 UTC  
**Branch:** `refinement/campaign-2026-10-12`  
**Deck changes:** None  
**Finalization gate:** NO

## Current card text

Blasphemous Act is a red sorcery with mana value 9 ({8}{R}). It costs {1} less for each creature on the battlefield and deals 13 damage to each creature. Its cost reduction cannot reduce the total casting cost below {R}.

## Commander-specific findings

1. **Own-board opportunity cost:** Abaddon's list relies on several small or mid-sized creature engines, including Thermo-Alchemist, Kessig Flamebreather, Storm-Kiln Artist, Birgi, Bloodletter of Aclazotz, Solphim, Neheb, Rakdos and Abaddon itself. A resolved 13-damage-to-each-creature effect normally destroys these creatures too, absent damage prevention, indestructible, sufficiently increased toughness, or another applicable protection effect. Blasphemous Act is therefore a board reset with a real engine-rebuild cost, not one-sided removal.
2. **No direct Abaddon threshold contribution:** the damage is dealt to creatures, not players. It does not itself cause opponent life loss and does not increase Abaddon's threshold through creature damage.
3. **Abaddon may grant cascade before the wipe resolves:** if cast from hand during your turn while Abaddon is on the battlefield and opponents have already lost at least 9 aggregate life this turn, Blasphemous Act qualifies for Abaddon's cascade grant. Its mana value remains 9 even when creature-count reduction makes it cost only {R}. Cascade resolves before the original sorcery; any creature cast from the cascade resolution will normally be on the battlefield when Blasphemous Act resolves and can also take the 13 damage. The cascade hit can still generate immediate value, but a creature hit is exposed to the pending wipe.
4. **Cost and sequencing:** the cost reduction counts creatures on the battlefield as Blasphemous Act is cast; the total cost is determined before mana abilities are activated to pay it. Players may respond after the spell has been cast, but not between announcement and calculation/payment of its casting cost.

## Strategic disposition

The card retains a distinct role as an efficient emergency reset against creature-heavy boards. Its drawback is material because it can remove Abaddon's damage, mana and cascade-support engines alongside opposing creatures. The rules check alone does not prove it should be cut; retain the current baseline pending a comparative, commander-specific reason to replace it. No card change is proposed here.

## References

- [Current Blasphemous Act Oracle text and rulings (Scryfall-sourced card page)](https://www.mtg.wtf/card/40k/204/Blasphemous-Act)
- [Scryfall card page](https://scryfall.com/search?q=%21%22Blasphemous+Act%22)
- [Official Magic rules landing page](https://magic.wizards.com/en/rules)

## Disposition

**CHECKED — material rules and own-board trade-off documented.** This closes the Blasphemous Act contextual question only. It does not close every per-card disposition, the fresh exact-list Oracle/color-identity and legality checks, final independent list/hash verification, or the explicit user-approval gate.
