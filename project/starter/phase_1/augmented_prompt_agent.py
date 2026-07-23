# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="../../tests/.env")

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'

augmented_agent_response = augmented_agent.respond(prompt)
# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt:
#   The AugmentedPromptAgent has no external knowledge base or retrieval step attached,
#   so the factual answer ("Paris") comes purely from the LLM's own parametric/pretrained
#   knowledge, the same general world knowledge it learned during training, not from any
#   knowledge passed in by this agent.
# - How the system prompt specifying the persona affected the agent's response:
#   The persona system message ("You are a college professor... start with 'Dear students,'")
#   did not change the underlying fact, but it shaped the style, tone, and framing of the
#   reply: the model adopts a formal, instructional voice and opens with "Dear students,"
#   which a plain DirectPromptAgent call (no system prompt) would not produce.