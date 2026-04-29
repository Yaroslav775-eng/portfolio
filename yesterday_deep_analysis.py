import os
import json
import datetime
from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension, OrderBy, Filter, FilterExpression
)

import sys

# Ensure UTF-8 output for Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv(r"c:\Users\User\Кейсы\.env")
PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"c:\Users\User\Кейсы\service_account.json"
client = BetaAnalyticsDataClient()

yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
print(f"\n{'='*60}")
print(f"АНАЛІЗ САЙТУ ЗА: {yesterday}")
print(f"{'='*60}\n")

def run(dimensions, metrics, order_metric=None, order_dim=None, desc=True, limit=20):
    order_bys = []
    if order_metric:
        order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_metric), desc=desc)]
    elif order_dim:
        order_bys = [OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name=order_dim), desc=desc)]
    req = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        date_ranges=[DateRange(start_date=yesterday, end_date=yesterday)],
        limit=limit,
        order_bys=order_bys
    )
    return client.run_report(req)

# ─── 1. ЗАГАЛЬНА ЗВЕДЕННЯ ────────────────────────────────────────
print("── 1. ЗАГАЛЬНА ЗВЕДЕННЯ ──")
r = run(["pagePath"], ["activeUsers","sessions","screenPageViews","averageSessionDuration","bounceRate"])
total_users = sum(int(row.metric_values[0].value) for row in r.rows)
total_sessions = sum(int(row.metric_values[1].value) for row in r.rows)
total_views = sum(int(row.metric_values[2].value) for row in r.rows)
print(f"  Користувачі: {total_users}")
print(f"  Сесії:       {total_sessions}")
print(f"  Перегляди:   {total_views}")
print(f"  Сторінок/сесія: {round(total_views/total_sessions,2) if total_sessions else 0}")

# ─── 2. СТОРІНКИ — ЯКУ ЧИТАЛИ НАЙДОВШЕ ───────────────────────────
print("\n── 2. ТОП СТОРІНОК ЗА ПЕРЕГЛЯДАМИ ──")
r = run(
    ["pagePath"],
    ["screenPageViews","activeUsers","averageSessionDuration"],
    order_metric="screenPageViews"
)
for row in r.rows[:8]:
    page = row.dimension_values[0].value
    views = row.metric_values[0].value
    users = row.metric_values[1].value
    dur = round(float(row.metric_values[2].value))
    print(f"  {page:<35} переглядів:{views:>4}  юзерів:{users:>3}  час:{dur:>4}с")

# ─── 3. ДЖЕРЕЛА ТРАФІКУ ──────────────────────────────────────────
print("\n── 3. ДЖЕРЕЛА ТРАФІКУ ──")
r = run(
    ["sessionSource","sessionMedium"],
    ["sessions","activeUsers"],
    order_metric="sessions"
)
for row in r.rows[:10]:
    src = row.dimension_values[0].value
    med = row.dimension_values[1].value
    ses = row.metric_values[0].value
    usr = row.metric_values[1].value
    print(f"  {src}/{med:<25} сесій:{ses:>3}  юзерів:{usr:>3}")

# ─── 4. ПОГОДИННИЙ ПАТЕРН ────────────────────────────────────────
print("\n── 4. ПОГОДИННИЙ ПАТЕРН (скільки юзерів о котрій годині) ──")
r = run(
    ["hour"],
    ["activeUsers","sessions"],
    order_dim="hour", desc=False
)
hourly = {row.dimension_values[0].value: int(row.metric_values[0].value) for row in r.rows}
peak_hour = max(hourly, key=hourly.get) if hourly else "—"
peak_val = hourly.get(peak_hour, 0)
for hour, val in sorted(hourly.items(), key=lambda x: int(x[0])):
    bar = "█" * val
    print(f"  {hour}:00  {bar} ({val})")
print(f"\n  Пік активності: {peak_hour}:00 ({peak_val} юзерів)")

# ─── 5. ПРИСТРОЇ ─────────────────────────────────────────────────
print("\n── 5. ПРИСТРОЇ ──")
r = run(
    ["deviceCategory"],
    ["activeUsers","sessions","bounceRate"],
    order_metric="activeUsers"
)
for row in r.rows:
    dev = row.dimension_values[0].value
    usr = row.metric_values[0].value
    ses = row.metric_values[1].value
    br  = round(float(row.metric_values[2].value)*100, 1)
    print(f"  {dev:<12} юзерів:{usr:>3}  сесій:{ses:>3}  bounce:{br}%")

# ─── 6. ПОДІЇ / КОНВЕРСІЇ ────────────────────────────────────────
print("\n── 6. ПОДІЇ ──")
r = run(
    ["eventName"],
    ["eventCount","activeUsers"],
    order_metric="eventCount"
)
for row in r.rows[:15]:
    ev  = row.dimension_values[0].value
    cnt = row.metric_values[0].value
    usr = row.metric_values[1].value
    print(f"  {ev:<40} кількість:{cnt:>4}  юзерів:{usr:>3}")

# ─── 7. ГЕОГРАФІЯ ────────────────────────────────────────────────
print("\n── 7. ГЕОГРАФІЯ (міста) ──")
r = run(
    ["city","country"],
    ["activeUsers","sessions"],
    order_metric="activeUsers"
)
for row in r.rows[:8]:
    city    = row.dimension_values[0].value
    country = row.dimension_values[1].value
    usr     = row.metric_values[0].value
    ses     = row.metric_values[1].value
    print(f"  {city},{country:<20} юзерів:{usr:>3}  сесій:{ses:>3}")

# ─── 8. МОВА БРАУЗЕРА ────────────────────────────────────────────
print("\n── 8. МОВА БРАУЗЕРА ──")
r = run(
    ["language"],
    ["activeUsers"],
    order_metric="activeUsers"
)
for row in r.rows[:6]:
    lang = row.dimension_values[0].value
    usr  = row.metric_values[0].value
    print(f"  {lang:<15} юзерів:{usr}")

# ─── 9. ШЛЯХИ НАВІГАЦІЇ (перша сторінка → де йдуть) ─────────────
print("\n── 9. ТОЧКИ ВХОДУ (landing pages) ──")
r = run(
    ["landingPage"],
    ["sessions","activeUsers","bounceRate"],
    order_metric="sessions"
)
for row in r.rows[:8]:
    page = row.dimension_values[0].value
    ses  = row.metric_values[0].value
    usr  = row.metric_values[1].value
    br   = round(float(row.metric_values[2].value)*100, 1)
    print(f"  {page:<40} сесій:{ses:>3}  bounce:{br}%")

print(f"\n{'='*60}")
print("АНАЛІЗ ЗАВЕРШЕНО")
print(f"{'='*60}\n")
