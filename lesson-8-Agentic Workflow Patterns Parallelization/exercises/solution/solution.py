import os
from openai import OpenAI
from dotenv import load_dotenv
import threading

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# Shared dict for thread-safe collection of agent outputs
agent_outputs = {}

# Example contract text (in a real application, this would be loaded from a file)
contract_text = """
CONSULTING AGREEMENT

This Consulting Agreement (the "Agreement") is made effective as of January 1, 2025 (the "Effective Date"), by and between ABC Corporation, a Delaware corporation ("Client"), and XYZ Consulting LLC, a California limited liability company ("Consultant").

1. SERVICES. Consultant shall provide Client with the following services: strategic business consulting, market analysis, and technology implementation advice (the "Services").

2. TERM. This Agreement shall commence on the Effective Date and shall continue for a period of 12 months, unless earlier terminated.

3. COMPENSATION. Client shall pay Consultant a fee of $10,000 per month for Services rendered. Payment shall be made within 30 days of receipt of Consultant's invoice.

4. CONFIDENTIALITY. Consultant acknowledges that during the engagement, Consultant may have access to confidential information. Consultant agrees to maintain the confidentiality of all such information.

5. INTELLECTUAL PROPERTY. All materials developed by Consultant shall be the property of Client. Consultant assigns all right, title, and interest in such materials to Client.

6. TERMINATION. Either party may terminate this Agreement with 30 days' written notice. Client shall pay Consultant for Services performed through the termination date.

7. GOVERNING LAW. This Agreement shall be governed by the laws of the State of Delaware.

8. LIMITATION OF LIABILITY. Consultant's liability shall be limited to the amount of fees paid by Client under this Agreement.

9. INDEMNIFICATION. Client shall indemnify Consultant against all claims arising from use of materials provided by Client.

10. ENTIRE AGREEMENT. This Agreement constitutes the entire understanding between the parties and supersedes all prior agreements.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.
"""

class LegalTermsChecker:
    """Agent that checks for problematic legal terms and clauses in contracts."""
    def run(self, contract_text):
        print("Legal Terms Checker analyzing contract...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a legal expert specializing in contract law. Analyze the contract for potentially problematic legal terms, clauses, or language that could create legal issues or disputes. Focus on liability, rights, obligations, and ambiguous language."},
                {"role": "user", "content": f"Analyze this contract for problematic legal terms and clauses:\n\n{contract_text}"}
            ],
            temperature=0.3
        )
        agent_outputs["legal"] = response.choices[0].message.content
        print("Legal Terms Checker completed analysis.")

class ComplianceValidator:
    """Agent that validates regulatory and industry compliance of contracts."""
    def run(self, contract_text):
        print("Compliance Validator analyzing contract...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a compliance expert specializing in regulatory requirements across industries. Analyze the contract for potential compliance issues related to data privacy, labor laws, industry-specific regulations, and standard business practices."},
                {"role": "user", "content": f"Analyze this contract for regulatory and industry compliance issues:\n\n{contract_text}"}
            ],
            temperature=0.3
        )
        agent_outputs["compliance"] = response.choices[0].message.content
        print("Compliance Validator completed analysis.")

class FinancialRiskAssessor:
    """Agent that assesses financial risks and liabilities in contracts."""
    def run(self, contract_text):
        print("Financial Risk Assessor analyzing contract...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial analyst specializing in contract risk assessment. Analyze the contract for financial risks, liability exposure, payment terms issues, and potential financial implications that could negatively impact a business."},
                {"role": "user", "content": f"Analyze this contract for financial risks and liabilities:\n\n{contract_text}"}
            ],
            temperature=0.3
        )
        agent_outputs["financial"] = response.choices[0].message.content
        print("Financial Risk Assessor completed analysis.")

class SummaryAgent:
    """Agent that synthesizes findings from all specialized agents."""
    def run(self, contract_text, inputs):
        print("Summary Agent synthesizing findings...")
        combined_prompt = (
            f"Contract:\n{contract_text}\n\n"
            f"Here are the expert analyses:\n\n"
            f"LEGAL ANALYSIS:\n{inputs['legal']}\n\n"
            f"COMPLIANCE ANALYSIS:\n{inputs['compliance']}\n\n"
            f"FINANCIAL ANALYSIS:\n{inputs['financial']}\n\n"
            "Please synthesize these analyses into a comprehensive contract assessment report with the following sections:\n"
            "1. Executive Summary\n"
            "2. Key Legal Concerns\n"
            "3. Compliance Issues\n"
            "4. Financial Risks\n"
            "5. Recommended Actions\n\n"
            "The report should be concise, actionable, and highlight the most critical findings."
        )
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior contract analyst skilled at synthesizing expert insights into clear, actionable business recommendations."},
                {"role": "user", "content": combined_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

# Main function to run all agents in parallel
def analyze_contract(contract_text):
    """Run all agents in parallel and summarize their findings."""
    # Create agent instances
    legal_agent = LegalTermsChecker()
    compliance_agent = ComplianceValidator()
    financial_agent = FinancialRiskAssessor()
    summary_agent = SummaryAgent()
    
    # Run agents in parallel
    threads = [
        threading.Thread(target=legal_agent.run, args=(contract_text,)),
        threading.Thread(target=compliance_agent.run, args=(contract_text,)),
        threading.Thread(target=financial_agent.run, args=(contract_text,))
    ]
    
    # Start all threads
    for t in threads:
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    # Generate summary from all agent outputs
    final_analysis = summary_agent.run(contract_text, agent_outputs)
    
    return final_analysis

if __name__ == "__main__":
    print("Enterprise Contract Analysis System")
    print("Analyzing contract...")
    
    final_analysis = analyze_contract(contract_text)
    print("\n=== FINAL CONTRACT ANALYSIS ===\n")
    print(final_analysis)