# Routing Agent Pattern Explanation

## Overview

The **Routing Agent Pattern** is a design pattern that leverages an intelligent agent to direct tasks to the most appropriate specialized agent for execution. This pattern is particularly useful when you have a variety of tasks that can be handled by different agents, each with specific knowledge or capabilities. The routing agent analyzes the input task prompt, determines which agent is best suited to handle the task, and delegates the execution to that agent.

In this demo, the routing agent utilizes a large language model (LLM) to determine the correct agent based on the task description. It then forwards the task to the relevant agent, allowing each agent to execute its specific function. This is an example of a flexible, modular system that can handle a range of tasks with minimal manual intervention.

### Key Components:
1. **Routing Agent**: The central agent responsible for determining which specialized agent should handle the task.
2. **Specialized Agents**: Agents that handle specific tasks, such as research, writing, or data analysis.
3. **Task Prompts**: Input prompts that describe the task to be executed. The routing agent uses these prompts to decide which agent to route the task to.
4. **Execution Flow**: The routing agent routes the task, and the appropriate agent performs the task and returns results.

## Code Walkthrough

### Helper Function: `call_openai`

The `call_openai` function is a simple wrapper that interacts with OpenAI's API to send a system prompt and user prompt, retrieve a response, and return the generated output.

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

## Agents

### 1. Researcher Agent:
This agent is responsible for gathering structured information on a given topic. It receives a topic, formulates a request to research the topic, and returns the results.

def researcher_agent(topic):
    """Research agent gathers information."""
    system_prompt = """You are a research agent. Your task is to provide structured research on the given topic.
    Provide details such as an overview, key points, and any other relevant details."""
    
    user_prompt = f"Research this topic thoroughly: {topic}"
    return call_openai(system_prompt, user_prompt)

### 2. Writer Agent:
The writer agent takes the research results and creates a well-structured article based on the information gathered. It uses the provided research to write an engaging article with a clear introduction, body, and conclusion.

def writer_agent(topic, research_results):
    """Writer agent creates content based on research."""
    system_prompt = """You are a content writer. Your task is to create an article using the provided research.
    Structure your content with a clear introduction, body, and conclusion."""
    
    user_prompt = f"Write an engaging article about {topic} using this research: {research_results}"
    return call_openai(system_prompt, user_prompt)

### 3. Analyzer Agent:
The analyzer agent processes data to extract insights, trends, and key takeaways. It is used for tasks that require data analysis, such as identifying patterns or performing statistical analysis.

def analyzer_agent(data):
    """Analyzer agent processes data and provides insights."""
    system_prompt = """You are an analyst. Your task is to provide insights from the given data.
    Focus on identifying trends, anomalies, and key takeaways."""
    
    user_prompt = f"Analyze the following data and provide insights: {data}"
    return call_openai(system_prompt, user_prompt)

##cRouting Agent
The Routing Agent is responsible for determining which specialized agent should handle a given task. It uses the task prompt to analyze the request and decide whether the task requires research, content creation, or data analysis. The routing decision is made using an LLM, which is provided with the task prompt and asked to choose the most appropriate agent.

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

## Example Usage
In the example usage, the routing agent is used to route three different types of tasks: a research task, a writing task, and a data analysis task. The routing agent selects the appropriate agent to handle each task and forwards the task to the correct agent.

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

## Benefits of the Routing Agent Pattern
**Flexibility:** The routing agent can easily be extended to route tasks to additional agents as the system grows.

**Modularity:** Tasks are delegated to specialized agents, each responsible for specific actions, leading to a more maintainable system.

**Scalability:** The system can scale with the addition of more agents or task types without affecting the routing logic.

**Efficiency:** The routing agent minimizes manual intervention by automatically determining which agent is best suited to handle a given task.