"""
This file contains the code to get the different platforms from the platforms.csv file
it than scrapes each platform url and construct the article
"""
from scrape_category import http_to_soup
import csv
from time import sleep


PLATFORMS_TABLE_FILENAME = "platforms.csv"
PLATFORM_ID = 0
PLATFORM_NAME = 1
PLATFORM_URL = 2

ARTICLES_TABLE_HEADERS = ["id", "Title", "url"]
DATA_FOLDER = "./data/"
URL_LOCATION = 3
ARTICLE_URL_HEAD = "https://www.metacritic.com"


def read_table(filename):
    """
    This function gets a filename to a csv table and reads it. it returns the the fields and rows of the file
    """

    rows = []
    with open(filename, "r") as source_file:
        reader = csv.reader(source_file)
        fields = next(reader)
        for row in reader:
            rows.append(row)

    return rows, fields


def main():
    """
    The main function will:
    1. get the platforms details from the platforms csv file
    2. scrape each platform for its articles and writing their name and url to a csv file
    """


    # get the list of platforms from the platforms csv file
    platforms_list, platforms_fields = read_table(PLATFORMS_TABLE_FILENAME)

    # scrape all the platforms url pages
    for platform in platforms_list:
        platform_soup = http_to_soup(platform[PLATFORM_URL])
        articles = platform_soup.find_all('td', class_='clamp-summary-wrap')
        id_num = 1
        with open(DATA_FOLDER + platform[PLATFORM_NAME] + ".csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(ARTICLES_TABLE_HEADERS)
            for article in articles:
                article_name = article.h3.text
                article_url = str(article.find('a', class_='title')).split("\"")[URL_LOCATION]
                writer.writerow([id_num, article_name, ARTICLE_URL_HEAD + article_url])
                id_num += 1
        sleep(5)


if __name__ == "__main__":
    main()
