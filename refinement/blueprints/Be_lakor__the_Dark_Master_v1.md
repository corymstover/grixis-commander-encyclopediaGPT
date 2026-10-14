# Be'lakor, the Dark Master — commander-first working blueprint

Status: WORKING, NOT APPROVAL_READY. Deck #7 in tracker order, after user-approved Ashnod (#6).

Frozen baseline: GrixisFINALTXT60--2026.zip / Be_lakor__the_Dark_Master.txt. Preserve exactly as supplied; no approved edits yet.

## Commander identity
Be'lakor is a six-mana Grixis Demon Noble with two distinct payoff axes: ETB draws cards and loses life equal to Demons controlled; every **other Demon entering under your control** deals damage equal to its power to any target. Therefore optimization should balance Demon density and meaningful power, ETB multipliers, token/copy effects, blink/reanimation, and life-total management. Do not convert into generic Grixis reanimator/control or force cEDH.

## Baseline engines to protect pending verification
- Molten Echoes, Reflections of Littjara, Roaming Throne, Panharmonicon, Rite of Replication: multiplication of Demon arrivals/trigger volume, with text and legend-rule details requiring precise review.
- Liliana's Contract: Demon count and distinct Demon-name alternate victory; verify upkeep timing and life loss.
- Sneak Attack, Patriarch's Bidding, Reanimate, Whip of Erebos, Herald of Slaanesh, Heartless Summoning: deploy or recur expensive Demons, with nonbo and power reduction checks.
- Archfiend of Despair, Bloodletter of Aclazotz, Sower of Discord: damage amplification; distinguish life loss from damage and timing.
- Gyruda, Doom of Depths, Burning-Rune Demon, Rakdos, the Showstopper: value and risk of high-variance triggers.

## Candidate screen priorities
- Varragoth, Bloodsky Sire (rank 1), Dream Devourer (rank 2), Bloodcrusher of Khorne (rank 3): assess low-curve Demon density and deployment setup against existing 6-8 mana creature congestion.
- Full top-100 candidate ranking must be reviewed without auto-inclusion. Each replacement must preserve Be'lakor-specific identity.

## Mandatory next checks
1. Reconcile exact baseline counts, source hashes, singleton and 3-color identity; inspect project audit freshness.
2. Evaluate all 99 noncommander slots and 100 candidates with explicit dispositions.
3. Verify Oracle/rulings for copies, legends, ETB multipliers, triggers, and death/recursion timing; legality.
4. Evaluate curve, Demon density, colored mana, life-payment exposure, and winning lines; red-team.
5. Prepare a full verified 100-card proposal only at approval gate. Do not lock without user approval.

## Prior deck status
Ashnod explicit approval recorded at refinement/approvals/Ashnod_the_Uncaring_Approved_2026-10-13.md, with approved decklist at refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt. Central registry synchronization is blocked by connector safety checks; do not treat absence of registry entry as permission to reopen Ashnod.
