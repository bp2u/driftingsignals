---
title: Feature spec lifecycle
summary: "How a paragraph of product intent becomes an approved, machine-consumable Feature Spec."
order: 4
---

# FEATURE_SPEC_LIFECYCLE.md
## The Anchor Model — Human-Owned, AI-Assisted Feature Specification Creation

**Status:** Concept Outline  
**Version:** 0.1  
**Purpose:** Preserve the proposed process for converting a lightweight human Feature Request into an approved, machine-consumable Feature Spec.

---

# 1. Core Principle

Feature specification creation should itself follow the Anchor Model.

> **Humans own truth. AI authors its representation.**

The Product Manager owns the business and product truth of the feature.

AI should reduce the clerical burden of specification creation by assembling context, identifying ambiguity, researching dependencies, drafting the specification, and validating it against applicable Anchors.

The PM should not become a specification clerk.

The PM should concentrate on:

- What problem are we solving?
- For whom?
- Why does it matter?
- What outcome do we expect?
- Which ambiguities require a human decision?

---

# 2. Two Distinct Artifacts

## FEATURE_REQUEST

A lightweight expression of intent.

This may be only a paragraph.

Example:

> Customers abandon checkout when identity verification fails. We need a way for them to retry verification without restarting the entire application.

The Feature Request should not require the PM to complete a large template before work can begin.

Its purpose is to capture intent.

---

## FEATURE_SPEC

The approved delivery contract.

The Feature Spec is created through an AI-assisted workflow and becomes sufficiently rigorous for downstream orchestration and execution.

It should contain, as applicable:

- Business value
- Customer/user problem
- Desired behavior
- Acceptance criteria
- Applicable Anchors
- Dependencies
- Risk classification
- Security considerations
- Data considerations
- UX considerations
- Required Guardians
- Required tests
- Required telemetry
- Human gates
- Assumptions
- Resolved decisions
- Remaining approved assumptions
- Explicit non-goals

The Feature Spec represents one bounded unit of business value.

---

# 3. Proposed Lifecycle

```text
              PRODUCT / BUSINESS INTENT
                        |
                 BRD + PRD Anchors
                        |
                        v
              FEATURE REQUEST / IDEA
                        |
                        v
              FEATURE ORCHESTRATOR
                        |
              assembles relevant context
                        |
       +----------------+----------------+
       |                |                |
       v                v                v
      PRD          Existing Product    Telemetry /
   Context            Behavior         Research
       |                |                |
       +----------------+----------------+
                        |
                        v
                 DISCOVERY AGENTS
                        |
              identify unknowns,
            dependencies & conflicts
                        |
                        v
                  HUMAN / PM
              resolves ambiguity
                        |
                        v
                   SPEC AGENT
                        |
                        v
                  FEATURE_SPEC
                        |
                        v
                    GUARDIANS
          +-------------+-------------+
          |             |             |
          v             v             v
       Product          UX          Risk
      Guardian       Guardian      Guardian
          |             |             |
          +-------------+-------------+
                        |
                        v
                 SPEC QA REPORT
                        |
                 +------+------+
                 |             |
              Issues          Ready
                 |             |
                 v             v
              Revise       HUMAN GATE
                               |
                               v
                         PM APPROVES
                               |
                               v
                    APPROVED FEATURE_SPEC
                               |
                               v
                    DELIVERY ORCHESTRATOR
```

---

# 4. Stage 1 — Feature Request

**Owner:** Product  
**Authorship:** Human, optionally AI-assisted

The PM provides the smallest useful description of the desired business value.

The system should not force premature specification.

A Feature Request should normally identify:

- Problem or opportunity
- Target customer/user
- Desired outcome
- Why it matters

The Feature Request may intentionally contain unresolved details.

---

# 5. Stage 2 — Context Assembly

**Owner:** Feature Orchestrator  
**Execution:** AI agents/tools

Before drafting a specification, the Orchestrator gathers relevant organizational context.

Potential sources include:

- BRD
- PRD
- Existing Feature Specs
- Product behavior
- Product telemetry
- Customer research
- UX/UI Anchors
- Architecture Anchors
- Stack Anchors
- Security Anchors
- Risk Anchors
- Data Governance Anchors
- Previous exceptions
- Architecture Decision Records
- Relevant production incidents

