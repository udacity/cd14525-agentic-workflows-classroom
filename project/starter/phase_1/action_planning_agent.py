from workflow_agents.base_agents import ActionPlanningAgent
import os

openai_api_key = "voc-446254091159874495708569e8ffe718ef35.52178059"

knowledge = """
# Fried Egg
1. Heat pan with oil or butter
2. Crack egg into pan
3. Cook until white is set (2-3 minutes)
4. Season with salt and pepper
5. Serve

# Scrambled Eggs
1. Crack eggs into a bowl
2. Beat eggs with a fork until mixed
3. Heat pan with butter or oil over medium heat
4. Pour egg mixture into pan
5. Stir gently as eggs cook
6. Remove from heat when eggs are just set but still moist
7. Season with salt and pepper
8. Serve immediately

# Boiled Eggs
1. Place eggs in a pot
2. Cover with cold water (about 1 inch above eggs)
3. Bring water to a boil
4. Remove from heat and cover pot
5. Let sit: 4-6 minutes for soft-boiled or 10-12 minutes for hard-boiled
6. Transfer eggs to ice water to stop cooking
7. Peel and serve
"""

agent = ActionPlanningAgent(openai_api_key=openai_api_key, knowledge=knowledge)

prompt = "One morning I wanted to have scrambled eggs"
print(f"Prompt: {prompt}")

response = agent.extract_steps_from_prompt(prompt)

# Print the agent's response
print("Agent's response to the prompt:")
print("\n".join(response))

with open("/workspace/cd14525-agentic-workflows-classroom/project/starter/phase_1/test_output/action_planning_agent_response.txt", "w") as file:
    file.write(f"Prompt: \n{prompt}\n")
    file.write("\n")
    file.write(f"Response: \n")
    file.write("\n".join(response) + "\n")
