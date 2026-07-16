# Web Scraper Projects

Python-based web scraping examples using **BeautifulSoup** (static HTML) and **Selenium** (dynamic pages).

---

## 📁 Repository Structure

### [bs4_req/](file:///d:/Web-Scraper/bs4_req) (BeautifulSoup)
*   [main.py](file:///d:/Web-Scraper/bs4_req/main.py) - Parses course prices from a local HTML file ([sample.html](file:///d:/Web-Scraper/bs4_req/sample.html)).
*   [scraper.py](file:///d:/Web-Scraper/bs4_req/scraper.py) - Scrapes and filters book titles from `books.toscrape.com` to individual text files.

### [selenium/](file:///d:/Web-Scraper/selenium) (Selenium WebDriver)
*   [main.py](file:///d:/Web-Scraper/selenium/main.py) - Simple Selenium search test on `python.org`.
*   [locating_single.py](file:///d:/Web-Scraper/selenium/locating_single.py) - Basic selector test on Amazon India.
*   [project.py](file:///d:/Web-Scraper/selenium/project.py) - Multi-page Amazon product HTML harvester (saves pages to `data/`).
*   [collect.py](file:///d:/Web-Scraper/selenium/collect.py) - Parses harvested HTML to structured CSV ([data.csv](file:///d:/Web-Scraper/selenium/data.csv)).

---

## 🛠️ Setup & Installation

```bash
pip install beautifulsoup4 requests lxml selenium pandas
```
*Note: Ensure Google Chrome is installed for Selenium scripts.*