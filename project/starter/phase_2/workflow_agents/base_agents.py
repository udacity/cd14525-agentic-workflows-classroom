from openai import OpenAI
import numpy as np
import pandas as pd
import re
import csv
import uuid
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../../tests/.env")

# DirectPromptAgent class definition
class DirectPromptAgent:
    
    def __init__(self, openai_api_key):
        # Initialize the agent
        # TODO: 2 - Define an attribute named openai_api_key to store the OpenAI API key provided to this class.
        self.openai_api_key = openai_api_key

    def respond(self, prompt):
        # Generate a response using the OpenAI API
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

# AugmentedPromptAgent class definition
class AugmentedPromptAgent:
    def __init__(self, openai_api_key, persona):
        """Initialize the agent with given attributes."""
        # TODO: 1 - Create an attribute for the agent's persona
        self.openai_api_key = openai_api_key
        self.persona = persona

    def respond(self, input_text):
        """Generate a response using OpenAI API."""
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)

        # TODO: 2 - Declare a variable 'response' that calls OpenAI's API for a chat completion.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                # TODO: 3 - Add a system prompt instructing the agent to assume the defined persona and explicitly forget previous context.
                {"role": "system", "content": f"You are {self.persona}. Forget previous context."},
                {"role": "user", "content": input_text}
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()


# KnowledgeAugmentedPromptAgent class definition
class KnowledgeAugmentedPromptAgent:
    def __init__(self, openai_api_key, persona, knowledge):
        """Initialize the agent with provided attributes."""
        self.persona = persona
        # TODO: 1 - Create an attribute to store the agent's knowledge.
        self.knowledge = knowledge
        self.openai_api_key = openai_api_key

    def respond(self, input_text):
        """Generate a response using the OpenAI API."""
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are {self.persona} knowledge-based assistant. Forget all previous context.\n"
                        f"Use only the following knowledge to answer, do not use your own knowledge: {self.knowledge}\n"
                        "Answer the prompt based on this knowledge, not your own."
                    )
                },
                {
                    "role": "user",
                    "content": input_text
                }
                # TODO: 3 - Add the user's input prompt here as a user message.
            ],
            temperature=0
        )
        return response.choices[0].message.content


# RAGKnowledgePromptAgent class definition
class RAGKnowledgePromptAgent:
    """
    An agent that uses Retrieval-Augmented Generation (RAG) to find knowledge from a large corpus
    and leverages embeddings to respond to prompts based solely on retrieved information.
    """

    def __init__(self, openai_api_key, persona, chunk_size=2000, chunk_overlap=100):
        """
        Initializes the RAGKnowledgePromptAgent with API credentials and configuration settings.

        Parameters:
        openai_api_key (str): API key for accessing OpenAI.
        persona (str): Persona description for the agent.
        chunk_size (int): The size of text chunks for embedding. Defaults to 2000.
        chunk_overlap (int): Overlap between consecutive chunks. Defaults to 100.
        """
        self.persona = persona
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.openai_api_key = openai_api_key
        self.unique_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.csv"

    def get_embedding(self, text):
        """
        Fetches the embedding vector for given text using OpenAI's embedding API.

        Parameters:
        text (str): Text to embed.

        Returns:
        list: The embedding vector.
        """
        client = OpenAI(base_url="https://openai.vocareum.com/v1", api_key=self.openai_api_key)
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=text,
            encoding_format="float"
        )
        return response.data[0].embedding

    def calculate_similarity(self, vector_one, vector_two):
        """
        Calculates cosine similarity between two vectors.

        Parameters:
        vector_one (list): First embedding vector.
        vector_two (list): Second embedding vector.

        Returns:
        float: Cosine similarity between vectors.
        """
        vec1, vec2 = np.array(vector_one), np.array(vector_two)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def chunk_text(self, text):
        """
        Splits text into manageable chunks, attempting natural breaks.

        Parameters:
        text (str): Text to split into chunks.

        Returns:
        list: List of dictionaries containing chunk metadata.
        """
        separator = "\n"
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text) <= self.chunk_size:
            return [{"chunk_id": 0, "text": text, "chunk_size": len(text)}]

        chunks, start, chunk_id = [], 0, 0

        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            if separator in text[start:end]:
                end = start + text[start:end].rindex(separator) + len(separator)

            chunks.append({
                "chunk_id": chunk_id,
                "text": text[start:end],
                "chunk_size": end - start,
                "start_char": start,
                "end_char": end
            })

            # break the loop if we have reached the end of the text
            if end == len(text):
                break

            start = end - self.chunk_overlap
            chunk_id += 1

        with open(f"chunks-{self.unique_filename}", 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["text", "chunk_size"])
            writer.writeheader()
            for chunk in chunks:
                writer.writerow({k: chunk[k] for k in ["text", "chunk_size"]})

        return chunks

    def calculate_embeddings(self):
        """
        Calculates embeddings for each chunk and stores them in a CSV file.

        Returns:
        DataFrame: DataFrame containing text chunks and their embeddings.
        """
        df = pd.read_csv(f"chunks-{self.unique_filename}", encoding='utf-8')
        df['embeddings'] = df['text'].apply(self.get_embedding)
        df.to_csv(f"embeddings-{self.unique_filename}", encoding='utf-8', index=False)
        return df

    def find_prompt_in_knowledge(self, prompt):
        """
        Finds and responds to a prompt based on similarity with embedded knowledge.

        Parameters:
        prompt (str): User input prompt.

        Returns:
        str: Response derived from the most similar chunk in knowledge.
        """
        prompt_embedding = self.get_embedding(prompt)
        df = pd.read_csv(f"embeddings-{self.unique_filename}", encoding='utf-8')
        df['embeddings'] = df['embeddings'].apply(lambda x: np.array(eval(x)))
        df['similarity'] = df['embeddings'].apply(lambda emb: self.calculate_similarity(prompt_embedding, emb))

        best_chunk = df.loc[df['similarity'].idxmax(), 'text']

        client = OpenAI(base_url="https://openai.vocareum.com/v1", api_key=self.openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are {self.persona}, a knowledge-based assistant. Forget previous context."},
                {"role": "user", "content": f"Answer based only on this information: {best_chunk}. Prompt: {prompt}"}
            ],
            temperature=0
        )

        return response.choices[0].message.content


