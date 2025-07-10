import os
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content

def feedstock_analyst_agent(feedstock_name):
    """Analyzes incoming hydrocarbon feedstock"""
    system_prompt = """You are a refinery feedstock analyst.
Provide a detailed analysis of the input hydrocarbon feed.
Always include these sections:
# FEEDSTOCK COMPOSITION
# YIELD POTENTIAL
# PROCESSING NOTES
"""
    user_prompt = f"Analyze the feedstock: {feedstock_name}"
    print(f"Feedstock Analyst working on: {feedstock_name}")
    return call_openai(system_prompt, user_prompt)

def distillation_planner_agent(feedstock_report):
    """Plans the distillation based on feedstock analysis"""
    system_prompt = """You are a refinery planner.
Use the feedstock report to propose an allocation through the distillation tower.
Include:
# PRODUCT ALLOCATION (percentage of each product)
# ASSUMPTIONS
# NOTES FOR OPERATIONS
"""
    user_prompt = f"Based on this feedstock report, plan the distillation:\n\n{feedstock_report}"
    print("Distillation Planner generating product allocation...")
    return call_openai(system_prompt, user_prompt)

def market_analyst_agent(product_list_text):
    """Analyzes market demand for refinery products"""
    system_prompt = """You are a market analyst for petroleum products.
Provide current demand and pricing insights.
Format the response as:
# PRODUCT DEMAND ANALYSIS
# PRICE TRENDS
# MARKET RECOMMENDATIONS
"""
    user_prompt = f"Analyze market conditions for the following products:\n{product_list_text}"
    print("Market Analyst evaluating market demand...")
    return call_openai(system_prompt, user_prompt)

def production_optimizer_agent(distillation_output, market_analysis):
    """Recommends production strategy based on operations and market"""
    system_prompt = """You are a refinery production strategist.
Make a recommendation balancing operational output and market demand.
Include:
# OPTIMIZED PRODUCTION PLAN
# RATIONALE
# STRATEGIC NOTES
"""
    user_prompt = f"""Use the following inputs to recommend a production plan:

Distillation Plan:
{distillation_output}

Market Analysis:
{market_analysis}
"""
    print("Production Optimizer creating final plan...")
    return call_openai(system_prompt, user_prompt)

def run_refinery_chain(feedstock_name):
    """Run the refinery agentic workflow"""
    print(f"\nStarting refinery optimization workflow for: '{feedstock_name}'")

    # Step 1: Feedstock Analysis
    feedstock_report = feedstock_analyst_agent(feedstock_name)
    print("\nFeedstock analysis complete.")

    # Step 2: Distillation Planning
    distillation_plan = distillation_planner_agent(feedstock_report)
    print("\nDistillation planning complete.")

    # Step 3: Market Analysis
    # We need to extract the list of products from the distillation plan
    system_prompt = "List all products from the distillation plan above."
    product_list = call_openai(system_prompt, distillation_plan)

    # This list of products is then used to perform market analysis
    market_analysis = market_analyst_agent(product_list)
    print("\nMarket analysis complete.")

    # Step 4: Production Optimization
    production_plan = production_optimizer_agent(distillation_plan, market_analysis)
    print("\nProduction optimization complete.")

    # Print results
    print("\n===== FEEDSTOCK REPORT =====")
    print(feedstock_report)

    print("\n===== DISTILLATION PLAN =====")
    print(distillation_plan)

    print("\n===== MARKET ANALYSIS =====")
    print(market_analysis)

    print("\n===== FINAL PRODUCTION PLAN =====")
    print(production_plan)

    return {
        "feedstock": feedstock_report,
        "distillation": distillation_plan,
        "market": market_analysis,
        "plan": production_plan
    }

# Run the example
if __name__ == "__main__":
    feedstock_input = "Light Sweet Crude"
    results = run_refinery_chain(feedstock_input)