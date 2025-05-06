"""
Program Management Knowledge Agent - Starter Code

This program demonstrates two approaches to answering program management questions:
1. Using hardcoded knowledge
2. Using an LLM API

Complete the TODOs to build your knowledge agent.
"""

from openai import OpenAI
import os

# TODO: Initialize the OpenAI client if API key is available
# Hint: Use os.getenv() to get the API key from environment variables

def get_hardcoded_answer(question):
    """
    Return answers to program management questions using hardcoded knowledge.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer to the question
    """
    # TODO: Convert question to lowercase for easier matching
    
    # TODO: Implement responses for at least 5 common program management questions
    # Include questions about: Gantt charts, Agile, sprints, critical path, and milestones
    
    # TODO: Add a default response for questions not in your knowledge base
    pass

def get_llm_answer(question):
    """
    Get answers to program management questions using an LLM API.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer from the LLM
    """
    # TODO: Check if the LLM client is initialized
    
    # TODO: Implement the API call to get an answer from the LLM
    # Use a system message to specify that the LLM should act as a program management expert
    
    # TODO: Add error handling for API calls
    pass

# Demo function to compare both approaches
def compare_answers(question):
    """Compare answers from both approaches for a given question."""
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    # TODO: Get and display the hardcoded answer
    
    # TODO: Get and display the LLM answer (or a placeholder message)
    
    print("=" * 50)

# Demo with sample questions
if __name__ == "__main__":
    print("PROGRAM MANAGEMENT KNOWLEDGE AGENT DEMO")
    print("=" * 50)
    
    # TODO: Create a list of sample program management questions
    
    # TODO: Loop through the questions and compare answers