# google-trend-for-python

Sample code for the [Google Trends for Python](https://hobbyworker.me/en/series/google-trends-for-python/) series on hobbyworker.me. The scripts use [pytrends](https://pypi.org/project/pytrends/), an unofficial Google Trends API for Python.

## Setup

```bash
pip install -r requirements.txt
```

## Status

Last checked on 2026-10-02 with Python 3.11 (the requirements also install and run on Python 3.13): 5 of the 10 scripts work. pytrends has had no release since 4.9.2 (April 2023), and Google no longer serves some of the data it requests. Each script below is marked with its result.

## [Pytrends 1: How to use Google Trend unofficially with Python](https://hobbyworker.me/en/dev/2023-03-26-pytrends-1-how-to-use-google-trend-unofficially-with-python/)

* No script for this part.

## [Pytrends 2: Analyzing Interest Over Time](https://hobbyworker.me/en/dev/2023-03-27-pytrends-2-analyzing-interest-over-time/)

* analyzing-interest-over-time.py — works

## [Pytrends 3: Harnessing Multi-Range Interest Over Time Analysis](https://hobbyworker.me/en/dev/2023-03-28-pytrends-3-harnessing-multirange-interest-over-time-analysis/)

* harnessing-multirange-interest-over-time-analysis.py — works with pandas 2 (fails with pandas 3, so `requirements.txt` pins pandas 2.3.3)

## [Pytrends 4: Diving into Historical Hourly Interest Data](https://hobbyworker.me/en/dev/2023-03-29-pytrends-4-diving-into-historical-hourly-interest-data/)

* diving-into-historical-hourly-interest-data.py — does not work: `get_historical_interest` was removed in pytrends 4.8.0, and with 4.7.3 it returns an empty result

## [Pytrends 5: Exploring Interest by Region for Targeted Insights](https://hobbyworker.me/en/dev/2023-03-30-pytrends-5-exploring-interest-by-region-for-targeted-insights/)

* exploring-interest-by-region-for-targeted-insights.py — works

## [Pytrends 6: Investigating Related Topics to Expand Keyword Research](https://hobbyworker.me/en/dev/2023-03-31-pytrends-6-investigating-related-topics-to-expand-keyword-research/)

* investigating-related-topics-to-expand-keyword-research.py — does not work: Google returns an empty list of related topics, so pytrends raises `IndexError`

## [Pytrends 7: Uncovering Related Queries for In-Depth Analysis](https://hobbyworker.me/en/dev/2023-04-01-pytrends-7-uncovering-related-queries-for-indepth-analysis/)

* uncovering-related-queries-for-indepth-analysis.py — works

## [Pytrends 8: Tracking Trending Searches to Stay Ahead](https://hobbyworker.me/en/dev/2023-04-02-pytrends-8-tracking-trending-searches-to-stay-ahead/)

* tracking-trending-searches-to-stay-ahead.py — does not work: Google returns HTTP 404

## [Pytrends 9: Mastering Top Charts Analysis for Data-Driven Insights](https://hobbyworker.me/en/dev/2023-04-03-pytrends-9-mastering-top-charts-analysis-for-datadriven-insights/)

* mastering-top-charts-analysis-for-datadriven-insights.py — does not work: Google returns HTTP 404

## [Pytrends 10: Refining Trend Searches with Suggestions](https://hobbyworker.me/en/dev/2023-04-04-pytrends-10-refining-trend-searches-with-suggestions/)

* refining-trend-searches-with-suggestions.py — works

## [Pytrends 11: Discovering Real-Time Trending Searches for Up-to-the-Minute Insights](https://hobbyworker.me/en/dev/2023-04-05-pytrends-11-discovering-realtime-trending-searches-for-uptotheminute-insights/)

* discovering-realtime-trending-searches-for-uptotheminute-insights.py — does not work: Google returns HTTP 404

## Removed: `-temp429` variants

Parts 2, 3, 5, 6 and 7 used to have `*-temp429.py` variants that fetched an `NID` cookie with Selenium to work around HTTP 429 errors (March 2023). As of October 2026 the plain scripts no longer get 429 responses, and the Selenium step timed out with current Chrome, so the variants were removed. They remain in the history at commit [fdc2587](https://github.com/hobbyworker/google-trend-for-python/tree/fdc2587e0bfa836692d6b511fb89a37f7002e9a4).

## License

MIT. See [LICENSE](LICENSE).
