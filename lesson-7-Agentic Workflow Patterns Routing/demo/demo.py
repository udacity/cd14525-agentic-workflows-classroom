import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
# Make sure you have a .env file with your OPENAI_API_KEY
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-4o"):
    """Simple wrapper for OpenAI API calls."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


# --- Agent Class Implementations ---

class CodeGenerationAgent:
    """Agent that generates code based on a natural language description."""
    def __init__(self):
        self.description = "Code Generation Agent: Use this agent to generate code in various programming languages based on a textual description of the desired functionality."
        self.name = "Code Generation Agent"

    def get_description(self):
        """Returns the agent's description."""
        return self.description

    def run(self, task_prompt):
        """Executes the code generation task."""
        system_prompt = """You are a specialist Code Generation Agent. Your task is to write clean, efficient, and well-documented code based on the user's request.
        Provide only the code block for the requested language, followed by a brief explanation of how it works."""
        
        user_prompt = f"Generate code for the following task: {task_prompt}"
        return call_openai(system_prompt, user_prompt)


class EuropeanHistoryQAAgent:
    """Agent that answers questions about European history."""
    def __init__(self):
        self.description = "European History Q&A Agent: Use this agent to get answers to specific questions about European history, from ancient times to the modern era."
        self.name = "European History Q&A Agent"

    def get_description(self):
        """Returns the agent's description."""
        return self.description

    def run(self, task_prompt):
        """Executes the history question-answering task."""
        system_prompt = """You are a specialist European History Agent. Your task is to provide accurate and detailed answers to questions about European history.
        Cite key dates, figures, and events in your response."""
        
        user_prompt = f"Answer the following European history question: {task_prompt}"
        return call_openai(system_prompt, user_prompt)


class MathematicalProblemSolvingAgent:
    """Agent that solves mathematical problems."""
    def __init__(self):
        self.description = "Mathematical Problem Solving Agent: Use this agent to solve mathematical problems, including algebra, calculus, and other quantitative tasks."
        self.name = "Mathematical Problem Solving Agent"

    def get_description(self):
        """Returns the agent's description."""
        return self.description

    def run(self, task_prompt):
        """Executes the mathematical problem-solving task."""
        system_prompt = """You are a specialist Mathematical Problem Solving Agent. Your task is to solve the given mathematical problem, showing the steps involved for clarity.
    Provide the final answer clearly."""
        
        user_prompt = f"Solve the following mathematical problem: {task_prompt}"
        return call_openai(system_prompt, user_prompt)


# --- Routing Agent with Dynamic Prompt Generation ---
def routing_agent(task_prompt, agents):
    """
    Routing agent that uses an LLM to determine which agent to use based on the task prompt.
    
    Args:
        task_prompt (str): The user's request.
        agents (list): A list of agent objects to choose from.
    """
    
    # Dynamically create the list of available agents from their descriptions
    agent_descriptions = "\n".join([f"- {agent.get_description()}" for agent in agents])
    
    system_prompt = f"""You are an expert AI routing assistant. Your job is to analyze a user's task prompt and route it to the most appropriate agent.
    You have the following agents available:
    {agent_descriptions}

    Analyze the user's task prompt below and determine which agent is the best fit.
    Respond only with the exact name of the agent (e.g., 'Code Generation Agent'), and nothing else.

    Task: {task_prompt}"""
    
    user_prompt = f"Given the task: '{task_prompt}', which agent should handle this task?"
    
    # Use an LLM to choose the agent
    agent_choice_name = call_openai(system_prompt, user_prompt).strip()
    
    # Find the chosen agent object and run it
    for agent in agents:
        if agent.name == agent_choice_name:
            print(f"--- Routing task to {agent.name}... ---")
            return agent.run(task_prompt)
            
    return f"Error: Could not find an agent named '{agent_choice_name}'. Please check the routing prompt."


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Initialize all available agents
    code_agent = CodeGenerationAgent()
    history_agent = EuropeanHistoryQAAgent()
    math_agent = MathematicalProblemSolvingAgent()
    
    all_agents = [code_agent, history_agent, math_agent]

    # --- Example 1: Code Generation Task ---
    task1_prompt = "Write a Python function that implements a recursive binary search algorithm."
    print(f"User Task: \"{task1_prompt}\"")
    result1 = routing_agent(task1_prompt, all_agents)
    print("\nAgent Output:\n", result1)
    print("\n" + "="*50 + "\n")

    # --- Example 2: European History Task ---
    task2_prompt = "What were the main causes of the French Revolution?"
    print(f"User Task: \"{task2_prompt}\"")
    result2 = routing_agent(task2_prompt, all_agents)
    print("\nAgent Output:\n", result2)
    print("\n" + "="*50 + "\n")

    # --- Example 3: Mathematical Task ---
    task3_prompt = "Calculate the derivative of f(x) = 5x^4 + 3x^2 - 2x + 7."
    print(f"User Task: \"{task3_prompt}\"")
    result3 = routing_agent(task3_prompt, all_agents)
    print("\nAgent Output:\n", result3)