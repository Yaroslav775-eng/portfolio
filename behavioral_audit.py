import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Metric,
    Dimension,
    OrderBy
)

# Load configuration
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
CREDENTIALS_PATH = "service_account.json"

# Initialize Clients
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
analytics_client = BetaAnalyticsDataClient()
ai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_behavioral_signals():
    """Fetches behavior-related metrics and events from GA4."""
    print(f"Fetching behavioral signals for Property {PROPERTY_ID}...")
    
    try:
        # 1. Page-level behavior
        page_request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[
                Dimension(name="pagePath"),
                Dimension(name="sessionSource")
            ],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="screenPageViews"),
                Metric(name="averageSessionDuration"),
                Metric(name="bounceRate")
            ],
            date_ranges=[DateRange(start_date="2daysAgo", end_date="today")],
        )
        
        # 2. Event-level behavior (Micro-conversions)
        event_request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name="eventName")],
            metrics=[Metric(name="eventCount")],
            date_ranges=[DateRange(start_date="2daysAgo", end_date="today")],
        )
        
        page_response = analytics_client.run_report(page_request)
        event_response = analytics_client.run_report(event_request)
        
        report_text = "--- BEHAVIORAL DATA (Last 2 Days) ---\n\n"
        
        report_text += "PAGE ACTIVITY:\n"
        for row in page_response.rows:
            path = row.dimension_values[0].value
            source = row.dimension_values[1].value
            users = row.metric_values[0].value
            views = row.metric_values[1].value
            duration = float(row.metric_values[2].value)
            bounce = float(row.metric_values[3].value)
            report_text += f"- Page: {path} | Source: {source}\n"
            report_text += f"  Users: {users}, Views: {views}, Avg Duration: {duration:.1f}s, Bounce: {bounce:.1%}\n"
            
        report_text += "\nEVENT SIGNALS (Micro-conversions):\n"
        for row in event_response.rows:
            name = row.dimension_values[0].value
            count = row.metric_values[0].value
            report_text += f"- Event: {name} | Count: {count}\n"
            
    except Exception as e:
        report_text = f"GA4 Error: {e}"
    
    return report_text

def run_behavioral_analysis(signals):
    """Analyzes the signals using GPT-4o."""
    print("Analyzing behavioral patterns with GPT-4o...")
    
    prompt = f"""
    You are a Senior UX Researcher and Digital Marketing Analyst.
    I have collected behavioral signals from Google Analytics 4 for a portfolio website.
    We recently added micro-conversion tracking (start_quiz, submit_brief_success, view_case_study, etc.) and fixed mobile layout issues.
    
    BEHAVIORAL SIGNALS:
    {signals}
    
    TASK:
    1. Interpret the "signals". What do these metrics say about user intent?
    2. Analyze the "Friction vs. Interest" balance. Are users getting stuck or are they genuinely engaged?
    3. Look for the "Golden Path": Do users from specific sources (like robota.ua or direct) follow the intended conversion funnel?
    4. Provide 3 specific UX or Content recommendations to increase the quality of leads.
    5. Evaluate the success of recent changes (if events like 'open_calculator' or 'view_case_study' are appearing).
    
    Format the output as a professional strategic report in Russian.
    """
    
    response = ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional behavioral analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    signals = get_behavioral_signals()
    analysis = run_behavioral_analysis(signals)
    
    # Save to file
    filename = f"behavioral_audit_{datetime.date.today()}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(analysis)
    
    print(f"\nAudit complete! Report saved to {filename}")
    print("\n" + "="*50 + "\n")
    print(analysis)
