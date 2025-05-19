# Phase 1: Building Your Agent Library

## 1. Introduction

In the first phase of the project, you will build a library of reusable agents designed to support agentic workflows. While these agents will be used in the Phase 2 Project Management workflow, they are intended for general use across a variety of workflows.

In this phase, you will develop both the agent library and supporting scripts that instantiate and test each agent. These scripts will help verify that the agents function correctly and give you a deeper understanding of their behavior and capabilities.

**By the end of this phase, you will have:**

* Implemented seven agent classes in a single `base_agents.py` file, each demonstrating a unique agent workflow.
* Verified each agent’s behavior with a standalone test script.
* Organized your code into a clean, importable package that can be extended in Phase 2.

---

## 2. Directory Structure

You will see files inside the `phase_1` folder arranged as follows:

```
phase_1/
├── workflow_agents/
│   ├── __init__.py             ← (empty)
│   └── base_agents.py          ← Student implementation file
├── direct_prompt_agent.py
├── augmented_prompt_agent.py
├── knowledge_augmented_prompt_agent.py
├── rag_knowledge_prompt_agent.py
├── evaluation_agent.py
├── routing_agent.py
└── action_planning_agent.py
```

* `workflow_agents` is a Python package containing all your agent class definitions.
* One script per agent to test their functionality has also been provided in the folder.

**Environment Configuration:** Create a `.env` file in the `tests/` folder containing your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## 3. Agent Library Implementation

Complete each agent class in `workflow_agents/base_agents.py` in the following order, and validate using the provided test scripts.

### 3.1 Direct Prompt Agent

A **Direct Prompt Agent** offers the most straightforward method for interacting with a Large Language Model (LLM). It directly relays a user's input (prompt) to the LLM and returns the LLM's response without incorporating additional context, memory, or specialized tools.

---

#### Define the `DirectPromptAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following tasks to implement your `DirectPromptAgent` class:

1.  **Import the `OpenAI` Class:** Import the `OpenAI` class from the OpenAI Python library.
2.  **Store the API Key:** Within the class constructor (`__init__`), create an attribute named `openai_api_key` to store the provided OpenAI API key.
3.  **Select the LLM Model:** When calling the OpenAI API, select the `gpt-3.5-turbo` model for generating completions.
4.  **Send the User Prompt:** Pass the user-provided prompt directly to the model as a user message. Do not include a system prompt.
5.  **Implement the `respond` method:** Return only the content (text) of the LLM's response, not the full JSON payload.

---

#### Test the `DirectPromptAgent` Class

**File:** `direct_prompt_agent_test.py`

Complete these steps in your test script to verify the functionality of the `DirectPromptAgent`:

1.  **Import the Class:** Import the `DirectPromptAgent` class from `base_agents.py`.
2.  **Load the API Key:** Use the `dotenv` library to securely load your OpenAI API key from an environment file.
3.  **Instantiate the Agent:** Create an instance of the `DirectPromptAgent` class named `direct_agent` using the loaded API key.
4.  **Prompt the Agent:** Send the following prompt to the agent, store the response, and print it:
    ```
    "What is the Capital of France?"
    ```
5.  **Explain Knowledge Source:** Include a descriptive print statement explaining source of the knowledge the agent used to respond to your prompt (Hint: the agent uses general knowledge from the selected LLM model).

---

### 3.2 Augmented Prompt Agent

An **Augmented Prompt Agent** is a specialized agent designed to respond according to a predefined persona. Unlike basic prompt-response interactions, this agent explicitly adopts a persona, leading to more targeted and contextually relevant outputs.

---

#### Define the `AugmentedPromptAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following steps to implement your `AugmentedPromptAgent` class:

1.  **Create Persona Attribute:** Create an attribute within the class to store the agent's persona.
2.  **Call OpenAI API:** Declare a variable (e.g., `response`) to store the result of calling OpenAI's API for chat completions.
3.  **Include System Prompt:** Construct a system prompt that instructs the agent to assume the defined persona. Ensure the agent is explicitly told to forget any previous conversational context.
4.  **Return Textual Content:** In the `respond` method, return only the textual content of the response from the API, not the full JSON response.

---

#### Test the `AugmentedPromptAgent` Class

**File:** `augmented_prompt_agent_test.py`

Complete the following tasks in your test script to test the `AugmentedPromptAgent`:

1.  **Import the Class:** Import the `AugmentedPromptAgent` class from `base_agents.py`.
2.  **Instantiate the Agent:** Create an instance of the `AugmentedPromptAgent` class using your OpenAI API key and a defined persona.
3.  **Send a Prompt:** Send a prompt to the agent and store the result in a variable named `augmented_agent_response`.
4.  **Print the Response:** Clearly print the `augmented_agent_response` to verify the agent’s behavior.
5.  **Provide Explanatory Comments:** Include comments discussing:
    * The type of knowledge the agent likely used to generate its response.
    * How specifying the agent’s persona affected the final output.

