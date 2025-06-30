import time
import json
import os
from typing import List, Dict, Any, Tuple
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

class Task:
    def __init__(self, name, complexity, priority, deadline="normal"):
        self.name = name
        self.complexity = complexity  # 1-10
        self.priority = priority      # 1-10
        self.deadline = deadline      # "urgent", "normal", "flexible"
        self.completed = False
    
    def __str__(self):
        return f"Task: {self.name} (Complexity: {self.complexity}, Priority: {self.priority}, Deadline: {self.deadline})"

class SimpleAgent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty  # "high_priority" or "low_complexity"
    
    def decide_action(self, tasks):
        """Determines what action to take based on available tasks."""
        if not tasks:
            return None, "No tasks available"
        
        if self.specialty == "high_priority":
            # This agent focuses on high priority tasks
            best_task = max(tasks, key=lambda t: t.priority)
            return best_task, f"Selected highest priority task: {best_task.name}"
        
        elif self.specialty == "low_complexity":
            # This agent focuses on easiest tasks first
            best_task = min(tasks, key=lambda t: t.complexity)
            return best_task, f"Selected lowest complexity task: {best_task.name}"
    
    def process_task(self, task):
        """Process the selected task."""
        if task:
            print(f" - Agent {self.name} processing {task.name}...")
            time.sleep(0.5)
            task.completed = True
            return f"Completed task: {task.name}"
        return "No task to process"

class LLMAgent:
    """An agent that uses OpenAI's LLM to make strategic decisions."""
    
    def __init__(self, name):
        self.name = name
    
    def format_tasks_for_prompt(self, tasks):
        """Format the tasks into a readable string for the prompt."""
        task_details = []
        for i, task in enumerate(tasks):
            task_details.append(f"Task {i+1}: {task.name}")
            task_details.append(f"  - Priority: {task.priority}/10")
            task_details.append(f"  - Complexity: {task.complexity}/10")
            task_details.append(f"  - Deadline: {task.deadline}")
        
        return "\n".join(task_details)
    
    def decide_strategy(self, tasks):
        """Use OpenAI to decide between priority or efficiency strategy."""
        if not tasks:
            return "none", "No tasks available", "No strategy needed"
        
        # Create a prompt for the LLM
        prompt = f"""
        I have {len(tasks)} tasks to complete. I need to decide whether to prioritize tasks based on their priority level (PRIORITY strategy) or handle them based on their complexity (EFFICIENCY strategy, doing easiest tasks first).

        Here are the current tasks:
        {self.format_tasks_for_prompt(tasks)}

        As a task management expert, analyze this situation and decide whether I should use the PRIORITY strategy or the EFFICIENCY strategy.

        Your response must be in JSON format with these fields:
        {{
            "reasoning": "Your detailed analysis of the situation",
            "decision": "priority OR efficiency",
            "explanation": "A concise explanation of your recommendation"
        }}
        """
        
        try:
            # Make API call to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a workflow management expert that helps decide the best strategy for handling tasks."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,  # Lower temperature for more consistent decision-making
            )
            
            # Extract the response text
            result_text = response.choices[0].message.content
            
            try:
                # Parse the JSON response
                result = json.loads(result_text)
                return result["decision"], result["reasoning"], result["explanation"]
            except (json.JSONDecodeError, KeyError):
                # If JSON parsing fails, extract what we can from the text
                if "priority" in result_text.lower():
                    return "priority", "LLM recommended priority approach", result_text
                else:
                    return "efficiency", "LLM recommended efficiency approach", result_text
                
        except Exception as e:
            # Handle API errors gracefully
            print(f"Error calling OpenAI API: {e}")
            # Default to priority if there's an error
            return "priority", f"API error: {str(e)}", "Defaulting to priority strategy due to API error"

