from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://books.toscrape.com/').text
soup=BeautifulSoup(html_text, 'lxml')