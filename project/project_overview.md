## Introduction

Welcome to the project AI-Powered Agentic Workflow for Project Management! Imagine yourself as a highly sought-after AI Workflow Architect. Startups and tech companies alike are clamoring for your expertise in designing and implementing intelligent agentic systems that don't just automate tasks, but dynamically *manage* them. Your newest client, **InnovateNext Solutions**, a rapidly scaling startup brimming with brilliant ideas but hampered by inconsistent project execution, has a critical challenge they believe only *you* can solve.

They are seeking a revolutionary way to manage their entire product development lifecycle. Your goal is to step in and engineer a sophisticated, **reusable agentic workflow**. This system should bring order and efficiency to their process, ensuring their *various* product ideas can be *consistently and scalably* transformed into well-defined user stories, product features, and detailed engineering tasks. You will pioneer this system by first applying it to their upcoming "Email Router" project as a pilot.

## The Challenge: Building a Scalable Engine for Innovation

InnovateNext Solutions is overflowing with innovative concepts but faces a significant bottleneck: turning these ideas into actionable development plans efficiently and consistently. Their current ad-hoc methods lead to miscommunications, varied output quality, and delays across *all* their projects. They need a foundational, AI-driven project management framework that can be applied company-wide.

Your **Role** as an AI Workflow Architect is twofold:
1.  First, you'll construct a robust library of diverse, reusable AI agents – the versatile building blocks for this and future advanced agentic systems. This is about crafting your core, adaptable toolkit.
2.  Then, you'll deploy a selection of these agents to build the **general-purpose agentic workflow for technical project management**. You will demonstrate its power and flexibility by using their "AI-Powered Email Router" product specification (`Product-Spec-Email-Router.txt`) as the initial input for this pilot implementation.

The **Audience** for your solution are the technical project managers, the leadership team, particularly the Head of Product and Lead Technical Program Manager at InnovateNext. They are looking for a robust system that not only works for the Email Router but also assists the technical project managers at InnovateNext for future product development.

## Your Product: AI-Powered Agentic Workflow for Project Management (Pilot: Email Router)

You will deliver a two-part solution:

**Phase 1: The Agentic Toolkit**
* A Python package (`workflow_agents`) containing seven meticulously crafted and individually tested agent classes (`base_agents.py`):
    * `DirectPromptAgent`
    * `AugmentedPromptAgent`
    * `KnowledgeAugmentedPromptAgent`
    * `RAGKnowledgePromptAgent` (provided, but understand its role)
    * `EvaluationAgent`
    * `RoutingAgent`
    * `ActionPlanningAgent`
* Standalone test scripts for each agent, proving their individual capabilities, along with screenshots of successful test runs.

**Phase 2: The Project Management Workflow Implementation**
* A primary Python script (`agentic_workflow.py`) that orchestrates a selection of your Phase 1 agents (`ActionPlanningAgent`, `KnowledgeAugmentedPromptAgent`, `EvaluationAgent`, `RoutingAgent`) to perform the multi-step technical project management task. This script will be designed as a **general-purpose workflow**.
* For the pilot, this workflow will:
    1.  Accept a high-level prompt (simulating a TPM's request) and InnovateNext's `Product-Spec-Email-Router.txt` (as the example product spec).
    2.  Employ an **Action Planning Agent** to break down the overall goal into logical sub-tasks.
    3.  Utilize a **Routing Agent** to intelligently assign each sub-task to the appropriate specialized agent team.
    4.  Simulate a **Product Manager** team (a `KnowledgeAugmentedPromptAgent` for generating user stories based on the provided product spec, paired with an `EvaluationAgent` to ensure stories meet specific criteria like: `"As a [type of user], I want [an action or feature] so that [benefit/value]."`).
    5.  Simulate a **Program Manager** team (a `KnowledgeAugmentedPromptAgent` for defining product features, paired with an `EvaluationAgent` to ensure features meet criteria like detailed descriptions, functionality, and user benefits).
    6.  Simulate a **Development Engineer** team (a `KnowledgeAugmentedPromptAgent` for creating detailed engineering tasks, paired with an `EvaluationAgent` to ensure tasks meet criteria like task IDs, descriptions, acceptance criteria, and estimations).
    7.  Produce a final, structured output representing the comprehensively planned project (for the Email Router), demonstrating the workflow's capability.

## Project Submission

At the end of the project, you will need to submit the following documents for review:
1. Phase 1:
  - Fully implemented reusable agent library (`workflow_agents/base_agents.py`).
  - Test scripts for each agent in the reusable agent library
  - Screenshots of correct outputs on running each of the seven scripts
2. Phase 2:
  - 

You'll be drawing upon your understanding of LLMs, agent design patterns (like personas, knowledge augmentation, evaluation loops, and routing), and your Python programming skills to bring this cutting-edge, scalable solution to life.

Ready to show InnovateNext Solutions how AI can revolutionize their entire approach to project management, starting with the Email Router? Let's architect the future of work!

---