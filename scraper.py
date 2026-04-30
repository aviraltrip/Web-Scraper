from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://books.toscrape.com/')
print(html_text)