flowchart TD
    Start[Start] --> StrategicAgent[StrategicAgent: Manage Aid Request]

    subgraph Parallel Execution
        InventoryAgent[InventoryAgent]
        WeatherAgent[WeatherAgent]
        RoadAgent[RoadAgent]
    end

    StrategicAgent --> InventoryAgent
    StrategicAgent --> WeatherAgent
    StrategicAgent --> RoadAgent

    InventoryAgent --> StrategicAgent
    WeatherAgent --> StrategicAgent
    RoadAgent --> StrategicAgent

    StrategicAgent --> DispatchDecision{Ready to Dispatch?}
    DispatchDecision -- Yes --> DispatchAgent[DispatchAgent]
    DispatchDecision -- No --> Replan[StrategicAgent: Replan or Wait]

    DispatchAgent --> Confirm[StrategicAgent: Confirm Delivery]
    Confirm --> End[End]