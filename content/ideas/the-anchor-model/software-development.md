---
title: Software development
summary: "The first reference implementation: BRD/PRD anchors, feature specs, guardians, and a risk-adaptive SDLC."
order: 3
---

# The Anchor Model for Software Development
## Applying Human-Governed AI Orchestration to the SDLC

**White Paper — Version 1.0**


> **This paper describes the software-development implementation of the broader Anchor Model: an organizational architecture for AI-enabled work.**

> **Humans own truth. AI authors its representation.**

**Operating vocabulary:** Anchors define. Orchestrators direct. Agents execute. Guardians verify. Humans decide.

### Abstract

AI coding systems are rapidly reducing the cost of software implementation. As execution becomes cheaper and faster, a different constraint becomes dominant: maintaining alignment with business intent, product outcomes, user experience, architecture, security, risk, data governance, and approved technology patterns.

The Anchor Model is a company-wide software development lifecycle designed for this environment. It treats durable, human-owned documents as machine-consumable **anchors**; treats feature specifications as bounded units of business value; uses an **orchestration layer** to move work through the appropriate controls; allows AI agents and small engineering teams to execute rapidly; continuously detects **drift** from organizational intent; and provides an explicit **exception mechanism** through which better patterns can be proposed rather than suppressed.

The central principle is:

> **Humans own truth and accountability. AI may author, execute, verify, and recommend.**

The result is not a fully autonomous SDLC. It is a high-velocity, human-governed system in which organizational intent becomes continuously executable.

---

# 1. The Shift in the Software Bottleneck

Traditional software organizations were built around the assumption that implementation capacity was scarce. Product teams prioritized backlogs, engineering teams converted requirements into code, specialists reviewed the work, and delivery cadence was constrained by the number of engineers available to design, implement, test, and integrate software.

AI changes that assumption.

A small team of two or three engineers equipped with capable coding agents can increasingly perform work that once required a substantially larger delivery team. Code generation, refactoring, testing, documentation, analysis, and routine implementation can all be accelerated.

But faster implementation creates a new problem.

If software can be produced faster than an organization can communicate and enforce its intent, the organization does not necessarily get better software. It gets **faster drift**.

A coding agent can produce a technically valid implementation that:

- solves the wrong business problem;
- violates the intended product behavior;
- introduces an inconsistent user experience;
- bypasses sanctioned architecture;
- introduces an unsupported technology;
- weakens security controls;
- exceeds organizational risk appetite;
- mishandles governed data;
- or creates operational debt that is invisible at feature completion.

The scarce resource therefore shifts.

> **As the marginal cost of implementation falls, alignment becomes the scarce resource.**

The Anchor Model is designed around that shift.

---

# 2. From Documentation to Executable Intent

Most enterprises already have requirements, architecture standards, design systems, security policies, technology standards, and risk controls.

The problem is not the absence of documentation.

The problem is that traditional documentation is passive.

A document is written. It is published. Humans are expected to remember that it exists, determine whether it applies, interpret it correctly, and enforce it during delivery. Over time, documents become stale and implementations diverge.

AI changes the economics of documentation because a machine-readable document can become an active participant in delivery.

An architecture standard can be supplied directly to an architecture-review agent. A UX guideline can be evaluated against generated UI. A security policy can become context for a security guardian. A PRD can be used to test whether a completed feature still serves the intended product outcome.

The document is no longer merely a reference.

It becomes an **anchor**.

An anchor is a durable, human-owned representation of organizational truth against which work can be planned, executed, and continuously evaluated.

---

# 3. The Anchor Hierarchy

The Anchor Model separates durable organizational intent from individual units of execution.

A representative hierarchy is:

```text
                         BUSINESS INTENT
                              |
                             BRD
                              |
                             PRD
                              |
                     DELIVERY ORCHESTRATION
                              |
                          FEATURE SPEC
                              |
       +-----------+----------+----------+-----------+
       |           |          |          |           |
 ARCHITECTURE     UX/UI      STACK    SECURITY      RISK
    ANCHOR        ANCHOR     ANCHOR     ANCHOR      ANCHOR
       |           |          |          |           |
       +-----------+----------+-----+----+-----------+
                                  |
                              DATA ANCHOR
                                  |
                         AI + ENGINEERS
                                  |
                              VERIFICATION
                                  |
                            DRIFT DETECTION
                                  |
                       EXCEPTION / CONFORMANCE
```

