import requests
import bs4


class Web:
    # initializing the class members
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    # ----------------------------------------------------------------------
    #   Extracting The webpage Code and parsing It

    def website_scraping(self):
        response = requests.get(self.url)  # Object

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        formatted_text = soup.prettify()
        # print(formatted_text)
    # ----------------------------------------------------------------------
    #   Parsing and saving the Http request data in a Local file

    def save_code(self):
        response = requests.get(self.url)  # Object

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        formatted_text = soup.prettify()
        with open(self.filename, "w+", encoding="utf-8") as f:
            f.write(formatted_text)

# ----------------------------------------------------------------------

    def get_anchor_tags(self):
        response = requests.get(self.url)  # Object

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        list_anchor_tag = soup.find_all('td', 'a', class_='titleColumn')
        for data in list_anchor_tag:
            movie_name = data.text.split()[1:-1]
            print(" ".join(movie_name))


if __name__ == "__main__":
    Url = input("Enter Your URL : ")
    file_name = input("Enter Filename with Extension : ")
    w = Web(Url, file_name)
    w.website_scraping()
    w.save_code()
    w.get_anchor_tags()

