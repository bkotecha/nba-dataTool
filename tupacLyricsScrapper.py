##get lyrics to all tupac songs 

import time
import requests
from bs4 import BeautifulSoup

def get_lyric_urls():
    index = requests.get("http://www.allthelyrics.com/lyrics/2pac")
    soup = BeautifulSoup(index.text, 'html.parser')
    lyric_paths = [link.get('href') for link in
                   soup.find_all('div', class_='lyricslist-output')[0].find_all('a')]
    lyric_urls = ['http://www.allthelyrics.com'+path for path in lyric_paths]
    return lyric_urls

 lyric_urls = get_lyric_urls()

 def get_lyric(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    html_lyrics = soup.find_all('div', class_='content-text-inner')[0].find_all('p')
    html_lyrics = [l.getText() for l in html_lyrics]
    return '\n'.join(html_lyrics)


def get_all_lyrics(lyric_urls):
    for url in lyric_urls:
        time.sleep(1.0)
        yield get_lyric(url)

lyrics = get_all_lyrics(lyric_urls)

with open('all_tupac_lyrics.txt', 'w') as f:
    for lyric in lyrics:
        f.write(lyric.replace('\r\n', '\n'))
        f.write('\n')
