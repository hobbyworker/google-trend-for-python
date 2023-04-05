import traceback
import time
from selenium import webdriver
from pytrends.request import TrendReq
import pandas as pd

def get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://trends.google.com/")
    time.sleep(5)
    cookie = driver.get_cookie("NID")["value"]
    driver.quit()
    return cookie

if __name__ == '__main__':
    nid_cookie = f"NID={get_cookie()}"

    # Set up pytrends request
    pytrends = TrendReq(
        hl='en-US',
        tz=360,
        requests_args={"headers": {"Cookie": nid_cookie}}
    )

    # Define the keywords and time range for the analysis
    keywords = ['Python', 'JavaScript']
    time_range = '2022-01-01 2023-01-31'

    try:
        # Build the payload
        pytrends.build_payload(keywords, cat=0, timeframe=time_range, geo='', gprop='')
        
        # Retrieve interest over time data
        interest_over_time_data = pytrends.interest_over_time()
        
        print(interest_over_time_data.head())
    except Exception as e:
        print(traceback.format_exc())
