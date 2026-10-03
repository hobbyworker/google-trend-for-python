"""Part 3: compare the same keyword across several time ranges."""
from common import make_client

KEYWORD = "Python"
TIMEFRAMES = [
    "2024-09-01 2024-09-30",
    "2025-09-01 2025-09-30",
]

pytrends = make_client()
# With a list of time ranges, pytrends pairs kw_list[i] with timeframe[i],
# so repeat the keyword once for each range.
pytrends.build_payload([KEYWORD] * len(TIMEFRAMES), timeframe=TIMEFRAMES, geo="")
df = pytrends.multirange_interest_over_time()

# The first row is the average of each range. The rest are the values per date.
print(df.head(10))
