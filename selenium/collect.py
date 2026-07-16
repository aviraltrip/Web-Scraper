import sys
import os
from bs4 import BeautifulSoup
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

d = {"title": [], "price": [], "link": []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        t = soup.find("h2")
        if t is not None:
            title = t.get_text(strip=True)
            # h2 is wrapped inside the 'a' tag, so find_parent("a") finds it
            a = t.find_parent("a") or t.find("a")
            link = "https://www.amazon.in" + a["href"] if (a and "href" in a.attrs) else "No Link"
            p = soup.find("span", class_="a-price-whole")
            price = p.get_text(strip=True) if p else "Not Available"
            d["title"].append(title)
            d["price"].append(price)
            d["link"].append(link)
        else:
            print(f"Skipping {file}: No <h2> tag found (this file may only contain price HTML)")

    except Exception as e:
        print(f"Error in {file}: {e}")

df = pd.DataFrame(d)
df.to_csv("data.csv", index=False)
print(df)
