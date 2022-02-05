import requests
import bs4
import time


class Web:
    # initializing the class members
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.response = requests.get(self.url)  # Object
        self.soup = bs4.BeautifulSoup(self.response.text, "html.parser")

    # ----------------------------------------------------------------------

    # Saving the parsed Website code in Local File
    def save_code(self):
        formatted_text = self.soup.prettify()
        with open(self.filename, "w+", encoding="utf-8") as f:
            f.write(formatted_text)

    # ----------------------------------------------------------------------

    #   Extracting The webpage Code ,Parsing and saving the Http request data in a Local file
    def website_scraping(self):

        print("Put some skill that you are unfamiliar with ")
        unfamiliar_skill = input('> ')
        print(f'Filtering out {unfamiliar_skill}')

        jobs = self.soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for index, job in enumerate(jobs):
            job_published_date = job.find('span', class_='sim-posted').get_text()
            if 'few' in job_published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
                skills_required = job.find('span', class_='srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']
                if unfamiliar_skill not in skills_required:
                    with open(f'Job_Posts/{index}.txt', 'w') as f:
                        f.write(f'''Company Name : {company_name.strip()} \n''')
                        f.write(f'''Required Skills : {skills_required.strip()} \n''')
                        f.write(f'''Published Date : {job_published_date.strip()} \n''')
                        f.write(f'''more_info : {more_info}''')
                    print(f'File Saved : {index}.txt')

    # ----------------------------------------------------------------------


def main():
    url = 'https://www.timesjobs.com/candidate/job-search.html?' \
          'searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    file_name = input("Enter Filename with Extension : ")
    while True:
        w = Web(url, file_name)
        w.save_code()
        w.website_scraping()
        print("Waiting For 30 Seconds........")
        time.sleep(30)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