class EvaluationAgent:
    
    def __init__(self, openai_api_key, persona, evaluation_criteria, worker_agent, max_interactions, required_fields=None):
        # Initialize the EvaluationAgent with given attributes.
        # TODO: 1 - Declare class attributes here
        self.openai_api_key = openai_api_key
        self.persona = persona
        self.max_interactions = max_interactions
        self.evaluation_criteria = evaluation_criteria
        self.worker_agent = worker_agent
        self.required_fields = required_fields or []

    def evaluate(self, initial_prompt):
        # This method manages interactions between agents to achieve a solution.
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)
        prompt_to_evaluate = initial_prompt
        iterations = 0
        for i in range(self.max_interactions): #2 - Set loop to iterate up to the maximum number of interactions:
            print(f"\n--- Interaction {i+1} ---")

            print(" Step 1: Worker agent generates a response to the prompt")
            print(f"Prompt:\n{prompt_to_evaluate}")
            if iterations == 0:
                response_from_worker = prompt_to_evaluate
            else:
                response_from_worker = self.worker_agent.respond(prompt_to_evaluate) # TODO: 3 - Obtain a response from the worker agent
            print(f"Worker Agent Response:\n{response_from_worker}")

            print(" Step 2: Evaluator agent judges the response")
            eval_prompt = (
                f"Evaluate whether the following answer meets the criteria.\n\n"
                f"ANSWER: {response_from_worker}\n\n"
                f"CRITERIA: {self.evaluation_criteria}\n\n"
                f"Respond using EXACTLY this format:\n"
                f"VERDICT: YES\n"
                f"REASON: <why it meets the criteria>\n\n"
                f"OR:\n\n"
                f"VERDICT: NO\n"
                f"REASON: <why it does not meet the criteria>"
            )
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages=[{"role": "system", "content": f"You are {self.persona}. You must respond with VERDICT: YES or VERDICT: NO on the first line, followed by REASON: on the second line. Follow the output format exactly."},
                          {"role": "user", "content": f"{eval_prompt}"}
                ],
                temperature = 0
            )
            evaluation = response.choices[0].message.content.strip()
            iterations += 1
            print(" Step 3: Check if evaluation is positive")
            verdict_line = next((line for line in evaluation.splitlines() if line.strip().upper().startswith("VERDICT:")), "")
            missing_fields = [f for f in self.required_fields if f not in response_from_worker]
            if "YES" in verdict_line.upper() and missing_fields:
                evaluation = f"VERDICT: NO\nREASON: Response is missing required labeled fields: {', '.join(missing_fields)}"
                verdict_line = "VERDICT: NO"
                print(f"Evaluator Agent Evaluation:\n{evaluation}")
            if "YES" in verdict_line.upper():
                print(f"Evaluator Agent Evaluation:\n{evaluation}")
                print("✅ Final solution accepted.")
                break
            else:
                print(" Step 4: Generate instructions to correct the response")
                reason_line = next((line for line in evaluation.splitlines() if line.strip().upper().startswith("REASON:")), "")
                reason = reason_line.split(":", 1)[-1].strip() if reason_line else evaluation
                instruction_prompt = (
                    f"Provide instructions to fix an answer based on these reasons why it is incorrect: {reason}"
                )
                response = client.chat.completions.create(
                    model = "gpt-3.5-turbo",
                    messages=[{"role": "system", "content": f"You are {self.persona}, you will provide correction based on evaluation"},
                          {"role": "user", "content": f"{instruction_prompt}"}], # TODO: 6 - Define the message structure sent to the LLM to generate correction instructions (use temperature=0)
                    temperature = 0
                )
                instructions = response.choices[0].message.content.strip()
                print(f"Instructions to fix:\n{instructions}")

                print(" Step 5: Send feedback to worker agent for refinement")
                prompt_to_evaluate = (
                    f"The original prompt was: {initial_prompt}\n"
                    f"The response to that prompt was: {response_from_worker}\n"
                    f"It has been evaluated as incorrect.\n"
                    f"Make only these corrections, do not alter content validity: {instructions}"
                )

        return {
            # TODO: 7 - Return a dictionary containing the final response, evaluation, and number of iterations
            "final_response": response_from_worker,
            "evaluation": evaluation,
            "iterations number": iterations
        }   


