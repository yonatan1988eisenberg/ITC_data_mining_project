from print_submenu import print_submenu
from get_num_of_articles_from_soup import get_num_of_articles_from_soup
from scrape_search_page import scrape_search_page
from configparser import ConfigParser
from parse_args import parse_args
from init_logger import init_logger
from asc_and_fetch_event import asc_and_fetch_event
from get_search_soup_and_url import get_search_soup_and_url


config_object = ConfigParser()
config_object.read("config.ini")
# todo: split main into functions
# todo: implement the logger in more places. add all kinds of massages
# todo: multi-threading!
# todo: combine functions into files to reduce the number of files


def main():
    """
    The main function calls all the functions needed to run this program.
    """

    # config logger
    logger = init_logger()
    logger.info('STARTED RUNNING')
    # parse args
    args = parse_args()

    # if in manual mode: print the menu
    # else: validate search_code
    if args.search_code is None:
        print(config_object["MAIN"]["WELCOME"])
        user_menu = print_submenu(config_object["MAIN"]["MAIN_MENU_LIST"])
    elif not args.search_code.isdigit():
        print('invalid search code')
        logger.fatal('invalid search code - terminating')
        exit()
    else:
        print('Please hold.')
        user_menu = int(args.search_code[0])

    # get the search soup and url
    try:
        # ask the user for additional input, get to the relevant search page and obtain it's html
        search_soup, search_url = get_search_soup_and_url(args.search_code, user_menu, logger)
    except IndexError as er:
        print(str(er) + '; could be invalid search code, too short etc.')
        logger.fatal('could not get search soup and url - terminating')
        exit()

    # check for the number of available games
    # todo: check what happens if -fetch is larger than available games
    try:
        num_of_articles_found = get_num_of_articles_from_soup(search_soup, logger)
    except UnboundLocalError as er:
        print(str(er) + '; search page missing. could be invalid search code, try running the program on manual mode')
        logger.fatal('could not get the number of available articles - terminating')
        exit()

    # if no results were found on the site
    if num_of_articles_found == 0:
        print(config_object['MAIN']['FAREWELL'])
        logger.fatal('no articles found - terminating')
        exit()

    # if we are in manual mode: check if we can sort by ascending and get the number of articles to fetch
    search_soup, search_url, num_to_fetch = asc_and_fetch_event(args, search_soup, search_url,
                                                                num_of_articles_found, logger)

    # fetch the articles
    scrape_search_page(search_soup, search_url, int(num_to_fetch), logger)

    logger.info('FINISHED RUNNING')


if __name__ == "__main__":
    main()
