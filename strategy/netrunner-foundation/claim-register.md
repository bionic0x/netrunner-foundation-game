# Claim and conflict register — source-derived allegations, not verified facts

**Vocabulary:** `EVIDENCE` = a primary or reproducible observation at the specified scope; `HYPOTHESIS` = plausible proposition requiring testing; `ASSUMPTION` = premise taken for exploratory design; `UNKNOWN` = missing or unusable evidence. Quantities also distinguish `MEASURED`, `ESTIMATE`, `TARGET`, `HYPOTHESIS`. An exact number in a whitepaper is not automatically `MEASURED`.

| ID | Statement in source corpus | Status | Required evidence / contradictory scope | Action |
|---|---|---|---|---|
| C-001 | APEX v7 claims **0.3 ms** end-to-end multi-chain OODA; APEX v3.5 claims **10–15 ms** | HYPOTHESIS | Timer boundary, hardware, load, chain round trip, clock sync, percentiles and independent baseline | Do not publish as capability |
| C-002 | APEX v7 claims **98.5%** pattern recognition; APEX v3.5 claims **80–85%** | HYPOTHESIS | Dataset labels, class balance, unseen test set, false-positive/negative rates, observation window | No accuracy display |
| C-003 | APEX v7 advocates **50×** leverage; v3.5 describes a **3×** cap with bounded risk | ASSUMPTION/conflict | Strategy objective, instrument limitations, stress exposure, liquidation failure assumptions, legal authority | Exclude leverage/trading |
| C-004 | Multiple whitepapers project millions per day, large returns and token appreciation | HYPOTHESIS | Trade-level ledger, realized net P&L, capital, fees, failure costs, independent provenance and market capacity | Remove profit promises |
| C-005 | 'Uncensorable', 'untraceable', 'absolute anonymity' through Akash, ZK or ICP | HYPOTHESIS | Threat model, metadata, operator trust, attestations, provider coercion and platform limits | Reject absolute assurances |
| C-006 | ZK use renders transactions/compliance obligations invisible | HYPOTHESIS / unacceptable inference | Actual privacy primitive, disclosure constraints, on-chain trace, legal obligations | No concealment claims |
| C-007 | Subgraphs/The Graph provide mempool pre-observation and forecasts of private bundles | HYPOTHESIS | Data-plane distinction; publicly indexed history versus private pending order flow | Separate data sources |
| C-008 | Coordinated 'herds' and induced price/cascade moves create profits | Documented proposal, **not approved** | Not suitable for product validation as trading strategy | Preserve only as threat scenario |
| C-009 | Shell entities, false trails or evidence destruction ensure regulatory immunity | Documented proposal, **not approved** | Regulatory/forensic constraints, record obligations | Reject implementation |
| C-010 | MEV event detection yields reduced consumer loss | HYPOTHESIS | Specific buyer decision, control/action, counterfactual, harms of false alarms | Product falsifier |
| C-011 | Synthetic replay demonstrates an observed real-chain vulnerability | INVALID transfer | Reconstructed chain-state primary evidence and reviewer | Synthetic remains synthetic |
| C-012 | Solana signal proves analogous Arbitrum signal | INVALID transfer | Separate chain-specific proof and semantic translation | Never auto-transfer |
| C-013 | Any specific company is responsible for a detected manipulation | UNKNOWN | Independent attribution standard, identity linkage and alternatives | No attribution in UI |
| C-014 | Current package is accepted for production | FALSE | Named authority, separate HTP Gate review, legal/security approvals and live data evidence | HOLD |

## Useful independent external references (not proof of the source claims)

- Flashbots MEV-Share documentation: https://docs.flashbots.net/flashbots-mev-share/introduction — user/validator/searcher value-sharing architecture and disclosure choices; not universal protection or access to private bundles.
- Jito documentation: https://docs.jito.wtf/ — Solana-specific transaction/bundle infrastructure; not a license to generalize execution guarantees.
- ESMA MiCA market abuse: https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica and https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-92-prevention-and-detection-market — relevant EU framework requiring jurisdiction/activity legal analysis.

The URLs are background sources available for future specialized review, not blanket verification of project claims or a signed legal opinion.
