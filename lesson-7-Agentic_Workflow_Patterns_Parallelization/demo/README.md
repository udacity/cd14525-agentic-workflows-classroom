# Parallel Agentic Workflow Demo – Energy Industry Use Case

This demo showcases how to run multiple specialized agents **in parallel** using OpenAI's `gpt-4`, then synthesize their responses into a final summary using another agent. It demonstrates the basics of **agent orchestration** using threads and OpenAI's v1+ Python SDK.

## Use Case

Prompt:
> _"What are current trends shaping the future of the energy industry?"_

Three expert agents—**Policy**, **Technology**, and **Market**—respond independently to the prompt. Their insights are then passed to a **Summary Agent**, which synthesizes them into a final response.

---

## Components

### `PolicyAgent`
Provides insights on global energy policy, climate regulations, and geopolitical shifts.

### `TechnologyAgent`
Covers advances in renewables, smart grids, hydrogen, energy storage, and related tech.

### `MarketAgent`
Focuses on trends in pricing, demand, supply chains, and global investments in energy.

### `SummaryAgent`
Reads the responses from all three agents and combines them into a concise, coherent summary.

---

## How It Works

1. The script loads the OpenAI API key from `.env`.
2. Each agent runs **in parallel using `threading.Thread`**.
3. After all agents finish, their results are passed to the `SummaryAgent`.
4. The final synthesized answer is printed.

---

## Concepts Demonstrated
Agent-based design

Threading for parallel execution

Prompt engineering by role

API usage with OpenAI v1 SDK

Summarization from multiple sources