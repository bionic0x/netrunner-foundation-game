> Standalone integration note: the profiles and `strategy/htp-gate0/` paths below belong to the external Ante project. They are planning references, not installed agents or completed independent reviews in this repository.

# NETRUNNER — Ante/NEXUS preparatory runbook

**Mode:** documentary + local deterministic replay. **Human decision owner:** `PENDING`. **Authority:** none to transact or deploy. **NEXUS relationship:** uses the Gate 0 handoff model; no alteration to existing HTP decisions.

## Real agent roster and boundaries

| Seat | Concrete Ante agent | Mandate | Review / limit |
|---|---|---|---|
| G0 | `specialized-strategic-assurance-lead` | Seven coherence tests; object and non-object; stop conditions | Cannot authorize a financial action |
| G1 | `specialized-chief-of-staff` | Manage plan, dependencies, documented decisions | Cannot invent human owners |
| P1 | `product-manager` | Buyer hypothesis, outcome, failure criteria, UI acceptance | Adoption is unverified |
| D1 | `research-synthesist` | Primary source weight, alternative explanations, gap identification | Not an empirical oracle |
| D3 | `research-proposition-citation-auditor` | Claim ledger, scope/date/status and citation integrity | No unearned `EVIDENCE` |
| S1 | `security-blockchain-security-auditor` | Threat model, negative tests, invariants, independent challenge | No live proof-of-concept attacks |
| E1-SOL | `engineering-solana-program-engineer` | Solana observation/data interface and chain semantics | Solana-only; no signing/submission |
| E1-ARB | `engineering-solidity-smart-contract-engineer` | Arbitrum feed/contract/state semantics | Arbitrum-only; no signing/submission |
| A1 | `engineering-multi-agent-systems-architect` | NEXUS task isolation, scoped handoffs and budgets | No cross-domain authority transfer |
| U1 | `design-ux-architect` + `design-ui-designer` | CRASHOVERRIDE terminal, accessible trace views | No fake revenue, inducement or misleading live status |
| T1 | `testing-test-automation-engineer` + `testing-accessibility-auditor` | Deterministic tests and keyboard/a11y review | Tests do not prove real-world outcomes |
| G2 | `support-legal-compliance-checker` | Jurisdiction/activity issue spotting, MiCA market-abuse risks | Human competent legal sign-off remains pending |

## Eight bounded tasks

| ID | Depends on | Lead | Deliverable / acceptance | State |
|---|---|---|---|---|
| NR-001 | — | G0, P1 | Charter & non-object fixed; users unvalidated | prepared |
| NR-002 | NR-001 | D1, D3 | Source triage, quantitative conflicts, alternatives | prepared |
| NR-003 | NR-001 | E1-SOL, E1-ARB, A1 | Chain-specific domain map; shared schema with no semantic transfer | prepared |
| NR-004 | NR-002, NR-003 | S1 | Negative threat model and authority gates | drafted; review pending |
| NR-005 | NR-003 | E1-SOL, E1-ARB, T1 | Deterministic synthetic replay + tests | implemented as local prototype; independent review pending |
| NR-006 | NR-001, NR-005 | U1, P1 | Offline console, explanatory status/evidence interaction | implemented as local prototype; usability review pending |
| NR-007 | NR-002, NR-004, NR-005, NR-006 | G0, D3 | Seven tests, falsifiers, documented dissent | pending independent review |
| NR-008 | NR-007 | Human owner | Scope and budget of real research next stage, or terminate | HOLD |

**Task ownership is a planned mapping, not a claim that the named model profiles actually executed a signed review.** Creation of this package alone is not independent S1/G2/G0 acceptance.

## Handoffs

Each artifact handed to S1 or D3 must name `artifact_ref`, commit/digest, network, evidence status, non-object, observed/assumed distinction, reviewer, open questions and expiry. Use the existing `strategy/htp-gate0/handoff-e1-s1.md` lifecycle, but never misreport completed generic work as an accepted HTP handoff.

If a finding concerns both networks, create two explicit records, each with its own data requirements and reviewer. Favor replays, fixtures and offline synthetic attack modeling; disallow production adversarial experiments.

## Seven coherence tests, preliminary

| Test | Assessment | Missing condition |
|---|---|---|
| Governing object | CONDITIONAL | Name buyer and accountable owner |
| Causal | HYPOTHESIS | Demonstrate whether evidence materially improves a risk decision |
| Interactive | HYPOTHESIS | Include market participants' benign adaptation and false-positive costs |
| Conversion | CONDITIONAL | Verify trace completeness, adapter feasibility and review capacity |
| Legitimacy / admissibility | HOLD for live actions | Competent human legal assessment; no manipulation or regulator evasion |
| Epistemic | CONDITIONAL | Claim source/date/scope; independent testing |
| Exit | CONDITIONAL | Defined stop/revise triggers and post-pilot ownership |

**Conclusion:** `PROCEED_WITH_CONDITIONS` for offline research only; live activity remains `HOLD` regardless of prototype functionality.
