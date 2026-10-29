# NETRUNNER roadmap — evidence before autonomy

| Gate | Output | Exit evidence | Failure decision |
|---|---|---|---|
| **G0 — Corpus consolidation** | Charter, source conflict registry, role mapping, legal/security boundaries | Every material claim traceable and unverified claims marked | REJECT unsafe features / REDESIGN object |
| **G1 — Offline prototype** | Deterministic local replay, terminal UI, chain-scoped dossier | Test logs, same-input/same-output digest, invalid-schema rejection, no network/transaction paths | HOLD if evidence laundering or cross-chain bleed |
| **G2 — Historical research** | Named protocol and bounded public historical dataset per chain | Reproducible snapshots, missing-data accounting, documented alternative explanations, chain reviewers | Redesign if reconstruction insufficient |
| **G3 — Shadow decision support** | Non-executing alert dossiers for a willing risk team | Pre-registered precision/recall, timestamp windows, false positives, review utility, privacy/legal approvals | HOLD if false positives or timing make it net harmful |
| **G4 — Controlled product pilot** | Read-only dashboard + agreed incident/review workflow | Named customer owner, SLOs derived from measured baseline, security review, retention policy | Stop/transfer if no decision utility |

**Not on roadmap:** autonomous finance, capital custody, tokens/reward monetization, attack storefront, live third-party exploitation, manipulative multi-wallet strategies or legal-obfuscation infrastructure.

## Proposed release tests

- `unit`: schema validation, duplicate event refusal, invalid timestamp, cross-network isolation, deterministic result and provenance.
- `property`: permutation of independent events cannot alter per-event findings; unsupported values never become evidence.
- `review`: domain-specific S1 challenge, D3 claim/evidence audit, accessibility and user-flow evaluation.
- `benchmark`: capture hardware, build hash, input volume, p50/p95/p99 wall time and warm/cold conditions; no promised microsecond target.
- `legal`: G2 issue map followed by competent human review before real data ingestion or offering a service.

## Decision owners and preservation

Human owner, budget, user/buyer and live-data rights remain `PENDING`; they cannot be inferred from code authorship or PR merger. Keep the existing Ante HTP Gate 0 on `HOLD`. A prototype may be accepted while another proposed capability is rejected.
