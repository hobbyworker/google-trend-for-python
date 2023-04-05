import traceback
from pytrends.request import TrendReq
import pandas as pd

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords
keywords = ['pizza', 'bagel']
time_ranges = [
    '2022-09-04 2022-09-10',
    '2022-09-18 2022-09-24',
]

try:
    # Build the payload
    pytrends.build_payload(keywords, timeframe=time_ranges)

    # Retrieve multi-range interest over time data
    interest_over_time_data = pytrends.multirange_interest_over_time()

    # Display the interest over time data
    print(interest_over_time_data)
except Exception as e:
    print(traceback.format_exc())
