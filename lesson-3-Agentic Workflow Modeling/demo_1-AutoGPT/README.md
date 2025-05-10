# AutoGPT-Style Agentic Workflow

# Goal Setting Workflow Model

This demo illustrates a foundational **agentic workflow pattern** inspired by systems like **AutoGPT**, **BabyAGI**, and other autonomous AI agents. It captures how such agents operate through a loop of **goal planning, task execution, and self-evaluation**, progressively working toward complex objectives with minimal or no human intervention after the initial prompt.

## Workflow Stages

The agent follows a structured loop composed of five key components:

### 1. Input Prompt
The user initiates the system with a high-level **objective**, such as:
- “Research the top 3 competitors in the renewable energy sector.”
- “Create a weekly content plan for a tech blog.”

This prompt acts as the **initial driver** for the agent's reasoning loop.

---

### 2. Goal Setting
The agent interprets the prompt and formulates a **specific, actionable goal**. This step transforms a vague or broad instruction into a structured target that guides the subsequent steps.

*Example*:  
From the prompt “Plan a product launch,” the agent may set the goal:  
> “Deliver a 5-step launch plan covering messaging, timeline, and required assets.”

---

### 3. Defining and Sequencing Tasks
The agent decomposes the goal into **subtasks** and determines their optimal execution order. This is the core of the **task planning** phase, common in agentic workflow patterns such as:

- **Plan-Act-Evaluate**
- **Goal → Task → Tool Selection**
- **Think → Do → Reflect**

The output is a structured sequence, like:
1. Research target audience
2. Define launch message
3. Create asset checklist
4. Draft timeline
5. Assign roles

---

### 4. Task Execution
Each task is performed using the agent’s available **tools and functions**—for example:
- Calling APIs
- Running code
- Using a language model (LLM) for writing or summarization
- Fetching data from the web

The agent combines logic, tool usage, and generative capabilities to carry out the plan.

---

### 5. Evaluation
Once tasks are completed, the agent **evaluates** whether the original goal has been met. This may include:
- Verifying task outputs
- Comparing results to criteria
- Re-assessing if the objective needs further refinement

Based on this evaluation, the agent either:
- Concludes the process (if the goal is achieved), or
- Returns to the **task planning** stage to re-define or re-sequence the next steps

This establishes a **feedback loop** that enables autonomous correction and iteration.

---

## Agentic Workflow Pattern Reference

This demo aligns with the growing family of **agentic workflow patterns**, particularly:

- **Plan → Execute → Reflect (PER)**
- **AutoGPT-style Loops** with dynamic planning and re-evaluation
- **Modular Agent Architectures** that separate planning, execution, and evaluation as distinct agents or subsystems

These patterns are foundational in the design of **LLM-based autonomous systems**, and are increasingly used in domains such as:

- Software agents
- Digital assistants
- Workflow copilots
- Scientific research agents
