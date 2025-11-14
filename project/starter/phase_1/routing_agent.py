# DONE: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
from workflow_agents.base_agents import RoutingAgent

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

knowledge = "You know everything about Texas"
# DONE: 2 - Define the Texas Knowledge Augmented Prompt Agent
texas_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key=openai_api_key, persona=persona, knowledge=knowledge)

knowledge = "You know everything about Europe"
# DONE: 3 - Define the Europe Knowledge Augmented Prompt Agent
europe_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key=openai_api_key, persona=persona, knowledge=knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# DONE: 4 - Define the Math Knowledge Augmented Prompt Agent
math_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key=openai_api_key, persona=persona, knowledge=knowledge)

routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_knowledge_agent.respond(x) # DONE: 5 - Call the Texas Agent to respond to prompts
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_knowledge_agent.respond(x) # DONE: 6 - Define a function to call the Europe Agent
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_knowledge_agent.respond(x) # TODO: 7 - Define a function to call the Math Agent
    }
]

routing_agent.agents = agents

# DONE: 8 - Print the RoutingAgent responses to the following prompts:
#           - "Tell me about the history of Rome, Texas"
#           - "Tell me about the history of Rome, Italy"
#           - "One story takes 2 days, and there are 20 stories"
prompt = "Tell me about the history of Rome, Texas"
print(f"Prompt: {prompt}")
print(f"Response: {routing_agent.route(prompt)}")

prompt = "Tell me about the history of Rome, Italy"
print(f"Prompt: {prompt}")
print(f"Response: {routing_agent.route(prompt)}")

prompt = "One story takes 2 days, and there are 20 stories"
print(f"Prompt: {prompt}")
print(f"Response: {routing_agent.route(prompt)}")
