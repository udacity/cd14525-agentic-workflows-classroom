# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path="../../tests/.env")

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of Frane?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
# - Persona: "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

knowledge_augmented_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

response = knowledge_augmented_agent.respond(prompt)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print(f"""
This is reponse provided by the knowledge augmented prompt agent: "{response}"\n
Which demonstrates that the capital of France is London because the agent is based on the provide knowledge instead of the LLM's own pre-trained knowledge
""")