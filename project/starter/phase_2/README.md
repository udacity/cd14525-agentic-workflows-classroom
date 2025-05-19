# Project Title: AI-Powered Agentic Workflow for Project Management
# Phase 2: Implement an agentic workflow using a predefined agent library.

Congratulations on reaching Phase 2 of the project! In this phase, you'll use the agent classes from Phase 1 to implement an agentic workflow.

As you’ve learned, agentic workflows offer greater flexibility compared to traditional automation. Instead of fixed, prescriptive steps, AI agents collaborate to dynamically execute workflow variations.

For this phase, you’ll build a general-purpose agentic workflow for product development project management. Agents will possess domain knowledge (interpreting product specs, defining user stories, features, and engineering tasks). A Technical Program Manager (TPM) persona will conceptually drive this workflow, interacting with specialized agents.

This is not about building a chatbot. You will develop an agentic system that processes a prompt and produces a structured output. You'll test this with "golden prompts"—realistic inputs a TPM might use.

## Workflow Agents Library

1.  Locate the `workflow_agents` folder. Ensure it contains the `base_agents.py` file with the code for all agent classes. Confirm you have completed testing these classes as required in Phase 1.
2.  You will be working in the `agentic_workflow.py` file in the Phase 2 folder to construct the agentic workflow using the agents from the `workflow_agents.base_agents` module.

## Workflow Script Implementation Steps

Follow the `TODO` comments in the `agentic_workflow.py` starter code. Below are detailed instructions for each step:

1.  **Import Agents (TODO 1):**
    Import `ActionPlanningAgent`, `KnowledgeAugmentedPromptAgent`, `EvaluationAgent`, and `RoutingAgent` from the `workflow_agents.base_agents` module.

2.  **Load OpenAI API Key (TODO 2):**
    Load your OpenAI API key from environment variables (e.g., using a `.env` file and the `python-dotenv` library) and store it in a variable named `openai_api_key`.

3.  **Load Product Specification (TODO 3):**
    Load the content of the `Product-Spec-Email-Router.txt` document into a string variable named `product_spec`.

4.  **Instantiate Action Planning Agent (TODO 4):**
    Instantiate the `ActionPlanningAgent`. The required `knowledge` string (`knowledge_action_planning`) is provided in the starter code.

5.  **Complete Product Manager Knowledge (TODO 5):**
    The `knowledge_product_manager` string for the Product Manager agent is partially provided. Complete it by appending the `product_spec` content (loaded in TODO 3) to the end of the string. This allows the agent to have the product specification as part of its knowledge.

6.  **Instantiate Product Manager Knowledge Agent (TODO 6):**
    Instantiate the `KnowledgeAugmentedPromptAgent` for the Product Manager. Use the `persona_product_manager` and the completed `knowledge_product_manager` (from TODO 5) strings provided in the starter code.

7.  **Instantiate Product Manager Evaluation Agent (TODO 7):**
    Define the `persona` and `evaluation_criteria` for the Product Manager's Evaluation Agent, then instantiate it. This agent will assess the outputs of the `product_manager_knowledge_agent`.
    * **Persona:** `"You are an evaluation agent that checks the answers of other worker agents"`
    * **Evaluation Criteria:** `"The answer should be stories that follow the following structure: As a [type of user], I want [an action or feature] so that [benefit/value]."`
    Pass the `product_manager_knowledge_agent` as the `agent_to_evaluate` parameter during instantiation.

8.  **Instantiate Program Manager Agents (Before and for TODO 8):**
    * First, instantiate the `KnowledgeAugmentedPromptAgent` for the Program Manager. The `persona_program_manager` and `knowledge_program_manager` strings are provided in the starter code. (A comment prompts this action before TODO 8).
    * **(TODO 8)** Then, instantiate the `EvaluationAgent` for the Program Manager.
        * Use the `persona_program_manager_eval` string provided in the starter code.
        * The `evaluation_criteria` are provided directly in the comment for TODO 8:
            ```
            "The answer should be product features that follow the following structure: " \
            "Feature Name: A clear, concise title that identifies the capability\n" \
            "Description: A brief explanation of what the feature does and its purpose\n" \
            "Key Functionality: The specific capabilities or actions the feature provides\n" \
            "User Benefit: How this feature creates value for the user"
            ```

9.  **Instantiate Development Engineer Agents (Before and for TODO 9):**
    * First, instantiate the `KnowledgeAugmentedPromptAgent` for the Development Engineer. The `persona_dev_engineer` and `knowledge_dev_engineer` strings are provided in the starter code. (A comment prompts this action before TODO 9).
    * **(TODO 9)** Then, instantiate the `EvaluationAgent` for the Development Engineer.
        * Use the `persona_dev_engineer_eval` string provided in the starter code.
        * The `evaluation_criteria` are provided directly in the comment for TODO 9:
            ```
            "The answer should be tasks following this exact structure: " \
            "Task ID: A unique identifier for tracking purposes\n" \
            "Task Title: Brief description of the specific development work\n" \
            "Related User Story: Reference to the parent user story\n" \
            "Description: Detailed explanation of the technical work required\n" \
            "Acceptance Criteria: Specific requirements that must be met for completion\n" \
            "Estimated Effort: Time or complexity estimation\n" \
            "Dependencies: Any tasks that must be completed first"
            ```

10. **Instantiate Routing Agent (TODO 10):**
    Instantiate the `RoutingAgent`. You will need to create a list of dictionaries, where each dictionary represents a route and contains:
    * `name`: (e.g., `"Product Manager"`)
    * `description`: A description of what this role is responsible for (e.g., `"Responsible for defining product personas and user stories only. Does not define features or tasks. Does not group stories"`)
    * `func`: A lambda function or a reference to a support function (defined in step 11) that will be called when this route is chosen (e.g., `lambda x: product_manager_support_function(x)`).
    Create routes for the Product Manager, Program Manager, and Development Engineer. Assign this list of routes to the `agents` attribute of your `routing_agent` instance.

11. **Define Support Functions (TODO 11):**
    Define the support functions that were referenced in the `func` field of your routing agent's routes (e.g., `product_manager_support_function`, `program_manager_support_function`, `development_engineer_support_function`). Each of these functions should:
    * Accept an input query (this will be a step from the action plan).
    * Call the `respond()` method of the corresponding Knowledge Augmented Prompt Agent (e.g., `product_manager_knowledge_agent.respond(query)`).
    * Take the response from the Knowledge Agent and pass it to the `evaluate()` method of the corresponding Evaluation Agent (e.g., `product_manager_evaluation_agent.evaluate(response_from_knowledge_agent)`).
    * Return the final, validated response (typically found in the `'final_response'` key of the dictionary returned by the `evaluate` method).

12. **Implement Workflow (TODO 12):**
    This is where the agentic workflow comes together:
    * Use the `action_planning_agent.extract_steps_from_prompt()` method with the `workflow_prompt` to get a list of workflow steps.
    * Initialize an empty list called `completed_steps`.
    * Iterate through the `workflow_steps` obtained from the Action Planning Agent. In each iteration:
        * Print the current step being processed.
        * Use the `routing_agent.route()` method to pass the current step. This will invoke the appropriate support function based on the routes you defined.
        * Append the result returned by the `routing_agent` to your `completed_steps` list.
        * Print the result of the current step.
    * After processing all steps, print the final output of the workflow, which is usually the last item in the `completed_steps` list.

This structured approach will guide you in building a functional agentic workflow. Good luck!