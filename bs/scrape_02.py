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


print("  - title")
print(title)
print("  - title_name")
print(title_name)
print("  - title_string")
print(title_string)
print("  - title_parent_name")
print(title_parent_name)
print("  - p")
print(p)
print("  - p_class")
print(p_class)
print("  - a")
print(a)
print("  - find_all_a")
print(find_all_a)
print("  - find_id")
print(find_id)

print("\n")

print(soup.prettify())
