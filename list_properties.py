import os
from dotenv import load_dotenv
from google.analytics.admin_v1alpha import AnalyticsAdminServiceClient

# Load configuration
load_dotenv()
CREDENTIALS_PATH = "service_account.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH

def list_properties():
    """Lists all GA4 properties the service account can access."""
    client = AnalyticsAdminServiceClient()
    
    print("Checking accessible GA4 properties...")
    try:
        # First, find accessible accounts
        # Note: listing properties directly might require account IDs or searching
        # In GA4 Admin API, we can list account summaries
        summaries = client.list_account_summaries()
        
        found = False
        for summary in summaries:
            print(f"\nAccount: {summary.display_name} ({summary.account})")
            for prop in summary.property_summaries:
                print(f"  -> Property: {prop.display_name} (ID: {prop.property.split('/')[-1]})")
                found = True
        
        if not found:
            print("\nNo properties found. Please double check that you added the service account email to the correct GA4 Property.")
            
    except Exception as e:
        print(f"An error occurred while listing properties: {e}")

if __name__ == "__main__":
    list_properties()
