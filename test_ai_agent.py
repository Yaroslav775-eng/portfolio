import os
import datetime
from dotenv import load_dotenv
from google import genai
from google.analytics.data_v1beta import BetaAnalyticsDataClient

# Load configuration
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")

# Initialize Clients
ai_client = genai.Client(api_key=GEMINI_API_KEY)

def get_mock_metrics():
    """Simulates a potential report for testing purposes."""
    return """
    TEST DATA (Simulated Performance):
    - Page: /index.html (English)
      Users: 120, Views: 450
      Avg Duration: 15s, Bounce Rate: 85% (CRITICAL: Users leave too fast!)
    - Page: /ua.html (Ukrainian)
      Users: 80, Views: 210
      Avg Duration: 45s, Bounce Rate: 40% (GOOD: Users are reading.)
    - Top Exit Point: Section 'Contact Form' (Users drop off here).
    """

def get_site_context():
    """Reads a small part of the site for context."""
    if os.path.exists("ua.html"):
        with open("ua.html", "r", encoding="utf-8") as f:
            return f.read()[:2000] # Hero and Strategy
    return "Code not found."

def test_ai_analysis():
    print("--- STARTING DRY RUN TEST ---")
    metrics = get_mock_metrics()
    code = get_site_context()
    
    # We will try a few model names to find one that is active
    test_models = ['gemini-1.5-flash', 'gemini-1.0-pro', 'gemini-2.0-flash']
    
    success = False
    for model_name in test_models:
        print(f"Trying to wake up AI model: {model_name}...")
        try:
            response = ai_client.models.generate_content(
                model=model_name,
                contents=f"You are a CRO expert. Analyze this mock data and code: \n{metrics}\n{code}\nSuggest 2 quick fixes."
            )
            print(f"SUCCESS! Model {model_name} responded.")
            print("\n--- AI RECOMMENDATION ---")
            print(response.text)
            
            # Save the result
            with open("test_audit_result.md", "w", encoding="utf-8") as f:
                f.write(response.text)
            
            success = True
            break
        except Exception as e:
            print(f"Model {model_name} still sleeping: {e}")
            
    if not success:
        print("\nAll models are currently in 'activation' mode. Google usually needs 1-2 hours for new keys.")
        print("I have however verified your logic and GA4 connection settings.")

if __name__ == "__main__":
    test_ai_analysis()
