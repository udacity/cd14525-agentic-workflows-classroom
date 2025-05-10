import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


# --- Agents for Different Tasks ---

def researcher_agent(topic):
    """Research agent gathers information."""
    system_prompt = """You are a research agent. Your task is to provide structured research on the given topic.
    Provide details such as an overview, key points, and any other relevant details."""
    
    user_prompt = f"Research this topic thoroughly: {topic}"
    return call_openai(system_prompt, user_prompt)


def writer_agent(topic, research_results):
    """Writer agent creates content based on research."""
    system_prompt = """You are a content writer. Your task is to create an article using the provided research.
    Structure your content with a clear introduction, body, and conclusion."""
    
    user_prompt = f"Write an engaging article about {topic} using this research: {research_results}"
    return call_openai(system_prompt, user_prompt)


def analyzer_agent(data):
    """Analyzer agent processes data and provides insights."""
    system_prompt = """You are an analyst. Your task is to provide insights from the given data.
    Focus on identifying trends, anomalies, and key takeaways."""
    
    user_prompt = f"Analyze the following data and provide insights: {data}"
    return call_openai(system_prompt, user_prompt)


# --- Routing Agent with LLM-Based Task Determination ---
def routing_agent(task_prompt, *args):
    """Routing agent that uses an LLM to determine which agent to use based on the task prompt."""
    
    # Use LLM to analyze the prompt and determine the correct task type
    system_prompt = """You are an AI assistant that can route tasks to the right agents. 
    You will be given a task prompt, and your job is to determine the appropriate agent to handle it.
    Agents available:
    - Researcher Agent: Researches a topic and provides structured information.
    - Writer Agent: Creates articles or content from research.
    - Analyzer Agent: Analyzes data and provides insights.
    
    Task: {task_prompt}
    
    Determine the task type and which agent should handle it. Respond only with the agent's name, nothing else."""
    
    user_prompt = f"Given the task: '{task_prompt}', which agent should handle this task?"
    
    agent_choice = call_openai(system_prompt, user_prompt)
    
    # Route the task to the correct agent based on the choice
    if "Researcher Agent" in agent_choice:
        print("Routing task to Researcher Agent...")
        return researcher_agent(task_prompt)  # Pass topic as argument
    
    elif "Writer Agent" in agent_choice:
        print("Routing task to Writer Agent...")
        # Assuming research_results is needed, but the research has already been done
        research_results = args[0]  # Retrieve research results passed from previous step
        return writer_agent(task_prompt, research_results)
    
    elif "Analyzer Agent" in agent_choice:
        print("Routing task to Analyzer Agent...")
        data = args[0]  # Assuming data is passed from previous step
        return analyzer_agent(data)
    
    else:
        raise ValueError(f"Unknown agent decision: {agent_choice}")


# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Research Task
    task_prompt = "Research the impact of artificial intelligence on the healthcare industry."
    research_results = routing_agent(task_prompt)  # Pass topic to routing agent
    print("\nResearch Results:\n", research_results)

    # Example 2: Writing Task
    task_prompt = "Write an article on the future of AI in healthcare."
    article_content = routing_agent(task_prompt, research_results)  # Pass research results to routing agent
    print("\nArticle Content:\n", article_content)

    # Example 3: Analysis Task
    task_prompt = "Analyze the trends in AI adoption in healthcare."
    data = "AI adoption data in healthcare, including usage statistics, trends, and outcomes."
    analysis_results = routing_agent(task_prompt, data)  # Pass data to routing agent
    print("\nAnalysis Results:\n", analysis_results)
