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
