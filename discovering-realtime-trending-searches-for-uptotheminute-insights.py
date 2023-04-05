import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

try:
    # Retrieve real-time trending searches data
    realtime_trending_searches = pytrends.realtime_trending_searches(pn='US')

    # Display the top 10 real-time trending searches
    print(realtime_trending_searches.head(10))
except Exception as e:
    print(traceback.format_exc())
