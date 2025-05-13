import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OpenAI wrapper
def call_openai(system_prompt, user_prompt, model="gpt-4"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# ------------------- AGENT: TASK DECOMPOSITION ----------------------

def task_decomposition_agent(customer_prompt):
    """Generates custom build steps based on customer-selected features, using trim knowledge"""
    system_prompt = """
You are a car manufacturing task decomposition agent.

You know the detailed build steps of the following trims:

--- TRIM KNOWLEDGE ---

[Base Trim]
1. Install standard engine
2. Mount basic wheels
3. Install cloth seats
4. Basic infotainment setup
5. Paint standard color

[Sport Trim]
1. Install turbo engine
2. Mount sport wheels
3. Install cloth racing seats
4. Add rear spoiler
5. Calibrate sport suspension
6. Paint red or black

[Luxury Trim]
1. Install V6 engine
2. Mount alloy wheels
3. Install leather seats
4. Add sunroof
5. Add premium infotainment system
6. Add noise insulation
7. Paint metallic silver or pearl white

--- INSTRUCTIONS ---

Given a customer's desired features, extract the relevant build steps from any trim. Combine steps as needed to match the features. 
Do not name trims. The final car is a custom build, not a specific trim.

Respond with a step-by-step build plan, including:
- Step number
- Action
- Source trim (for transparency)
- (Optional) notes if assumptions are made
"""
    
    user_prompt = f"Customer wants: {customer_prompt}"
    
    print("[Task Decomposition Agent] Generating build plan...")
    return call_openai(system_prompt, user_prompt)

# ------------------- RUNNER ----------------------

def run_build_plan_workflow(customer_prompt):
    print("\n==============================")
    print(f"🚗 Customer Request: {customer_prompt}")
    print("==============================")
    
    build_plan = task_decomposition_agent(customer_prompt)
    
    print("\n🛠️ Build Plan:\n")
    print(build_plan)

# ------------------- EXAMPLES ----------------------

if __name__ == "__main__":
    example_prompts = [
        "I want leather seats, a turbo engine, and basic wheels.",
        "Please build a quiet car with a sunroof and standard engine.",
        "I want a sporty car with racing seats and a rear spoiler, but with leather interior.",
    ]

    for prompt in example_prompts:
        run_build_plan_workflow(prompt)
        print("\n" + "="*70 + "\n")
