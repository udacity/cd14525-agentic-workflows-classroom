
# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="../../tests/.env")

openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

knowledge = "You know everything about Texas"
texas_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
# TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent

knowledge = "You know everything about Europe"
# TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent
europe_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# TODO: 4 - Define the Math Knowledge Augmented Prompt Agent
math_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_knowledge_agent.respond(x) # TODO: 5 - Call the Texas Agent to respond to prompts
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_knowledge_agent.respond(x)# TODO: 6 - Define a function to call the Europe Agent
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        # TODO: 7 - Define a function to call the Math Agent
        "func": lambda x: math_knowledge_agent.respond(x)
    }
]

routing_agent.agents = agents
# TODO: 8 - Print the RoutingAgent responses to the following prompts:
prompts = ["Tell me about the history of Rome, Texas",
          "Tell me about the history of Rome, Italy",
          "One story takes 2 days, and there are 20 stories"]

for prompt in prompts:
    print(f"\n=== User's input: {prompt}")
    response = routing_agent.route(prompt)
    print(f"\n=== Response to the user's input: {response}")

