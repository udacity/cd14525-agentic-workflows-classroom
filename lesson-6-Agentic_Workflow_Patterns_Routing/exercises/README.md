# Creating an Agentic Workflow with a ROuting Agent for Retail Applications

Let me create an exercise that teaches agentic workflows in the context of retail applications, using the provided code as a reference.

## Exercise: Building a Retail Product Intelligence System

In this exercise, you'll implement an agentic workflow for a retail product intelligence system that helps store managers make informed decisions about inventory, pricing, and customer preferences.
Exercise Overview
You'll build a system with three specialized agents:

**Product Researcher Agent:** Researches product specifications, market trends, and competitor pricing
**Customer Analyzer Agent:**: Analyzes customer feedback and purchase patterns
**Pricing Strategist Agent:** Recommends optimal pricing strategies based on research and analysis

The system will use a Routing Agent to direct queries to the appropriate specialized agent.

## Retail Agentic Workflow Exercise

In this exercise, you'll build an agentic workflow system for a retail product intelligence application. The system will help store managers make data-driven decisions by directing queries to specialized AI agents.

## Your Task

You need to implement:

The pricing_strategist_agent function that can recommend optimal pricing strategies based on product research and customer analysis data
The routing_agent function that determines which specialized agent should handle a given query

Your implementation should demonstrate key principles of agentic workflows:

Task decomposition
Specialized agent capabilities
Intelligent routing
Context passing between agents

## Expected Functionality
When a user submits a query about pricing (e.g., "What should be the optimal price for our new organic skincare line?"), the system should:

Recognize this is a pricing question
Gather necessary product information first
Collect relevant customer insights next
Use both sets of data to inform a pricing recommendation

For product research and customer analysis queries, the system should route directly to the appropriate agent.
Implementation Steps

Complete the pricing_strategist_agent function to use both product and customer data
Implement the routing_agent function to:

Analyze the query content
Determine which specialized agent to use
Gather prerequisite information when needed (for pricing questions)
Return results from the appropriate agent



## Example Solution

I've provided a complete solution that demonstrates how these functions should work. Study it to understand the expected behavior, but I encourage you to implement your own version.
When you're done, your system should be able to handle all three example queries and route them to the appropriate agents.
Would you like to start by implementing one of these functions first, or would you prefer to see any specific aspects of the solution explained in more detail?RetryClaude can make mistakes. Please double-check responses.
