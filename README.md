# google-trend-for-python

Sample code for the [Google Trends for Python 2026](https://hobbyworker.me/en/series/google-trends-for-python-2026/) series on hobbyworker.me. The scripts use [pytrends](https://pypi.org/project/pytrends/), an unofficial Google Trends API for Python, and the Google Trends RSS feed.

## Versions

| Tag | Series |
|---|---|
| `v2026` | Google Trends for Python 2026 (October 2026) |
| [`v2023`](https://github.com/hobbyworker/google-trend-for-python/tree/v2023) | Google Trends for Python (March–April 2023). The README at that tag lists which of its scripts still work. |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python 01_basic_search.py
```

All scripts share the settings in `common.py`. Charts are saved as PNG files in the current directory.

## Scripts

| Part | Script | Topic |
|---|---|---|
| 1 | `01_basic_search.py` | [Setting up pytrends and running a basic search](https://hobbyworker.me/en/dev/2026-10-06-google-trends-for-python-2026-1-setup-and-basic-search/) |
| 2 | `02_interest_over_time.py` | [Analyzing interest over time](https://hobbyworker.me/en/dev/2026-10-07-google-trends-for-python-2026-2-interest-over-time/) |
| 3 | `03_multirange_interest_over_time.py` | [Comparing time ranges](https://hobbyworker.me/en/dev/2026-10-08-google-trends-for-python-2026-3-multirange-interest-over-time/) |
| 4 | `04_recent_hourly_interest.py` | [Hourly interest for the past 7 days](https://hobbyworker.me/en/dev/2026-10-09-google-trends-for-python-2026-4-recent-hourly-interest/) |
| 5 | `05_interest_by_region.py` | [Interest by region](https://hobbyworker.me/en/dev/2026-10-10-google-trends-for-python-2026-5-interest-by-region/) |
| 6 | `06_related_queries.py` | [Related queries](https://hobbyworker.me/en/dev/2026-10-11-google-trends-for-python-2026-6-related-queries/) |
| 7 | `07_suggestions.py` | [Keyword suggestions and topics](https://hobbyworker.me/en/dev/2026-10-12-google-trends-for-python-2026-7-suggestions-and-topics/) |
| 8 | `08_trending_now_rss.py` | [Trending searches from the RSS feed](https://hobbyworker.me/en/dev/2026-10-13-google-trends-for-python-2026-8-trending-now-rss/) |

The posts are published one per day from 2026-10-06 to 2026-10-13.

## Status

Last checked on 2026-10-03 with Python 3.11 (the requirements also install on Python 3.13): all 8 scripts ran against Google Trends.

pytrends has had no release since 4.9.2 (April 2023). It calls the endpoints that the Google Trends website uses internally, so it can stop working whenever Google changes them. Google returns HTTP 429 when you send many requests in a short time; wait a few minutes and space out your requests.

## Not covered

Compared with the 2023 series, these are left out or replaced:

- `related_topics()`: Google returns an empty result. Left out.
- `top_charts()`: HTTP 404. Left out.
- `trending_searches()`, `realtime_trending_searches()`: HTTP 404. Part 8 uses the RSS feed instead.
- `get_historical_interest()`: removed in pytrends 4.8.0. Part 4 covers hourly data for the past 7 days instead.

## License

MIT. See [LICENSE](LICENSE).
