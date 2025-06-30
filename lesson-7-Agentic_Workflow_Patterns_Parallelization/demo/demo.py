import os
from openai import OpenAI
from dotenv import load_dotenv

import threading

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# Shared dict for thread-safe collection
agent_outputs = {}

# The shared user prompt
user_prompt = "What are current trends shaping the future of the energy industry?"
print(f"Using parallel agents to answer prompt: {user_prompt}")

# Agent classes using the new OpenAI v1+ SDK
class PolicyAgent:
    def run(self, prompt):
        print(f"Policy Agent resolving prompt: {prompt}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a policy expert in global energy policy and climate regulations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        agent_outputs["policy"] = response.choices[0].message.content

class TechnologyAgent:
    def run(self, prompt):
        print(f"Technology Agent resolving prompt: {prompt}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in renewable energy, smart grids, and energy storage technologies."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        agent_outputs["tech"] = response.choices[0].message.content

class MarketAgent:
    def run(self, prompt):
        print(f"Market Agent resolving prompt: {prompt}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an energy market analyst focused on global investment, pricing, and demand trends."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        agent_outputs["market"] = response.choices[0].message.content

class SummaryAgent:
    def run(self, prompt, inputs):
        combined_prompt = (
            f"The user asked: '{prompt}'\n\n"
            f"Here are the expert responses:\n"
            f"- Policy Expert: {inputs['policy']}\n\n"
            f"- Technology Expert: {inputs['tech']}\n\n"
            f"- Market Expert: {inputs['market']}\n\n"
            "Please summarize the combined insights into a single clear and concise response."
        )
        print(f"Summary Agent resolving prompt: {combined_prompt}")

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an energy strategist skilled at synthesizing expert insights."},
                {"role": "user", "content": combined_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

# Run the agents
def main():
    policy_agent = PolicyAgent()
    tech_agent = TechnologyAgent()
    market_agent = MarketAgent()
    summary_agent = SummaryAgent()

    threads = [
        threading.Thread(target=policy_agent.run, args=(user_prompt,)),
        threading.Thread(target=tech_agent.run, args=(user_prompt,)),
        threading.Thread(target=market_agent.run, args=(user_prompt,))
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    final_summary = summary_agent.run(user_prompt, agent_outputs)

    print("\n=== FINAL SUMMARY ===\n")
    print(final_summary)

if __name__ == "__main__":
    main()
