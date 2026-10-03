"""Part 1: interest over the past 5 years for one keyword."""
from common import make_client

pytrends = make_client()
pytrends.build_payload(["Python"], timeframe="today 5-y", geo="", gprop="")
df = pytrends.interest_over_time()

print(df.head())
print("...")
print(df.tail())
print(f"{len(df)} rows, {df.index.min():%Y-%m-%d} ~ {df.index.max():%Y-%m-%d}")
