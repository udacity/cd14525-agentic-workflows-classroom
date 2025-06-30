import os
import time
from typing import Any, List, Dict

class Agent:
    """Simple agent that can perform a specific task"""
    
    def __init__(self, name: str):
        self.name = name
    
    def run(self, input_data: Any) -> Any:
        print(f"Agent '{self.name}' processing: {str(input_data)[:30]}...")
        return input_data


class ResearchAgent(Agent):
    """Agent that simulates researching a topic"""
    
    def run(self, query: str) -> str:
        print(f"🔍 {self.name} researching: '{query}'")
        time.sleep(0.5)
        # Simulate a case with suspicious keywords
        return f"Research results for '{query}': This topic is debated and contains uncertain claims."


class SummarizerAgent(Agent):
    """Agent that summarizes information"""
    
    def run(self, text: str) -> str:
        print(f"📝 {self.name} summarizing text...")
        time.sleep(0.5)
        return f"Summary: {text.split(':', 1)[1][:30]}..."


class FactCheckerAgent(Agent):
    """Agent that verifies information and flags suspicious content"""
    
    suspicious_keywords = ["error", "uncertain", "debated"]
    
    def run(self, text: str) -> Dict:
        print(f"✓ {self.name} fact checking...")
        time.sleep(0.5)
        # Identify suspicious keywords in the text
        flags = [kw for kw in self.suspicious_keywords if kw in text.lower()]
        return {
            "text": text,
            "accuracy": "high",
            "verified_claims": 3,
            "flags": flags
        }

print("=== AGENTIC WORKFLOW DEMO ===")
    
# Create agents
researcher = ResearchAgent("Research Assistant")
fact_checker = FactCheckerAgent("Fact Checker")
summarizer = SummarizerAgent("Summarizer")

print("\n🚀 Starting 'Information Processing' workflow\n")

# Initial input
query = "Agentic workflows in AI systems"

# Step 1: Research
research_results = researcher.run(query)
print(f"  → Output: {str(research_results)[:50]}...\n")

# Step 2: Fact check
fact_check_results = fact_checker.run(research_results)
print(f"  → Output: {str(fact_check_results)[:50]}...")

# Show keyword flags if any
if fact_check_results["flags"]:
    print(f"  ⚠️  Flags found: {fact_check_results['flags']}\n")
else:
    print("  ✅ No suspicious content detected\n")

# Step 3: Summarize
summary = summarizer.run(fact_check_results["text"])
print(f"  → Output: {str(summary)[:50]}...\n")

print("✅ Workflow 'Information Processing' completed\n")

print("Final result:")
print(summary)

print("\nKey concepts demonstrated:")
print("1. Agents as components that perform specific tasks")
print("2. Workflow connecting agents in sequence")
print("3. Information flowing through the system")
print("4. Each agent transforming the data")
print("5. Customizing agents to add meaningful logic (e.g., keyword flagging)")
