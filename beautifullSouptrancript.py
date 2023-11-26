import os

import requests
from bs4 import BeautifulSoup


class Transcript:

    def __init__(self, website):
        try:
            self.website = website
            result = requests.get(self.website)
            content = result.text
            print(self.website)

            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            TranscriptWriter(title, transcript)

        except:
            print('Link is not working')
            print(self.website)


class TranscriptWriter:
    def __init__(self, title, transcript):
        # Sanitize the title for creating a valid file name
        sanitized_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_'))

        # Define the directory where you want to save the transcript
        transcript_directory = 'Transcript'

        # Create the directory if it doesn't exist
        os.makedirs(transcript_directory, exist_ok=True)

        # Create the file with the sanitized title
        file_path = os.path.join(transcript_directory, f'{sanitized_title}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(title + '\n\n' + transcript)
            pass
