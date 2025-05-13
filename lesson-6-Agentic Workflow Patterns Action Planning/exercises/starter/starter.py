# ------------------- AGENT: TASK DECOMPOSITION ----------------------

def task_decomposition_agent(customer_prompt):
    """
    This function takes the customer's request (customer_prompt) and returns
    a list of steps required to build the car based on the features they want.
    
    Use the knowledge of different trims to determine the necessary steps for
    building the car with those features.
    
    The function should:
    - Extract relevant features from the customer prompt.
    - Break down the features into actionable build steps.
    - Combine steps from different trims as needed.
    - Return a step-by-step list of build actions.
    
    Example steps:
    1. Install turbo engine (from Sport Trim)
    2. Install leather seats (from Luxury Trim)
    3. Basic wheels (from Base Trim)
    """
    # TODO: Implement task decomposition logic here.
    pass

# ------------------- RUNNER ----------------------

def run_build_plan_workflow(customer_prompt):
    """
    This function takes the customer's request (customer_prompt) and prints
    the corresponding build plan, broken down into steps.
    """
    # TODO: Call the task_decomposition_agent() here and print the result.
    pass

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
