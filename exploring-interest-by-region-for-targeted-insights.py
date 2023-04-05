import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords
keywords = ['Python', 'JavaScript']
timeframe = '2023-01-01 2023-03-31'

try:
    # Build payload
    pytrends.build_payload(keywords, timeframe=timeframe, geo='')

    # Retrieve interest by region data
    region_interest = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)

    # Sort the data by interest value
    region_interest = region_interest.sort_values(by='Python', ascending=False)

    # Plot the interest by region data
    plt.figure(figsize=(12, 6))
    plt.bar(region_interest.index, region_interest['Python'])

    plt.xlabel('Country')
    plt.ylabel('Interest')
    plt.title('Interest by Region for Python (Q1 2023)')
    plt.xticks(rotation=90)
    plt.show()

except Exception as e:
    print(traceback.format_exc())
