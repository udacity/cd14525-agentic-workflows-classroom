from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = "voc-446254091159874495708569e8ffe718ef35.52178059"

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

augmented_agent = AugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona)

augmented_agent_response = augmented_agent.respond(input_text=prompt)

# Print the agent's response
print(augmented_agent_response)

explanation = """The agent likely used its inherent knowledge about the capital of France, which is Paris, to answer the prompt.
The system prompt specifying the persona as a college professor influenced the agent's response to start with "Dear students," which adds a formal tone to the answer.
"""
print(explanation)


with open("/workspace/cd14525-agentic-workflows-classroom/project/starter/phase_1/test_output/action_planning_agent_response.txt", "w") as file:
    file.write(f"Explanation of the agent's response:\n{explanation}\n")
    file.write("\n")
    file.write(f"Prompt: \n{prompt}\n")
    file.write("\n")
    file.write(f"Response: \n{augmented_agent_response}\n")
