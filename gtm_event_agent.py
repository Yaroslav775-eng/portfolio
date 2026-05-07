import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# Load configuration
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ai_client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_html_for_events(html_content, url=""):
    """
    Analyzes HTML content to identify key elements for GA4 tracking via GTM.
    """
    print("Agent is analyzing HTML structure...")
    
    prompt = f"""
    You are a Senior Web Analytics Engineer and GTM Expert.
    Your task is to identify key user interaction points on a webpage for GA4 event tracking.
    
    WEBPAGE URL: {url}
    
    HTML CONTENT (excerpt):
    {html_content[:4000]}
    
    TASK:
    1. Identify the most important conversion elements (Forms, Main CTAs, Phone links, Email links).
    2. For each element, provide:
       - Suggested GA4 Event Name (e.g., generate_lead, click_contact_phone).
       - Recommended GTM Trigger Type (e.g., Form Submission, All Elements Click).
       - Precise CSS Selector or ID to use in GTM.
       - Recommended Event Parameters (e.g., link_url, form_id).
    
    3. Generate a "GTM Implementation Plan" in Markdown.
    4. Provide a JSON-like summary that could be used for automated setup.
    
    Format output as a professional technical report.
    """
    
    response = ai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional GTM & GA4 implementation agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="GTM/GA4 Event Setup Agent")
    parser.add_argument("--file", help="Path to HTML file to analyze")
    parser.add_argument("--url", help="URL of the page (for context)", default="")
    
    args = parser.parse_args()
    
    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found in .env")
        return

    content = ""
    if args.file:
        if os.path.exists(args.file):
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            print(f"Error: File {args.file} not found.")
            return
    else:
        # Default to index.html if no file provided
        if os.path.exists("index.html"):
            with open("index.html", "r", encoding="utf-8") as f:
                content = f.read()
        else:
            print("Error: No input file provided and index.html not found.")
            return

    report = analyze_html_for_events(content, args.url)
    
    # Save the report
    output_file = "gtm_setup_report.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\nSuccess! GTM Setup Plan generated: {output_file}")
    print("-" * 30)
    print(report)

if __name__ == "__main__":
    main()
