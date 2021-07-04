from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from main_menu_event import main_menu_event
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")

def genre_event():
    """
    This function prints to the user the available genres to search for and allows the user to choose one.
    It then prompt available platforms and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    """

    search_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + config_object['USER_QUESTIONS']['GAMES_URL']
    search_soup = http_to_soup(search_url)

    # a. get available genres and input from user
    search_soup, search_url = main_menu_event(search_soup, search_url, 'ul', 'genre_nav', case='genre')

    # b. get available platforms and input from user
    print(config_object['USER_QUESTIONS']['PLATFORMS'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 platform')

    # c. get available sort options and input from user
    print(config_object['USER_QUESTIONS']['SORT'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort')

    return search_soup, search_url