---

### 3.3 Knowledge Augmented Prompt Agent

The **Knowledge Augmented Prompt Agent** is designed to incorporate specific, provided knowledge alongside a defined persona when responding to prompts, ensuring answers are based on that explicit information.

---

#### Define the `KnowledgeAugmentedPromptAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following steps to build this agent class:

1.  **Create Persona Attribute:** Create an attribute for storing the agent’s persona.
2.  **Create Knowledge Attribute:** Create an attribute for storing the agent’s specific knowledge.
3.  **Implement the `respond` method:** Within this method:
    * Construct a **system message** that clearly defines the persona with the instruction:
        ```
        You are _persona_ knowledge-based assistant. Forget all previous context.
        ```
        (Replace `_persona_` with the actual persona variable/attribute).
    * Clearly specify the provided knowledge in the system message:
        ```
        Use only the following knowledge to answer, do not use your own knowledge: _knowledge_
        ```
        (Replace `_knowledge_` with the actual knowledge variable/attribute).
    * Include a final instruction in the system message:
        ```
        Answer the prompt based on this knowledge, not your own.
        ```
4.  **Append User Prompt:** Append the user's input prompt as a separate message in the API request.

---

#### Test the `KnowledgeAugmentedPromptAgent` Class

**File:** `knowledge_augmented_prompt_agent.py`

Complete the following steps in your test script to instantiate and test the `KnowledgeAugmentedPromptAgent`:

1.  **Import the Class:** Import the `KnowledgeAugmentedPromptAgent` class from `base_agents.py`.
2.  **Load the API Key:** Load your OpenAI API key from your `.env` file.
3.  **Instantiate the Agent:** Create an instance of the agent with the following parameters:
    * **Persona:**
        ```
        "You are a college professor, your answer always starts with: Dear students,"
        ```
    * **Knowledge:**
        ```
        "The capital of France is London, not Paris"
        ```
4.  **Test the Agent:** Use the following prompt:
    ```
    "What is the capital of France?"
    ```
5.  **Confirm Knowledge Usage:** Add a print statement to confirm the agent’s response explicitly uses the provided knowledge rather than its inherent knowledge from the LLM.

---

### 3.4 RAG Knowledge Prompt Agent

The **RAG Knowledge Prompt Agent** uses retrieval-augmented generation for dynamic knowledge sourcing. You don't need to implement this, as the code has been provided. Feel free to go through the code if you are familiar with RAG. You can learn more about RAG [here](https://dl.acm.org/doi/abs/10.5555/3495724.3496517) and [here](https://en.wikipedia.org/wiki/Retrieval-augmented_generation).

---

### 3.5 Evaluation Agent

The **Evaluation Agent** is designed to assess responses from another agent (a "worker" agent) against a given set of criteria, potentially refining the response through iterative feedback.

---

#### Define the `EvaluationAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following tasks to implement the `EvaluationAgent` class:

1.  **Declare Class Attributes:** Define all necessary class attributes for the `EvaluationAgent`, including one for `max_interactions`.
2.  **Implement Interaction Loop:** Create a loop that is limited by the `max_interactions` attribute.
3.  **Retrieve Worker Response:** Within the loop, retrieve a response from the worker agent.
4.  **Construct Evaluation Prompt:** Formulate an evaluation prompt that incorporates the predefined evaluation criteria.
5.  **Define Evaluation Message Structure:** Define the message structure to evaluate responses using the OpenAI API. Set `temperature=0` for this call.
6.  **Define Correction Instruction Message Structure:** Define the message structure to generate instructions for correcting responses, also using the OpenAI API with `temperature=0`.
7.  **Return Results:** Ensure the `respond` method (or equivalent) returns a dictionary containing the final response from the worker agent, the evaluation result, and the count of iterations performed.

---

#### Test the `EvaluationAgent` Class

**File:** `evaluation_agent.py`

Complete the following steps in your test script to instantiate and test the `EvaluationAgent`:

1.  **Import Classes:** Import the `EvaluationAgent` and `KnowledgeAugmentedPromptAgent` from `base_agents.py`.
2.  **Instantiate Worker Agent:** Create an instance of `KnowledgeAugmentedPromptAgent` with:
    * **Persona:**
        ```
        "You are a college professor, your answer always starts with: Dear students,"
        ```
    * **Knowledge:**
        ```
        "The capitol of France is London, not Paris"
        ```
3.  **Instantiate Evaluation Agent:** Create an instance of the `EvaluationAgent` with a maximum of `10` interactions.
4.  **Evaluate Prompt and Print:** Evaluate the prompt `"What is the capital of France?"` using the `EvaluationAgent` and print the resulting evaluation.

