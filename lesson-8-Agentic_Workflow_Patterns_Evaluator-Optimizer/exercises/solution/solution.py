import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# Maximum number of recipe optimization attempts
MAX_RETRIES = 6

# Recipe constraints - this complex set of requirements will require multiple iterations
recipe_request = """
Create a dinner recipe with the following requirements:
- Must be high in protein (at least 30g per serving)
- Must be low in carbohydrates (under 15g per serving)
- Cannot contain gluten, dairy, or nuts (severe allergies)
- Must be suitable for someone with diabetes (low glycemic index)
- Should have no more than 8 ingredients
- Must be flavorful and appealing to someone who normally eats a standard American diet
- Total preparation and cooking time should be under 30 minutes
- Should contain at least 3 different vegetables
- Must include a source of omega-3 fatty acids
"""

class RecipeCreatorAgent:
    """Agent that creates and modifies recipes based on constraints."""
    def create_recipe(self, recipe_request, feedback=None):
        """Generate a recipe meeting the specified requirements, incorporating feedback if available."""
        system_message = """You are a creative chef known for generating innovative dishes.
        Prioritize flavor and general appeal. Follow dietary guidelines, but you can be flexible unless told otherwise.
        Experiment with different flavors, styles, try fusion of different places, each time you are asked it must be something new, 
        follow the instructions but be flexible to invent something new, never seen before.
        Try foods that are slightly outside the guilines given, experiment, try something bold, don't be affraid to break the rules."""

        # ✨ Force a more relaxed initial generation to induce errors
        if feedback is None:
            user_prompt = f"""Recipe Request: {recipe_request}
            
            Create an exciting, flavorful recipe inspired by comfort food classics.
            Do your best to follow the dietary guidelines, but prioritize creativity and taste first."""
            print("\n👨‍🍳 Creating initial recipe (flexible interpretation)...")
        else:
            # 🧠 Once feedback is received, become strict about rules
            system_message = """You are an expert chef specializing in creating recipes that follow strict dietary constraints.
            You must correct previous issues and follow all requirements with precision."""
            
            user_prompt = f"""Recipe Request: {recipe_request}
            
            Your previous recipe had the following issues:
            {feedback}
            
            Please create a revised recipe addressing these specific issues.
            Be precise and ensure all constraints are satisfied."""
            print("\n🔄 Generating revised recipe based on feedback...")

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            temperature=1  # Higher for more creativity
        )
        return response.choices[0].message.content

class NutritionEvaluatorAgent:
    """Agent that evaluates recipes for nutritional content and constraint compliance."""
    def evaluate(self, recipe_request, proposed_recipe):
        """Check if the proposed recipe meets all specified constraints and requirements."""
        print("\n🔍 Evaluating recipe for nutritional content and constraints...")

        system_message = """You are a strict dietitian. Your job is to find ANY and ALL violations of dietary constraints.
        Do not accept approximations. Be meticulous and provide corrective feedback."""

        user_prompt = f"""Recipe Request: {recipe_request}
        
        Proposed Recipe:
        {proposed_recipe}
        
        Please evaluate this recipe against ALL the specified requirements.
        Check EACH constraint individually and confirm whether it is satisfied:
        
        1. Is the protein content at least 30g per serving?
        2. Is the carbohydrate content under 15g per serving?
        3. Does it contain ANY gluten, dairy, or nuts (even trace amounts)?
        4. Is it suitable for someone with diabetes (low glycemic index foods)?
        5. Does it have no more than 8 ingredients?
        6. Would it be flavorful and appealing to someone used to standard American diet?
        7. Is total preparation and cooking time under 30 minutes?
        8. Does it contain at least 3 different vegetables?
        9. Does it include a source of omega-3 fatty acids?
        
        If ALL constraints are fully satisfied, begin your response with "APPROVED: This recipe meets all requirements."
        
        Otherwise, list specifically which requirements are NOT met and provide detailed suggestions for how to modify 
        the recipe to meet those requirements while maintaining the integrity of the dish."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content

def optimize_recipe(recipe_request):
    """Attempt to create a recipe meeting all constraints, using an optimization loop if needed."""
    creator = RecipeCreatorAgent()
    evaluator = NutritionEvaluatorAgent()

    recipe = None
    feedback = None
    attempts = 0

    for attempt in range(MAX_RETRIES):
        attempts += 1
        print(f"\n--- Attempt #{attempts} ---")

        recipe = creator.create_recipe(recipe_request, feedback)
        evaluation = evaluator.evaluate(recipe_request, recipe)

        print(f"\n📋 Evaluation Result:")
        print(evaluation[:200] + "..." if len(evaluation) > 200 else evaluation)

        if evaluation.lower().startswith("approved"):
            print("\n✅ All dietary constraints satisfied!")
            break
        else:
            feedback = evaluation
            print(f"\n⚠️ Some constraints not met. Optimizing recipe...")

    return recipe, evaluation, attempts

if __name__ == "__main__":
    print("Recipe Optimizer for Dietary Restrictions")
    print("\nRecipe Request:")
    print(recipe_request)
    print("\nCreating optimized recipe...")

    recipe, evaluation, attempts = optimize_recipe(recipe_request)

    print(f"\nAttempts: {attempts}")
    if "APPROVED" in evaluation:
        print("\n✅ All dietary constraints satisfied!")
    else:
        print("\n⚠️ Could not satisfy all constraints after maximum retries.")

    print("\nFinal Recipe:")
    print(recipe)

    print("\nEvaluation:")
    print(evaluation)
