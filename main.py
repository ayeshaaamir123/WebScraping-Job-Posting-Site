from bs4 import BeautifulSoup
import requests
import time

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html_text)
# returns Response [200] status code to show the request was succesful
# to not show the status code add .text to requests.get()
print('Put some skill that you are not familiar with:')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}...')

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')

    # finds all jobs posted on that page

    # jobs = soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")
    # print(jobs)

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")  # finds the first job or first li tag

    for index,job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').text
        if '2' in job_published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ',
                                                                                   '')  # .replace to avoid wide spaces
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()}")
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f"More info: {more_info}")
                print(f'File saved... {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        print(f'Waiting...')
        time.sleep(600)


