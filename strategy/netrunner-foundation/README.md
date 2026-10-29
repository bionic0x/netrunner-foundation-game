> Standalone host decision: `bionic0x/netrunner-foundation-game`. See the [repository README](../../README.md) for current setup and status. Ante references describe upstream foundations, not a bundled runtime.

# NETRUNNER FOUNDATION — 27-source consolidated v0.2

**Canonical decision document:** [`MASTER-BLUEPRINT.md`](MASTER-BLUEPRINT.md) — 2026-10-29. **Source-derived** assertions are not real-world facts, returns or operating approvals.

- [`SOURCE-CROSSWALK.md`](SOURCE-CROSSWALK.md): 9 historical source aliases + 18 new sources.
- [`CLAIM-ADJUDICATION.md`](CLAIM-ADJUDICATION.md): 20 explicit source claims, inconsistencies and accepted boundaries.
- [`DECISION-RECORD.md`](DECISION-RECORD.md): strategic tests, alternative courses and human owner/authority.
- [`DESIGN-BRIEF.md`](DESIGN-BRIEF.md): CRASHOVERRIDE terminal UX, accessibility and Work Product Design handoff.
- [`architecture.md`](architecture.md), [`ante-runbook.md`](ante-runbook.md), [`roadmap.md`](roadmap.md): preserved v0.1 operational foundation.

**Verified standalone baseline:** 23 test cases (22 pass, one private-manifest check skipped) in `examples/netrunner-foundation/`. No transaction or funds access. HTP Gate 0 status **HOLD**.

---

# NETRUNNER FOUNDATION — APEX / CRASHOVERRIDE / HACK THE PLANET

**Status:** v0.1 research prototype · **Decision:** `PROCEED_WITH_CONDITIONS` for documentary/replay-only work, `HOLD` for deployment or financial activity · **Date:** 2026-10-29

## Governing object

Determine whether a bounded, auditable Solana + Arbitrum One **MEV observability and decision-support product** can produce reproducible, correctly scoped dossiers that help a protocol risk team distinguish observable adverse transaction ordering, degraded valuation inputs and recovery uncertainty. Preserve the retro-terminal experience as a UI layer, not as authority or a statement that funds were earned.

### Intended user, beneficiary and minimum sufficient result

- **Candidate user/buyer (unvalidated):** DeFi protocol security/risk teams or independent MEV researchers.
- **Beneficiary:** users, protocol operators and analysts who need earlier and clearer evidence of adverse ordering and valuation/recovery degradation.
- **Minimum result for the next stage:** one frozen synthetic example per network, full claim lineage, reproducible deterministic replay, a distinct reason/alternative explanation per flagged event, and independently reviewed acceptance criteria.
- **Not a result:** bots deployed, dollars extracted, an attractive game UI, latency claims or token price.

### Explicit non-object

No real transaction signing/submission, trading, custody, liquidations, market or oracle manipulation, hostile sandwiching, induced cascades, consensus reorganization, bribery, wash trading, deceptive attribution, transaction-trace destruction, KYC evasion, circumvention of regulator requests, promised returns or monetary rewards. Unsafe themes in the source documents remain **source material for threat modeling**, never product features. No agent creates permission by emitting a `PROCEED` decision.

## What is being consolidated

| Source family | Retained in the design | Rejected, quarantined or unsupported |
|---|---|---|
| APEX v3.5 / Cartel Takeover | Opportunity observation, modular scout/analyst/commander, human verification, separation of risk and execution | Performance / return claims without provenance; offensive operations |
| APEX v7.0 | Digital twins as a research hypothesis, replay/simulation concepts, multi-agent decomposition | 0.3 ms multi-chain OODA, 98.5% accuracy, 50x leverage, 'uncensorable' guarantees and other unevidenced superlatives |
| HACK THE PLANET v4.0 | Visual command center, research academy, evidence viewer, scenario analysis | Oracle manipulation, induced cascades, false narratives, time-bandit attacks, live wrongdoing |
| CRASHOVERRIDE UI gallery | Dark/green terminal layout, status/navigation, replay console, operator logs | Fake live profit counters, click-to-attack, gamified manipulation or fabricated security claims |
| HTP UI gallery | Retro ASCII navigation, explainable mission rehearsal, learning pathways | Tokenized ROI boosts, attack marketplace, identity concealment |
| WOLF PACK | Research/scout, analysis, coordination, security, engineering role decomposition | Coordinated market distortion or deceptive tactics |
| ANTI-FRAGILE | Failure scenarios: flash crash, congestion, degraded oracle, service disruption | Profit guarantees during disasters, preying on unconsenting vulnerable parties |
| LEGAL FORTRESS | Jurisdiction/activity issue spotting and evidence retention | Fictitious legal immunity, shell structures for concealment, destruction of evidence, regulatory obstruction |
| General Strategy Doctrine | Purpose-first decision, seven coherence tests, distinct evidence statuses, reserve, falsifiers and exit | Any claim that a strategic metaphor authorizes a live financial action |

The uploaded documents are **not copied into this public repository**. Their claims do not become factual by inclusion in this inventory. Detailed per-document content and original source files remain under the user's control.

## Existing Ante foundations to reuse

- `strategy/STRATEGIC-CONTROL-PLANE.md`: governing object, constraints, admission, challenge and termination.
- `strategy/htp-gate0/`: existing Solana and Arbitrum Gate 0 with E1-SOL / E1-ARB / S1 handoffs, six artifacts and chain-specific evidence.
- `strategy/contracts.json`: normative vocabulary — refer to its canonical states rather than creating incompatible ones.
- `strategy/alpha-research-suite/`: non-executing finance research discipline.
- `strategy/NEXUS-INSTANCE.md`: versioned task/dependency/authority rules.

**Compatibility rule:** this is a preparatory project package. It is **not** inserted into `strategy/runbooks.json` and does not alter HTP's recorded `HOLD`. Registration requires schema validation, named human accountability and separate review.

## Concrete deliverables in v0.1

1. [Architecture](architecture.md): separation of domains, chain overlays, trust boundaries, data contracts.
2. [Ante runbook](ante-runbook.md): seats, handoffs, deliverables, challenge, staging and decision gates.
3. [Claim and conflict register](claim-register.md): numbered allegations and required falsification.
4. [Roadmap](roadmap.md): phased outcomes and acceptance criteria.
5. [Offline replay engine](../../examples/netrunner-foundation/replay.py): synthetic event classifier, JSONL dossier export.
6. [Fixture](../../examples/netrunner-foundation/fixture.json): independent Solana and Arbitrum synthetic samples.
7. [Retro console](../../examples/netrunner-foundation/index.html): demonstrator; intentionally no external services.
8. [Unit tests](../../examples/netrunner-foundation/test_replay.py): evidence separation, deterministic replay and negative cases.

## Run locally

```sh
python3 examples/netrunner-foundation/replay.py examples/netrunner-foundation/fixture.json
python3 -m unittest discover -s examples/netrunner-foundation -p 'test_*.py' -v
# Open examples/netrunner-foundation/index.html directly in a browser.
```

There is no RPC endpoint, wallet, key, market order, bridge, contract write or outbound network request. All displayed event values are synthetic and labeled as such.

## Current verdict

- Documentary architecture, deterministic replay and illustrative UI: **in scope**.
- Live data acquisition, detection performance, chain-specific protocol adapters and buyer value: **unvalidated / pending**.
- Material financial automation and strategies described as manipulating prices, order flow, users or oversight: **not in scope**.

Acceptance of this PR must not be reported as validation of a MEV trading or production security system.
