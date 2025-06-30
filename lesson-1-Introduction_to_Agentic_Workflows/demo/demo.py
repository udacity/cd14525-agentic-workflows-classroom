"""
Python Demo: Functions vs OpenAI Agents
This demo shows the parallels between traditional Python functions and OpenAI-powered agents.
Both follow similar patterns: they take inputs, process them, and return outputs.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client if key is available
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=openai_api_key)

def traditional_generate_response(query):
    """
    A traditional function that returns predefined responses based on keywords.
    """
    query_lower = query.lower()
    if "weather" in query_lower:
        return "The weather today is sunny with a high of 75°F."
    elif "time" in query_lower:
        return "The current time is 12:00 PM."
    elif "hello" in query_lower or "hi" in query_lower:
        return "Hello! How can I help you today?"
    else:
        return "I'm not sure how to respond to that query."

def openai_generate_response(query):
    """
    Uses the OpenAI API to generate a response to the user's query.
    """
    if not client:
        return "OpenAI client not initialized. Please set your API key."

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Sample queries
queries = [
    "Hello there!",
    "What's the weather like?",
    "Tell me a short joke."
]

print("=" * 50)
print("DEMO: TRADITIONAL FUNCTION VS OPENAI AGENT")
print("=" * 50)

for query in queries:
    print(f"\nQuery: {query}")
    print("-" * 30)
    
    traditional_response = traditional_generate_response(query)
    print(f"Traditional Function Response:\n{traditional_response}")
    print("-" * 30)
    
    print("OpenAI Agent would process this query similarly:")
    print("1. Take the query as input")
    print("2. Process it (send to OpenAI API)")
    print("3. Return a response")

    # Uncomment below to enable OpenAI API call (make sure your key is valid)
    ai_response = openai_generate_response(query)
    print(f"OpenAI Agent Response:\n{ai_response}")
    
    print("=" * 50)