import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI
import json

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class FitnessUser:
    """Represents a fitness app user."""
    def __init__(self, id: str, age: int, fitness_level: int, 
                 goals: List[str], preferences: List[str], 
                 limitations: List[str] = None):
        self.id = id
        self.age = age
        self.fitness_level = fitness_level
        self.goals = goals
        self.preferences = preferences
        self.limitations = limitations or []

    def __str__(self):
        return f"User {self.id}: Level {self.fitness_level}, Goals: {', '.join(self.goals)}"


# ======== TODO: AGENT 1 — Deterministic Planner ========
# Create a rule-based planner that adjusts:
# - number of workout days
# - intensity
# - workout types
# - session duration
# based on fitness level and goals

def deterministic_agent(user: FitnessUser) -> Dict:
    """
    Implement your logic here to generate:
    {
        "weekly_schedule": {
            "Monday": {"type": "strength training", "duration": 45, "intensity": "moderate", "description": "..."},
            ...
        }
    }
    """
    # Your code goes here
    pass


# ======== AGENT 2 — LLM-Based Planner ========
# We've handled the API part. Your task is to COMPLETE THE PROMPT below
# that will instruct the LLM how to generate the plan.

def llm_agent(user: FitnessUser) -> Dict:
    goals_text = ", ".join(user.goals)
    preferences_text = ", ".join(user.preferences)
    limitations_text = ", ".join(user.limitations) if user.limitations else "None"

    prompt = f"""
    As a certified fitness trainer, create a personalized weekly workout plan for this client.

    Client Information:
    - Age: {user.age}
    - Fitness Level: {user.fitness_level}/5
    - Goals: {goals_text}
    - Preferences: {preferences_text}
    - Limitations: {limitations_text}

    # TODO: Add prompt instructions here to guide the LLM:
    # What should it focus on? How should it present the plan?
    # What format should the response follow?
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a certified fitness trainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        result_text = response.choices[0].message.content
        return json.loads(result_text)

    except Exception as e:
        fallback = deterministic_agent(user)
        return {
            "reasoning": f"LLM planning failed: {str(e)}",
            "weekly_schedule": fallback["weekly_schedule"],
            "considerations": "Fallback to rule-based plan."
        }


# ======== COMPARISON LOGIC (DO NOT EDIT) ========

def compare_workout_planning(users: List[FitnessUser]):
    print("\n===== WORKOUT PLAN COMPARISON =====")
    for i, user in enumerate(users, 1):
        print(f"\n--- User {i}: {user.id} ---")
        print(f"Age: {user.age} | Fitness Level: {user.fitness_level}/5")
        print(f"Goals: {', '.join(user.goals)}")
        print(f"Preferences: {', '.join(user.preferences)}")
        print(f"Limitations: {', '.join(user.limitations)}")

        det_plan = deterministic_agent(user)
        print("\n[Deterministic Agent]")
        for day, workout in det_plan["weekly_schedule"].items():
            print(f"- {day}: {workout['type']} ({workout['intensity']}, {workout['duration']} min)")

        llm_plan = llm_agent(user)
        print("\n[LLM Agent]")
        print(f"Reasoning: {llm_plan.get('reasoning', 'No reasoning provided')}")
        for day, workout in llm_plan["weekly_schedule"].items():
            print(f"- {day}: {workout['type']} ({workout['intensity']}, {workout['duration']} min)")
            print(f"  {workout['description']}")
        print(f"Considerations: {llm_plan.get('considerations', 'None')}")


# ======== SAMPLE USERS ========

def main():
    users = [
        FitnessUser(
            id="U001",
            age=35,
            fitness_level=2,
            goals=["weight management", "stress reduction"],
            preferences=["home workouts", "morning routines"],
            limitations=["limited equipment", "time constraints (max 30 min/day)"]
        ),
        FitnessUser(
            id="U002",
            age=55,
            fitness_level=3,
            goals=["joint mobility", "strength building"],
            preferences=["outdoor activities", "swimming"],
            limitations=["mild joint stiffness"]
        )
    ]

    compare_workout_planning(users)

if __name__ == "__main__":
    main()