The exact physical representation may be Markdown, structured YAML, a policy service, a design-system repository, or another machine-readable format. The important concept is ownership and authority, not the file extension.

## 3.1 Business Requirements Document — BRD

**Owner:** Business/Product leadership

The BRD anchors why the organization is investing.

It should define:

- business problem;
- strategic context;
- target outcomes;
- measurable business value;
- constraints;
- major stakeholders;
- economic rationale;
- regulatory or market drivers.

The BRD should change less frequently than individual feature specifications.

## 3.2 Product Requirements Document — PRD

**Owner:** Product

The PRD anchors what product outcome must exist.

It should define:

- customer problem;
- target users;
- product behavior;
- success measures;
- scope and non-scope;
- product principles;
- key constraints;
- major capabilities;
- dependencies;
- product-level acceptance.

The PRD is not a backlog. It is the durable product truth from which bounded units of value are derived.

## 3.3 UX/UI Anchor

**Owner:** UX/Design

The UX/UI anchor defines sanctioned experience patterns.

It may include:

- design-system usage;
- interaction patterns;
- accessibility requirements;
- content and voice standards;
- component guidance;
- responsive behavior;
- research-backed experience principles.

## 3.4 Architecture Anchor

**Owner:** Enterprise/Solution Architecture

The architecture anchor defines sanctioned structural patterns and boundaries.

It may include:

- reference architectures;
- domain boundaries;
- integration patterns;
- eventing patterns;
- API standards;
- resilience expectations;
- service ownership;
- approved architectural decision patterns.

## 3.5 Stack Anchor

**Owner:** Engineering/Platform, often in partnership with Architecture

The stack anchor defines sanctioned implementation technologies and operational conventions.

It may include:

- languages and versions;
- frameworks;
- databases;
- cloud services;
- build systems;
- observability tools;
- dependency policies;
- deployment patterns;
- supported libraries.

Architecture governs structural intent. Stack governs approved implementation choices. They overlap, but they are not identical.

## 3.6 Security Anchor

**Owner:** Security

Security is a first-order anchor, not a downstream checklist.

It should encode:

- authentication and authorization standards;
- secrets management;
- encryption requirements;
- secure coding requirements;
- threat-model triggers;
- vulnerability expectations;
- supply-chain controls;
- logging and audit requirements;
- security review thresholds.

## 3.7 Risk Anchor

**Owner:** Risk

Risk is distinct from security.

Security asks whether systems are adequately protected. Risk asks whether the aggregate exposure created by a change is acceptable to the organization.

The risk anchor may govern:

- operational risk;
- model risk;
- regulatory risk;
- third-party risk;
- reputational risk;
- customer-impact thresholds;
- financial exposure;
- control requirements;
- escalation thresholds.

## 3.8 Data Governance Anchor

**Owner:** Data Governance / Data Architecture

The data anchor governs:

- data classification;
- retention;
- lineage;
- residency;
- quality;
- ownership;
- PII handling;
- data contracts;
- permitted use;
- model-training restrictions;
- deletion requirements.

---

# 4. Ownership Is Not Authorship

The Anchor Model deliberately separates ownership from authorship.

> **AI can write the document. The human owner remains accountable for its truth.**

A Product Manager may use an AI workflow to produce most of a PRD. Product still owns the PRD.

An architecture agent may draft an updated reference pattern. Architecture owns the approved pattern.

A security agent may propose new controls based on recurring findings. Security owns the resulting security anchor.

An AI coding assistant may generate most of a feature. Engineering owns the implementation.

This distinction becomes increasingly important as AI contribution rises. Measuring who typed an artifact becomes less useful. Knowing who has authority to approve its meaning becomes more important.

---

# 5. The Feature Specification: The Unit of Business Value

The Feature Spec is the primary unit of delivery.

It is similar in scale to a well-formed agile story or small feature, but is designed to be sufficiently complete for AI-assisted execution.

**Owner:** Product, human-owned and AI-assisted.

