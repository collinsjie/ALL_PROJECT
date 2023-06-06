# # Search for lines that have an at sign between characters
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)
# # Search for lines that start with 'From'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)
        

# # Search for lines that have an at sign between characters
# # The characters must be a letter or number
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)


# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.

# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^school\S*: [0-9.]+', line):
#         print(line)

# # Search for lines that start with 'X' followed by any
# # non whitespace characters and ':' followed by a space
# # and any number. The number can include a decimal.
# # Then print the number if it is greater than zero.
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)
        
        # # Send a GET request to the website
# url = "https://www.linkedin.com/"
# response = requests.get(url)

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, "html.parser")

# # Extract the title of the website
# title = soup.title.string
# print(title)

# # Extract all the links on the website
# links = []
# for link in soup.find_all("a"):
#     href = link.get("href")
#     links.append(href)
# print(links)


# import requests
# from bs4 import BeautifulSoup
# import csv

# # Make a request to the website
# # url = "https://www.example.com"
# # response = requests.get(url)

# # # Parse the HTML content using Beautiful Soup
# # soup = BeautifulSoup(response.content, 'html.parser')

# # # Find the elements that you want to extract
# # data = []
# # table = soup.find('table')
# # rows = table.find_all('tr')
# # for row in rows:
# #     cols = row.find_all('td')
# #     cols = [col.text.strip() for col in cols]
# #     data.append(cols)

# # # Save the data into a CSV file
# # filename = "output.csv"
# # with open(filename, 'w', newline='') as file:
# #     writer = csv.writer(file)
# #     writer.writerows(data)

import requests
from bs4 import BeautifulSoup
import time


print('put some skill that you are not familar with ')
unfamiliar_skils=input('>')
print(f'Filtering out: {unfamiliar_skils}')
def find_jobs():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup =BeautifulSoup(html_text, 'lxml')
    jobs =soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span', class_='sim-posted').text
        if 'few' in published_date:
            company_name =job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span', class_='srp-skills').text.replace(' ','')
            job_links=job.header.h2.a['href']
            if unfamiliar_skils not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    
                    f.writer(f"Company Name: {company_name.strip()}")
                    f.writer(f'Required Skills: {skills.strip()}')
                    f.writer(f'Job links: {job_links}')
                print(f'File Saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting{time_wait} minutes...')
        time.sleep(time_wait*60)