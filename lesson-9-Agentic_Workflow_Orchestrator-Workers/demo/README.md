# Task Decomposition or Action Planning Agent Demo

This document explains how a **Task Decomposition Agent** can be used to break down a complex task into smaller, manageable steps, using the example of handling a flat tire. The workflow involves two agents:

1. **Researcher Agent**: Gathers the necessary knowledge or information required for the task.
2. **Task Decomposition Agent**: Breaks down the gathered knowledge into actionable, sequential steps.

## Overview of Task Decomposition Agents

A **Task Decomposition Agent** is an AI-driven agent responsible for analyzing and breaking down a task into specific actions or steps needed to accomplish it. The agent takes input in the form of task descriptions, processes the information, and decomposes it into smaller sub-tasks.

In this demonstration, we are building a system where:

- A **Researcher Agent** gathers knowledge about how to handle a flat tire.
- A **Task Decomposition Agent** uses this research to break down the process into clear, actionable steps.

## Code Walkthrough

The Python code demonstrates how these agents work together. Here is a breakdown of the key components:

### 1. **Setting Up the Environment**

We use the `OpenAI` API to interact with the GPT-3 model for both research and task decomposition. The environment variables (like the OpenAI API key) are loaded from a `.env` file.

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

### 2. The Researcher Agent
The Researcher Agent is responsible for gathering knowledge related to the given task. In this case, it will research how to change a flat tire. The system prompt is designed to guide the agent to look for structured and detailed information about the task.

def researcher_agent(topic):
    """Researches the steps required for a given task"""
    system_prompt = """You are a knowledgeable research agent. Your task is to find the necessary steps to complete a given task.
    Provide the steps in a detailed, structured manner.
    """
    
    user_prompt = f"Research the steps required to complete the task: {topic}"
    
    return call_openai(system_prompt, user_prompt)
The Researcher Agent sends a prompt to the OpenAI API to fetch detailed steps required to complete the task and returns the research results.

### 3. The Task Decomposition Agent
Once the Researcher Agent provides the gathered research, the Task Decomposition Agent is responsible for breaking down the research into clear, actionable tasks.

def task_decomposition_agent(research_results):
    """Decomposes the task into actionable steps based on the research provided"""
    system_prompt = """You are a task decomposition agent. Your job is to break down a research result into a list of actionable tasks.
    The research contains a general guide, and your job is to create a sequence of steps.
    """
    
    user_prompt = f"Given the following research, break it down into actionable steps:\n\n{research_results}\n\nProvide the steps in a numbered list."
    
    return call_openai(system_prompt, user_prompt)
Here, the Task Decomposition Agent processes the research from the Researcher Agent and breaks it down into clear tasks.

### 4. Combining the Agents
The main function that combines both agents (run_task_decomposition_with_research) is responsible for orchestrating the workflow:

The Researcher Agent first gathers the research.

The Task Decomposition Agent then breaks down the gathered research into actionable steps.

def run_task_decomposition_with_research(topic):
    # Step 1: Research the task
    research_results = researcher_agent(topic)
    
    # Step 2: Decompose the task based on research results
    decomposition = task_decomposition_agent(research_results)

    return decomposition

### 5. Example Usage

The example demonstrates how to use the system with a real-world task: changing a flat tire. The system first researches the steps for changing a tire and then decomposes those steps into actionable tasks:

if __name__ == "__main__":
    # Test the task decomposition with input: 'I have a flat tire, what do I do?'
    prompt = "I have a flat tire, what do I do?"
    result = run_task_decomposition_with_research(prompt)
    
    print(result)

### 6. Expected Output

For the input "I have a flat tire, what do I do?", the output might look like this:

1. Ensure the car is on a flat, stable surface.
2. Engage the parking brake to secure the vehicle.
3. Gather necessary tools: car jack, lug wrench, spare tire, and wheel chocks.
4. Place the wheel chocks behind the opposite tires for additional safety.
5. Loosen the lug nuts on the flat tire (do not remove them completely).
6. Use the car jack to lift the vehicle until the flat tire is off the ground.
7. Remove the loosened lug nuts completely and take off the flat tire.
8. Place the spare tire on the wheel hub and hand-tighten the lug nuts.
9. Lower the vehicle using the jack and remove it once the car is secure on the spare tire.
10. Tighten the lug nuts in a crisscross pattern to ensure a secure fit.
11. Check the spare tire’s air pressure to ensure it is inflated properly.
12. Store the flat tire and tools back in the trunk of the car.

**Key Concepts in Task Decomposition**
Task Decomposition Agent: This agent takes high-level information (like a general task description) and breaks it down into detailed, actionable steps. It enables complex tasks to be tackled in smaller, manageable parts.

**Research Agent:** This agent gathers the required knowledge to complete a task. It collects all the information that will be necessary for the Task Decomposition Agent to break down into steps.

**Modular and Scalable Workflow:** This agent-based pattern can be extended to other complex tasks, such as troubleshooting, cooking, or even project management. As long as the Researcher Agent provides the correct data, the Task Decomposition Agent can break it down into actionable steps.

# Conclusion
The Task Decomposition Agent pattern helps to break down complex workflows into digestible pieces, enabling better task management and execution. By using a Researcher Agent for gathering information and a Task Decomposition Agent for breaking down tasks, this pattern creates a scalable and modular approach for solving problems and completing tasks efficiently.

This method is particularly useful in scenarios where tasks involve multiple steps, and breaking them down into smaller components is essential for successful execution.