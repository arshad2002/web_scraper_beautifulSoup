import requests
from bs4 import BeautifulSoup
from beautifullSouptrancript import Transcript


class Movielist:
    def __init__(self, website):
        self.website = website
        result = requests.get(self.website)
        content = result.text

        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        movie = box.find_all('a')
        links = []

        for link in movie:
            links.append('https://subslikescript.com/' + link['href'])

        for link in links:
            Transcript(link)
