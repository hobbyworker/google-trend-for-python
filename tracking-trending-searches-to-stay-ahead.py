import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords
keywords = ['Python']

try:
    # Retrieve trending searches data
    trending_searches = pytrends.trending_searches(pn='united_states')

    # Display the top 10 trending searches
    print(trending_searches.head(10))
except Exception as e:
    print(traceback.format_exc())
