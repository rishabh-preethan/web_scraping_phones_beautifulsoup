from bs4 import BeautifulSoup
import requests
import csv


html_text = requests.get('https://www.devicespecifications.com/en/model-sar/e48a5dad').text
print(html_text)