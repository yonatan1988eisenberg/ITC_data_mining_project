from http_to_soup import http_to_soup
from configparser import ConfigParser
from check_input import check_input

config_object = ConfigParser()
config_object.read("config.ini")


def asc_and_fetch_event(args, search_soup, search_url, num_of_articles_found, logger):
    """
    In the case the search results can be oreder by ascending order, this function will prompt the question to the uses
    (in menual mode) or use the arg in (in CLI mode) to determine if it should be done (and updates search soup and url)
    :param args: the input arguments (CLI mode)
    :param search_soup: the current search soup
    :param search_url: the current search url
    :param num_of_articles_found: the maximum num of article to fetch
    :param logger: a handle to the program's logger
    :return: updated search soup and url and the number or article to fetch
    """
    logger.info('fetching the number of available to fetch')

    if args.search_code is None:
        if 'desc' in search_url:
            asc = input('do you want to sort by ascending? y for yes, anything else for no')
            if asc == 'y':
                search_url = search_url.replace("desc", "asc")
                search_soup = http_to_soup(search_url)
        print(f"{num_of_articles_found}", config_object['MAIN']['NUM_FETCH'])
        num_to_fetch = check_input(num_of_articles_found)
    else:
        num_to_fetch = args.fetch
        # CLI mode: check if we can order by ascending
        if args.asc is True and 'desc' in search_url:
            search_url = search_url.replace("desc", "asc")
            search_soup = http_to_soup(search_url)
    logger.info('fetched the number of available to fetch')

    return search_soup, search_url, num_to_fetch
