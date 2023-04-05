import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

try:
    # Retrieve search suggestions for the query 'Python'
    suggestions = pytrends.suggestions(keyword='Python')

    # Display the search suggestions
    for suggestion in suggestions:
        print(suggestion['title'])
except Exception as e:
    print(traceback.format_exc())
