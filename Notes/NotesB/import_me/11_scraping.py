# Web scraping

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)
print(page)  # prints the response

print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())  # nicer way to look at it

# find data by tagname
# find method just gets the first one it finds
title = soup.find("title")  # title is the tag name
print(title)
print(title.text)
