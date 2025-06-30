# Nested Agent Agentic Workflow Demo

This demo illustrates a simple yet powerful agentic workflow architecture using four core agents: the **ConversableAgent**, **User Proxy**, **Worker**, and **Critic**. The goal is to show how agent collaboration and feedback can be structured to support iterative task completion and refinement.

## Agent Descriptions

### 🗣️ ConversableAgent
- **Function**: Initiates the workflow.
- **Behavior**: Accepts an input prompt from a human or another system and begins the process by sending the task to the **User Proxy**.
- **Purpose**: Acts as the entry point and primary interface for task definition.

### User Proxy
- **Function**: Mediates between the user-facing agent (ConversableAgent) and the task-executing agents.
- **Behavior**: Forwards the task to the **Worker**, monitors feedback from the **Critic**, and determines whether to loop the task back for improvement.
- **Purpose**: Serves as a coordinator that holds task context and routes communication.

### Worker
- **Function**: Performs the task.
- **Behavior**: Executes instructions received from the **User Proxy** and generates an output or solution.
- **Purpose**: Handles the logic or processing required for the task.

### Critic
- **Function**: Evaluates and critiques the Worker’s output.
- **Behavior**: Reviews the response from the **Worker** and sends improvement suggestions or corrections back to the **User Proxy**.
- **Purpose**: Introduces a quality control step to refine output over one or more iterations.

## Workflow Dynamics

1. **Task Initiation**: The **ConversableAgent** receives a user prompt and forwards it to the **User Proxy**.
2. **Task Delegation**: The **User Proxy** hands off the task to the **Worker**, initiating task execution.
3. **Execution**: The **Worker** completes the task and returns the result.
4. **Review**: The result is passed to the **Critic**, who reviews and suggests revisions or enhancements.
5. **Iteration**: The **User Proxy** receives the critique and can either:
   - Re-engage the **Worker** with revised instructions,
   - Modify the prompt,
   - Or conclude the task if the result is satisfactory.

This feedback loop can repeat multiple times, enabling emergent reasoning and self-improvement within the workflow.

## Key Characteristics

- **Modularity**: Each agent has a clear, decoupled role, allowing for easy replacement or scaling.
- **Iterativity**: The system is designed to support repeated critique and improvement cycles.
- **Traceability**: Each message and decision point is managed explicitly by the **User Proxy**, making it easy to track state and logic over time.
- **Extensibility**: New agent roles (e.g., Planner, Optimizer) can be integrated without disrupting core logic.

## Use Cases

This demo serves as a foundation for building more advanced systems involving:
- Code generation and review loops
- Autonomous product planning workflows
- Research assistants with feedback-driven refinement
- Educational agents that learn from critique

