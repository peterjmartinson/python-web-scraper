from urllib.request import urlopen
from bs4 import BeautifulSoup

html_doc = urlopen("http://localhost:8080")
soup = BeautifulSoup(html_doc, 'html.parser')

title             = soup.title
title_name        = soup.title.name
title_string      = soup.title.string
title_parent_name = soup.title.parent.name
p                 = soup.p
p_class           = soup.p['class']
a                 = soup.a
find_all_a        = soup.find_all('a')
find_id           = soup.find(id="link3")


print("  - Extract all the URLs within the <a> tags:")
for link in soup.find_all('a'):
    print(link.get('href'))

print("\n")

print("  - Extract all the text:")
print(soup.get_text())

print("\n")

print(soup.prettify())
