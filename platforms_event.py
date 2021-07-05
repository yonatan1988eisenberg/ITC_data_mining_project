from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from main_menu_event import main_menu_event
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")


def platforms_event(search_code):
    """
    This function prints to the user the available platforms to search for and allows the user to choose one.
    It then prompt available time frames and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    """
    search_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + config_object['USER_QUESTIONS']['GAMES_URL']
    search_soup = http_to_soup(search_url)
    if search_code is None:
        search_code = [None, None, None, None]
    # a. get available platforms and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['PLATFORMS'])
    search_soup, search_url = main_menu_event(search_soup, search_url, 'div', 'platforms_wrap',
                                              case='platform', search_code=search_code[1])
    # updating url - go to "platform -> all the games" page (search page)
    search_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + search_soup.find('div',
                                                                                  class_='foot_wrap').span.a.get('href')
    search_soup = http_to_soup(search_url)

    # b. get available time frames and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['TIMEFRAME'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 filter',
                                             search_code=search_code[2])

    # c. get available sort options and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['SORT'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort',
                                             search_code=search_code[3])

    return search_soup, search_url
