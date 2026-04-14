import google.generativeai as genai
import os

GEMINI_API_KEY = "AIzaSyBHNjsq3kaGJDnXXj3eP3qKwYoZqja61ok"
genai.configure(api_key=GEMINI_API_KEY)

print("Available models:")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
