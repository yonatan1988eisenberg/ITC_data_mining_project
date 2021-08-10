import requests
from bs4 import BeautifulSoup
GET_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                             "70.0.3538.77 Safari/537.36"}

# todo: consider getting the user agents from the operating device


def http_to_soup(url):
    """
    This function get a url address and returns it http as a soup object
    """
    page = requests.get(url, headers=GET_HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
