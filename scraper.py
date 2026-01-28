import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sample public scraping website (used to demonstrate scraping logic)
URL = "https://quotes.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

data = []

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    quote_text = q.find("span", class_="text").text.strip()
    author = q.find("small", class_="author").text.strip()
    tags = [tag.text for tag in q.find_all("a", class_="tag")]

    data.append({
        "quote": quote_text,
        "author": author,
        "tags": ", ".join(tags)
    })

df = pd.DataFrame(data)

# Save output
df.to_csv("quotes_data.csv", index=False)

print("Scraping completed. Data saved as quotes_data.csv")
