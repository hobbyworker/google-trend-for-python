"""Part 7: keyword suggestions, and searching by topic instead of search term."""
import time

from common import drop_partial, make_client

pytrends = make_client()
suggestions = pytrends.suggestions("Python")
for s in suggestions:
    print(f"{s['title']:<45} {s['type']:<35} {s['mid']}")

# A suggestion's mid is a topic ID. Searching by topic groups related search terms
# (for example misspellings and other languages) into one.
topic = next((s for s in suggestions if s["type"] == "Programming language"), suggestions[0])
time.sleep(5)
pytrends.build_payload(["Python", topic["mid"]], timeframe="today 12-m", geo="")
df = drop_partial(pytrends.interest_over_time())
df.columns = ["Python (search term)", f"{topic['title']} (topic)"]
print(df.tail())
print("Average:", df.mean().round(1).to_dict())
