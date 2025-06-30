# Parallel Agentic Workflow Demo – Energy Industry Use Case

This demo showcases how to run multiple specialized agents **in parallel** using OpenAI's `gpt-4`, then synthesize their responses into a final summary using another agent. It demonstrates the basics of **agent orchestration** using threads and OpenAI's v1+ Python SDK.

## Use Case

Prompt:
> _"What are current trends shaping the future of the energy industry?"_

Three expert agents—**Policy**, **Technology**, and **Market**—respond independently to the prompt. Their insights are then passed to a **Summary Agent**, which synthesizes them into a final response.

---

## Components

### `PolicyAgent`
Provides insights on global energy policy, climate regulations, and geopolitical shifts.

### `TechnologyAgent`
Covers advances in renewables, smart grids, hydrogen, energy storage, and related tech.

### `MarketAgent`
Focuses on trends in pricing, demand, supply chains, and global investments in energy.

### `SummaryAgent`
Reads the responses from all three agents and combines them into a concise, coherent summary.

---

## How It Works

1. The script loads the OpenAI API key from `.env`.
2. Each agent runs **in parallel using `threading.Thread`**.
3. After all agents finish, their results are passed to the `SummaryAgent`.
4. The final synthesized answer is printed.

---

## Concepts Demonstrated
Agent-based design

Threading for parallel execution

Prompt engineering by role

API usage with OpenAI v1 SDK

Summarization from multiple sources

## Code Explanation
The demo consists of a single script: agentic_parallel_demo.py. Here's how the key parts work:

### 1. Environment Setup

from dotenv import load_dotenv
load_dotenv()
Loads your OpenAI API key from a .env file so it can be used securely within the script.

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
Initializes the OpenAI client using the v1+ SDK.

### 2. Shared Prompt and Data Structure

user_prompt = "What are current trends shaping the future of the energy industry?"
agent_outputs = {}
Defines the prompt all agents will use and a shared dictionary where agents will write their outputs. This dictionary is accessible across threads.

### 3. Agent Classes

Each agent class has a .run(prompt) method that:

Sets up a system role to guide the agent's behavior

Sends the user prompt to OpenAI using client.chat.completions.create

Stores the result in agent_outputs using a key specific to the agent

Example (TechnologyAgent):

messages=[
  {"role": "system", "content": "You are an expert in renewable energy..."},
  {"role": "user", "content": prompt}
]
This helps tailor each agent’s perspective.

### 4. Parallel Execution with Threads


threads = [
    threading.Thread(target=policy_agent.run, args=(user_prompt,)),
    threading.Thread(target=tech_agent.run, args=(user_prompt,)),
    threading.Thread(target=market_agent.run, args=(user_prompt,))
]
Each agent runs on its own thread, allowing responses to be generated in parallel (faster overall execution).


for t in threads:
    t.start()
for t in threads:
    t.join()
This pattern starts all threads and waits until all finish before moving on.

### 5. Summary Agent
After all three expert agents have responded:


summary_agent.run(user_prompt, agent_outputs)
This method takes the prompt and the three responses, formats them into a new combined prompt, and sends it to OpenAI to generate a high-level summary.

The result is a synthesized response that reflects the inputs from all three perspectives.

### 6. Main Function
python
Copy
Edit
if __name__ == "__main__":
    main()
The main() function ties it all together—initializing agents, launching threads, gathering outputs, and printing the final summary.

