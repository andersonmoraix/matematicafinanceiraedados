#aula 14, conteudo complementar, web scrapping

import requests 

from bs4 import BeautifulSoup 

pages = []
pageCodes = []
allQuotes = []

for i in range(10):
    page = requests.get("https://quotes.toscrape.com/page/" + str(1+i))
    pages.append(page)
    pageCode = BeautifulSoup(page.text, 'html.parser')
    pageCodes.append(pageCode)
    quotes = pageCode.find_all('div', class_="quote")
    allQuotes.extend(quotes)

for quote in allQuotes:
    phrase = quote.find('span', class_="text").text
    author = quote.find('small', class_="author").text
    print(phrase, "\nby", author, "\n\n")