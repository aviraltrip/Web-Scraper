from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://books.toscrape.com/').text
soup=BeautifulSoup(html_text, 'lxml')
books = soup.find_all('article', class_='product_pod')
for book in books:
    book_name = book.find('h3').a['title']
    price = book.find('p', class_='price_color').text.strip()
    print(f'''
Book Name: {book_name}
Price: {price}
''')