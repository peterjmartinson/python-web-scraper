from urllib.request import urlopen
from bs4 import BeautifulSoup

html_doc = urlopen("http://localhost:8080")
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
