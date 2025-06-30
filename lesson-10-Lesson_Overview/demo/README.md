# Demo: Comparing Deterministic and Agentic Workflows for Pump Maintenance

This demo compares two approaches to factory pump maintenance:

1. **Deterministic Workflow** – a fixed, rule-based process.
2. **Agentic Workflow** – a dynamic, AI-powered workflow using autonomous agents.

---

## 1. Deterministic Workflow (Traditional Approach)

The deterministic workflow uses a linear, hardcoded sequence. Every pump, regardless of its condition, goes through the same steps.

### Flowchart

flowchart TD
    Start([Start Maintenance Workflow]) --> CheckSchedule
    CheckSchedule[Check Maintenance Schedule] --> InspectPump
    InspectPump[Perform Visual Inspection] --> RunDiagnostics
    RunDiagnostics[Run Sensor-Based Diagnostics] --> Analyze
    Analyze[Analyze Inspection & Diagnostic Results] --> Decision
    Decision{Is Maintenance Required?}
    Decision -- Yes --> CreateWorkOrder[Create Work Order]
    Decision -- No --> End([No Action Needed])
    CreateWorkOrder --> End

#### Limitations
Rigid: Follows the same sequence regardless of real-time data.

Low adaptability: Hard to update when tools, conditions, or insights change.

Manual: All logic is pre-scripted and static.

### 2. Agentic Workflow (AI-Driven and Adaptive)
The agentic workflow dynamically assembles tasks based on context. It uses intelligent agents that reason, communicate, and act using tools. This model enables flexible, goal-driven execution rather than following a fixed script.

## Flowchart

flowchart TD
    Start([Start Agentic Workflow])
    Decomposer[Task Decomposition Agent]
    Router[Router Agent]
    Evaluator[Evaluator Agent]
    End([Finish])

    Start --> Decomposer
    Decomposer --> Router

    Router --> A
    Router --> B
    Router --> C

    A --> Evaluator
    B --> Evaluator
    C --> Evaluator

    Evaluator -->|Fix Needed| D
    D --> Evaluator
    Evaluator -->|OK| End

    subgraph "Knowledge Agents"
        A[Pump Info Agent\nTool: Fetch Pump History]
        B[Visual Inspection Agent\nTool: Camera/Report Parser]
        C[Diagnostics Agent\nTool: Sensor Data Analysis]
        D[Work Order Agent\nTool: Create/Track Orders]
    end

## Agent Roles
Task Decomposition Agent: Breaks down the high-level goal ("assess pump") into actionable subtasks.

Router Agent: Sends subtasks to the correct knowledge agents based on their domain expertise.

### Knowledge Agents:

Pump Info Agent – Looks up past issues and maintenance logs.

Visual Inspection Agent – Reviews reports or drone/camera footage.

Diagnostics Agent – Analyzes live or historical sensor data.

Work Order Agent – Creates and submits work requests for repairs.

Evaluator Agent: Assesses all collected data and decides whether to trigger a fix or confirm the pump is operational.



## Key Takeaways
Deterministic workflows are straightforward but rigid. They work best for routine tasks where every condition is known in advance.

Agentic workflows provide dynamic, real-time flexibility. They let you build maintainable, modular systems where agents can take on tasks autonomously and evolve with your environment.

This agent-based approach is more robust in the face of variability and scales well as you introduce new tools or automation capabilities.