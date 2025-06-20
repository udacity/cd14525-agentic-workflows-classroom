import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
# Make sure you have a .env file with your OPENAI_API_KEY
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-4o"):
    """A wrapper for making calls to the OpenAI API."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during API call: {e}"

# --- Worker Agent Classes ---

class DietaryProfilerWorker:
    """
    Analyzes the user's request to extract key dietary parameters.
    """
    def run(self, user_request):
        system_prompt = """You are an expert at parsing user dietary requests. Analyze the user's prompt and extract the following details: plan_duration (in days), dietary_restrictions (e.g., 'vegetarian', 'vegan', 'gluten-free'), health_goals (e.g., 'weight_loss', 'high_protein'), and known_allergies (as a list of strings).
Your response MUST be a valid JSON object with these keys. Do not add any markdown formatting like ```json."""
        
        user_prompt = f"User request: '{user_request}'"
        
        try:
            response_text = call_openai(system_prompt, user_prompt)
            
            # Sanitize the LLM response to make it valid JSON.
            if response_text.strip().startswith("```json"):
                response_text = response_text.strip()[7:-3].strip()
            cleaned_text = response_text.replace(u'\u00A0', ' ')

            return json.loads(cleaned_text)
        except (json.JSONDecodeError, TypeError) as e:
            return {"error": f"Failed to parse user profile. Details: {e}", "raw_response": response_text}

class RecipeFinderWorker:
    """
    Finds recipes tailored to the user's dietary profile.
    """
    def run(self, dietary_profile):
        system_prompt = "You are a nutritionist and chef. Based on the user's dietary profile, suggest a list of suitable recipes for breakfast, lunch, and dinner. Provide a brief description and ingredients for each recipe."
        user_prompt = f"Find recipes for a {dietary_profile.get('plan_duration')}-day meal plan with the following needs: {json.dumps(dietary_profile)}"
        return call_openai(system_prompt, user_prompt)

class GroceryListGeneratorWorker:
    """
    Generates a consolidated grocery list from a list of recipes.
    """
    def run(self, recipes_text):
        system_prompt = "You are a helpful assistant. Parse the provided list of recipes and create a single, consolidated grocery list. Categorize the items (e.g., Produce, Protein, Pantry) and combine quantities where possible."
        user_prompt = f"Please generate a grocery list from these recipes:\n\n{recipes_text}"
        return call_openai(system_prompt, user_prompt)

class MealPlanCompilerWorker:
    """
    Takes all the gathered information and compiles a day-by-day meal plan.
    """
    def run(self, dietary_profile, recipes, grocery_list):
        system_prompt = """You are a professional meal planner. Your task is to create a coherent, day-by-day meal plan using the provided recipes.
After the daily plan, append the consolidated grocery list. Structure the entire output clearly with Markdown headings."""
        user_prompt = f"""Please create a {dietary_profile.get('plan_duration')}-day meal plan based on the user's profile: {json.dumps(dietary_profile)}.

--- Suggested Recipes ---
{recipes}

--- Consolidated Grocery List ---
{grocery_list}
"""
        return call_openai(system_prompt, user_prompt)


# --- Orchestrator Agent Class ---

class MealPlanOrchestrator:
    """
    Orchestrator that manages a team of workers to create a personalized meal plan.
    """
    def __init__(self):
        self.profiler = DietaryProfilerWorker()
        self.recipe_finder = RecipeFinderWorker()
        self.grocery_generator = GroceryListGeneratorWorker()
        self.compiler = MealPlanCompilerWorker()
        print("MealPlanOrchestrator initialized with its team of workers.")

    def execute_plan(self, user_request):
        """
        Executes the dynamic, branching plan to generate a meal plan.
        """
        print(f"\nOrchestrator: Received new request: '{user_request}'")
        
        # 1. Initial Analysis - This determines the entire workflow
        print("\n--- Step 1: Profiling User's Dietary Needs ---")
        dietary_profile = self.profiler.run(user_request)
        if "error" in dietary_profile:
            print(f"Orchestrator Error: Could not understand the user request. Aborting. Details: {dietary_profile['error']}")
            return dietary_profile
        print(f"Orchestrator: Profile created successfully: {dietary_profile}")

        # 2. Dynamic Worker Delegation (Branching and Chaining)
        print("\n--- Step 2: Generating Recipes and Grocery List ---")
        
        # Call Recipe Finder based on profile
        print("Orchestrator -> RecipeFinderWorker")
        recipes = self.recipe_finder.run(dietary_profile)
        print("Orchestrator: Got recipe suggestions.")

        # Call Grocery Generator based on the recipes found
        print("Orchestrator -> GroceryListGeneratorWorker")
        grocery_list = self.grocery_generator.run(recipes)
        print("Orchestrator: Generated grocery list.")

        # 3. Synthesis (Final Compilation Step)
        print("\n--- Step 3: Compiling Final Meal Plan ---")
        print("Orchestrator -> MealPlanCompilerWorker")
        final_plan = self.compiler.run(dietary_profile, recipes, grocery_list)
        print("Orchestrator: Plan complete!")
        
        return final_plan


# --- Example Usage ---
if __name__ == "__main__":
    # Example 1
    request = "I need a 3-day meal plan. I'm vegetarian and want high-protein meals to support my workouts."

    # Instantiate and run the orchestrator
    orchestrator = MealPlanOrchestrator()
    final_meal_plan = orchestrator.execute_plan(request)

    # Print the final result
    print("\n" + "="*50)
    print("      YOUR PERSONALIZED MEAL PLAN      ")
    print("="*50 + "\n")
    print(final_meal_plan)

    # --- Second Example for Contrast ---
    print("\n\n" + "#"*60)
    print("### RUNNING A DIFFERENT SCENARIO ###")
    print("#"*60)

    request_2 = "Create a 5-day, low-carb meal plan for one person trying to lose weight. I am allergic to shellfish."
    final_meal_plan_2 = orchestrator.execute_plan(request_2)

    print("\n" + "="*50)
    print("      YOUR PERSONALIZED MEAL PLAN      ")
    print("="*50 + "\n")
    print(final_meal_plan_2)