A Feature Spec should define one coherent piece of business value and include:

- problem or opportunity;
- user/business value;
- desired behavior;
- acceptance criteria;
- relevant constraints;
- affected personas;
- telemetry expectations;
- non-functional requirements where known;
- links to applicable anchors;
- known dependencies;
- explicit non-goals.

The Feature Spec should say **what value is being delivered**, not prescribe implementation unless implementation itself is part of the requirement.

AI can assist in transforming a Product Manager's rough intent into a complete Feature Spec, but the Product Manager approves the final artifact.

---

# 6. Orchestration: The Executable Delivery Contract

Anchors alone are insufficient.

The organization also needs to define how a unit of work moves through them.

This is the role of **delivery orchestration**.

The orchestration artifact is an executable description of the development lifecycle for a product or product family.

It answers:

- Which anchors apply?
- Which agents or humans participate?
- Which steps are deterministic?
- Which steps may use inexpensive AI?
- Which require frontier reasoning?
- Which require human approval?
- What evidence must be produced?
- What constitutes a blocking failure?
- When is an exception allowed?
- What artifacts must exist before deployment?
- What must be observed after deployment?

A representative flow is:

```text
Feature Spec
    |
Context Assembly
    |
Architecture / Security / Risk Classification
    |
Implementation Plan
    |
Human Gate (when required)
    |
AI-Assisted Implementation
    |
Automated Tests
    |
Guardian Reviews
    |
Drift Assessment
    |
Exception Resolution if needed
    |
Human Gate (risk-adaptive)
    |
Deployment
    |
Production Verification
    |
Telemetry and Learning
```

## 6.1 Product Ownership of Orchestration

The team that owns the PRD should own the **orchestration policy** because orchestration ultimately determines whether delivery remains attached to product intent.

This does not mean Product owns every technical mechanism.

A useful division is:

**Product owns:**
- required outcomes;
- lifecycle policy;
- product acceptance;
- required gates;
- evidence expectations;
- completion criteria;
- escalation expectations.

**Engineering/Platform owns:**
- CI/CD implementation;
- coding-agent integration;
- test infrastructure;
- policy execution machinery;
- repository automation;
- telemetry pipelines;
- model/tool integration.

**Anchor owners own:**
- their respective standards;
- severity definitions;
- exceptions;
- changes to their anchors.

This preserves product accountability without turning Product into the owner of technical tooling.

---

# 7. Risk-Adaptive Orchestration

Not every feature requires the same process.

A copy change should not move through the same controls as a new authentication mechanism.

The orchestration layer should classify work and dynamically activate the appropriate controls.

Examples:

### Low-risk UI copy change
- Product validation
- UX/content validation
- automated tests
- lightweight human review

### New database field containing customer information
- Product
- Architecture
- Security
- Risk
- Data Governance
- migration testing
- retention/lineage checks

### New authentication mechanism
- Architecture
- Security
- Risk
- threat modeling
- integration testing
- mandatory human security approval
- production monitoring

This makes governance proportional rather than bureaucratic.

---

# 8. Small Human Teams, Large AI Execution Capacity

A central operating hypothesis of the Anchor Model is that a feature team may increasingly consist of only two or three engineers supported by AI coding systems.

The humans provide:

- engineering judgment;
- decomposition;
- technical accountability;
- review;
- debugging;
- exception reasoning;
- operational ownership.

AI systems provide scalable execution capacity for:

- code generation;
- test generation;
- refactoring;
- repository exploration;
- documentation;
- static analysis;
- migration assistance;
- routine debugging;
- implementation planning.

The goal is not to remove engineers from the loop.

The goal is to change their leverage.

A small engineering team becomes responsible for directing, validating, and owning a much larger effective implementation capacity.

---

# 9. Guardian Agents and Continuous Drift Detection

Traditional review is episodic. The Anchor Model makes alignment continuous.

Specialized **guardian agents** evaluate implementation against specific anchors.

Examples:

- Product Guardian
- Architecture Guardian
- Stack Guardian
- UX Guardian
- Security Guardian
- Risk Guardian
- Data Guardian

Each guardian should be narrow in mandate.

