import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "laptop"
file = 0

for i in range(1, 20):
    if file >= 50:
        break
        
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2RKOOCZHIKESC&sprefix=lapt%2Caps%2C337&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    print(f"Page {i}: {len(elems)} items found")

    for elem in elems:
        if file >= 50:
            break
        try:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{file}", "w", encoding="utf-8") as f:
                f.write(d)
            print(f"file saved: {query}_{file}")
            file += 1
        except Exception as e:
            print(f"Error reading element: {e}")
            
    time.sleep(2)  

driver.quit()
