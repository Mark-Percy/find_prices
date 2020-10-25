import requests
from bs4 import BeautifulSoup as bs
import logging
import time

"""
Begins the searching web process

"""

def search_web(search_term):
    page = requests.get(f'https://google.com/search?q={search_term}+price')
    soup = bs(page.text, 'html.parser')
    print(soup.prettify())
