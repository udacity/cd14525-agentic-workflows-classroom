# Exercise: Transform a Deterministic Flow into an Agentic Workflow

## Goal:
Re-structure the incomplete deterministic flowchart below into an agentic flowchart using Mermaid.js. You'll define agents that operate in parallel and interact with a central decision-maker, reflecting an agentic AI workflow.

## Context:
You're managing an emergency aid dispatch system. In the original deterministic process, a central function handles everything step-by-step: checking inventory, weather, and roads before dispatching a team. Now, you're asked to design an agent-based system where specialized agents work in parallel and report results to a strategic coordinator agent.

## What You’re Given (Starter Code):

flowchart TD
    Start[Start] --> Manage[Manage Aid Request]

    Manage --> Inventory[Check Inventory]
    Manage --> 

    Inventory --> 

    Manage --> DispatchDecision{Ready to Dispatch?}
    DispatchDecision -- Yes --> Dispatch[Dispatch Team]
    DispatchDecision -- No --> Replan[Replan or Wait]

    Dispatch --> Confirm[Confirm Delivery]
    Confirm --> End[End]

## Your Tasks:
Insert Missing Parallel Steps:

Add Check Weather and Check Road Conditions nodes.

Connect them to and from the Manage Aid Request node, just like Check Inventory.

Create Agent Roles:

Replace Check Inventory, Check Weather, and Check Road Conditions with named agents (e.g., InventoryAgent, WeatherAgent, RoadAgent).

Encapsulate these three agents in a subgraph Parallel Execution block.

Add Message Flow Back to Manager:

Ensure each agent returns its result back to the Manage Aid Request node (e.g., StrategicAgent in your final version).

Rename Manage as a Central Coordinator Agent:

Once you introduce agents, rename Manage Aid Request to StrategicAgent.

Clean Up and Label Final Steps:

Rename Dispatch to DispatchAgent.

Rename Confirm and Replan steps appropriately to reflect agent roles (if needed).

## Think About:
What does it mean for agents to operate in parallel?

How should results be coordinated before making the dispatch decision?

How would this structure improve modularity, autonomy, and fault tolerance in an AI system?

Once complete, test your diagram at mermaid.live. When finished, your flowchart should be structured similarly to an agentic AI system with distributed decision-making.
