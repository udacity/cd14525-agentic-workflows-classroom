import os
import re
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

# === Setup ===
# This setup assumes you have a .env file with your OPENAI_API_KEY
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# === Utility Functions ===

def llm_call(prompt: str, model: str = "gpt-4") -> str:
    """Basic LLM call wrapper."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def extract_xml(text: str, tag: str) -> str:
    """Extract content between XML-style tags."""
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def parse_tasks(xml: str) -> List[Dict]:
    """Parses <task> XML blocks into dictionaries."""
    tasks = []
    current_task = {}

    for line in xml.splitlines():
        line = line.strip()
        if line.startswith("<task>"):
            current_task = {}
        elif line.startswith("<type>"):
            current_task["type"] = line[6:-7].strip()
        elif line.startswith("<description>"):
            current_task["description"] = line[12:-13].strip()
        elif line.startswith("</task>"):
            if "description" in current_task:
                if "type" not in current_task:
                    current_task["type"] = "default"
                tasks.append(current_task)
    return tasks

# === Worker Agent Base Class ===

class WorkerAgent:
    """Abstract base class for all specialized worker agents."""
    def __init__(self, task_type: str):
        self.task_type = task_type

    def run(self, original_task: str, task_description: str) -> str:
        """This method should be implemented by each specific worker agent."""
        raise NotImplementedError("The 'run' method must be implemented in a subclass.")

# === Worker Agent Implementations ===

class HematologyAgent(WorkerAgent):
    """Worker that analyzes blood cell counts (Complete Blood Count)."""
    def run(self, original_task: str, task_description: str) -> str:
        prompt = f"""
You are a hematology analysis expert. Your task is to interpret the blood count section of a lab report.

Main Task: {original_task}
Your Subtask: {task_description}

<response>
- Explain the purpose of analyzing these blood values.
- Identify any out-of-range values (e.g., high/low RBC, WBC, Platelets).
- Briefly note the potential clinical significance of any abnormalities.
</response>
"""
        raw_output = llm_call(prompt)
        return extract_xml(raw_output, "response")

class RenalFunctionAgent(WorkerAgent):
    """Worker that analyzes kidney function markers."""
    def run(self, original_task: str, task_description: str) -> str:
        prompt = f"""
You are a renal function analysis expert. Your task is to interpret the kidney-related markers from a lab report.

Main Task: {original_task}
Your Subtask: {task_description}

<response>
- Explain the purpose of analyzing these kidney markers.
- Identify any out-of-range values (e.g., Creatinine, BUN, GFR).
- Briefly note the potential clinical significance of any abnormalities.
</response>
"""
        raw_output = llm_call(prompt)
        return extract_xml(raw_output, "response")

class LiverFunctionAgent(WorkerAgent):
    """Worker that analyzes liver enzyme markers."""
    def run(self, original_task: str, task_description: str) -> str:
        prompt = f"""
You are a liver function analysis expert. Your task is to interpret the liver enzyme section of a lab report.

Main Task: {original_task}
Your Subtask: {task_description}

<response>
- Explain the purpose of analyzing these liver enzymes.
- Identify any out-of-range values (e.g., ALT, AST, ALP).
- Briefly note the potential clinical significance of any abnormalities.
</response>
"""
        raw_output = llm_call(prompt)
        return extract_xml(raw_output, "response")

# === Orchestrator ===

class Orchestrator:
    def __init__(self, orchestrator_prompt: str):
        self.orchestrator_prompt = orchestrator_prompt

    def get_worker(self, task_type: str) -> WorkerAgent:
        """Inspects the task type and returns the correct specialized agent."""
        type_lower = task_type.lower()
        if "hematology" in type_lower or "blood count" in type_lower:
            return HematologyAgent(task_type)
        elif "renal" in type_lower or "kidney" in type_lower:
            return RenalFunctionAgent(task_type)
        elif "liver" in type_lower:
            return LiverFunctionAgent(task_type)
        else:
            # This would be a good place for a GenericAgent if needed,
            # but for this specific workflow, we expect specialized tasks.
            raise ValueError(f"No worker agent configured for task type: {task_type}")

    def process(self, task: str) -> Dict:
        """Runs the full Orchestrator-Workers workflow."""
        # Step 1: Decompose task using orchestrator LLM
        orchestrator_input = self.orchestrator_prompt.format(task=task)
        response = llm_call(orchestrator_input)
        print("\n[Raw Orchestrator Output]\n", response)

        analysis = extract_xml(response, "analysis")
        tasks_xml = extract_xml(response, "tasks")
        tasks = parse_tasks(tasks_xml)

        print("\n=== ORCHESTRATOR ANALYSIS & PLAN ===")
        print("Analysis:", analysis)
        print("Parsed Tasks:", tasks)

        # Step 2: Dispatch tasks to worker agents
        results = []
        for task_info in tasks:
            try:
                agent = self.get_worker(task_info["type"])
                result = agent.run(task, task_info["description"])
                print(f"\n=== {task_info['type'].upper()} RESULT ===\n{result}")
                results.append({
                    "type": task_info["type"],
                    "description": task_info["description"],
                    "result": result
                })
            except ValueError as e:
                print(f"\n--- ERROR --- \n{e}")

        return {"analysis": analysis, "worker_results": results}

# === Prompt Template for Orchestrator ===

orchestrator_prompt = """
You are a clinical lab data analyst. Your job is to analyze a set of patient lab results and create a plan to interpret them systematically.

The plan must be broken down into subtasks, one for each major panel in the lab report.

Return your response in the following format, with an <analysis> section and a <tasks> section.

<analysis>
Provide a high-level summary of the lab panels present and the overall goal of the interpretation.
</analysis>

<tasks>
Provide one <task> entry for each major lab panel found in the data. Each task must have a <type> and a <description>.
Example task format:
<task>
  <type>hematology</type>
  <description>Analyze the Complete Blood Count (CBC) panel, including RBC, WBC, and platelets.</description>
</task>
</tasks>

Here is the high-level task and data:
Task: {task}
"""

# === Main Runner ===

if __name__ == "__main__":
    lab_results_data = """
    Patient Lab Report:
    - Panel: Complete Blood Count (CBC)
      - White Blood Cell (WBC): 11.5 x10^9/L (Normal: 4.5-11.0)
      - Red Blood Cell (RBC): 4.6 x10^12/L (Normal: 4.2-5.4)
      - Platelets: 140 x10^9/L (Normal: 150-450)
    - Panel: Renal Function Panel
      - Creatinine: 1.4 mg/dL (Normal: 0.6-1.2)
      - BUN: 25 mg/dL (Normal: 7-20)
    - Panel: Liver Function Panel
      - ALT: 55 U/L (Normal: 7-56)
      - AST: 60 U/L (Normal: 10-40)
    """
    
    user_prompt = f"Please interpret the following lab results and provide a summary: {lab_results_data}"

    orchestrator = Orchestrator(orchestrator_prompt)
    final_report = orchestrator.process(user_prompt)

    print("\n\n=== FINAL INTERPRETATION REPORT ===")
    print("Overall Analysis:\n", final_report.get("analysis", "N/A"))
    for r in final_report.get("worker_results", []):
        print(f"\n--- {r['type'].upper()} PANEL ---")
        print("Task Description:", r["description"])
        print("Interpretation:\n", r["result"])

