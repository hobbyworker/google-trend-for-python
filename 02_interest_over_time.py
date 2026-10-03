"""Part 2: compare interest over time for several keywords and save a chart."""
import matplotlib

matplotlib.use("Agg")  # Save to a file without opening a window.
import matplotlib.pyplot as plt  # noqa: E402

from common import drop_partial, make_client  # noqa: E402

KEYWORDS = ["Python", "JavaScript", "Rust"]
TIMEFRAME = "today 12-m"  # e.g. "today 3-m", "2026-01-01 2026-06-30", "now 7-d"

pytrends = make_client()
pytrends.build_payload(KEYWORDS, timeframe=TIMEFRAME, geo="")
df = drop_partial(pytrends.interest_over_time())

print(df.tail())
print("Average:", df.mean().round(1).to_dict())
print("Peak:", {kw: f"{df[kw].idxmax():%Y-%m-%d}" for kw in KEYWORDS})

ax = df.plot(figsize=(10, 5), title=f"Interest over time ({TIMEFRAME})")
ax.set_ylabel("Interest (0-100)")
plt.tight_layout()
plt.savefig("interest_over_time.png", dpi=150)
print("Saved interest_over_time.png")