class RoutingAgent():
    def __init__(self, openai_api_key, agents):
        # Initialize the agent with given attributes
        self.openai_api_key = openai_api_key
        # TODO: 1 - Define an attribute to hold the agents, call it agents
        self.agents = agents

    def get_embedding(self, text):
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=text,
            encoding_format="float"
        )
        return response.data[0].embedding

    # TODO: 3 - Define a method to route user prompts to the appropriate agent
    def route(self, user_input, payload=None):
        # TODO: 4 - Compute the embedding of the user input prompt
        input_emb = self.get_embedding(user_input)
        best_agent = None
        best_score = -1

        for agent in self.agents:
        #     # TODO: 5 - Compute the embedding of the agent description
            agent_emb = self.get_embedding(agent["description"])
            if agent_emb is None:
                continue

            similarity = np.dot(input_emb, agent_emb) / (np.linalg.norm(input_emb) * np.linalg.norm(agent_emb))
            print(similarity)

            if similarity > best_score:
                best_agent = agent
                best_score = similarity

        #     # TODO: 6 - Add logic to select the best agent based on the similarity score between the user prompt and the agent descriptions

        if best_agent is None:
            return "Sorry, no suitable agent could be selected."

        print(f"[Router] Best agent: {best_agent['name']} (score={best_score:.3f})")
        execution_input = payload if payload is not None else user_input
        return best_agent["func"](execution_input)


class ActionPlanningAgent:

    def __init__(self, openai_api_key, knowledge):
        # TODO: 1 - Initialize the agent attributes here
        self.openai_api_key = openai_api_key
        self.knowledge = knowledge

    def extract_steps_from_prompt(self, prompt):

        # TODO: 2 - Instantiate the OpenAI client using the provided API key
        client = OpenAI(base_url = os.getenv("BASE_URL"),
                        api_key=self.openai_api_key)
        # TODO: 3 - Call the OpenAI API to get a response from the "gpt-3.5-turbo" model.
        # Provide the following system prompt along with the user's prompt:
        # "You are an action planning agent. Using your knowledge, you extract from the user prompt the steps requested to complete the action the user is asking for. You return the steps as a list. Only return the steps in your knowledge. Forget any previous context. This is your knowledge: {pass the knowledge here}"
        system_prompt = f"""
        "You are an action planning agent. Using your knowledge, you extract from the user prompt the steps requested to complete the action the user is asking for. 
        You return the steps as a list. Only return the steps in your knowledge. Forget any previous context. This is your knowledge: {self.knowledge}"
        """
        response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages=[{"role": "system", "content": system_prompt},
                          {"role": "user", "content": prompt}
                ], #5 - Define the message structure sent to the LLM for evaluation (use temperature=0)
                temperature = 0
            )
        response_text = response.choices[0].message.content.strip() # TODO: 4 - Extract the response text from the OpenAI API response

        # TODO: 5 - Clean and format the extracted steps by removing empty lines and unwanted text
        # steps = response_text.split("\n")
        steps = [line.strip() for line in response_text.split("\n") if line.strip()]

        return steps
