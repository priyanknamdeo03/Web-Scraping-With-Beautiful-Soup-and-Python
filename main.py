import requests             # importing Libraries
from bs4 import BeautifulSoup
import html5lib

url = "https://codewithharry.com"
# Getting The HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Parse The HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# HTML Tree Traversal

# Commonly Used Objects
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# Get Title Of HTML Page
title = soup.title

# Get All Paragraphs From Page
paragraphs = soup.find_all('p')
# print(paragraphs)
# print('\n')

# Get First Element
# print(soup.find('p'))

# Get Classes of any element in HTML page
# print(soup.find('p')['class'])

# Get text from tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get All Anchor Tags From Page
anchor_tags = soup.find_all('a')
all_links = set()
# get all links
for link in anchor_tags:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
# print(all_links)

# .contents = A tag's children are available as a list
# .children = A tag's children are available as an generator(Memory Less Usage)

search_content = soup.find(id='__next')
for element in search_content.stripped_strings:
    print(element)









