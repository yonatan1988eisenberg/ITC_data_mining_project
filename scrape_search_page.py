from http_to_soup import http_to_soup
from tqdm import tqdm
from scrape_game_page import scrape_game_page
from configparser import ConfigParser
from insert_row_to_database import insert_row_to_database
from init_mysql_conn import init_mysql_conn, sql_query
from create_tables import create_tables
from update_twitch_header import update_twitch_header

config_object = ConfigParser()
config_object.read("config.ini")
# todo: implement multi-threading to speed up to process
# todo: clean up, move queries/constants to config file
# todo: decide how to handle the password part


def scrape_search_page(search_soup, search_url, num_of_articles_to_fetch, logger):
    """
    This function gets a soup and a url to a search page and fetch the first num_of_articles_to_fetch from
    it into a mysql local server
    :return: num_of_articles_to_fetch if successful, otherwise False
    """

    api_header = update_twitch_header()
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
                # insert_row_to_table(get_game_api_data(article_soup))
                data_dict = scrape_game_page(article_soup, api_header)
                # insert_row_to_database(data_dict, sql_conn)
                articles_fetched += insert_row_to_database(data_dict, sql_conn)
                pbar.update()
                if articles_fetched == num_of_articles_to_fetch:
                    print("done!, you can find your data in your Data Base")
                    logger.info('fetched the articles')
                    return num_of_articles_to_fetch
            # if we finished the page but need more articles, go to the next page
            pages = search_soup.find('span', class_="flipper next")
            if pages:
                next_page = pages.a.get('href')
            search_soup = http_to_soup(config_object['USER_QUESTIONS']['DOMAIN_URL'] + next_page)

    print("error scraping!")
    logger.warning('encountered error while fetching articles')
    return False
