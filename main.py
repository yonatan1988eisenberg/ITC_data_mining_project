from print_submenu import print_submenu
from get_num_of_articles_from_soup import get_num_of_articles_from_soup
from scrape_search_page import scrape_search_page
from check_input import check_input
from platforms_event import platforms_event
from genre_event import genre_event
from time_frame_event import time_frame_event
from http_to_soup import http_to_soup
from configparser import ConfigParser
import argparse
import sys


config_object = ConfigParser()
config_object.read("config.ini")


def main():
    """
    The main function will
    1.check if running through CLI or printing to stdio (if --search_code was inserted)
    2. call the relevant functions
    :return:
    """
    my_parser = argparse.ArgumentParser(description='This program helps the user navigate throught metacritic.com/game '
                                                    'to a search page. It does so by getting input from user on '
                                                    'available search parameters such as platform, dates etc.\n'
                                                    'This program can be run in two modes:\n 1. manually (when search_'
                                                    'code is not provided)\n 2. automaticly When the program is run'
                                                    ' manually it will help the user find the search page he is looking'
                                                    ' for by prompting available options.\n'
                                                    ' In auto-mode the user knows which search page is he looking for'
                                                    ' and knows the code to get there. If the code is uknown run the '
                                                    'program manually and the search code is the cancatanation of your'
                                                    ' input.\n usage in auto-mode: [program_name] [options]')
    my_parser.add_argument('--search_code', '-sc',
                           default=None,
                           type=str,
                           help='a sting of ints indicating the search page the user whishes to scrape. if the search '
                                'code is too long the program will use its first n digits. If not provided the program '
                                'will run on manual mode.')
    my_parser.add_argument('--fetch', '-f',
                           default=100,
                           type=int,
                           help='int; the number of articles to fetch from the search page. default is 100. Can be used'
                                ' only in combination with search_code.')
    my_parser.add_argument('--asc', '-a',
                           default=False,
                           type=bool,
                           help='bool; some search pages allow to sort the results ascending. if a code to such a '
                                'search page was used asc can be chossen as True. default is False. Can be used only'
                                ' in combination with search_code.')
    args = my_parser.parse_args()

    # if in manual mode: print the menu
    # else: validate search_code
    if args.search_code is None:
        print(config_object["MAIN"]["WELCOME"])
        user_menu = print_submenu(config_object["MAIN"]["MAIN_MENU_LIST"])
    elif not args.search_code.isdigit():
        print('invalid search code')
        exit()
    else:
        user_menu = int(args.search_code[0])
    try:
        # ask the user for additional input, get to the relevant search page and obtain it's html
        if user_menu == 0:
            search_soup, search_url = platforms_event(args.search_code)

        elif user_menu == 1:
            search_soup, search_url = genre_event(args.search_code)

        elif user_menu == 2:
            search_soup, search_url = time_frame_event(args.search_code)
    except IndexError as er:
        print(str(er) + '; could be invalid search code, too short etc.')
        exit()

    # check for the number of available games and ask the user how many he would like to fetch
    try:
        num_of_articles_found = get_num_of_articles_from_soup(search_soup)
    except UnboundLocalError as er:
        print(str(er) + '; search page missing. could be invalid search code, try running the program on manual mode')
        exit()

    # if no results were found on the site
    if num_of_articles_found == 0:
        print(config_object['MAIN']['FAREWELL'])
        exit()

    # if we are in manual mode: check if we can sort by ascending and get the number of articles to fetch
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
    # fetch the articles
    scrape_search_page(search_soup, search_url, int(num_to_fetch))


if __name__ == "__main__":
    main()