The goal is:

> **Bring the organization's existing knowledge to the feature rather than requiring the PM to manually find it.**

---

# 6. Stage 3 — Discovery

**Execution:** Discovery Agents

Discovery Agents inspect the Feature Request and assembled context.

They identify:

- Missing information
- Contradictions
- Dependencies
- Existing capabilities
- Potential reuse
- Relevant Anchors
- Product ambiguity
- Security implications
- Risk implications
- Data implications
- UX implications
- Technical constraints

Agents should distinguish between:

1. Questions they can resolve from organizational evidence.
2. Questions requiring human judgment.

---

# 7. Stage 4 — Open Questions

AI must not silently invent business truth.

When an important ambiguity cannot be resolved from authoritative context, create an explicit Open Question.

Example:

```yaml
question_id: FQ-003
question: "How long should an incomplete identity verification session remain resumable?"
impact:
  - customer experience
  - data retention
  - security
recommended_owner: Product
status: unresolved
```

The system should consolidate questions and avoid overwhelming the PM with low-value decisions.

Only material ambiguity should require human attention.

---

# 8. Stage 5 — Human Resolution

**Owner:** Product or appropriate human authority

Humans resolve questions involving organizational truth.

Examples:

- Desired customer behavior
- Business policy
- Product tradeoffs
- Risk tolerance
- Scope
- Priority
- Customer promises

The responsible human may delegate factual research to AI, but retains decision authority.

Resolved decisions become part of the Feature Spec provenance.

---

# 9. Stage 6 — Feature Spec Draft

**Execution:** Spec Agent  
**Owner:** Product

The Spec Agent converts:

```text
Feature Request
+
Applicable Anchors
+
Organizational Context
+
Discovery Findings
+
Human Decisions
```

into a structured Feature Spec.

The Spec Agent may author the representation.

Product owns its truth.

---

# 10. Stage 7 — Pre-Implementation Guardian Review

Guardian review begins before code exists.

Applicable Guardians inspect the proposed Feature Spec.

Potential Guardians include:

- Product Guardian
- UX Guardian
- Architecture Guardian
- Stack Guardian
- Security Guardian
- Risk Guardian
- Data Guardian

Not every feature should invoke every Guardian.

The Feature Orchestrator should select Guardians based on scope and risk.

---

# 11. Example Guardian Discovery

A Security Guardian may determine:

> This feature persists identity-verification state. SECURITY-014 and DATA-022 apply.

An Architecture Guardian may determine:

> This capability crosses the Identity and Application domains. ARCH-031 applies.

A Risk Guardian may determine:

> Failed identity verification is part of a fraud-control boundary. Human Risk review is required.

These findings become part of the Feature Spec before implementation begins.

---

# 12. Stage 8 — Spec QA

Guardian findings are consolidated into a Spec QA Report.

The report should distinguish:

- Blocking issues
- Required clarification
- Recommendations
- Informational findings
- Applicable Anchor references
- Required human gates

The system should avoid presenting developers or PMs with dozens of redundant AI findings.

Findings should be deduplicated and prioritized.

---

# 13. Stage 9 — Revision

If material issues remain:

```text
SPEC QA
   |
   v
REVISION
   |
   +--> AI-resolvable issue -> Agent resolves
   |
   +--> Human decision -> Human resolves
   |
   +--> Anchor conflict -> Anchor owner / exception workflow
```

The Feature Spec should iterate until it is sufficiently complete for execution.

---

# 14. Stage 10 — Product Approval

**Human Gate**

Product approves the Feature Spec.

Approval means:

> This artifact accurately represents the business value and product behavior we intend to deliver.

It does not mean Product certifies every technical implementation detail.

Once approved, the Feature Spec becomes the authoritative delivery contract for that unit of value.

---

# 15. Stage 11 — Handoff to Delivery Orchestrator

The approved Feature Spec is passed to the Delivery Orchestrator.

The Delivery Orchestrator should receive:

```text
Business value
User behavior
Acceptance criteria
Relevant Anchors
Dependencies
Risk classification
Required Guardians
Required tests
Required telemetry
Human gates
Resolved decisions
Assumptions
Explicit non-goals
```

The Delivery Orchestrator then determines how the work should be implemented and verified.

---

# 16. Risk-Adaptive Guardian Selection

