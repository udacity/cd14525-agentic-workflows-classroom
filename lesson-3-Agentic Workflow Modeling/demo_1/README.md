# Factory Risk Assessment Workflow Demo
This demo showcases two approaches for evaluating whether a factory should be built:

A deterministic, rule-based workflow

An agentic, modular implementation leveraging autonomous agents.

## 1. Deterministic Workflow (Rule-Based Steps)
This traditional approach follows a fixed, sequential logic:

**Data Collection**
Gather key inputs such as:

Income

Credit score

Employment history

Debt-to-income ratio

**Data Validation**
Ensure data completeness and accuracy:

Income must be non-zero

Credit score must be between 300–850

**Risk Scoring**
Apply a formula to compute risk:

ini
Copy
Edit
RiskScore = (0.4 × CreditScore) + (0.3 × Income) - (0.3 × DebtToIncomeRatio)

**Risk Categorization**
Classify risk based on the computed score:

≥ 700 → Low Risk

600–699 → Medium Risk

< 600 → High Risk

**Decision Making**
Determine outcome:

Low Risk → Approve

Medium Risk → Manual Review

High Risk → Reject

## 2. Agentic Workflow (Modular Agent-Based System)
This approach models the assessment as a pipeline of autonomous agents, each with a specialized function. Information flows top-down, with feedback loops when needed.

**Task Decomposition Agent**
Breaks the goal ("Should we build a new factory?") into manageable subtasks:

Location analysis

Cost estimation

Market analysis

Risk identification

Financial modeling

**Routing Agent**
Dispatches each subtask to the appropriate agent and defines execution order:

Resolves dependencies (e.g., cost and market depend on location)

Optimizes for parallel execution when possible

**Knowledge Gathering Agents**
Specialized agents for each subtask:

Location Agent: Infrastructure, political risk, environmental constraints

Cost Agent: Capital and operating expenses

Market Agent: Demand forecasts, price sensitivity

Risk Agent: Regulatory, supply chain, and environmental risks

Each agent returns structured outputs (e.g., documents, confidence scores, or KPIs).

**Evaluation Agent**
Synthesizes all inputs and performs:

Scenario modeling (e.g., best/worst-case)

ROI, IRR, and risk-adjusted return calculations

Inconsistency detection

Outputs holistic risk/benefit assessment

**Decision Agent**
Makes a recommendation based on the evaluation:

Strong case & acceptable risk → Approve

Borderline or uncertain → Escalate for human review

Checks for alignment with business criteria and thresholds

**Optional Human Review**
Engages a human expert if needed:

Handles edge cases or low-confidence decisions

Adds human accountability in high-risk situations

**Key Characteristics**
Modular: Agents are independent and replaceable

Deterministic logic: Rule-based flow, even with probabilistic internals

Scalable: Easily extend with more agents or evaluation criteria

Auditable: Transparent, traceable decision steps
