from bs4 import BeautifulSoup
import requests
import time
import os

print('Put a book title that you want to filter out')
unwanted_keyword = input('>')
print(f'Filtering out books containing: {unwanted_keyword}\n')

def find_books():
    html_text=requests.get('https://books.toscrape.com/').content
    soup=BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('article', class_='product_pod')
    for count, book in enumerate(books, start=1):
        book_name = book.find('h3').a['title']
        if unwanted_keyword.lower() not in book_name.lower():
            price = book.find('p', class_='price_color').text.strip()
            
            os.makedirs('posts', exist_ok=True)
            clean_name = book_name.replace(':', '').replace('?', '')
            
            with open(f'posts/{count}-{clean_name}.txt', 'w', encoding='utf-8') as f:
                f.write(book_name+'\n'+price+'\n') 
            print(f'file saved: {count}-{clean_name}.txt')
            print(f'''
            Book {count}
            Book Name: {book_name}
            Price: {price}
            ''')

if __name__ == '__main__':  #code in dis block only runs when script executed directly
    while True:
        find_books()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)