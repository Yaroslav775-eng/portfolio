"""
Site Intelligence Agent
=======================
Crawls the portfolio site, merges page-level data with GA4 behavioral signals,
then asks GPT-4o to generate prioritized improvement proposals.

Run:  python site_agent.py
"""

import os
import time
import datetime
import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension
)

load_dotenv()

# ─── CONFIG ────────────────────────────────────────────────────────────────
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
PROPERTY_ID     = os.getenv("GA4_PROPERTY_ID")
CREDENTIALS_PATH = "service_account.json"

SITE_URLS = [
    "https://yaroslav775-eng.github.io/portfolio/index.html",
    "https://yaroslav775-eng.github.io/portfolio/ua.html",
    "https://yaroslav775-eng.github.io/portfolio/cv_eng.html",
    "https://yaroslav775-eng.github.io/portfolio/cv_ua.html",
]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
ga_client = BetaAnalyticsDataClient()
ai_client = OpenAI(api_key=OPENAI_API_KEY)

# ─── STEP 1: CRAWL PAGES ───────────────────────────────────────────────────
def crawl_page(url: str) -> dict:
    """Fetches a page and extracts structural signals."""
    try:
        start = time.time()
        resp = requests.get(url, timeout=15, headers={"User-Agent": "SiteAgent/1.0"})
        load_time = round(time.time() - start, 2)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Extract key signals
        title = soup.title.string.strip() if soup.title else "MISSING"
        h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
        meta_desc = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            meta_desc = meta.get("content", "")

        # CTA buttons
        ctas = [a.get_text(strip=True) for a in soup.find_all("a", class_=lambda c: c and "btn" in c)]

        # Word count (approximate)
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())

        # Mobile viewport meta
        viewport = soup.find("meta", attrs={"name": "viewport"})
        has_viewport = bool(viewport)

        # Images without alt
        imgs_no_alt = [str(img) for img in soup.find_all("img") if not img.get("alt")]

        # OG tags
        og_title = soup.find("meta", property="og:title")
        has_og = bool(og_title)

        # Forms
        forms = soup.find_all("form")
        
        # Canonical
        canonical = soup.find("link", rel="canonical")
        canonical_url = canonical.get("href", "") if canonical else "MISSING"

        return {
            "url": url,
            "status_code": resp.status_code,
            "load_time_s": load_time,
            "title": title,
            "h1s": h1s,
            "meta_description": meta_desc[:200] if meta_desc else "MISSING",
            "word_count": word_count,
            "has_viewport_meta": has_viewport,
            "has_og_tags": has_og,
            "canonical": canonical_url,
            "cta_buttons": ctas[:10],
            "images_missing_alt": len(imgs_no_alt),
            "form_count": len(forms),
            "error": None,
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


# ─── STEP 2: GA4 BEHAVIORAL DATA ───────────────────────────────────────────
def get_ga4_data(days: int = 7) -> dict:
    """Returns per-page behavioral metrics from GA4."""
    try:
        resp = ga_client.run_report(RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name="pagePath"), Dimension(name="sessionSource")],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="sessions"),
                Metric(name="screenPageViews"),
                Metric(name="averageSessionDuration"),
                Metric(name="bounceRate"),
            ],
            date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="today")],
        ))

        # Build lookup: pagePath → aggregated metrics
        pages = {}
        for row in resp.rows:
            path   = row.dimension_values[0].value
            source = row.dimension_values[1].value
            users  = int(row.metric_values[0].value)
            sess   = int(row.metric_values[1].value)
            views  = int(row.metric_values[2].value)
            dur    = float(row.metric_values[3].value)
            bounce = float(row.metric_values[4].value)

            if path not in pages:
                pages[path] = {"users": 0, "sessions": 0, "views": 0,
                               "avg_duration_s": 0, "bounce_rate": 0,
                               "sources": []}
            p = pages[path]
            p["users"]       += users
            p["sessions"]    += sess
            p["views"]       += views
            p["avg_duration_s"] = round((p["avg_duration_s"] + dur) / 2, 1)
            p["bounce_rate"] = round((p["bounce_rate"] + bounce) / 2, 3)
            if source not in p["sources"]:
                p["sources"].append(source)

        return pages
    except Exception as e:
        return {"error": str(e)}


