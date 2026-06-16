from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = "voc-446254091159874495708569e8ffe718ef35.52178059"

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)

knowledge_agent_response = knowledge_agent.respond(input_text=prompt)

print(knowledge_agent_response)

# Explanation of the agent's response
explanation = """The agent relied exclusively on the provided information, which incorrectly identifies London as the capital of France instead of Paris. This demonstrates that the agent is strictly adhering to the instruction to use only the supplied knowledge, rather than drawing on its own general knowledge, which would normally indicate Paris as the correct capital. Additionally, the system prompt assigning the persona of a college professor influenced the tone of the response, leading the agent to begin with “Dear students,” and thereby creating a more formal style.
"""

print(explanation)

with open("/workspace/cd14525-agentic-workflows-classroom/project/starter/phase_1/test_output/action_planning_agent_response.txt", "w") as file:
    file.write(f"Explanation of the agent's response:\n{explanation}\n")
    file.write("\n")
    file.write(f"Prompt: \n{prompt}\n")
    file.write("\n")
    file.write(f"Response: \n{knowledge_agent_response}\n")