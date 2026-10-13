# Abaddon Baseline Metadata and Identity Closeout — 2026-10-13

**Purpose:** document the deck-specific metadata evidence available for the frozen Abaddon list before final approval.  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Baseline membership:** unchanged; no card changes.  
**Finalization status:** NOT APPROVED / final gate NO.

## Verified evidence already committed

- The frozen source package and compact decklist archive were integrity checked. The compact archive contains 62 CSV + 62 TXT decklists; all 124 files match the source package byte-for-byte.
- The global current Scryfall metadata refresh matched 5,964/5,964 current decklist rows to exact set + collector number + card name records. It reported no unmatched/ambiguous printings, missing Oracle IDs, blank Oracle text, unresolved commanders, commander color-identity mismatches, or unexpected official Commander-illegal rows outside registered exceptions.
- The Abaddon static audit (CI run 38345446231, as logged in the tracker) joined 94/94 unique Abaddon card names to deck-scoped metadata rows and verified the frozen TXT hash, 100-card total, one commander, and zero nonbasic singleton violations.
- The current Scryfall bulk snapshot recorded in the audit summary was updated at 2026-10-12T21:06:24.577Z. The exact-printing metadata refresh is valid for that timestamp; it is not a live refresh as of final approval.

## Commander and special status

Abaddon the Despoiler has mana cost {2}{U}{B}{R}, mana value 5, and Grixis color identity. The blueprint and interaction review correctly use five as its mana value. The official Commander ban-list checkpoint was checked 2026-10-13 and found no Abaddon baseline card on that list. No Abaddon-specific project legality exception is identified in the tracker.

## Remaining limitations — do not mark complete

- The evidence above is a reproducible static audit and a dated global metadata refresh, not an independent live Oracle/rulings re-fetch for every Abaddon card on the approval date.
- The tracker’s closeout instruction calls for a fresh official legality check at approval and an independent final count/singleton/color-identity/hash check.
- The exact list has not yet been presented to the user as a final approval proposal in this campaign.
- No gameplay win-rate claim is supported. The Aurora Phoenix vs Mind’s Desire Forge pilot was inconclusive and is closed for that engine/setup.

## Gate decision

The metadata and structural evidence is strong enough to preserve the baseline, but this note does not replace the remaining closeout steps. Final gate remains **NO** until the last exact-list verification and the user’s explicit approval are recorded.
