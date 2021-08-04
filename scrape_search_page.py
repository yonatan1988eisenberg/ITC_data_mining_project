from http_to_soup import http_to_soup
from tqdm import tqdm
from final_data_scrape import scrape_data
from configparser import ConfigParser
from insert_row_to_database import insert_row_to_database
from init_mysql_conn import init_mysql_conn, sql_query
import getpass
from create_tables import create_tables
from insert_row_to_table import insert_row_to_table
import csv

config_object = ConfigParser()
config_object.read("config.ini")



def scrape_search_page(search_soup, search_url, num_of_articles_to_fetch, logger):
    """
    This function gets a soup and a url to a search page and fetch the first num_of_articles_to_fetch from
    it into a csv file
    :return: True if successful, otherwise False
    """

    db_name = "metacritic_db"
    logger.info('fetching the articles')
    articles_fetched = 0
    # initialize mysql connection
    password = 'pnmqcX78k' #input('please enter mysql password:')
    sql_conn = init_mysql_conn(password=password)
    # check if the database already exists. If not, create it and the tables
    # sql_query(sql_conn, 'DROP DATABASE metacritic_db')

    if not sql_query(sql_conn, 'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s;', db_name):
        sql_query(sql_conn, f'CREATE DATABASE {db_name};')
        sql_conn = init_mysql_conn(password=password, db=db_name)
        create_tables(sql_conn)
    sql_conn = init_mysql_conn(password=password, db=db_name)

    # start scraping the articles from the search page
    with tqdm(desc='fetching data', total=num_of_articles_to_fetch) as pbar:
        # while we haven't fetch enough articles, find all the articles in the page
        while articles_fetched < num_of_articles_to_fetch:
            articles = search_soup.find_all('td', class_='clamp-summary-wrap')
            # for every article in the page, get its url and send to the function which scrape the data from it
            # and than update counter etc
            for article in articles:
                article_url = article.find('a', class_='title')
                article_url = article_url.get('href')
                article_soup = http_to_soup(config_object['USER_QUESTIONS']['DOMAIN_URL'] + article_url)
                # insert_row_to_table(scrape_data(article_soup))
                data_dict = scrape_data(article_soup)
                # todo implement a function which scrapes the data from the API and adds it to data_dict
                # insert_row_to_database(data_dict, sql_conn)
                articles_fetched += insert_row_to_database(data_dict, sql_conn)
                pbar.update()
                if articles_fetched == num_of_articles_to_fetch:
                    print("done!, you can find your data in your Data Base")
                    logger.info('fetched the articles')
                    return num_of_articles_to_fetch
            # if we finished the page but need more articles, go to the next page
            pages = search_soup.find('ul', class_="pages")
            pages = pages.find_all('li')
            for j in range(len(pages) - 1):
                if pages[j].a is None:
                    next_page = pages[j + 1].a.get("href")
            search_soup = http_to_soup(config_object['USER_QUESTIONS']['DOMAIN_URL'] + next_page)

    print("error scraping!")
    logger.warning('encountered error while fetching articles')
    return
