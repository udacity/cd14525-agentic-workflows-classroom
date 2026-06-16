# Test script for DirectPromptAgent class
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = "voc-446254091159874495708569e8ffe718ef35.52178059"

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key=openai_api_key)

direct_agent_response = direct_agent.respond(prompt=prompt)


# Print the response from the agent
print(direct_agent_response)

explanation = "The agent used its inherent knowledge to answer the prompt, which is based on the training data it was trained on.\nIt did not use any external knowledge sources or specific knowledge provided in the prompt."
print(explanation)

with open("/workspace/cd14525-agentic-workflows-classroom/project/starter/phase_1/test_output/action_planning_agent_response.txt", "w") as file:
    file.write(f"Explanation of the agent's response:\n{explanation}\n")
    file.write("\n")
    file.write(f"Prompt: \n{prompt}\n")
    file.write("\n")
    file.write(f"Response: \n{direct_agent_response}\n")