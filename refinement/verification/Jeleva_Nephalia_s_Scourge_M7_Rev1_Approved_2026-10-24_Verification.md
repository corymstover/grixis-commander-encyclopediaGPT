# Jeleva, Nephalia's Scourge M7 Rev1 — whole-100 and owner-source verification

**Candidate raw SHA-256:** `6f2cdafa089c3e923104429f764bed66e500fe20cafb3b00dd4d29488bd52cac`. Owner explicitly replied “Approved” on 2026-10-24 after seeing the entire exact 100 and this SHA. Jeleva-only five-floor waiver and 23 independent whole-100 alternatives documented in [engineering PR #699](https://github.com/corymstover/GrokBotMTGCompanion/pull/699), exact head `6596a61f147a4f70efccea1e792dd5ffa982659f`.

## Exact source and preservation

- Historical canonical approved source `refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt`: raw SHA `00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f`, no terminal LF. Preserved unchanged.
- New exact candidate `refinement/decklists/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24.txt`: **100 lines**, commander first, single terminal LF, **100 distinct names** including one Island and one Swamp, no duplicate other cards.
- Only **two** additions `Cavern of Souls`, `Fire Covenant`; only two cuts `City of Traitors`, `Toxic Deluge`.
- **27 lands**, **45 instant/sorcery cards**, **20 Game Changers**. **11 top-deck stagers** and **four haste/flash pathways** retained.
- Power Bracket **5 — fringe cEDH**; tags `cEDH`, `Spellslinger`, `Combo`.
- Current M7 owners #1-#23 regression SHA lock preservation must PASS. Previously locked decks may not be changed without their own owner authorization.

## Oracle and legality provenance

Companion evidence `refinement/verification/Jeleva_Nephalia_s_Scourge_M7_Rev1_Oracle_Identity_Index_2026-10-24.json` contains **99** per-card records exactly from frozen Oct23 Scryfall 204-name research pool, all `commander_legality=legal` and B/R/U-subset identity, plus **one** separate Cavern official Wizards source entry. This is not falsely described as a fresh October 24 API refresh of 100 Oracle cards. Official Cavern source: https://magic.wizards.com/en/news/feature/the-lost-caverns-of-ixalan-release-notes ; official bans https://magic.wizards.com/en/banned-restricted-list . No project exceptions apply.

## Mechanics and opportunity costs

- Cavern named Wizard produces colored mana only for Wizard creature spells; Jeleva's Wizard creature spell cannot be countered only if such mana was spent casting it, and her triggered abilities remain vulnerable. Thassa's Oracle is also a Wizard; the ability does not itself secure Oracle's win trigger. Drannith Magistrate continues to block Jeleva from being cast from the command zone if present.
- City of Traitors taps for two generic mana: losing this can delay Jeleva, its commander tax, or a ritual/ramp line. The bounded no-turn/no-rock three-distinct-land UBR Wizard cost-coverage changes `1,975/2,925` → `2,250/2,925` (+9.40 percentage points) and is **not** simulated commander casting or win rate.
- Fire Covenant has an additional life payment equal to X even under Jeleva's attack ability (which waives only printed mana cost); its targeted damage must be divided among legal creatures. Instant selective removal keeps Jeleva and friends alive, but Deluge was untargeted -X/-X, more effective into indestructible/hexproof and multiple equal-toughness threats for one life payment. Normal casting cost `{1}{B}{R}` has stricter colored pip than Deluge's `{2}{B}`.
- Historic core is retained: linked Jeleva exile attack casting, Harmonic Prodigy triggers, Doomsday, Oracle / Consultation / Tainted Pact, Breach + LED + Brain Freeze, Mind's Desire, Yawgmoth's Will, 11 recognized topdeck stagers and four haste/flash pathways.
- No multiplayer games, win-rate estimate, Monte Carlo cast turn, comprehensive stack/rules simulation, fresh whole-100 live Scryfall API, or separate third-model attestation claimed.

## Fail-closed finalization

The narrow test `tests/test_jeleva_nephalia_s_scourge_m7_rev1_approval.py` asserts exact bytes, historical source, full 100/count/Oracle/legality, two deltas, owner waiver, registry/tracker, and 23 previous M7 locks. `.github/workflows/verify-jeleva-nephalia-s-scourge-m7-rev1-approval.yml` is configured for exact-head actions. Other M7 regression gates need to accept Jeleva's newly owner-approved successor while preserving original Oct14 source.

**Approval is not equivalent to merge**: post-merge independent main refetch and raw SHA/registry/tracker checks are required before reporting Jeleva canonically locked.
