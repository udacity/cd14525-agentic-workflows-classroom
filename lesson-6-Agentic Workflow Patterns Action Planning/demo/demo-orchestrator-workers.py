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

class UserProfilerWorker:
    """
    Analyzes the user's request to extract key trip parameters.
    """
    def run(self, user_request):
        system_prompt = """You are an expert at parsing user travel requests. Analyze the user's prompt and extract the following details: destination, trip_duration (in days), budget_level ('budget', 'mid-range', 'luxury'), and primary_interests (as a list of strings).
Your response MUST be a valid JSON object with these keys. Do not send anything except for the json output."""
        
        user_prompt = f"User request: '{user_request}'"
        
        try:
            response_text = call_openai(system_prompt, user_prompt)
            print(response_text)
            # 1. Remove potential markdown fences if the LLM ignored the instruction.
            if response_text.strip().startswith("```json"):
                response_text = response_text.strip()[7:-3].strip()

            # 2. Replace non-standard whitespace characters (like non-breaking spaces) with standard spaces.
            cleaned_text = response_text.replace(u'\u00A0', ' ')
            
            return json.loads(response_text)
        except (json.JSONDecodeError, TypeError) as e:
            # Fallback for safety
            return {"error": f"Failed to parse user profile. Details: {e}", "raw_response": response_text}

class ActivityFinderWorker:
    """
    Finds activities tailored to the user's interests and budget.
    """
    def run(self, destination, interests, budget_level):
        system_prompt = "You are a travel agent specializing in finding unique activities. Based on the user's interests and budget, suggest 3-5 relevant activities or attractions."
        user_prompt = f"Find activities in {destination} for someone interested in {', '.join(interests)} with a {budget_level} budget."
        return call_openai(system_prompt, user_prompt)

class RestaurantFinderWorker:
    """
    Finds dining options tailored to the user's budget.
    """
    def run(self, destination, budget_level):
        system_prompt = "You are a food critic who recommends restaurants. Suggest a list of dining options (e.g., specific restaurants, types of food stalls) that fit the user's budget."
        user_prompt = f"Find {budget_level} dining options in {destination}."
        return call_openai(system_prompt, user_prompt)

class ItineraryCompilerWorker:
    """
    Takes all the gathered information and compiles a day-by-day itinerary.
    """
    def run(self, trip_profile, activities, restaurants):
        system_prompt = """You are a meticulous travel planner. Your task is to create a coherent, day-by-day itinerary using the provided list of activities and dining suggestions.
Structure the output clearly with headings for each day. Make logical suggestions for how to group activities."""
        user_prompt = f"""Please create a {trip_profile.get('trip_duration')}-day itinerary for a trip to {trip_profile.get('destination')}.

Use the following suggestions:
--- Activities ---
{activities}

--- Restaurants ---
{restaurants}
"""
        return call_openai(system_prompt, user_prompt)


# --- Orchestrator Agent Class ---

class TravelOrchestrator:
    """
    Orchestrator that manages a team of workers to create a personalized travel itinerary.
    """
    def __init__(self):
        self.profiler = UserProfilerWorker()
        self.activity_finder = ActivityFinderWorker()
        self.restaurant_finder = RestaurantFinderWorker()
        self.compiler = ItineraryCompilerWorker()
        print("TravelOrchestrator initialized with its team of workers.")

    def execute_plan(self, user_request):
        """
        Executes the dynamic, branching plan to generate an itinerary.
        """
        print(f"\nOrchestrator: Received new request: '{user_request}'")
        
        # 1. Initial Analysis - This step determines the entire workflow
        print("\n--- Step 1: Profiling User Request ---")
        trip_profile = self.profiler.run(user_request)
        if "error" in trip_profile:
            print(f"Orchestrator Error: Could not understand the user request. Aborting. Details: {trip_profile['error']}")
            return trip_profile
        print(f"Orchestrator: Profile created successfully: {trip_profile}")

        # 2. Dynamic Worker Delegation (Branching)
        # In a more complex app, these could be parallel API calls.
        print("\n--- Step 2: Gathering Recommendations (Dynamic Dispatch) ---")
        
        # Call Activity Finder based on profile
        print("Orchestrator -> ActivityFinderWorker")
        activities = self.activity_finder.run(
            trip_profile['destination'], 
            trip_profile['primary_interests'], 
            trip_profile['budget_level']
        )
        print("Orchestrator: Got activity suggestions.")

        # Call Restaurant Finder based on profile
        print("Orchestrator -> RestaurantFinderWorker")
        restaurants = self.restaurant_finder.run(
            trip_profile['destination'], 
            trip_profile['budget_level']
        )
        print("Orchestrator: Got restaurant suggestions.")

        # 3. Synthesis (Final Chaining Step)
        print("\n--- Step 3: Compiling Final Itinerary ---")
        print("Orchestrator -> ItineraryCompilerWorker")
        final_itinerary = self.compiler.run(trip_profile, activities, restaurants)
        print("Orchestrator: Plan complete!")
        
        return final_itinerary


# --- Example Usage ---
if __name__ == "__main__":
    # The high-level goal provided by the user
    request = "I want to plan a 3-day budget-friendly trip to Berlin. I'm really into history and street art."

    # Instantiate and run the orchestrator
    orchestrator = TravelOrchestrator()
    final_plan = orchestrator.execute_plan(request)

    # Print the final result
    print("\n" + "="*50)
    print("      YOUR PERSONALIZED TRAVEL ITINERARY      ")
    print("="*50 + "\n")
    print(final_plan)

    # --- Second Example for Contrast ---
    print("\n\n" + "#"*60)
    print("### RUNNING A DIFFERENT SCENARIO ###")
    print("#"*60)

    request_2 = "My partner and I want a 2-day luxury getaway to Paris for our anniversary. We love fine dining and classic art museums."
    final_plan_2 = orchestrator.execute_plan(request_2)

    print("\n" + "="*50)
    print("      YOUR PERSONALIZED TRAVEL ITINERARY      ")
    print("="*50 + "\n")
    print(final_plan_2)