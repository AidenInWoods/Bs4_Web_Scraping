from bs4 import BeautifulSoup
import requests
import re

search_item = input("Input what you want to search for: ")

url = f"https://search.rakuten.co.jp/search/mall/{search_item}/?p=1"

response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
pages = doc.find(class_='dui-pagination')

# Find the maximum page of the search_item
mx_page = 0
for page in pages:
    page_num = int(page.string) if page.string.isnumeric() else 0
    mx_page = max(mx_page, page_num)

# Iterate through each page to scrape info we need
item_prices = []
for page in range(1, mx_page):
    uurl = f"https://search.rakuten.co.jp/search/mall/{search_item}/?p={page}"
    response = requests.get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    items = doc.find_all(class_='price--OX_YW')

    for item in items:
        item_price = item.text 
        item_prices.append(item_price)

print(item_prices)
