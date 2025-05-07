# Agentic Workflow Example: Traditional vs AI-Driven Agents
This Python script demonstrates the conceptual similarities between traditional Python functions and OpenAI-powered agents. Both approaches take input, process it, and return output—but the way they do so differs significantly. Understanding this distinction is a key step in designing effective agentic workflows.

## Purpose
The goal of this script is to:

Highlight how deterministic (rule-based) agents work.

Introduce the concept of AI-enabled agents.

Show why AI-driven agents are essential for building agentic systems.

While deterministic agents can play a role in agentic workflows, they lack the flexibility and reasoning capabilities of true AI agents. This script helps clarify the role each type of agent can play.

## Components
The script includes two core functions:

traditional_generate_response()
Returns hardcoded responses based on simple keyword matching. This is a deterministic, rule-based approach often used for prototyping.

openai_generate_response()
Uses the OpenAI API to generate dynamic, natural-language responses. This represents an AI-enabled agent capable of understanding and adapting to context.

## Environment Configuration
The script uses the python-dotenv library to securely load environment variables, including:

OPENAI_API_KEY – your OpenAI API key, stored in a .env file to avoid hardcoding credentials.

## How It Works
A list of sample user queries is defined.

Each query is passed through both the traditional and AI-powered response functions.

The output is printed side-by-side to help you compare the responses.

## Why This Matters
This example lays the foundation for building more complex agentic workflows by:

Demonstrating the limits of deterministic logic.

Showing the power and adaptability of AI-enabled agents.

Preparing for later stages where agent collaboration and reasoning are required.
