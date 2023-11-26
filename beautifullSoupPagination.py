import requests
from bs4 import BeautifulSoup
from beautifullSoupMovieList import Movielist

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
lastPage = pages[-2].get_text()

for page in range(1, int(lastPage)+1) :
    root = 'https://subslikescript.com'
    website = f'{root}/movies_letter-A?page={page}'
    Movielist(website)