It should not decide organizational truth. It should compare implementation with the anchor it represents and produce evidence.

Representative outputs:

```text
product_drift.md
architecture_drift.md
stack_drift.md
ux_drift.md
security_drift.md
risk_drift.md
data_drift.md
```

A drift finding should include:

- anchor requirement;
- observed implementation;
- severity;
- evidence;
- likely impact;
- confidence;
- recommended disposition.

The orchestration layer determines whether a finding blocks delivery.

---

# 10. Drift Is Not Automatically Wrong

A critical design principle is that divergence from an anchor can mean two different things:

1. The implementation has accidentally drifted.
2. The implementation has discovered a better approach.

A mature system must distinguish the two.

A guardian should therefore not simply command:

> "You violated STACK.md. Fix it."

It should report:

> "The implementation differs from the sanctioned stack pattern. Determine whether this is accidental drift or an intentional exception."

This prevents governance from freezing innovation.

---

# 11. The Exception Request

When a team or coding agent believes a non-sanctioned approach is materially better, it should create an explicit exception artifact.

Example:

```text
EXCEPTION_REQUEST_0042.md
```

The request should include:

- applicable anchor;
- sanctioned approach;
- proposed alternative;
- reason for divergence;
- expected benefit;
- risks;
- security implications;
- operational implications;
- migration implications;
- cost;
- evidence or benchmarks;
- whether the exception is temporary or strategic;
- recommended disposition.

The owning anchor team evaluates the request.

Possible outcomes:

### Reject
The implementation must conform to the existing anchor.

### Approve one-time exception
The implementation may proceed, but the anchor remains unchanged.

### Approve and evolve the anchor
The alternative is judged superior enough that the organization's sanctioned pattern should change.

This creates a governed path for bottom-up innovation.

---

# 12. Anchors Must Evolve

An anchor that cannot change becomes a constraint on learning.

The Anchor Model therefore treats anchors as versioned, governed artifacts.

Changes should include:

- owner;
- version;
- effective date;
- rationale;
- impacted systems;
- migration expectations;
- compatibility policy.

Guardian agents should evaluate work against the appropriate anchor version.

This also makes architectural and policy change observable rather than implicit.

---

# 13. A Reference Repository Structure

A product repository might contain:

```text
/product
    BRD.md
    PRD.md
    DELIVERY_ORCHESTRATION.md

/anchors
    UX_UI.md
    ARCHITECTURE.md
    STACK.md
    SECURITY.md
    RISK.md
    DATA_GOVERNANCE.md

/features
    /F-001
        FEATURE_SPEC.md
        implementation_plan.md
        test_evidence.md
        product_drift.md
        architecture_drift.md
        stack_drift.md
        ux_drift.md
        security_drift.md
        risk_drift.md
        data_drift.md
        exceptions/
        delivery_evidence.md

/decisions
    ADR-001.md
    ADR-002.md

/exceptions
    EXCEPTION_REQUEST_0042.md

/telemetry
    product_metrics.md
    operational_metrics.md
```

In a large enterprise, many anchors would be centrally managed and referenced rather than copied into each repository.

---

# 14. Human Gates

Human-in-the-loop should not mean humans manually approve every AI action.

It should mean humans remain accountable at consequential decision points.

Examples of human gates include:

- approval of BRD;
- approval of PRD;
- approval of Feature Spec;
- high-risk implementation plan;
- material security/risk exceptions;
- architecture exceptions;
- production release for high-impact changes;
- changes to anchor documents.

Low-risk, reversible work can move autonomously within policy.

This creates **bounded autonomy** rather than either extreme: manual bureaucracy or uncontrolled automation.

---

# 15. Model Routing and Economics

Not every task requires the most capable AI model.

An AI-native SDLC should explicitly route work by cost and reasoning requirement.

### Lower-cost models are suitable for:
- formatting;
- extraction;
- classification;
- repository summarization;
- first-pass documentation;
- test scaffolding;
- routine code transformations;
- drift pre-screening;
- metadata.

### Frontier models should be reserved for:
- ambiguous requirements;
- architectural reasoning;
- exception evaluation;
- complex security interpretation;
- risk reasoning;
- final product-intent validation;
- conflicting evidence;
- difficult debugging;
- consequential design decisions.

