from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import requests
import time
print('Enter some skills that are not feasible for you')
unfeasible_skills = input('---')
print(f'Filtering out {unfeasible_skills}')
def find_jobs():
    main_url = ('https://merojob.com/search/?q=python&education=&location=&start_date=&end_date=')
    url = requests.get(main_url).text
    soup = BeautifulSoup(url, 'lxml')
    jobs = soup.find_all('div',class_='card mt-3 hover-shadow')
    for index,job in enumerate(jobs):
        company_name = job.find('h3', class_='h6').text.replace(' ','')
        skills = job.find('span', class_='badge badge-pill badge-white text-muted').text.replace(' ','')
        more_info = job.div.h1.a['href']
        if unfeasible_skills not in skills:
            with open(f'data/{index}.txt','w') as f:
                f.write(f"Company name: {company_name.strip()} \n")
                f.write(f"Required Skills:{skills.strip()} \n")
                f.write(f"More Info:{urljoin(main_url,more_info)} \n")
            print(f'File saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        waiting_time = 10
        print(f'Waiting {waiting_time} minutes')
        time.sleep(waiting_time * 60)


