# Cult of Skaro M7 Rev2 — exact owner-approved source verification

**Approved raw SHA-256:** `e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d`.  
**Historical Oct14 source raw:** `4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b` (preserved byte-exact).  
**Owner approval:** Cory replied **“Approve”** on 2026-10-23 America/Chicago after full nine-swap 100 and hash presented. Not blanket approval.  
**Engineering:** [PR #686](https://github.com/corymstover/GrokBotMTGCompanion/pull/686), exact `426d8afcd76924ee1c036d91a91dc33abd1d79f7`, all four targeted workflows SUCCESS.

## Structural/Oracle

- Exactly 100 physical, 96 distinct card names, one Cult of Skaro commander, 99 library. Island x2, Mountain x3, Swamp x2 are the only duplicate names. All other names singleton.
- 34 lands, 9 mana rocks, 3 cost reducers (Etherium Sculptor, Enthusiastic Mechanaut, Shuri), 3 Game Changers (Cyclonic Rift, Fierce Guardianship, Mana Vault).
- Official Commander legal all 96; commander color identity UBR for all; full Oracle IDs and text in the canonical selected snapshot. Source inputs: Grok #659 Oct23 Cult 210-name live Scryfall frozen research and Crosis M7 selected Oct23 current Scryfall cards Otawara/Takenuma. No project exceptions or unresolved card identities.
- Original Oct14 full approved 100 bytes and old mismatch provenance preserved; swaps verified against exact approved-source physical multiset, not old tracker prose.

## Bounded commander-specific rules (not a gameplay simulator)

- Cult {1}{U}{B}{R}: on **attack declaration** choose one random mode (counters/artifact army, draw two, menace Dalek token, or opponent loses four). Tokens **entering tapped and attacking** from Shaun and myriad do not retro-trigger Cult. Next turn, retained copies can be declared and trigger.
- The Master, Multiplied prevents triggered abilities *we control* from causing sacrifice/exile of tokens *we control* while its continuous effect applies, including Shaun's leaves-battlefield trigger and myriad's delayed exile. The Master is retained; it cannot prevent an opponent-origin exile spell or state-based actions.
- Shaun + Karlach can make extra Cult declarations when new Synth tokens have haste, provided by Hammer of Purphoros or the Dalek Emperor; untapping alone does not negate summoning sickness.
- Kindred Discovery naming Dalek triggers when a Dalek enters or attacks; Resonator/Scientist copy a previously selected random trigger mode; Roaming Throne makes a distinct independently chosen trigger. Reverse the Polarity costs exactly **{1}{U}{U}**, and counters all other spells or makes creatures unblockable. It does not substitute for removing a resolved nonhistoric permanent the way Desynchronization did.
- Existing conditional Sword of Feast and Famine + Aggravated Assault repeat-combat line retained; no deterministic infinite or measured multiplayer win-rate claim.

## Governance / CI

- **Nine expressly approved** full 100. Original six-swap Grok formal I/J is **not** re-sealed; independent additive source-bound tests only.
- Canonical PR is the sole authority once exact-head checks PASS and merge occurs. After merge, refetch main approved artifact and verify raw SHA plus no other 61 registry changes.
