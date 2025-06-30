# Prompt Chaining Agent Pattern Demo

This file demonstrates a **prompt chaining pattern** using simple autonomous agents built on top of OpenAI’s chat completion API. It implements a two-agent pipeline where one agent researches a topic and another agent turns the research into a readable article.

This is a minimalist example of **agent collaboration via prompt chaining**, where the output of one LLM call serves as input to the next agent’s prompt.

---

## What’s Implemented

### Agent Pattern: Researcher → Writer

- **Researcher Agent**  
  Gathers structured information about a given topic using predefined headers.
  
- **Writer Agent**  
  Converts the research results into a full article with an introduction, body, and conclusion.

Together, these agents form a **sequential agent chain**, where each agent performs a distinct role with a clear prompt and no shared memory.

---

## Code Overview

### 1. Environment and Client Setup

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

Uses the dotenv library to securely load the API key from a .env file.

Initializes the OpenAI client for use in agent calls.

### 2. OpenAI Call Wrapper

def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content

A reusable function that sends a prompt to the OpenAI API.
Enforces a deterministic output by setting temperature=0.

### 3. Researcher Agent

def researcher_agent(topic):
    system_prompt = """You are a research specialist who provides structured information.
    Always format your response with these exact headings:
    # OVERVIEW
    # KEY POINTS
    # DETAILS
    """
    
    user_prompt = f"Research this topic thoroughly: {topic}"
    
    print(f"Researcher agent working on: {topic}")
    return call_openai(system_prompt, user_prompt)
Role: Information gathering

Output format is controlled via a structured system_prompt.
User prompt asks the LLM to research a specific topic.

### 4. Writer Agent

def writer_agent(topic, research_results):
    system_prompt = """You are a content writer who creates engaging material from research.
    Create a well-structured article with a clear introduction, body, and conclusion.
    """
    
    user_prompt = f"""Write an engaging article about {topic} using this research:
    
    {research_results}
    """
    
    print(f"Writer agent creating content for: {topic}")
    return call_openai(system_prompt, user_prompt)

Role: Content generation
Uses the research as input to produce a structured article.
Focuses on flow, readability, and narrative clarity.

### 5. Agent Chain Execution

def run_simple_chain(topic):
    print(f"\nStarting simple agent chain for: '{topic}'")
    
    # Step 1: Get research from researcher agent
    research = researcher_agent(topic)
    print("\nResearch complete!")
    
    # Step 2: Pass research to writer agent
    content = writer_agent(topic, research)
    print("\nContent creation complete!")
    
    # Print results
    print("\n===== RESEARCH OUTPUT =====")
    print(research)
    
    print("\n===== FINAL CONTENT =====")
    print(content)
    
    return {"research": research, "content": content}

if __name__ == "__main__":
    topic = "What are the latest breakthroughs on implementing AI in big corporations?"
    results = run_simple_chain(topic)

This function chains the Researcher → Writer agents.
Runs the entire workflow and prints both intermediate and final outputs.

## Prompt Chaining Pattern

This demo uses a basic prompt chaining pattern:
1. One agent completes a task (e.g., research_agent)
2. Its output becomes part of the next agent’s prompt (writer_agent)
3. Agents remain stateless and interact via explicit handoffs (prompt → response → prompt)    
This is a simplified version of multi-agent patterns used in systems such as CrewAI, where agent workflows are modular, chainable, and interpretable.


### Example Output

When run with the topic:     
What are the latest breakthroughs on implementing AI in big corporations?

You will get:     
- A structured research report from the Researcher Agent
- A readable article from the Writer Agent