# ─── STEP 3: MERGE CRAWL + GA4 ─────────────────────────────────────────────
def merge_signals(crawl_data: list, ga4_data: dict) -> list:
    """Attaches GA4 metrics to each crawled page."""
    merged = []
    for page in crawl_data:
        url = page.get("url", "")
        # GA4 paths strip the domain, e.g. /portfolio/ua.html
        path_candidates = [
            "/" + url.split("github.io/")[-1],
            url.split("github.io")[-1],
        ]
        ga = {}
        for path in path_candidates:
            if path in ga4_data:
                ga = ga4_data[path]
                break

        page["ga4"] = ga or {
            "users": 0, "sessions": 0, "views": 0,
            "avg_duration_s": 0, "bounce_rate": 0, "sources": [],
            "note": "No GA4 data matched — page may be new or untracked"
        }
        merged.append(page)
    return merged


# ─── STEP 4: GPT-4o ANALYSIS ───────────────────────────────────────────────
def analyze_with_gpt(merged: list) -> str:
    """Feeds merged signals to GPT-4o for prioritized recommendations."""
    payload = json.dumps(merged, ensure_ascii=False, indent=2)

    prompt = f"""
You are an expert Web Analyst, UX Researcher, and SEO Specialist.
Below is a JSON report combining:
- Crawl data (title, H1s, meta description, load time, CTAs, alt-text issues, etc.)
- GA4 behavioral data (users, sessions, views, bounce rate, avg session duration, traffic sources)

SITE DATA:
{payload}

TASK:
Analyze each page and produce a structured improvement report in Russian.

For EACH page:
1. Give an overall score out of 10 (UX + SEO + Conversion combined)
2. List TOP 3 specific issues found (e.g. "Bounce rate 72% on mobile source — CTA below the fold")
3. Give 1-2 concrete fixes with exact text or code changes where possible
4. Flag CRITICAL issues (broken, missing, or hurting conversions)

Then provide:
5. A site-wide priority list: top 5 actions ranked by impact (High/Medium/Low)
6. A "Quick Wins" section: changes that take < 30 minutes

Format: Professional Markdown report. Be specific, not generic.
"""

    resp = ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional web analyst and CRO expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
    )
    return resp.choices[0].message.content


# ─── MAIN ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    today = datetime.date.today()
    print("=" * 60)
    print(f"  Site Intelligence Agent — {today}")
    print("=" * 60)

    # Step 1: Crawl
    print("\n[1/4] Crawling pages...")
    crawl_results = []
    for url in SITE_URLS:
        print(f"  → {url}")
        result = crawl_page(url)
        crawl_results.append(result)
        print(f"     Status: {result.get('status_code')} | "
              f"Load: {result.get('load_time_s')}s | "
              f"Words: {result.get('word_count')}")

    # Step 2: GA4
    print("\n[2/4] Fetching GA4 data (last 7 days)...")
    ga4 = get_ga4_data(days=7)
    if "error" in ga4:
        print(f"  GA4 Error: {ga4['error']}")
    else:
        print(f"  Got data for {len(ga4)} page paths")

    # Step 3: Merge
    print("\n[3/4] Merging signals...")
    merged = merge_signals(crawl_results, ga4)

    # Save raw data
    raw_file = f"site_intelligence_raw_{today}.json"
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f"  Raw data saved to: {raw_file}")

    # Step 4: AI Analysis
    print("\n[4/4] Generating AI recommendations (GPT-4o)...")
    report = analyze_with_gpt(merged)

    report_file = f"site_intelligence_report_{today}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# Site Intelligence Report — {today}\n\n")
        f.write(report)

    print(f"\n✅ Done! Report saved to: {report_file}")
    print("\n" + "=" * 60)
    print(report)