### Deterministic tools should remain authoritative for:
- builds;
- tests;
- static analysis;
- schema validation;
- policy checks;
- calculations;
- dependency scanning;
- reproducible technical assertions.

The orchestration layer should select the least expensive adequate capability and escalate when confidence or consequence warrants it.

---

# 16. The Drift Control Loop

The complete control loop can be summarized as:

```text
Human-owned intent
      |
   Anchors
      |
Feature Spec
      |
Orchestration
      |
AI + Human Execution
      |
Verification
      |
Guardian Agents
      |
Drift Findings
      |
 +----+----+
 |         |
Conform  Intentional
 |         |
Fix     Exception Request
           |
       Anchor Owner
       /     |      \
    Reject  Allow   Evolve Anchor
       \      |      /
        \     |     /
          Delivery
             |
          Telemetry
             |
           Learning
             |
        Better Anchors
```

This is not a linear SDLC.

It is a learning system.

---

# 17. Preventing Product Drift

Product drift deserves special attention.

Technical systems can remain architecturally compliant while gradually ceasing to solve the intended customer problem.

A Product Guardian should compare:

- Feature Spec to PRD;
- implementation behavior to Feature Spec;
- telemetry to intended outcome;
- subsequent features to original product principles.

This gives Product a machine-assisted mechanism for maintaining coherence across hundreds of incremental changes.

The PRD becomes a living product anchor rather than a launch document that is forgotten after development begins.

---

# 18. Security and Risk as Continuous Participants

Security and Risk should not be late-stage approval functions.

Their anchors should be available during planning and implementation so coding agents can make compliant decisions before code exists.

Guardian agents then validate those decisions continuously.

Human specialists become most involved where they add the greatest value:

- novel threats;
- ambiguous controls;
- high-impact exceptions;
- systemic risk;
- changing regulatory interpretation.

This shifts specialist organizations from repetitive inspection toward higher-value judgment.

---

# 19. Evidence as a Delivery Artifact

AI-generated software increases the importance of evidence.

A completed feature should not merely consist of code.

It should have a machine-readable evidence package demonstrating:

- which Feature Spec was implemented;
- which anchor versions applied;
- tests executed;
- drift findings;
- exceptions granted;
- human approvals;
- security evidence;
- risk classification;
- deployment result;
- production verification.

This creates traceability from business intent to production behavior.

For regulated organizations, that traceability may become one of the model's most valuable properties.

---

# 20. Organizational Roles

A simplified ownership model:

| Artifact / Capability | Accountable Owner | AI Role |
|---|---|---|
| BRD | Business/Product | Draft, analyze, challenge |
| PRD | Product | Draft, refine, test coherence |
| Delivery Orchestration | Product | Execute workflow, recommend optimization |
| Feature Spec | Product | Draft, clarify, validate completeness |
| UX/UI Anchor | UX | Detect UX drift |
| Architecture Anchor | Architecture | Detect architecture drift |
| Stack Anchor | Engineering/Platform | Detect stack drift |
| Security Anchor | Security | Detect security drift |
| Risk Anchor | Risk | Classify and detect risk drift |
| Data Anchor | Data Governance | Detect data-policy drift |
| Implementation | Engineering | Generate, test, refactor |
| Exceptions | Relevant Anchor Owner | Analyze evidence and options |
| Production Operation | Engineering/SRE | Monitor, diagnose, automate |

Again, AI may author most of an artifact without owning it.

---

# 21. Metrics

The Anchor Model should be measured on outcomes rather than AI utilization.

Useful metrics include:

### Delivery
- lead time per Feature Spec;
- engineering hours per unit of value;
- deployment frequency;
- change failure rate;
- time to recovery.

### Alignment
- drift findings per feature;
- escaped drift;
- exception frequency;
- exception approval rate;
- anchor-related rework;
- product acceptance failures.

### AI Economics
- inference cost per feature;
- frontier-model percentage;
- coding-agent utilization;
- human review time;
- AI-generated code acceptance/rework rate.

### Governance
- time to resolve exceptions;
- stale anchor count;
- anchor update frequency;
- unresolved high-severity findings;
- audit evidence completeness.

