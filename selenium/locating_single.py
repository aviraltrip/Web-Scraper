import sys
sys.stdout.reconfigure(encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=2RKOOCZHIKESC&sprefix=lapt%2Caps%2C337&ref=nb_sb_noss_2")

elems = driver.find_elements(By.CLASS_NAME, "a-price")
print(f"{len(elems)} items found")
for elem in elems:
    print(elem.text)
#print(elem.get_attribute("outerHTML"))
time.sleep(5)
driver.close()
