# agentic_workflow.py

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from workflow_agents.base_agents import ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent
import os
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv(dotenv_path="../../tests/.env")

# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("Product-Spec-Email-Router.txt", "r") as f:
    product_spec = f.read()
# Instantiate all the agents

openai_api_key = os.getenv("OPENAI_API_KEY")
# Action Planning Agent
knowledge_action_planning = (
    "A development Plan for a product contains all these components:\n"
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)
# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    f"Product spec: {product_spec}"
)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_product_manager, knowledge_product_manager)
# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
persona_product_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
product_manager_eval_criteria = "The answer should be stories that follow the following structure: As a [type of user], I want [an action or feature] so that [benefit/value]."
product_manager_eval_agent = EvaluationAgent(openai_api_key, persona_product_manager_eval, product_manager_eval_criteria, product_manager_knowledge_agent, 5)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_program_manager, knowledge_program_manager)
# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents"

# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
                    #  "The answer should be product features that follow the following structure: " \
                    #  "Feature Name: A clear, concise title that identifies the capability\n" \
                    #  "Description: A brief explanation of what the feature does and its purpose\n" \
                    #  "Key Functionality: The specific capabilities or actions the feature provides\n" \
                    #  "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
program_manager_eval_criteria = (
    # "The answer must list product features where each feature explicitly uses ALL of these labeled fields in this order: "
    # "Feature Name: <title>, Description: <explanation>, Key Functionality: <capabilities>, User Benefit: <value>. "
    # "Reject any response that uses bullet points or numbered lists without these exact field labels. "
    # "Reject any response that does not define at least one complete feature with all four labeled fields."
     "The answer should be product features that follow the following structure: " \
     "Feature Name: A clear, concise title that identifies the capability\n" \
     "Description: A brief explanation of what the feature does and its purpose\n" \
     "Key Functionality: The specific capabilities or actions the feature provides\n" \
     "User Benefit: How this feature creates value for the user"
)

program_manager_eval_agent = EvaluationAgent(openai_api_key, persona_program_manager_eval, program_manager_eval_criteria, program_manager_knowledge_agent, 5,
    required_fields=["Feature Name:", "Description:", "Key Functionality:", "User Benefit:"])

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = (
    "Development tasks are defined by identifying what needs to be built to implement each feature. "
    # "You must define tasks for ALL features listed in the input, not just the first one. "
    # "For each feature, define multiple tasks using EXACTLY this labeled format:\n"
    # "Task ID: <unique identifier e.g. T1.1>\n"
    # "Task Title: <brief title of the work>\n"
    # "Related User Story: <which feature or story this implements>\n"
    # "Description: <detailed technical description of what to build>\n"
    # "Acceptance Criteria: <specific conditions that must be met>\n"
    # "Estimated Effort: <time estimate e.g. 3 days>\n"
    # "Dependencies: <Any tasks that must be completed first>"

    # "For each feature, define multiple tasks using EXACTLY this labeled format:\n"
    "For each feature, identify multiple tasks needed, each task should be characterized by an <unique identifier e.g. T1.1>, <brief title of the work>, <which feature or story this implements>,\
    <detailed technical description of what to build>, <specific conditions that must be met>, <time estimate e.g. 3 days>"
    # "Task ID: <unique identifier e.g. T1.1>\n"
    # "Task Title: <brief title of the work>\n"
    # "Related User Story: <which feature or story this implements>\n"
    # "Description: <detailed technical description of what to build>\n"
    # "Acceptance Criteria: <specific conditions that must be met>\n"
    # "Estimated Effort: <time estimate e.g. 3 days>\n"
    # "Dependencies: <Any tasks that must be completed first>"
)
# knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.

#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

dev_engineer_eval_criteria = (
    # "The answer must list tasks where each task explicitly uses ALL of these labeled fields in this order, "
    # "Task ID: <unique identifier>, Task Title: <brief title>, Related User Story: <reference>, "
    # "Description: <technical detail>, Acceptance Criteria: <completion requirements>, Estimated Effort: <time estimate>. "
    # "Reject any response that uses plain numbered lists or bullet points without these exact field labels. "
    # "Reject any response that does not define at least one complete task with all seven labeled fields:"
    "The answer should be tasks following this exact structure: " \
    "Task ID: A unique identifier for tracking purposes\n" \
    "Task Title: Brief description of the specific development work\n" \
    "Related User Story: Reference to the parent user story\n" \
    "Description: Detailed explanation of the technical work required\n" \
    "Acceptance Criteria: Specific requirements that must be met for completion\n" \
    "Estimated Effort: Time or complexity estimation\n" \
    "Dependencies: Any tasks that must be completed first"
)

dev_engineer_eval_agent = EvaluationAgent(openai_api_key, persona_dev_engineer_eval, dev_engineer_eval_criteria, development_engineer_knowledge_agent, 5,
    required_fields=["Task ID:", "Task Title:", "Related User Story:", "Description:", "Acceptance Criteria:", "Estimated Effort:", "Dependencies"])
# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.
routing_agent = RoutingAgent(openai_api_key, {})
routing_agent.agents = [
    {
        "name": "Product Manager",
        "description": "Writes user stories by identifying a persona, an action, and a desired outcome for each story.",
        "func": lambda x: product_manager_support_function(x)
    },
    {
        "name": "Program Manager",
        "description": "Groups related user stories into product features.",
        "func": lambda x: program_manager_support_function(x)
    },
    {
        "name": "Development Engineer",
        "description": "Identifies the engineering work required to build each user story as development tasks.",
        "func": lambda x: development_engineer_support_function(x)
    },
]
# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(query):
    response = product_manager_knowledge_agent.respond(query)
    evaluation = product_manager_eval_agent.evaluate(response)
    return evaluation["final_response"]

def program_manager_support_function(query):
    response = program_manager_knowledge_agent.respond(query)
    evaluation = program_manager_eval_agent.evaluate(response)
    return evaluation["final_response"]

def development_engineer_support_function(query):
    response = development_engineer_knowledge_agent.respond(query)
    evaluation = dev_engineer_eval_agent.evaluate(response)
    return evaluation["final_response"]


# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
# workflow_prompt = "What would the development tasks for this product be?"
workflow_prompt = "What would the development plan for this product be?"
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
completed_steps = []
response_from_prev_step = None
for i, step in enumerate(workflow_steps, start=1):
    print(f"\n=== Step {i}/{len(workflow_steps)}: {step}")
    if response_from_prev_step:
        current_step_prompt = f"{step} Context: {response_from_prev_step}"
    else:
        current_step_prompt = f"{step}"
    response_from_prev_step = routing_agent.route(step, payload=current_step_prompt)
    completed_steps.append(response_from_prev_step)
    print(f"\n=== Result: {response_from_prev_step}")

print(f"final output: {completed_steps[-1]}")