import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords
keywords = ['Python']

try:
    # Build payload
    pytrends.build_payload(keywords, timeframe='now 7-d', geo='')

    # Retrieve interest by region data
    related_queries = pytrends.related_queries()

    # Extract the related queries for the keyword 'Python'
    python_related_queries = related_queries[keywords[0]]['rising']

    # Display the top 10 rising related queries
    print(python_related_queries.head(10))
except Exception as e:
    print(traceback.format_exc())
