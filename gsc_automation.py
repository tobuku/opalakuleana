"""
Google Search Console Automation
Site: opalakuleana.com
Credentials: shared .gsc-credentials from towing repo

USAGE EXAMPLES:
  python gsc_automation.py                        # top queries (default)
  python gsc_automation.py --report queries       # top queries
  python gsc_automation.py --report pages         # top pages
  python gsc_automation.py --report summary       # overall stats
  python gsc_automation.py --report all           # run all reports
  python gsc_automation.py --days 7               # change date range (default: 28)
  python gsc_automation.py --report queries --days 90 --limit 25
"""

import argparse
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

# --- Config ---
KEY_FILE     = r"C:\Users\HDNG_HelpDesk\Documents\GitHub\towing\.gsc-credentials\laptoplane-blogspot-autoposter-c7da82883623.json"
PROPERTY_URL = "sc-domain:opalakuleana.com"
SCOPES       = ["https://www.googleapis.com/auth/webmasters",
                "https://www.googleapis.com/auth/webmasters.readonly"]


def get_service():
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    return build("searchconsole", "v1", credentials=creds)


def date_range(days):
    end   = date.today() - timedelta(days=3)
    start = end - timedelta(days=days)
    return str(start), str(end)


def query_gsc(service, dimensions, days, limit):
    start, end = date_range(days)
    body = {
        "startDate":  start,
        "endDate":    end,
        "dimensions": dimensions,
        "rowLimit":   limit,
        "orderBy":    [{"fieldName": "impressions", "sortOrder": "DESCENDING"}]
    }
    response = service.searchanalytics().query(siteUrl=PROPERTY_URL, body=body).execute()
    return response.get("rows", []), start, end


def report_summary(service, days, limit):
    rows, start, end = query_gsc(service, ["date"], days, 90)
    if not rows:
        print("No data available for this period.")
        return
    total_clicks      = sum(r["clicks"]      for r in rows)
    total_impressions = sum(r["impressions"] for r in rows)
    avg_ctr           = (total_clicks / total_impressions * 100) if total_impressions else 0
    avg_position      = sum(r["position"] for r in rows) / len(rows) if rows else 0
    print(f"\n{'='*50}")
    print(f"  SUMMARY  |  {start} to {end}")
    print(f"{'='*50}")
    print(f"  Total Clicks      : {total_clicks:,}")
    print(f"  Total Impressions : {total_impressions:,}")
    print(f"  Avg CTR           : {avg_ctr:.2f}%")
    print(f"  Avg Position      : {avg_position:.1f}")
    print(f"{'='*50}\n")


def report_queries(service, days, limit):
    rows, start, end = query_gsc(service, ["query"], days, limit)
    if not rows:
        print("No query data available.")
        return
    print(f"\nTop {len(rows)} Queries  |  {start} to {end}\n")
    print(f"{'#':<4} {'Query':<42} {'Clicks':>7} {'Impr':>8} {'CTR':>7} {'Pos':>8}")
    print("-" * 80)
    for i, row in enumerate(rows, 1):
        q = row["keys"][0][:41]
        print(f"{i:<4} {q:<42} {row['clicks']:>7.0f} {row['impressions']:>8.0f} "
              f"{row['ctr']:>6.1%} {row['position']:>8.1f}")
    print()


def report_pages(service, days, limit):
    rows, start, end = query_gsc(service, ["page"], days, limit)
    if not rows:
        print("No page data available.")
        return
    print(f"\nTop {len(rows)} Pages  |  {start} to {end}\n")
    print(f"{'#':<4} {'Page':<55} {'Clicks':>7} {'Impr':>8} {'CTR':>7} {'Pos':>8}")
    print("-" * 87)
    for i, row in enumerate(rows, 1):
        page = row["keys"][0].replace("https://opalakuleana.com", "")[:54] or "/"
        print(f"{i:<4} {page:<55} {row['clicks']:>7.0f} {row['impressions']:>8.0f} "
              f"{row['ctr']:>6.1%} {row['position']:>8.1f}")
    print()


def submit_urls(service, urls):
    """Submit URLs for inspection/indexing via the URL Inspection API."""
    print(f"\nSubmitting {len(urls)} URLs for indexing inspection...\n")
    print(f"{'#':<4} {'URL':<55} {'Status'}")
    print("-" * 80)
    for i, url in enumerate(urls, 1):
        try:
            result = service.urlInspection().index().inspect(
                body={
                    "inspectionUrl": url,
                    "siteUrl": PROPERTY_URL
                }
            ).execute()
            verdict = result.get("inspectionResult", {}).get("indexStatusResult", {})
            coverage = verdict.get("coverageState", "UNKNOWN")
            crawled  = verdict.get("lastCrawlTime", "never")
            indexing = verdict.get("indexingState", "UNKNOWN")
            short_url = url.replace("https://opalakuleana.com", "")
            print(f"{i:<4} {short_url:<55} {coverage}")
            if crawled != "never":
                print(f"     Last crawled: {crawled}")
            print(f"     Indexing state: {indexing}")
        except Exception as e:
            short_url = url.replace("https://opalakuleana.com", "")
            print(f"{i:<4} {short_url:<55} ERROR: {e}")
    print()


def main():
    parser = argparse.ArgumentParser(description="GSC Automation - opalakuleana.com")
    parser.add_argument("--report", choices=["queries", "pages", "summary", "all"],
                        default="queries", help="Report type (default: queries)")
    parser.add_argument("--days",  type=int, default=28,
                        help="Number of days to look back (default: 28)")
    parser.add_argument("--limit", type=int, default=10,
                        help="Max rows to return (default: 10)")
    parser.add_argument("--submit", nargs="*", metavar="URL",
                        help="Submit URLs for indexing inspection. No args = submit new service pages.")
    args = parser.parse_args()

    print(f"Connecting to GSC for {PROPERTY_URL}...")
    service = get_service()
    print("Connected.\n")

    if args.submit is not None:
        if args.submit:
            urls = args.submit
        else:
            urls = [
                "https://opalakuleana.com/furniture-removal-oahu/",
                "https://opalakuleana.com/appliance-removal-oahu/",
                "https://opalakuleana.com/ewaste-electronics-removal-oahu/",
                "https://opalakuleana.com/construction-debris-removal-oahu/",
                "https://opalakuleana.com/estate-cleanout-oahu/",
                "https://opalakuleana.com/yard-waste-removal-oahu/",
                "https://opalakuleana.com/hot-tub-removal-oahu/",
                "https://opalakuleana.com/commercial-cleanout-oahu/",
                "https://opalakuleana.com/mattress-removal-oahu/",
                "https://opalakuleana.com/storage-unit-cleanout-oahu/",
            ]
        submit_urls(service, urls)
        return

    if args.report == "all":
        report_summary(service, args.days, args.limit)
        report_queries(service, args.days, args.limit)
        report_pages(service, args.days, args.limit)
    elif args.report == "summary":
        report_summary(service, args.days, args.limit)
    elif args.report == "pages":
        report_pages(service, args.days, args.limit)
    else:
        report_queries(service, args.days, args.limit)


if __name__ == "__main__":
    main()
