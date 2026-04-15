import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

try:
    print("Listing models available for this API key using google-genai SDK:")
    for model in client.models.list():
        # Printing the whole model object to see attributes
        print(f"- Name: {model.name}")
except Exception as e:
    print(f"Error listing models: {e}")
