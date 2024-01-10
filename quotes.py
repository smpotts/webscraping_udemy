from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# define the url for the site to scrape
quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'

# open a connection to the website we are scraping
uClient = uReq(quotes_page)
# save the html from the page
page_html = uClient.read()
print(page_html)
# close the connection
uClient.close()

# pass the page html to html parser
page_soup = soup(page_html, "html.parser")

# grab all the div elements with the class "quotes"
quotes = page_soup.findAll("div", {"class":"quotes"})

for quote in quotes:
    fav_quote = quote.findAll("p", {"class": "aquote"})
    aquote = fav_quote[0].text.strip()

    fav_authors = quote.findAll("p", {"class": "author"})
    author = fav_authors[0].text.strip()

    print(aquote)
    print(author)