import random
import time

class Task:
    def __init__(self, name, complexity, priority):
        self.name = name
        self.complexity = complexity  # 1-10
        self.priority = priority      # 1-10
        self.completed = False
    
    def __str__(self):
        return f"Task: {self.name} (Complexity: {self.complexity}, Priority: {self.priority})"

def deterministic_workflow(tasks):
    """A deterministic workflow that processes tasks in a fixed sequence."""
    print("\n==== DETERMINISTIC WORKFLOW ====")
    print("This workflow follows a predefined sequence of steps regardless of context.")
    
    # Steps are hardcoded and always executed in the same order
    print("\nStep 1: Sort tasks by name")
    sorted_tasks = sorted(tasks, key=lambda t: t.name)
    for task in sorted_tasks:
        print(f" - {task}")
    
    print("\nStep 2: Process all tasks with complexity < 5")
    for task in sorted_tasks:
        if task.complexity < 5:
            print(f" - Processing {task.name}...")
            time.sleep(0.5)
            task.completed = True
    
    print("\nStep 3: Process remaining tasks")
    for task in sorted_tasks:
        if not task.completed:
            print(f" - Processing {task.name}...")
            time.sleep(0.5)
            task.completed = True
    
    print("\nWorkflow completed. All tasks processed in predetermined sequence.")
    return tasks

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

def agentic_workflow(tasks):
    """An agentic workflow where agents dynamically decide what to do next."""
    print("\n==== AGENTIC WORKFLOW ====")
    print("This workflow uses agents that reason about what to do at each step.")
    
    # Create two simple agents with different specialties
    priority_agent = SimpleAgent("Priority Handler", "high_priority")
    complexity_agent = SimpleAgent("Efficiency Expert", "low_complexity")
    
    # Create a copy of tasks to work with
    remaining_tasks = tasks.copy()
    
    step = 1
    while remaining_tasks:
        print(f"\nStep {step}: Agents analyze current situation and decide what to do")
        
        # Agents assess the situation and decide what to do next
        print(f"Current task status: {len(remaining_tasks)} tasks remaining")
        
        # Agents reason about which tasks to tackle next
        priority_task, priority_reasoning = priority_agent.decide_action(remaining_tasks)
        complexity_task, complexity_reasoning = complexity_agent.decide_action(remaining_tasks)
        
        print(f"Priority Agent reasoning: {priority_reasoning}")
        print(f"Efficiency Agent reasoning: {complexity_reasoning}")
        
        # Determine which agent's approach is better for the current situation
        if len(remaining_tasks) > 3:
            print("System decision: Many tasks remaining, focusing on efficiency")
            active_agent = complexity_agent
            chosen_task = complexity_task
        else:
            print("System decision: Few tasks remaining, focusing on priority")
            active_agent = priority_agent
            chosen_task = priority_task
        
        # Execute the chosen action
        result = active_agent.process_task(chosen_task)
        print(f"Result: {result}")
        
        # Update remaining tasks
        remaining_tasks = [t for t in remaining_tasks if not t.completed]
        
        step += 1
    
    print("\nWorkflow completed. All tasks processed through dynamic decision-making.")
    return tasks


def main():
    # Create some sample tasks
    tasks = [
        Task("Data cleaning", 3, 4),
        Task("Machine learning model training", 8, 7),
        Task("Report generation", 4, 9),
        Task("Database backup", 2, 10),
        Task("Code review", 5, 6)
    ]
    
    # Make copies for each workflow
    deterministic_tasks = [Task(t.name, t.complexity, t.priority) for t in tasks]
    agentic_tasks = [Task(t.name, t.complexity, t.priority) for t in tasks]
    
    # Run both workflows
    deterministic_workflow(deterministic_tasks)
    agentic_workflow(agentic_tasks)
    
    print("\n==== COMPARISON ====")
    print("Deterministic workflow: Followed fixed steps regardless of task attributes")
    print("Agentic workflow: Dynamically reasoned about each step based on remaining tasks")

if __name__ == "__main__":
    main()