---

### 3.6 Routing Agent

The **Routing Agent** is capable of directing user prompts to the most appropriate specialized agent from a collection, based on semantic similarity between the prompt and descriptions of what each agent handles.

---

#### Define the `RoutingAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following tasks to implement the `RoutingAgent` class:

1.  **Define `agents` Attribute:** Within the class constructor (`__init__`), define an attribute named `agents` to store agent details (e.g., descriptions and their callable functions/methods).
2.  **Implement `get_embedding` Method:** Implement a method to calculate text embeddings using the `text-embedding-3-large` model from OpenAI.
3.  **Create Routing Method:** Create a new method to route user prompts. This method should:
    * Compute the embedding for the user input prompt.
    * Iterate over each agent stored in the `agents` attribute:
        * Compute the embedding for each agent's description.
        * Calculate the cosine similarity between the user prompt embedding and the agent description embedding.
        * Select the agent that has the highest similarity score.
4.  **Return Selected Agent's Response:** The routing method should return the response obtained by calling the selected agent.

---

#### Test the `RoutingAgent` Class

**File:** `routing_agent.py`

Complete the following steps in your test script to instantiate and test the `RoutingAgent`:

1.  **Import Classes:** Import `KnowledgeAugmentedPromptAgent` and `RoutingAgent` from `base_agents.py`.
2.  **Instantiate Texas Agent:** Create an instance of `KnowledgeAugmentedPromptAgent` for Texas-related knowledge.
3.  **Instantiate Europe Agent:** Create another instance of `KnowledgeAugmentedPromptAgent` for Europe-related knowledge.
4.  **Instantiate Math Agent:** Create a third `KnowledgeAugmentedPromptAgent` specifically for math-related prompts.
5.  **Define Agent Functions/Lambdas:** For each agent, define a function or lambda expression that will be called if that agent is selected. These functions will embody the agent's task (e.g., answering Texas-related questions).
6.  **Assign Agents to Router:** Assign these agents (along with their descriptions and callable functions/lambdas) to the `agents` attribute of the `RoutingAgent` instance.
7.  **Test Routing with Prompts:** Test your routing agent with the following prompts and print the results:
    * `"Tell me about the history of Rome, Texas"`
    * `"Tell me about the history of Rome, Italy"`
    * `"One story takes 2 days, and there are 20 stories"`

---

### 3.7 Action Planning Agent

The **Action Planning Agent** is crucial for constructing agentic workflows. This agent uses its provided knowledge to dynamically extract and list the steps required to execute a task described in a user's prompt.

---

#### Define the `ActionPlanningAgent` Class

**File:** `workflow_agents/base_agents.py`

Complete the following tasks to implement the `ActionPlanningAgent` class:

1.  **Initialize Agent Attributes:** In the constructor (`__init__`), initialize attributes for the OpenAI API key and the agent's knowledge.
2.  **Instantiate OpenAI Client:** Instantiate the OpenAI client object.
3.  **Implement `respond` method (or similar logic):**
    * Send a request to OpenAI's `gpt-3.5-turbo` model using:
        * A **system prompt** defining the agent as an "Action Planning Agent" that extracts steps using provided knowledge.
        * The **user's input prompt**.
    * Extract and store the text response from the OpenAI API.
4.  **Process Response:** Process the response text to clearly extract individual action steps, removing any empty or irrelevant lines to produce a clean list of actions.

---

#### Test the `ActionPlanningAgent` Class

**File:** `action_planning_agent_test.py` (assuming this naming convention)

Complete the following steps in your test script to test the `ActionPlanningAgent`:

1.  **Import Libraries and Class:** Import necessary libraries (e.g., `dotenv`) and the `ActionPlanningAgent` class from `base_agents.py`.
2.  **Load API Key:** Load environment variables and assign your OpenAI API key to a variable, for example, `openai_api_key`.
3.  **Instantiate the Agent:** Create an instance of the `ActionPlanningAgent`, providing it with the defined knowledge (if any is specifically required for its action planning task beyond general instruction) and the API key.
4.  **Verify Functionality:** Test the agent by sending it the following prompt and printing the extracted action steps:
    ```
    "One morning I wanted to have scrambled eggs"
    ```

## 4. Phase 1 Artifacts (to carry into Phase 2)

At the end of Phase 1, you should have:

* A fully implemented `workflow_agents/base_agents.py`.
* Seven test scripts, each demonstrating correct agent behavior.
* Screenshots of correct outputs on running each of the seven scripts.

> **Note:** Bundle these artifacts with your Phase 2 deliverables at the project's conclusion.

---

## 5. Next Steps: Preview of Phase 2

In Phase 2, you will use the agents library that you just implemented to create a complex multi-step workflow. Prepare to solve real-world problems with your agent workflow!