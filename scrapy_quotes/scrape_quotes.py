import requests
from bs4 import BeautifulSoup
import json

url = "http://quotes.toscrape.com"
quotes = []
authors = {}

page_url = ""
while page_url is not None:
    r = requests.get(url+page_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    quote_elements = soup.find_all("div", class_="quote")
    for quote_element in quote_elements:
        text = quote_element.find("span", class_="text").text
        author_name = quote_element.find("small", class_="author").text  # Тут змінено код
        if author_name not in authors:
            authors[author_name] = {"name": author_name, "quotes": [text]}
        else:
            authors[author_name]["quotes"].append(text)
        quote = {"quote": text, "author": author_name}
        quotes.append(quote)
    page_url = soup.find("li", class_="next")
    if page_url is not None:
        page_url = page_url.a["href"]

with open('quotes.json', 'w') as f:
    json.dump(quotes, f)
with open('authors.json', 'w') as f:
    json.dump(list(authors.values()), f)
