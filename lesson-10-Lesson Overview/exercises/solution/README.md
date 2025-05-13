# Solution
1. Deterministic Workflow (Fixed Sequence)
In this approach, the process follows a predefined sequence of steps regardless of the warehouse's actual conditions.

Flowchart:

flowchart TD
    Start([Start Inventory Management]) --> CheckInventory
    CheckInventory[Check Inventory Levels] --> Decision
    Decision{Is Inventory Low?}
    Decision -- Yes --> CreateOrder[Create Reorder Order]
    Decision -- No --> AuditInventory[Periodic Inventory Audit]
    AuditInventory --> End([End Process])
    CreateOrder --> End
Explanation:
Check Inventory: The system checks the inventory of products.

Decision: If inventory levels are low, it triggers a reorder.

Periodic Audit: The system runs a periodic audit regardless of inventory levels.

Fixed Process: The process runs the same steps every time, regardless of real-time data from the warehouse.

Limitations:
Rigid: Inventory checks and audits run on fixed intervals.

Inefficient: If inventory levels are constantly high, the reorder process is unnecessarily triggered.

Manual updates: Changes in workflows require hardcoding updates.

2. Agentic Workflow (Dynamic and AI-Driven)
In the agentic workflow, intelligent agents autonomously handle tasks like checking inventory, creating orders, and conducting audits. Agents can communicate with each other and adjust their behavior based on real-time data.

Flowchart:

flowchart TD
    Start([Start Agentic Workflow])
    InventoryChecker[Inventory Check Agent]
    OrderCreator[Order Creation Agent]
    Auditor[Inventory Audit Agent]
    Evaluator[Evaluator Agent]
    End([Finish])

    Start --> InventoryChecker
    InventoryChecker --> Evaluator
    Auditor --> Evaluator

    InventoryChecker -->|Low Inventory| OrderCreator
    InventoryChecker -->|Normal Inventory| Auditor

    Evaluator -->|Order Created| End
    Evaluator -->|Audit Done| End

    subgraph "Knowledge Agents"
        InventoryChecker[Inventory Check Agent\nTool: Query Database]
        OrderCreator[Order Creation Agent\nTool: Place Order]
        Auditor[Inventory Audit Agent\nTool: Scan and Verify]
        Evaluator[Evaluator Agent\nTool: Decision Maker]
    end
    
Explanation:
Inventory Check Agent: This agent queries the database to check real-time inventory levels and sends a signal to the evaluator agent.

Order Creation Agent: If inventory is low, the Order Creation Agent creates and places a reorder request.

Inventory Audit Agent: The agent runs periodic audits to verify stock levels without following a fixed schedule.

Evaluator Agent: This agent evaluates results from the inventory check, the reorder process, and audit completion.

Dynamic Routing: If inventory is low, the system skips the audit and directly triggers the reorder process. Otherwise, it continues with the audit.

Benefits of Agentic Workflow:
Adaptability: Agents dynamically adjust based on inventory levels and actions taken.

Efficiency: No unnecessary reorders occur if inventory levels are adequate.

Automation: The process is driven by agents, making it easier to scale and adapt to new requirements.