### Product
- outcome attainment;
- customer impact;
- feature adoption;
- business value delivered.

The objective is not "more AI-generated code."

The objective is **more verified business value per unit of human effort without increasing unmanaged risk**.

---

# 22. Adoption Path

The Anchor Model does not require an enterprise to redesign its entire SDLC at once.

A practical adoption sequence is:

## Phase 1 — Establish Anchors
Identify authoritative product, architecture, stack, UX, security, risk, and data guidance. Convert high-value portions into machine-consumable forms.

## Phase 2 — Standardize Feature Specs
Create a human-owned, AI-assisted Feature Spec workflow.

## Phase 3 — Introduce Orchestration
Define how Feature Specs move through implementation and validation.

## Phase 4 — Add AI Execution
Allow small engineering teams to use coding agents within the orchestration contract.

## Phase 5 — Introduce Guardians
Begin with architecture, stack, and security drift detection.

## Phase 6 — Add Exceptions
Create the formal path for intentional divergence and anchor evolution.

## Phase 7 — Close the Learning Loop
Use production telemetry, drift patterns, and exception outcomes to improve anchors and orchestration.

---

# 23. What the Anchor Model Is Not

It is not:

- a replacement for engineers;
- a replacement for Product Managers;
- a collection of Markdown files;
- a new waterfall process;
- a requirement that every feature pass every governance team;
- an argument for fully autonomous production deployment;
- a centralized architecture bureaucracy.

It is a governance and execution model designed to allow **greater autonomy because intent and constraints are made explicit and continuously verifiable**.

---

# 24. Relationship to Agile

The Anchor Model does not require abandoning Agile principles.

It changes the role of several familiar artifacts.

The backlog remains useful for sequencing.

Feature Specs become stronger units of value.

PRDs become durable product anchors rather than transient project documents.

Definition of Done becomes partly executable through orchestration and guardian checks.

Retrospectives can use drift and exception data rather than relying only on anecdotal observations.

Small teams remain empowered, but empowerment is supported by machine-readable organizational context.

In this sense, the Anchor Model can be viewed as an AI-native extension of agile delivery rather than its replacement.

---

# 25. The Emerging Operating Model

The resulting organization looks different from a traditional software factory.

Product Managers increasingly manage durable product intent and value decomposition.

Specialist functions maintain high-quality anchors rather than repeatedly reviewing the same basic questions.

Small engineering teams direct large amounts of AI execution capacity.

Guardian agents continuously inspect alignment.

Orchestration agents coordinate the lifecycle.

Humans adjudicate ambiguity, exceptions, risk, and strategy.

The system becomes capable of moving much faster without requiring every human control function to scale linearly with implementation volume.

---

# 26. Core Principles

The Anchor Model can be reduced to ten principles:

1. **Humans own truth and accountability.**
2. **AI may author without owning.**
3. **Durable intent should be represented as machine-consumable anchors.**
4. **A Feature Spec should represent one bounded unit of business value.**
5. **Orchestration should make the delivery process executable.**
6. **Governance should be risk-adaptive rather than universally heavy.**
7. **Specialized guardians should continuously detect drift.**
8. **Drift should trigger evaluation, not automatic conformity.**
9. **Exceptions should provide a governed path for innovation.**
10. **Telemetry and exceptions should continuously improve the anchors themselves.**

---

# 27. Conclusion

AI coding assistants make software execution dramatically more abundant.

That abundance does not eliminate the need for Product, Architecture, UX, Security, Risk, Data Governance, or Engineering judgment. It increases the importance of expressing their intent clearly enough that machines can operate within it.

The Anchor Model proposes a company-wide SDLC in which durable human-owned anchors define organizational truth; Product-owned orchestration determines how units of value move through the system; small engineering teams direct AI-assisted execution; guardian agents continuously detect drift; and explicit exception mechanisms allow the organization to learn rather than fossilize.

The fundamental shift is from documentation as something people are expected to remember to **intent as something the delivery system can continuously execute and verify**.

As implementation becomes cheaper, the competitive advantage may no longer be the organization that can produce the most code.

It may be the organization that can move fastest **without losing alignment**.

---