def deterministic_workflow(tasks):
    """A deterministic workflow with fixed rules."""
    print("\n==== DETERMINISTIC WORKFLOW ====")
    print("This workflow uses hardcoded rules to decide between priority and efficiency.")
    
    # Create agents
    priority_agent = SimpleAgent("Priority Handler", "high_priority")
    complexity_agent = SimpleAgent("Efficiency Expert", "low_complexity")
    
    # Create a copy of tasks to work with
    remaining_tasks = tasks.copy()
    
    step = 1
    while remaining_tasks:
        print(f"\nStep {step}: Applying fixed decision rules")
        
        # Display current task status
        print(f"Current task status: {len(remaining_tasks)} tasks remaining")
        for i, task in enumerate(remaining_tasks):
            print(f"  {i+1}. {task}")
        
        # Hard-coded decision logic
        urgent_tasks = sum(1 for t in remaining_tasks if t.deadline == "urgent")
        high_priority_tasks = sum(1 for t in remaining_tasks if t.priority >= 8)
        
        # Fixed rule-based decision
        if urgent_tasks > 0 or high_priority_tasks > 0:
            print("\nFixed rule: Found urgent or high-priority tasks -> Using PRIORITY strategy")
            active_agent = priority_agent
        else:
            print("\nFixed rule: No urgent or high-priority tasks -> Using EFFICIENCY strategy")
            active_agent = complexity_agent
        
        # The specialist agent selects and processes a task
        chosen_task, selection_reasoning = active_agent.decide_action(remaining_tasks)
        print(f"Agent reasoning: {selection_reasoning}")
        
        result = active_agent.process_task(chosen_task)
        print(f"Result: {result}")
        
        # Update remaining tasks
        remaining_tasks = [t for t in remaining_tasks if not t.completed]
        
        step += 1
    
    print("\nWorkflow completed. All tasks processed through deterministic rules.")
    return tasks

def llm_agentic_workflow(tasks):
    """An agentic workflow where an LLM decides the strategy."""
    print("\n==== LLM-BASED AGENTIC WORKFLOW ====")
    print("This workflow uses an OpenAI LLM to reason about strategy in natural language.")
    
    # Create agents
    strategy_agent = LLMAgent("Strategy Advisor")
    priority_agent = SimpleAgent("Priority Handler", "high_priority")
    complexity_agent = SimpleAgent("Efficiency Expert", "low_complexity")
    
    # Create a copy of tasks to work with
    remaining_tasks = tasks.copy()
    
    step = 1
    while remaining_tasks:
        print(f"\nStep {step}: LLM analyzing situation and determining strategy")
        
        # Display current task status
        print(f"Current task status: {len(remaining_tasks)} tasks remaining")
        for i, task in enumerate(remaining_tasks):
            print(f"  {i+1}. {task}")
        
        # LLM agent reasons about the strategy
        strategy, reasoning, explanation = strategy_agent.decide_strategy(remaining_tasks)
        
        print("\nLLM Reasoning:")
        print(reasoning)
        print("\nLLM Recommendation:")
        print(explanation)
        
        # Execute the strategy using the appropriate specialist agent
        if strategy == "priority":
            print("\nExecuting PRIORITY strategy:")
            active_agent = priority_agent
        else:  # efficiency
            print("\nExecuting EFFICIENCY strategy:")
            active_agent = complexity_agent
        
        # The specialist agent selects and processes a task
        chosen_task, selection_reasoning = active_agent.decide_action(remaining_tasks)
        print(f"Agent reasoning: {selection_reasoning}")
        
        result = active_agent.process_task(chosen_task)
        print(f"Result: {result}")
        
        # Update remaining tasks
        remaining_tasks = [t for t in remaining_tasks if not t.completed]
        
        step += 1
    
    print("\nWorkflow completed. All tasks processed through LLM-guided decision-making.")
    return tasks

def main():
    # Create some sample tasks with varied properties
    tasks = [
        Task("Data cleaning", 3, 4, "normal"),
        Task("Machine learning model training", 8, 7, "flexible"),
        Task("Report generation", 4, 9, "urgent"),
        Task("Database backup", 2, 10, "urgent"),
        Task("Code review", 5, 6, "normal"),
        Task("Client presentation", 6, 9, "urgent"),
        Task("Documentation update", 2, 3, "flexible")
    ]
    
    # Create copies for each workflow
    deterministic_tasks = [Task(t.name, t.complexity, t.priority, t.deadline) for t in tasks]
    llm_agentic_tasks = [Task(t.name, t.complexity, t.priority, t.deadline) for t in tasks]
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  Warning: OPENAI_API_KEY not found in .env file")
        print("Create a .env file with your OpenAI API key to make actual API calls.")
        print("Example .env file content: OPENAI_API_KEY=your-key-here\n")
    
    # Run both workflows to compare
    deterministic_workflow(deterministic_tasks)
    llm_agentic_workflow(llm_agentic_tasks)
    
    print("\n==== COMPARISON ====")
    print("Deterministic workflow:")
    print("- Used simple if/else rules with fixed thresholds")
    print("- Limited flexibility with hardcoded decision boundaries")
    print("- Cannot consider nuanced context or multiple factors simultaneously")
    print("- Logic changes require code modifications")
    print("\nLLM-based agentic workflow:")
    print("- Used natural language reasoning about the specific situation")
    print("- Considered multiple interrelated factors simultaneously")
    print("- Provided detailed reasoning and explanation for decisions")
    print("- Can adapt to new types of inputs without code changes")
    print("- Same simple code can handle increasingly complex decisions")

if __name__ == "__main__":
    main()