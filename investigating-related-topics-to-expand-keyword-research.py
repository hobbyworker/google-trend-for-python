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
    related_topics = pytrends.related_topics()

    # Extract the related topics for the keyword 'Python'
    python_related_topics = related_topics[keywords[0]]['top']

    # Display the top 10 rising related topics
    print(python_related_topics.head(10))
except Exception as e:
    print(traceback.format_exc())
