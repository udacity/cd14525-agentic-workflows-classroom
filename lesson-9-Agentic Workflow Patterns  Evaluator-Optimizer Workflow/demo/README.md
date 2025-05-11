# Evaluation Agent Workflow: Financial Report Generator

This project demonstrates a **multi-agent AI workflow** where a content generation agent and a compliance evaluation agent collaborate in an **iterative loop** to produce a polished, regulation-compliant investment report. The system improves the generated content over successive rounds based on feedback until it meets all predefined standards.

It showcases how large language models can be used not just for text generation, but also for automated self-review and revision through structured agent interactions.

---

## Workflow Overview

This project simulates a professional approval pipeline using two autonomous agents:

### 1. FinancialReportAgent — Generator

- **Purpose**: Generate persuasive investment summaries about decentralized finance (DeFi).
- **Behavior**:
  - Produces an initial draft based on a user prompt.
  - Accepts feedback from a compliance review and integrates it into the next draft.
  - Operates with a tone designed to inspire investor confidence while remaining professional.

### 2. ComplianceAgent — Evaluator

- **Purpose**: Enforce strict compliance rules by reviewing the generated summary.
- **Behavior**:
  - Flags speculative claims and forward-looking statements.
  - Only approves reports that avoid phrases like “expected,” “will likely,” “projected,” etc.
  - Provides either an “Approved” result or actionable revision feedback.

---

## Iterative Evaluation Workflow

This system uses a **feedback loop** pattern where each iteration makes the response more aligned with expectations:

1. **Initial Prompt**: The user supplies a high-level instruction for the investment summary.
2. **Generation**: The `FinancialReportAgent` produces a draft.
3. **Evaluation**: The `ComplianceAgent` checks for compliance issues.
4. **Revision**: If not approved, the evaluator's feedback is used to revise the prompt.
5. **Repeat**: The cycle continues for up to 5 attempts or until approval is achieved.

This process mimics real-world editorial workflows, where a piece of content is refined step by step through reviews and revisions. In this case, all steps are automated using GPT-based agents.

---

## Evaluation Agent Pattern

The design follows a general **Generator-Evaluator Agent Pattern**, used in AI systems to improve content quality through self-correction:

- The **Generator Agent** focuses on expressing ideas.
- The **Evaluator Agent** applies domain-specific constraints or rules.
- Each round of feedback from the evaluator is integrated into the generator’s next attempt.
- The system is **self-improving**: it learns from its own feedback and iterates until it gets it right.

This approach is particularly useful when:
- There is a clear goal or standard (e.g. compliance, accuracy, tone).
- Multiple outputs might need evaluation and refinement.
- Human review needs to be scaled or automated.

---

## Example in Action

- **Prompt**: Ask for a persuasive report explaining why DeFi will outperform traditional banking.
- **First Draft**: May include phrases like “DeFi will likely dominate the market.”
- **Evaluation**: Flags the speculative language.
- **Revision**: Generator integrates feedback and rewrites with cautious optimism, e.g. “DeFi has demonstrated strong growth compared to traditional banking in recent years.”
- **Result**: After a few iterations, the output meets the rules and is approved.

---

By combining generation and evaluation in a controlled loop, this workflow produces outputs that are not only compelling but also meet specific quality and compliance thresholds—entirely autonomously.
