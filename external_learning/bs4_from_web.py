import requests
from bs4 import BeautifulSoup
import time

print("Put some skills that you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    
    html_text = requests.get('https://www.website.com').text
    soup = BeautifulSoup(html_text, 'lxml') # or html.parser for second param
    jobs = soup.find_all('li', class_="class_name")
    for index, job in enumerate(jobs):
        published_date = job.find('li', class_="class_name").span.text
        if 'few' in published_date: # to view jobs that have been published *few* days ago
            company_name = job.find('h3', class_name="class_name").text.replace(' ', '') # replace to eliminate white spaces
            skills = job.find('span', class_="class_name").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'dir/{index}.txt', 'w') as f:
                    f.write(f'company name: {company_name.strip()}\n')
                    f.write(f'skills required: {skills.strip()}\n')
                    f.write(f'More info: {more_info}')
                print(f'File saved {index}')
                
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
        
