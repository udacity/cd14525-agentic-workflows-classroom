# Hierarchical Agentic Workflow Demo

This demo illustrates a **hierarchical agentic workflow pattern** implemented by tools such as *CrewAI*. The workflow divides responsibilities between two specialized agents—a **Researcher Agent** and a **Writer Agent**—under the supervision of a **Crew Manager**. This structure supports clear task delegation, modular execution, and high-quality output generation for complex assignments.

## System Structure

- **Crew Manager**: Orchestrates the full process. It receives the user prompt, assigns subtasks to agents, and collects their outputs.
- **Researcher Agent**: Focused on gathering, validating, and analyzing information relevant to the task.
- **Writer Agent**: Uses the research findings to generate, structure, and refine final content.

This hierarchy ensures that each agent remains focused on a well-defined scope, improving task clarity and outcome consistency.

---

## Workflow Overview

### 1. User Input
The process starts when a user submits a request (e.g., “Write a report on clean energy trends”). The **Crew Manager** interprets this prompt and launches the corresponding workflow by engaging both the Researcher and Writer agents.

---

### 2. Researcher Agent

**Goal**: Deliver a high-quality research report as input for content generation.

#### Tasks and Tools:
- **Information Gathering**
  - *Tools*: Web Search, Database Access
- **Source Evaluation**
  - *Tools*: Credibility Checker
- **Data Analysis**
  - *Tools*: Data Processing Engine, Knowledge Graph

The Researcher Agent completes these tasks independently, then aggregates findings into a **Research Report**, which is returned to the Crew Manager.

---

### 3. Writer Agent

**Goal**: Produce polished content based on the Research Report.

#### Tasks and Tools:
- **Content Structuring**
  - *Tools*: Outline Generator
- **Draft Creation**
  - *Tools*: Language Model, Citation Manager
- **Editing & Refinement**
  - *Tools*: Grammar Checker, Readability Analyzer

The Writer Agent transforms the research into clear, structured, and well-edited final content, which is delivered back to the Crew Manager for final output.

---

## Key Features

- **Hierarchical Coordination**: A centralized manager ensures smooth communication and output integration across agents.
- **Agent Specialization**: Each agent is designed to focus on a distinct phase of the task, using tools optimized for its function.
- **Workflow Modularity**: The entire process is broken into modular, traceable steps, allowing for reusability and easy customization.
- **Quality Assurance**: Specialized tooling enables deeper analysis and higher-quality writing than single-agent approaches.
