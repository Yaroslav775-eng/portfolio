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

def get_recent_performance_data():
    """Fetches core metrics from GA4 for the last 4 days with daily breakdown."""
    print(f"Fetching data for Property {PROPERTY_ID} (Last 4 Days)...")
    
    try:
        request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[
                Dimension(name="date"),
                Dimension(name="pagePath"),
                Dimension(name="sessionSource")
            ],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="screenPageViews"),
                Metric(name="sessions"),
                Metric(name="averageSessionDuration")
            ],
            date_ranges=[DateRange(start_date="4daysAgo", end_date="today")],
            order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"))]
        )
        
        response = analytics_client.run_report(request)
        
        report_text = "GA4 DATA (Last 4 Days Breakdown):\n"
        if not response.rows:
            report_text += "(No traffic recorded in the last 4 days.)\n"
        else:
            for row in response.rows:
                date = row.dimension_values[0].value
                path = row.dimension_values[1].value
                source = row.dimension_values[2].value
                users = row.metric_values[0].value
                views = row.metric_values[1].value
                sessions = row.metric_values[2].value
                duration = float(row.metric_values[3].value)
                
                report_text += f"[{date}] Source: {source} | Page: {path}\n"
                report_text += f"      Users: {users}, Views: {views}, Sessions: {sessions}, Avg Dur: {duration:.1f}s\n"
    except Exception as e:
        report_text = f"GA4 Error: {e}"
    
    return report_text

def run_gpt_analysis(metrics_data):
    """Analyzes the GA4 data using GPT-4o."""
    print("Generating analysis with GPT-4o...")
    
    prompt = f"""
    You are an Expert Web Analyst and Digital Marketer.
    Below is the Google Analytics 4 (GA4) data for the LAST 4 DAYS for a portfolio website of a Google Ads Specialist.
    
    GA4 DATA:
    {metrics_data}
    
    TASK:
    1. Analyze traffic volume and sources. Is it growing or dropping?
    2. Identify the most active pages and sources of traffic.
    3. Note any unusual patterns or "disasters" (e.g., high traffic with zero engagement, or no traffic at all).
    4. Provide 3 actionable recommendations based on these recent 4-day trends.
    5. Compare (if data allows) with the fact that the user mentioned a "disaster" or "layout issues" recently.
    
    Format the output as a professional Markdown report in Russian.
    """
    
    response = ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional web analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if not PROPERTY_ID or not OPENAI_API_KEY:
        print("Error: Missing credentials in .env")
    else:
        data = get_recent_performance_data()
        print("\nData fetched successfully. Sending to GPT...")
        analysis = run_gpt_analysis(data)
        
        # Save to file
        filename = f"recent_analysis_{datetime.date.today()}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(analysis)
        
        print(f"\nAnalysis complete! Report saved to {filename}")
        print("\n" + "="*50 + "\n")
        print(analysis)
