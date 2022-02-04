import requests
import bs4

url = input("Enter Your URL : ")
response = requests.get(url)     # Object

filename = "temp.html"
soup = bs4.BeautifulSoup(response.text, "html.parser")

formatted_text = soup.prettify()
# print(formatted_text)

with open(filename, "w+", encoding="utf-8") as f:
    f.write(formatted_text)

list_img_tag = soup.find_all('img')
# print(list_img_tag)

list_anchor_tag = soup.find_all('a')
# print(list_anchor_tag)

no_of_imgtag = len(list_img_tag)
no_of_anchortag = len(list_anchor_tag)

print("Number Of Img Tags = ",no_of_imgtag)

print("Number Of Anchor Tags = ",no_of_anchortag)












