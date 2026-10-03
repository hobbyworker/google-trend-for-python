"""Part 8: today's trending searches from the Google Trends RSS feed."""
import xml.etree.ElementTree as ET

import requests

GEO = "KR"  # Country code, e.g. "US", "JP"
URL = f"https://trends.google.com/trending/rss?geo={GEO}"
NS = {"ht": "https://trends.google.com/trending/rss"}

response = requests.get(URL, timeout=10)
response.raise_for_status()
channel = ET.fromstring(response.content).find("channel")

for item in channel.findall("item"):
    title = item.findtext("title")
    traffic = item.findtext("ht:approx_traffic", namespaces=NS)
    published = item.findtext("pubDate")
    print(f"{title}  ({traffic} searches, {published})")
    for news in item.findall("ht:news_item", NS)[:2]:
        source = news.findtext("ht:news_item_source", namespaces=NS)
        headline = news.findtext("ht:news_item_title", namespaces=NS)
        print(f"    - [{source}] {headline}")
