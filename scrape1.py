
from bs4 import BeautifulSoup
import requests

url='https://www.tutorialspoint.com/index.htm'
page=requests.get(url)
soup=BeautifulSoup(page.content, 'lxml')
print(soup.title)




# title=lists.find('span')
# print(title.text)


#soup=BeautifulSoup(page.content, 'html.parser')

# lists=soup.find_all('section', class_="listing-search-item")
# for list in lists:
#     title=lists.find('a', class_='listing-search-item__link--title"').text
#     location=lists.find('divi',class_='listing-search-item__sub-title').text
#     price=lists.find('sivi', class_='class="listing-search-item__price').text
#     area=lists.find('li', class_="illustrated-features__item--surface-area").text
#     info=[title, location, price, area]
#     print(info) 