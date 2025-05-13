# Exercise: Building a Recipe Optimizer for Dietary Restrictions

## Exercise Overview
In this exercise, you’ll build an agentic workflow system that uses an optimization loop to iteratively improve a recipe until it satisfies multiple dietary constraints, nutritional goals, and taste expectations.

You will define and orchestrate two agents:

**RecipeCreatorAgent:** Generates or updates recipes to meet given constraints.

**NutritionEvaluatorAgent:** Evaluates recipes for compliance with dietary, nutritional, and taste requirements.

The system runs an optimization loop where it continues to improve the recipe using evaluator feedback until either:

All constraints are met, or

A maximum number of retries (MAX_RETRIES) is reached.

## Your Task

Implement the following components:

### RecipeCreatorAgent (class)
Method: create_recipe(recipe_request, feedback=None)

**Responsibilities:**

Generate or revise a recipe based on the user request.

If feedback is provided, incorporate changes accordingly.

Format output with ingredients, instructions, estimated nutrition, and taste description.

### NutritionEvaluatorAgent (class)
Method: evaluate(recipe, constraints)

**Responsibilities:**

Assess whether the recipe satisfies each constraint.

Provide a report with:

pass/fail for each constraint

Comments or suggestions for unmet constraints

A taste rating from 1–10

### optimize_recipe() (function)
Responsibilities:

Manage the optimization loop.

Use the agents to alternate between creation and evaluation.

Stop if the recipe meets all constraints or MAX_RETRIES is reached.

Return final recipe and constraint status.

## Sample Workflow Behavior

Attempt 1:
- Recipe: Chickpea pasta with coconut cream and tofu
- Feedback: Good Contains coconut, Bad Vegan, Bad High calorie, Good High protein, Good Taste

Attempt 2:
- Recipe: Chickpea pasta with cashew cream and seitan
- Feedback: Good All constraints met
- Final taste rating: 8/10

## Student Assignment

You must implement:

RecipeCreatorAgent

Prompt the model to creatively solve conflicting dietary goals.

Update recipes based on detailed feedback.

NutritionEvaluatorAgent

Design structured evaluation logic for nutritional and taste constraints.

Provide interpretable feedback.

optimize_recipe()

Coordinate the loop using both agents.

Log progress and track attempts.

## Success Criteria
Correctness: Final recipe satisfies all constraints.

Iteration: At least one failed attempt before success.

Creativity: Recipes change meaningfully between iterations.

Robust Prompts: Agents use prompts that reflect their specialized roles.