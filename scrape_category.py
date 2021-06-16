"""
This file contains the code to get the different platforms from metacritic.com/games
and create the platforms.csv file
"""

import requests
from bs4 import BeautifulSoup
import csv

GAMES_URL = "https://www.metacritic.com/game"
PLATFORM_URL_HEAD = "https://www.metacritic.com/browse/games/release-date/new-releases/"
SORTING_OPTIONS = ["/date", "/metascore"]
SORT_BY_DATE = 0
SORT_BY_METASCORE = 1


PLATFORMS_TABLE_FILENAME = "platforms.csv"
PLATFORMS_TABLE_HEADERS = ["id", "Name", "url"]


GET_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
URL_LOCATION = -2


def file_to_soup(filename):
    """
    This is a temp function, it gets an html from a file and returns a soup object
    """
    with open(filename, encoding="utf8") as file:
        text_html = file.read()
        soup = BeautifulSoup(text_html, 'html.parser')
    return soup


def http_to_soup(url):
    """
    This function get a url address and returns it http as a soup object
    """
    page = requests.get(url, headers=GET_HEADERS)
    # if page.status_code != 200:
    #     raise ResourceWarning("Could not download the http")
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def main():
    """
    The main function will access /games and scrape the platforms and their urls and creates the platforms csv file
    """


    # this is the scraping, uncomment it when done
    """
    try:
        games_soup = http_to_soup(GAMES_URL)
    except ResourceWarning:
        exit()
    """

    # this is reading the html from file, comment it when scraping
    games_soup = file_to_soup("temp_game_html.txt")

    platforms_module = games_soup.find('div', class_='platforms_wrap')
    platforms = platforms_module.find_all('li')

    # write the data to the csv file, exclude legacy platforms
    id_num = 1
    with open(PLATFORMS_TABLE_FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(PLATFORMS_TABLE_HEADERS)
        for platform in platforms[:-1]:
            platform_name = platform.div.span.a.text
            writer.writerow([id_num, platform_name, PLATFORM_URL_HEAD + platform_name + SORTING_OPTIONS[SORT_BY_DATE]])
            id_num += 1


if __name__ == "__main__":
    main()