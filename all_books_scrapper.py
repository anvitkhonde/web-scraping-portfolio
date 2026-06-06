import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_books = []

for page in range(1, 6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        all_books.append({"Title": title, "Price": price})
    
    print(f"Page {page} done — {len(all_books)} books collected so far")
    time.sleep(1)

df = pd.DataFrame(all_books)
df.to_csv("all_books.csv", index=False)
print(f"Finished! Saved {len(all_books)} books to all_books.csv")