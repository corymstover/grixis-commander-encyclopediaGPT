# Be'lakor, the Dark Master — Final Verification and Lock Record

**Date:** 2026-10-13  
**Status:** AUTO-APPROVED / LOCKED — standing user instruction applied after verification  
**Frozen baseline:** `GrixisFINALTXT60--2026.zip`, member `Be_lakor__the_Dark_Master.txt`; preserved unchanged  
**Frozen baseline TXT SHA-256:** `9b0e16a43add999252504948aa3104666a342bf4f8c80b758a2d9f65649fe6c7`  
**Final clean-list SHA-256 (UTF-8, LF, trailing newline):** `fff4ca3411067a0de6012c9252f651cc0807a68216b8dd2415e48f9c0c3c0230`

## Exact change

- Cut 1x Raphael, Fiendish Savior.
- Add 1x Ardyn, the Usurper.
- No other card or quantity changed.

## Structural integrity

- Total cards including commander: **100**.
- Distinct card names: **95**.
- Commander: exactly one, Be'lakor, the Dark Master, on the first line.
- Singleton: **PASS**. Only Island x3, Mountain x2, and Swamp x4 repeat; all repeated names are basic lands.
- One-for-one delta: **PASS**.

## Oracle, identity, legality, and rules

- Ardyn, the Usurper costs `{5}{B}{B}{B}`, is a 4/4 legendary creature, and has mono-black color identity; it fits Be'lakor's UBR identity.
- Current Oracle text: “Demons you control have menace, lifelink, and haste. Starscourge — At the beginning of combat on your turn, exile up to one target creature card from a graveyard. If you exiled a card this way, create a token that's a copy of that card, except it's a 5/5 black Demon.”
- Ardyn is Commander-legal. Current Oracle and ruling evidence: https://www.mtg.wtf/card/fin/89/Ardyn-the-Usurper and https://www.mtgseeker.com/card/fin/444/ardyn-the-usurper
- Be'lakor's Demon-entry ability triggers for the token Ardyn creates because that token is a Demon entering under your control. It does not trigger for Ardyn itself because Ardyn is not a Demon.
- If the copied creature card has an enters-the-battlefield ability, the token copy retains that ability and it triggers as the token enters. Official ruling summary: https://www.mtgseeker.com/card/fin/444/ardyn-the-usurper
- Raphael is a legal outgoing card; no legality or color-identity conflict is introduced.

## Strategic assessment

Ardyn replaces a static tribal bonus and narrow Devil recursion with a repeatable combat-step engine. Each turn, a creature card from any graveyard can become a 5/5 black Demon token, triggering Be'lakor's damage ability and any copied ETB ability. The token also benefits from Ardyn's menace, lifelink, and haste grant. This increases Demon-entry density while preserving the deck's existing Demon-copy, ETB, reanimation, and cost-reduction plan.

Tradeoff: Ardyn is eight mana and is not a Demon, so Demon-specific cost reducers do not reduce its cost. The deck has Heartless Summoning and other acceleration, but Ardyn is still a top-end investment. Raphael's +1/+1 bonus is lost. No gameplay win-rate or representative multiplayer testing claim is made.

## Final gate

- 100-card count: **PASS**.
- Singleton compliance: **PASS**.
- Commander identity and color identity: **PASS**.
- New card Oracle text and Commander legality: **PASS**.
- Be'lakor / Ardyn Demon-token ETB interaction: **PASS**.
- Frozen baseline preserved: **PASS**.
- Auto-approval: **APPLIED** under the user's standing instruction dated 2026-10-13.

No matched-start simulator or representative multiplayer playtest was available. No win-rate claim is made.
