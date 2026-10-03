"""Part 4: hourly interest for the past 7 days, 8-minute interest for the past day."""
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from common import make_client, to_local_time  # noqa: E402

KEYWORD = "Python"
pytrends = make_client()

pytrends.build_payload([KEYWORD], timeframe="now 7-d", geo="")
hourly = to_local_time(pytrends.interest_over_time())
print("now 7-d:", len(hourly), "rows")
print(hourly.tail())

time.sleep(5)  # Space out the requests to avoid HTTP 429.

pytrends.build_payload([KEYWORD], timeframe="now 1-d", geo="")
recent = to_local_time(pytrends.interest_over_time())
print("now 1-d:", len(recent), "rows")
print(recent.tail())

# Average interest by hour of day (local time) over the past 7 days
by_hour = hourly[KEYWORD].groupby(hourly.index.hour).mean().round(1)
print("Average by hour:", by_hour.to_dict())

fig, axes = plt.subplots(2, 1, figsize=(10, 7))
hourly[KEYWORD].plot(ax=axes[0], title="Past 7 days (hourly)")
recent[KEYWORD].plot(ax=axes[1], title="Past day (8 minutes)")
plt.tight_layout()
plt.savefig("recent_hourly_interest.png", dpi=150)
print("Saved recent_hourly_interest.png")
