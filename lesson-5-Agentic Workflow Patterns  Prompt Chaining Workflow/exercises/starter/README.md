# Exercise: Build an Agentic Workflow for a Refinery Distillation Optimization Use Case

## Objective

Create a prompt-chaining agentic workflow using OpenAI's API that simulates a system managing the distillation process in a refinery. Your workflow should involve agents that:

Understand the incoming hydrocarbon feedstock.

Manage the distillation tower process to determine the quantity of each output product (e.g., gasoline, diesel, kerosene).

Analyze market demand for each product.

Make production recommendations based on both operational capabilities and market conditions.

## Instructions

Using the example code provided below as a reference, implement a new Python script with the following components:

**Agent 1:** Feedstock Analyst Agent
Role: Understand and analyze the type of hydrocarbon feedstock received.

Input: Name of the hydrocarbon stream (e.g., "Light Sweet Crude").

Output: A breakdown of likely components and suitability for different product yields.

**Agent 2:** Distillation Planner Agent
Role: Based on the feedstock analysis, suggest how to allocate the hydrocarbon stream through the distillation tower.

Input: Output of Feedstock Analyst Agent.

Output: Estimated volumes for each product (e.g., 40% gasoline, 30% diesel, etc.).

**Agent 3:** Market Analyst Agent
Role: Assess the current demand and pricing trends for each product.

Input: List of output products.

Output: Market analysis with demand levels and profitability suggestions.

**Agent 4:** Production Optimizer Agent
Role: Recommend an optimal production plan that balances yield and market needs.

Input: Outputs from both Distillation Planner and Market Analyst Agents.

Output: Final recommendation on how much of each product to produce.

## Bonus Challenge:
Add logging and print statements at each step to trace agent behavior. For added realism, ask the agents to use structured formatting (e.g., headings, bullet points, tables) to make their outputs clearer.

## Example Starter:

You can start your script structure like this:


def feedstock_analyst_agent(feedstock_name):
    # Analyze the hydrocarbon feed
    ...

def distillation_planner_agent(feedstock_analysis):
    # Allocate through distillation tower
    ...

def market_analyst_agent(product_list):
    # Analyze market conditions
    ...

def production_optimizer_agent(distillation_plan, market_data):
    # Recommend a production plan
    ...


## Deliverable
A Python script that chains together the above four agents, passes data between them, and prints the final optimized production recommendation for the refinery.