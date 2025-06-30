# Nested Agent Agentic Workflow Demo with Group Chat Manager

This demo showcases an enhanced agentic workflow built around a central **Group Chat Manager** that orchestrates communication among multiple agents. The key innovation in this setup is that **all agent interactions are routed through the group chat manager**, enabling structured collaboration and shared context.

## Agent Roles

### ConversableAgent
- **Role**: Initiates the workflow by accepting a user prompt.
- **Behavior**: Sends the initial task definition to the **User Proxy** to kick off the process.

### User Proxy
- **Role**: Acts as the representative of the user within the agentic workflow.
- **Behavior**: Forwards tasks to the **Group Chat Manager**, where all agent collaboration occurs.
- **Purpose**: Acts as a boundary between user input and internal agent coordination.

### Group Chat Manager
- **Role**: The central hub for communication and coordination.
- **Behavior**: Receives all messages from the **User Proxy** and routes them to other agents (e.g., **Worker**, **Critic**).
- **Purpose**: Maintains a shared thread of conversation, ensuring agents have visibility into each other’s contributions and can collaborate more effectively.

### Worker
- **Role**: Executes the task or generates the desired output.
- **Behavior**: Listens to relevant prompts via the **Chat Manager** and responds with its output back to the shared context.

### Critic
- **Role**: Evaluates the output of the **Worker** and provides feedback or suggested improvements.
- **Behavior**: Also listens and responds within the group chat, fostering transparency and collective reasoning.

## Workflow Steps

1. The **ConversableAgent** begins with an input prompt.
2. The **User Proxy** receives the prompt and sends a message to the **Group Chat Manager**.
3. The **Group Chat Manager** broadcasts the message to both the **Worker** and the **Critic**.
4. The **Worker** performs the task and responds in the group chat.
5. The **Critic** evaluates the output and posts feedback or suggestions in the same shared chat.
6. The **User Proxy** observes the evolving conversation and can loop back revised prompts or terminate the cycle if satisfied.

## Key Advantages of Using a Group Chat Manager

- **Shared Context**: All agents operate within the same conversational space, enabling better awareness and alignment.
- **Loose Coupling**: Agents do not communicate directly with one another—this decoupling promotes modularity and simplifies debugging.
- **Scalability**: Additional agents (e.g., planner, verifier, memory) can be easily added without modifying existing agent logic.
- **Transparency**: Every agent sees the full message history, which supports richer interactions and emergent behavior.

## Design Considerations

- The **Group Chat Manager** acts as both a message router and a shared memory space.
- The **User Proxy** retains control of the task loop, allowing decisions about when to continue or end the task.
- The system supports asynchronous updates, allowing agents to act independently but within the shared group context.

