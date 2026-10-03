"""Part 6: related queries (top and rising) for a keyword."""
from common import make_client

KEYWORD = "Python"
pytrends = make_client()
pytrends.build_payload([KEYWORD], timeframe="today 3-m", geo="")
related = pytrends.related_queries()[KEYWORD]

for kind in ("top", "rising"):
    print(f"{kind}:")
    df = related[kind]
    print(df.head(10) if df is not None else "  (no data)")
