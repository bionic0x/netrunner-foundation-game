# NETRUNNER — architecture and technical contracts (v0.1)

## Trust and execution boundaries

```text
[Source: synthetic event fixture]
          |
          v
[Input schema / provenance checks] --invalid--> [explicit REJECT / UNKNOWN]
          |
          v
[Chain-specific observability adapters: SOL / ARB]
          |                  (only synthetic adapter in v0.1)
          v
[Pattern hypotheses] ---> [Alternative explanations / missingness]
          |                       |
          +---------> [Evidence dossier / immutable digest]
                                   |
                            [Ante S1 / D3 challenge]
                                   |
                  [Human decision / independent authority]
                                   |
                          [CRASHOVERRIDE UI]

          NO PATH FROM UI OR DOSSIER TO A SIGNER OR EXECUTOR
```

**Separation invariant:** `observation != detection != inference != policy != authorization != execution`. The UI may inspect and export a dossier; it cannot silently escalate a hypothesis or cause a financial action.

## Deployment surfaces

| Domain | Solana | Arbitrum One |
|---|---|---|
| Observation | Slots, transactions, account/program references (future adapter only) | L2 blocks/receipts, oracle feed calls, sequencer/recovery observations (future adapter only) |
| First research hypothesis | SOL-ORD ordering anomaly; SOL-ORC valuation degradation | ARB-ORC price-quality anomaly; ARB-RES interruption/recovery uncertainty |
| Network semantics | Account ownership, PDAs/CPI, SPL / Token-2022, slot boundaries | EVM call semantics, proxy/implementation, L1/L2 and sequencer dependencies |
| Required evidence before validation | Chain-specific timestamp/slot reconstruction, credible alternative explanations and coverage accounting | Feed decimals/staleness/heartbeat, sequencer and RPC separation, recovery evidence |
| Status at v0.1 | Synthetic replay only; never live validated | Synthetic replay only; never live validated |

No Solana detector accuracy or threshold transfers to Arbitrum; neither network uses an implementation merely because an event has a similar name.

## Minimal event schema

`fixture.json` is an object with `schema_version`, `dataset_kind="synthetic"`, `events`, and a human-readable `scope`. Each event must include:

- `id`: unique nonempty source identifier (in the synthetic fixture only).
- `network`: exactly `solana` or `arbitrum_one`.
- `kind`: `ordering_anomaly`, `oracle_deviation`, `sequencer_down`, `sequencer_recovered` or `insufficient_data`.
- `observed_at`: ISO-8601 timestamp with explicit UTC offset; never infer timezone.
- `source_ref`: declared source/fixture reference; not an attribution to an actor.
- `observed`: kind-specific observation structure.

The simulator does not consume real chain data and emits no confidence percentages or profit estimates. It calculates no universal 'attack probability' and asserts no identity or intent.

## Claim/dossier schema

Every finding has `event_id`, `network`, `classification`, `claim_status`, `source_kind`, `observed_at`, `observation`, `inference`, `alternative_explanations`, `missing_evidence`, `prohibited_inferences`. Synthetic signals retain `source_kind="synthetic_fixture"` all the way to export. A `flag` is a hypothesis requiring review, not a production alert.

The current classifications are bounded: `REVIEW_ORDERING`, `REVIEW_ORACLE`, `REVIEW_RECOVERY`, `INSUFFICIENT_DATA`. There are no pass/fail assertions about named protocols, malicious intent or material customer harm.

## Security, privacy and reliability

- **Input boundary:** parse local JSON; reject extra dangerous execution fields and unrecognized network/kind; cap event volume and field sizes before allocation.
- **No secrets:** no signing keys, wallet access, RPC credentials or private data in the dataset or UI.
- **No model authority:** a model-generated score cannot authorize any external operation.
- **Tamper indication:** canonical JSON dossier digest is reproducible; a hash is not proof of authenticity.
- **No fabricated 'live':** all demo values have persistent `SYNTHETIC / OFFLINE` labeling.
- **Resilience:** malformed events are rejected deterministically; one chain's status does not upgrade the other.
- **Data retention:** release criteria require policy for timestamps, provenance, retention and incident handling before importing real data.

## Falsifiers

1. A flagged pattern cannot be reconstructed from sufficient transaction/slot/feed history when real scope is later selected.
2. Results change across identical frozen replays or by reordering unrelated cross-chain events.
3. A reviewer cannot distinguish an unsupported claim from observed evidence or recover source lineage.
4. Too many normal scenarios are mislabeled, making the dossier unusable for an operator.
5. A buyer cannot articulate a decision improved by the information and a plausible loss-to-buy-down mechanism.
6. Actual data rights, legal boundaries or security prerequisites cannot be satisfied.

These trigger `REDESIGN` or `HOLD`, not automatic expansion of the model.
