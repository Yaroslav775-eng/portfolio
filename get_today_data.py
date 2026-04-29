import os
import datetime
import json
from dotenv import load_dotenv
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

PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
CREDENTIALS_PATH = "service_account.json"

# Initialize Clients
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
analytics_client = BetaAnalyticsDataClient()

def get_raw_data():
    """Fetches raw metrics from GA4 for today."""
    today_str = datetime.date.today().strftime("%Y%m%d")
    print(f"Fetching raw data for {today_str}...")
    
    try:
        request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[
                Dimension(name="pagePath"),
                Dimension(name="sessionSource")
            ],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="screenPageViews"),
                Metric(name="sessions")
            ],
            date_ranges=[DateRange(start_date="today", end_date="today")],
        )
        
        response = analytics_client.run_report(request)
        
        data = []
        for row in response.rows:
            data.append({
                "page": row.dimension_values[0].value,
                "source": row.dimension_values[1].value,
                "users": row.metric_values[0].value,
                "views": row.metric_values[1].value,
                "sessions": row.metric_values[2].value
            })
        
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    raw_data = get_raw_data()
    with open("today_raw_data.json", "w") as f:
        json.dump(raw_data, f, indent=2)
    print("Today's raw data saved to today_raw_data.json")
    print(json.dumps(raw_data, indent=2))
