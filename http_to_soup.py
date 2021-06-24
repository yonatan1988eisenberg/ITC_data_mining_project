import requests
from bs4 import BeautifulSoup
from time import sleep

GET_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                             "70.0.3538.77 Safari/537.36"}
SLEEP_TIME = 2


def http_to_soup(url):
    """
    This function get a url address and returns it http as a soup object
    """
    page = requests.get(url, headers=GET_HEADERS)
    # if page.status_code != 200:
    #     raise ResourceWarning("Could not download the http")
    soup = BeautifulSoup(page.content, 'html.parser')
    # sleep(SLEEP_TIME)
    return soup
