import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords
keywords = ['Python', 'JavaScript']

try:
    # Retrieve hourly interest data
    hourly_interest = pytrends.get_historical_interest(keywords, year_start=2023, month_start=3, day_start=1, hour_start=0, year_end=2023, month_end=3, day_end=2, hour_end=0, cat=0, geo='', gprop='', sleep=0)

    # Plot the hourly interest data
    plt.figure(figsize=(12, 6))
    plt.plot(hourly_interest.index, hourly_interest['Python'], label='Python')
    plt.plot(hourly_interest.index, hourly_interest['JavaScript'], label='JavaScript')

    plt.xlabel('Hour')
    plt.ylabel('Interest')
    plt.title('Hourly Interest for Python and JavaScript')
    plt.legend()
    plt.show()
except Exception as e:
    print(traceback.format_exc())
