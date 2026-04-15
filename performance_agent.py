import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Metric,
    Dimension
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

def get_performance_data():
    """Fetches core metrics from GA4 for the last 30 days."""
    print(f"Fetching data for Property {PROPERTY_ID}...")
    
    try:
        request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name="pagePath")],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="screenPageViews"),
                Metric(name="averageSessionDuration"),
                Metric(name="bounceRate")
            ],
            date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        )
        
        response = analytics_client.run_report(request)
        
        report_text = "GA4 DATA (Last 30 Days):\n"
        if not response.rows:
            report_text += "(No historical data yet. The tag was recently installed. Analyzing code structure instead.)\n"
            
        for row in response.rows:
            path = row.dimension_values[0].value
            users = row.metric_values[0].value
            views = row.metric_values[1].value
            duration = float(row.metric_values[2].value)
            bounce = float(row.metric_values[3].value)
            
            report_text += f"- Page: {path}\n"
            report_text += f"  Users: {users}, Views: {views}\n"
            report_text += f"  Avg Duration: {duration:.1f}s, Bounce Rate: {bounce:.2%}\n"
    except Exception as e:
        report_text = f"GA4 Error: {e}\nAnalyzing site structure fallback mode."
    
    return report_text

def get_site_content():
    """Reads the main portfolio files for context."""
    content = ""
    for filename in ["index.html", "ua.html"]:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                content += f"\n--- FILE: {filename} ---\n"
                content += "".join(lines[:400]) # Increased context for GPT
    return content

def run_ai_audit(metrics, code):
    """Feeds data to OpenAI to get actionable recommendations."""
    print("Analyzing data with OpenAI (GPT-4o-mini)...")
    
    prompt = f"""
    You are a Senior PPC Specialist and Conversion Rate Optimization (CRO) Expert.
    My site is a portfolio for a Google Ads Specialist.
    Goal: High-quality B2B/E-commerce leads.
    
    SITE PERFORMANCE DATA:
    {metrics}
    
    SITE CONTENT (excerpt):
    {code}
    
    TASK:
    1. Acknowledge the current data status (if empty, focus on UI/UX).
    2. Suggest 3 specific marketing/text improvements to the hero sections or grid based on the current code.
    3. Verify if the 'Read Strategy' red highlights we just added are prominent enough.
    4. Provide strategic advice for scaling this portfolio.
    
    Format output as a professional Markdown report.
    """
    
    response = ai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional marketing auditor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    try:
        if not PROPERTY_ID or not OPENAI_API_KEY:
            print("Error: Please check GA4_PROPERTY_ID and OPENAI_API_KEY in .env.")
        else:
            metrics = get_performance_data()
            code = get_site_content()
            report = run_ai_audit(metrics, code)
            
            # Save the report
            today = datetime.date.today()
            report_name = f"ai_audit_report_{today}.md"
            with open(report_name, "w", encoding="utf-8") as f:
                f.write(report)
            
            print(f"\nSuccess! GPT-powered Audit report generated: {report_name}")
            print("-" * 30)
            print(report)
            
    except Exception as e:
        print(f"An error occurred: {e}")
