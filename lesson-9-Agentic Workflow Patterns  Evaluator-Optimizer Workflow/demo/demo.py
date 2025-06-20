import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

MAX_RETRIES = 5
user_prompt = (
    "Write a summary for potential investors explaining why decentralized finance (DeFi) will outperform "
    "traditional banking in the next five years. Use strong language to inspire confidence and urgency. "
    "Include examples of past DeFi gains and suggest what investors can expect from leading protocols in the near future."
)

class FinancialReportAgent:
    def run(self, prompt, feedback=None):
        system_message = "You are a financial analyst writing a professional investment summary."

        # Modify the prompt if feedback is provided
        full_prompt = prompt
        if feedback:
            full_prompt += f"\n\nEvaluator feedback: {feedback}\nPlease revise accordingly."

        print(f"\n📊 Generating report with prompt:\n{full_prompt}\n")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content

class ComplianceAgent:
    def run(self, report_text):
        print("🔍 Evaluating report compliance...")
        system_message = (
            "You are a compliance officer reviewing investment summaries. "
            "Reject anything with forward-looking statements, speculative claims, or language like 'expected', 'projected', 'will likely', etc."
        )

        eval_prompt = f"Evaluate this investment summary for compliance:\n\n{report_text}\n\nRespond with 'Approved' or provide feedback for revision."

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": eval_prompt}
            ],
            temperature=0.0
        )
        return response.choices[0].message.content.strip()

def main():
    report_agent = FinancialReportAgent()
    eval_agent = ComplianceAgent()

    report_text = ""
    feedback = None

    for attempt in range(MAX_RETRIES):
        print(f"--- Attempt #{attempt} ---")
        report_text = report_agent.run(user_prompt, feedback)
        evaluation = eval_agent.run(report_text)

        print(f"\n🧾 Evaluation Result:\n{evaluation}\n")

        if evaluation.lower().startswith("approved"):
            print("\n✅ Final Approved Investment Summary:\n")
            print(report_text)
            break
        else:
            feedback = evaluation
    else:
        print("\n❌ Failed to meet compliance after max retries.")
        print("Last version of the report:")
        print(report_text)

if __name__ == "__main__":
    main()
