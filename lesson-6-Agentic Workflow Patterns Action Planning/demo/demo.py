import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to call OpenAI API
def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Wrapper for OpenAI API call"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# -------- AGENT 1: RESEARCHER AGENT --------

def researcher_agent(topic):
    """Researches the steps required for a given task"""
    system_prompt = """You are a knowledgeable research agent. Your task is to find the necessary steps to complete a given task.
    Provide the steps in a detailed, structured manner.
    """
    
    user_prompt = f"Research the steps required to complete the task: {topic}"
    
    print(f"Researching information for: {topic}")
    return call_openai(system_prompt, user_prompt)

# -------- AGENT 2: TASK DECOMPOSITION AGENT --------

def task_decomposition_agent(research_results):
    """Decomposes the task into actionable steps based on the research provided"""
    system_prompt = """You are a task decomposition agent. Your job is to break down a research result into a list of actionable tasks.
    The research contains a general guide, and your job is to create a sequence of steps.
    """
    
    user_prompt = f"Given the following research, break it down into actionable steps:\n\n{research_results}\n\nProvide the steps in a numbered list."
    
    print(f"Decomposing research into tasks.")
    return call_openai(system_prompt, user_prompt)

# -------- RUN DEMO --------

def run_task_decomposition_with_research(topic):
    print("\n=== USER INPUT ===")
    print(topic)

    # Step 1: Research the task
    research_results = researcher_agent(topic)
    print("\nResearch complete!\n")

    # Step 2: Decompose the task based on research results
    decomposition = task_decomposition_agent(research_results)
    print("\nTask Decomposition complete!\n")

    return decomposition

# -------- DEMO TEST --------

if __name__ == "__main__":
    # Test the task decomposition with input: 'I have a flat tire, what do I do?'
    prompt = "I have a flat tire, what do I do?"
    result = run_task_decomposition_with_research(prompt)
    
    print("\n=== TASK DECOMPOSITION RESULT ===")
    print(result)
    print("\n" + "-"*60 + "\n")