Guardian invocation should be proportional to the change.

Example:

## Copy Change

```text
Product Guardian
UX Guardian
```

## New API Endpoint

```text
Product Guardian
Architecture Guardian
Security Guardian
```

## Customer PII Pipeline

```text
Product Guardian
Architecture Guardian
Security Guardian
Risk Guardian
Data Guardian
```

## Authentication Platform Change

```text
Product Guardian
Architecture Guardian
Stack Guardian
Security Guardian
Risk Guardian
Data Guardian
UX Guardian
+
Mandatory Human Gates
```

The goal is high assurance without recreating enterprise bureaucracy through AI.

---

# 17. Feature Spec as Contract

Once approved, the Feature Spec should become the primary contract between Product intent and delivery execution.

It should be usable by:

- Delivery Orchestrators
- Coding Agents
- Engineers
- Test Agents
- Guardian Agents
- CI/CD systems
- Human reviewers
- Production verification systems

This makes the Feature Spec more than documentation.

It becomes machine-consumable execution context.

---

# 18. Traceability

A completed feature should eventually be traceable:

```text
BRD
 |
PRD
 |
FEATURE_REQUEST
 |
Human Decisions
 |
FEATURE_SPEC
 |
Applicable Anchors
 |
Implementation
 |
Guardian Findings
 |
Exceptions
 |
Tests
 |
Deployment
 |
Telemetry
```

This creates an evidence chain from business intent to production outcome.

---

# 19. Recursive Property of the Anchor Model

Feature Spec creation is itself an implementation of the Anchor Model.

```text
FEATURE_REQUEST
       |
       v
   ORCHESTRATOR
       |
       v
     AGENTS
       |
       v
   GUARDIANS
       |
       v
     HUMAN
       |
       v
FEATURE_SPEC
```

This follows the same core architecture used for delivery:

> **Anchors define.  
> Orchestrators direct.  
> Agents execute.  
> Guardians verify.  
> Humans decide.**

The Anchor Model therefore governs not only how software is created, but how the instructions for creating software are themselves produced.

---

# 20. Design Principle: Minimize Product Clerical Work

The Feature Spec workflow should not turn Product Managers into template administrators.

A successful implementation should allow a PM to begin with something as simple as:

> "Customers abandon checkout when identity verification fails. We need a way for them to retry without restarting the application."

The system should perform the heavy lifting required to turn that intent into a rigorous delivery artifact.

Human attention should be reserved for questions where human authority, judgment, strategy, or organizational truth actually matter.

---

# 21. Design Principle: AI Must Expose Uncertainty

AI should not silently convert uncertainty into specification.

When evidence is insufficient:

```text
UNKNOWN
   |
   +--> Researchable? -> Research
   |
   +--> Human truth? -> Ask owner
   |
   +--> Technical decision? -> Delivery/Architecture
   |
   +--> Policy conflict? -> Anchor owner
```

Explicit uncertainty is preferable to fabricated precision.

---

# 22. Design Principle: Specification Before Expensive Execution

The organization should resolve inexpensive ambiguity before expensive implementation.

AI makes specification analysis cheap.

Use that advantage.

The objective is to detect:

- product ambiguity;
- architectural conflict;
- security requirements;
- risk concerns;
- data obligations;
- UX conflicts;

before significant code is generated.

---

# 23. Future Work

This outline intentionally leaves several questions open for later design:

- Formal Feature Spec schema
- Feature Request schema
- Open Question schema
- Guardian finding schema
- Spec QA schema
- Risk classification algorithm
- Anchor discovery mechanism
- Context retrieval strategy
- Versioning
- Approval provenance
- Jira/ADO/GitHub integration
- Model-routing policy
- Agent identity and permissions
- Audit logging
- Exception workflow integration
- Metrics

These should be developed through a reference implementation rather than prematurely specified.

---

# 24. Working Thesis

The traditional workflow often expects humans to translate business intent into increasingly detailed documentation before implementation can begin.

The Anchor Model proposes a different division of labor:

> **Humans express and own intent. AI gathers context, exposes ambiguity, authors the specification, and verifies it against organizational Anchors. Humans resolve the decisions that require human truth.**

The result is an approved Feature Spec that can serve as a machine-consumable contract for AI-assisted delivery.

---
