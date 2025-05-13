# Exercise Instructions: Task Decomposition for Custom Car Build Plan

## Objective:
In this exercise, you will create a Task Decomposition Agent to generate a custom car build plan based on a customer's requested features. The agent will break down the steps needed to build the car using knowledge of different trims, without explicitly selecting a trim. The goal is to generate an actionable, step-by-step plan based on the customer's features.

## Starter Code:
Below is the starter code. You will need to implement the Task Decomposition Agent to decompose customer requests into the necessary steps for building the car. You do not need to call the LLM or handle the interaction with the OpenAI API here, just focus on structuring the task decomposition process.


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

## Task Breakdown and Instructions:
**Understand the Problem:**

Your goal is to break down a customer's request into a step-by-step build plan for assembling the car.

The customer may request features from different trims (e.g., "leather seats" from the Luxury Trim, "turbo engine" from the Sport Trim). You need to determine the necessary steps from each trim to meet the customer's requirements.

**The trims are:**

Base Trim

Sport Trim

Luxury Trim

## What You Need to Do:

Implement the task_decomposition_agent() function to decompose the customer’s request into actionable build steps. Each step should be clear and actionable.

Example: If the customer requests a turbo engine and leather seats, the agent should identify that:

The turbo engine comes from the Sport Trim.

The leather seats come from the Luxury Trim.

The function should return a list of steps that might look like this:


1. Install turbo engine (from Sport Trim)
2. Install leather seats (from Luxury Trim)
3. Mount basic wheels (from Base Trim)

## Structure:

Your function should not select a trim directly; it should only break down the customer request into necessary steps from different trims.

Decompose the features into steps, with each step potentially coming from a different trim.

## Expected Output:

Each step should include:

The action (e.g., "Install leather seats").

The source trim (e.g., "from Luxury Trim").

Optionally, additional notes if assumptions are made (e.g., default wheel type if unspecified).

## Hints:

Use the trim knowledge to figure out which steps come from which trim based on the features the customer asks for.

Each feature requested (e.g., "sunroof", "turbo engine") corresponds to specific steps that may span multiple trims.