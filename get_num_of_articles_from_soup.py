from http_to_soup import http_to_soup
MAX_ARTICLES_PER_PAGE = 100
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")


def get_num_of_articles_from_soup(soup, logger):
    """
    This function gets a search page's soup and returns the number of available games
    """

    logger.info('fetching the number of available articles')

    max_pages = soup.find('li', class_="page last_page")
    if max_pages is None:
        articles = soup.find_all('td', class_='clamp-summary-wrap')
        logger.info('fetched the number of available articles')
        return len(articles)
    else:
        max_page_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + max_pages.a.get('href')
        soup = http_to_soup(max_page_url)
        articles = soup.find_all('td', class_='clamp-summary-wrap')
        logger.info('fetched the number of available articles')
        return len(articles) + (int(max_pages.a.text) * MAX_ARTICLES_PER_PAGE)

