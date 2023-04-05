import traceback
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Set up pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

try:
    # Retrieve top charts data for 2022 
    top_charts = pytrends.top_charts(date=2022, hl='en-US', tz=360)

    # Display the top 10 in 2022
    print(top_charts.head(10))
except Exception as e:
    print(traceback.format_exc())
