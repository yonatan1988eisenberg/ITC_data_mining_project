"""
This file contains the code to get the different platforms from metacritic.com/games
and create the platforms.csv file
"""

import requests
from bs4 import BeautifulSoup
import csv

MAIN_URL = "https://www.metacritic.com"
GAMES_URL = "https://www.metacritic.com/game"
PLATFORMS_TABLE_FILENAME = "platforms.csv"
PLATFORMS_TABLE_HEADERS = ["id", "Name", "url"]


GET_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
URL_LOCATION = -2


def get_http(url):
    """
    This function get a url address and returns it http as a soup object
    """
    page = requests.get(url, headers=GET_HEADERS)
    if page.status_code != 200:
        raise ResourceWarning("Could not download the http")
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def main():
    """
    The main function will access /games and scrape the platforms and their urls. it will then send a list
    """


    # this is the scraping, uncomment it when done
    """
    try:
        games_soup = get_http(GAMES_URL)
    except ResourceWarning:
        exit()
    """

    # this is reading the html from file, comment it when scraping
    with open("temp_game_html.txt") as file:
        text_html = file.read()
        games_soup = BeautifulSoup(text_html, 'html.parser')
    # comment to this line

    platforms_module = games_soup.find('div', class_='platforms_wrap')
    platforms = platforms_module.find_all('li')

    id_num = 1
    platforms_list = []
    with open(PLATFORMS_TABLE_FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(PLATFORMS_TABLE_HEADERS)
        for platform in platforms:
            platform_name = platform.div.span.a.text
            platform_url = str(platform.div.span.a).split("\"")[URL_LOCATION]
            writer.writerow([id_num, platform_name, MAIN_URL + platform_url])
            id_num += 1






if __name__ == "__main__":
    main()