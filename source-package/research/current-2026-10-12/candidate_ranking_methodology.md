# Candidate ranking methodology — v8.1.4

The output `commander_candidate_rankings.csv` is a research triage list, not an objective card-power ranking. Candidates are checked against canonical card identity, effective Commander legality, target commander color identity, and exclusion from the target deck. Candidate sources include EDHREC evidence and optional, specifically selected Archidekt lists. Archidekt is not required and does not contribute to the default composite score.

## Default score components
- **EDHREC inclusion percentile (30%):** relative adoption for this commander.
- **EDHREC Lift percentile (30%):** association/distinctiveness evidence, not direct card strength.
- **EDHREC legacy synergy percentile (25%):** percentile of the source-provided synergy metric within this commander’s candidate pool; heuristic only.
- **Commander Oracle-text mechanic relevance (15%):** proportion of distinctive phrases extracted from the resolved commander Oracle text that appear literally in candidate name or Oracle text. Manually supplied strategy terms are additive. This is not semantic rules analysis.

Missing components are omitted and remaining weights renormalized. `evidence_coverage_pct` records the nominal weight represented. `evidence_confidence` describes evidence volume, not certainty about card quality.

## Limitations and safeguards
- EDHREC inclusion and Lift are observational measures; neither proves a card belongs in a specific build.
- Oracle phrase matching misses synonyms and context and can produce false positives. Inspect the candidate Oracle text and gameplay role.
- The EDHREC legacy synergy field is treated as a heuristic source signal, not as a validated power metric.
- No decklist is modified and no swap is automatically approved. Review commander identity, role, interaction, opportunity cost, project legality exceptions, and natural power ceiling before proposing changes.

Weights used this run: `{"edhrec_inclusion_percentile": 0.3, "edhrec_lift_percentile": 0.3, "edhrec_legacy_synergy_percentile": 0.25, "oracle_text_relevance_pct": 0.15}`.
