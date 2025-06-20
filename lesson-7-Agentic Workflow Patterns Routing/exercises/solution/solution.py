import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


# --- Agents for Different Retail Tasks ---

def product_researcher_agent(query):
    """Product researcher agent gathers product information."""
    system_prompt = """You are a product research agent for a retail company. Your task is to provide 
    structured information about products, market trends, and competitor pricing."""
    
    user_prompt = f"Research this product thoroughly: {query}"
    return call_openai(system_prompt, user_prompt)


def customer_analyzer_agent(query):
    """Customer analyzer agent processes customer data and feedback."""
    system_prompt = """You are a customer analysis agent. Your task is to analyze customer feedback, 
    preferences, and purchasing patterns."""
    
    user_prompt = f"Analyze customer behavior for: {query}"
    return call_openai(system_prompt, user_prompt)


def pricing_strategist_agent(query, product_data=None, customer_data=None):
    """Pricing strategist agent recommends optimal pricing."""
    system_prompt = """You are a pricing strategist agent. Your task is to recommend optimal pricing 
    strategies based on product research and customer analysis."""
    
    user_prompt = f"""Recommend a pricing strategy for: {query}
    
    Product information: {product_data if product_data else 'No product data available'}
    
    Customer information: {customer_data if customer_data else 'No customer data available'}"""
    
    return call_openai(system_prompt, user_prompt)


# --- Routing Agent with LLM-Based Task Determination ---
def routing_agent(query, context=None):
    """Routing agent that determines which agent to use based on the query."""
    
    # Use LLM to analyze the query and determine the correct task type
    system_prompt = """You are an AI assistant that can route retail queries to the right agents. 
    You will be given a query, and your job is to determine the appropriate agent to handle it.
    Agents available:
    - Product Researcher Agent: Researches product specifications, market trends, and competitor pricing.
    - Customer Analyzer Agent: Analyzes customer feedback, preferences, and purchasing patterns.
    - Pricing Strategist Agent: Recommends optimal pricing strategies based on research and analysis.
    
    Respond only with the agent's name, nothing else."""
    
    user_prompt = f"Given the query: '{query}', which agent should handle this task?"
    
    agent_choice = call_openai(system_prompt, user_prompt)
    print(f"Selected agent: {agent_choice}")
    
    # Route the query to the correct agent based on the choice
    if "Product Researcher" in agent_choice:
        print("Routing query to Product Researcher Agent...")
        return product_researcher_agent(query)
    
    elif "Customer Analyzer" in agent_choice:
        print("Routing query to Customer Analyzer Agent...")
        return customer_analyzer_agent(query)
    
    elif "Pricing Strategist" in agent_choice:
        print("Routing query to Pricing Strategist Agent...")
        
        # For pricing strategy, we might need additional information
        # First, get product information
        product_data = None
        if context and "product_data" in context:
            product_data = context["product_data"]
        else:
            print("Getting product information first...")
            product_data = product_researcher_agent(query)
        
        # Then, get customer insights
        customer_data = None
        if context and "customer_data" in context:
            customer_data = context["customer_data"]
        else:
            print("Getting customer insights...")
            customer_data = customer_analyzer_agent(query)
        
        # Finally, determine pricing strategy using both inputs
        return pricing_strategist_agent(query, product_data, customer_data)
    
    else:
        return f"Couldn't route query. Agent decision was: {agent_choice}"


# --- Example Usage ---
if __name__ == "__main__":
    # Example queries
    queries = [
        "What are the specifications and current market trends for wireless earbuds?",
        "What do customers think about our premium coffee brand?",
        "What should be the optimal price for our new organic skincare line?"
    ]
    
    # Process each query
    for query in queries:
        print(f"\nQuery: {query}")
        print("\nProcessing...")
        
        result = routing_agent(query)
        print("\nResult:")
        print(result)
        print("\n" + "-"*80)