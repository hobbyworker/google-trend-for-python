"""Part 5: interest by country, and by region within one country."""
import time

from common import make_client

KEYWORD = "Python"
pytrends = make_client()

pytrends.build_payload([KEYWORD], timeframe="today 12-m", geo="")
by_country = pytrends.interest_by_region(resolution="COUNTRY", inc_low_vol=True, inc_geo_code=True)
print("Top countries:")
print(by_country.sort_values(KEYWORD, ascending=False).head(10))

time.sleep(5)

pytrends.build_payload([KEYWORD], timeframe="today 12-m", geo="KR")
by_region = pytrends.interest_by_region(resolution="REGION", inc_low_vol=True, inc_geo_code=True)
print("Top regions in South Korea:")
print(by_region.sort_values(KEYWORD, ascending=False).head(10))
