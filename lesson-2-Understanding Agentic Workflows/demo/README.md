# Agentic vs Deterministic Workflow Demos

This folder contains two Python demos that illustrate the difference between deterministic workflows and agentic workflows, with and without the use of AI. Each demo highlights how tasks can be handled either through fixed logic or flexible reasoning.

## Demo 1: Deterministic vs Rule-Based Agentic Workflow (No AI)
This demo contrasts two non-AI workflows:

### Deterministic Workflow
Executes a hardcoded, linear sequence of steps

Ignores context or task characteristics

No flexibility or decision-making logic

### Agentic Workflow (Using Fixed Rules)
Uses simple agents that follow predefined, hardcoded rules

Agents decide what to do next based on task metadata

Priority Handler: Selects tasks with high priority

Efficiency Expert: Selects tasks with low complexity

Agents do not use AI or learning—all logic is static and rule-based

### Key Takeaways

Deterministic workflows always follow the same path.

Agentic (rule-based) workflows inspect the current state and decide the next action using fixed decision rules.

This shows how even non-AI agents can introduce basic adaptability into a workflow.

### Demo 2: LLM-Based Agentic Workflow (with OpenAI)
This version upgrades the agentic workflow by integrating real LLM calls using the OpenAI API. It compares:

### Deterministic Workflow (same as above)
Uses hardcoded logic with static decision paths

### LLM-Based Agentic Workflow
Replaces rule-based decision-making with a GPT-powered agent

The agent:

Analyzes tasks using natural language reasoning

Selects a strategy based on evolving context

Provides an explanation for each decision

Supports more nuanced, adaptable workflows without modifying logic code

### Key Benefits Over Fixed-Rule Agents
Simpler logic: No need for custom rule trees or scoring

Greater flexibility: Adapts to new task attributes dynamically

Explainability: Outputs human-readable reasoning for every decision
