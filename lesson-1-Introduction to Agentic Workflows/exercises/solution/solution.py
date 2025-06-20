"""
Program Management Knowledge Agent - Solution

This program demonstrates two approaches to answering program management questions:
1. Using hardcoded knowledge
2. Using an LLM API
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

# Initialize the OpenAI client if key is available
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=openai_api_key)

def get_hardcoded_answer(question):
    """
    Return answers to program management questions using hardcoded knowledge.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer to the question
    """
    question = question.lower()
    
    # Knowledge base of program management Q&A
    if "what is a gantt chart" in question:
        return "A Gantt chart is a bar chart that shows the schedule of a project. It displays project tasks against time, showing start and finish dates, dependencies, and progress."
    
    elif "what is agile" in question:
        return "Agile is an iterative approach to project management and software development that helps teams deliver value to their customers faster. Instead of betting everything on a 'big bang' launch, an agile team delivers work in small, but consumable, increments."
    
    elif "what is a sprint" in question:
        return "A sprint is a short, time-boxed period when a team works to complete a set amount of work. Sprints are typically 1-4 weeks long and are a key component of Agile methodologies like Scrum."
    
    elif "what is the critical path" in question:
        return "The critical path is the longest sequence of tasks that must be completed on time for a project to meet its deadline. It determines the shortest possible project duration."
    
    elif "what is a milestone" in question:
        return "A milestone is a significant point or event in a project. It typically marks the completion of a major deliverable or phase of work."
    
    else:
        return "I don't have a hardcoded answer for that question about program management. Try asking the LLM instead."

def get_llm_answer(question):
    """
    Get answers to program management questions using an LLM API.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer from the LLM
    """
    if not client:
        return "LLM client not initialized. Please set your API key."
    
    try:
        # Create a more specific prompt to focus on program management
        prompt = f"Please answer this question about program management: {question}"
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a program management expert. Provide concise, accurate answers to questions about program management concepts, methodologies, and best practices."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error getting answer from LLM: {str(e)}"

# Demo function to compare both approaches
def compare_answers(question):
    """Compare answers from both approaches for a given question."""
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    hardcoded = get_hardcoded_answer(question)
    print(f"Hardcoded Answer:\n{hardcoded}")
    print("-" * 50)
    
    print("LLM Answer:")
    # Uncomment the line below to enable actual LLM API calls
    llm_answer = get_llm_answer(question)
    print(llm_answer)
    
    print("=" * 50)

# Demo with sample questions
if __name__ == "__main__":
    print("PROGRAM MANAGEMENT KNOWLEDGE AGENT DEMO")
    print("=" * 50)
    
    sample_questions = [
        "What is a Gantt chart?",
        "What is Agile?",
        "What is the difference between a program and a project?",
        "What is a sprint?",
        "What is the critical path?"
    ]
    
    for question in sample_questions:
        compare_answers(question)