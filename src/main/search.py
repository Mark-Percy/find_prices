import requests
from bs4 import BeautifulSoup as bs
import logging
import time

"""
Begins the searching web process

"""

def search_web(search_term):
    page = requests.get(f'https://google.com/search?q={search_term}+price+amazon')
    soup = bs(page.text, 'html.parser')
    links = []
    for a_tag in soup.find_all('a'):
        link = a_tag.get('href')
        if('amazon.com') in link:

            page = requests.get(link[7:], headers = {'User-Agent': 'Chrome/83.0.4103.97'})
            print(a_tag.get('href'))
            time.sleep(2)
            print(page.status_code)
            if page.status_code == 202:
                print(a_tag.get('href'))
                print(page.status_code)