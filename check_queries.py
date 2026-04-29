import os
import sys
import datetime
from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv(r"c:\Users\User\Кейсы\.env")
PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"c:\Users\User\Кейсы\service_account.json"

client = BetaAnalyticsDataClient()
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

print(f"Checking queries for {yesterday}...")

def get_report(dim_name):
    try:
        req = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name=dim_name), Dimension(name="sessionSource")],
            metrics=[Metric(name="sessions")],
            date_ranges=[DateRange(start_date=yesterday, end_date=yesterday)]
        )
        return client.run_report(req)
    except Exception as e:
        print(f"Error for {dim_name}: {e}")
        return None

# Try different dimensions for more context
dims = ["pageReferrer", "pageTitle", "landingPage"]

for d in dims:
    print(f"\n--- Dimension: {d} ---")
    res = get_report(d)
    if res and res.rows:
        for row in res.rows:
            q = row.dimension_values[0].value
            src = row.dimension_values[1].value
            cnt = row.metric_values[0].value
            print(f"  Value: '{q}' | Source: {src} | Sessions: {cnt}")
    else:
        print("  No data captured.")
