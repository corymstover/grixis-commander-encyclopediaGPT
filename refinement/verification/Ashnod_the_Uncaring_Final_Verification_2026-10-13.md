# Ashnod the Uncaring — Final Verification and Lock Record

**Date:** 2026-10-13  
**Status:** AUTO-APPROVED / LOCKED — standing user instruction applied after verification  
**Frozen baseline:** `GrixisFINALTXT60--2026.zip`, member `Ashnod_the_Uncaring.txt`; preserved unchanged  
**Frozen baseline TXT SHA-256:** `d1b74569999818542ec3b787499c2a9e3d8a420c617af9b883cc875c324dd684`  
**Final clean-list SHA-256 (UTF-8, LF, trailing newline):** `8fd8f2ccac63371c880008b1931c7da3e99fcfa8a44b83074aeee30427386e2f`

## Exact change

- Cut 1x Commander's Sphere.
- Add 1x Trading Post.
- No other card or quantity changed.

## Structural integrity

- Total cards including commander: **100**.
- Distinct card names: **95**.
- Commander: exactly one, Ashnod the Uncaring, on the first line.
- Singleton: **PASS**. Only Island x3, Mountain x2, and Swamp x3 repeat; all repeated names are basic lands.
- One-for-one delta: **PASS**.

## Oracle, identity, legality, and rules

- Ashnod's current Oracle ability was reviewed: when a nontoken permanent is sacrificed to activate an ability or cast a spell, Ashnod copies that ability if this is the first time Ashnod's ability has triggered that turn. It triggers only once each turn.
- Trading Post's current Oracle text provides: gain 4 life; pay 1 life to create a 0/1 white Goat creature token; sacrifice a creature to return an artifact card from graveyard to hand; sacrifice an artifact to draw a card. The sacrifice modes include tapping Trading Post and paying one generic mana.
- Trading Post is colorless and has no white mana symbol or white color indicator; creating a white Goat token does not change the card's color identity. It fits Ashnod's UBR identity and is Commander-legal.
- Commander's Sphere is legal and has no identity issue.

## Interaction assessment

When Trading Post's creature-sacrifice mode resolves as an activation, sacrificing a nontoken creature can trigger Ashnod. If that is Ashnod's first trigger that turn, the ability is copied. The activation's cost is not paid a second time, so the same single sacrifice supports two artifact-card return effects. The artifact-sacrifice mode works similarly: one nontoken artifact is sacrificed, and the copied ability can draw an additional card. Ashnod's once-per-turn restriction means this does not multiply every activation in a turn cycle; it is a value engine, not an infinite-combo claim.

The change reduces one three-mana mana rock and raises the cost of the replacement by one mana, but adds flexible, repeatable graveyard recursion and card draw in a deck already dense with ramp, cost reduction, sacrifice outlets, artifact recursion, and artifact-death payoffs.

## Final gate

- 100-card count: **PASS**.
- Singleton compliance: **PASS**.
- Commander identity and color identity: **PASS**.
- New card Oracle text and Commander legality: **PASS**.
- Ashnod copy-trigger interaction: **PASS**.
- Frozen baseline preserved: **PASS**.
- Auto-approval: **APPLIED** under the user's standing instruction dated 2026-10-13.

No matched-start simulator or representative multiplayer playtest was available. No win-rate claim is made.
