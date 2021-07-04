from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")


def time_frame_event():
    """
    This function prints to the user the available time frames to search for and allows the user to choose one.
    It then prompt available years, platforms and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    :return:
    """
    search_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + config_object['TIMEFRAME']['TIME_FRAME_URL']  # (search page)
    search_soup = http_to_soup(search_url)

    # a. get available data frames and input from user
    print(config_object['USER_QUESTIONS']['TIMEFRAME'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 filter')
    # if year was chosen choose a year as well
    if "Year" in search_url:
        print(config_object['USER_QUESTIONS']['YEARS'])
        search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 year')

    # b. get available platforms and input from user
    print(config_object['USER_QUESTIONS']['PLATFORMS'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 platform')

    # c. get available sort options and input from user
    print(config_object['USER_QUESTIONS']['SORT'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort')

    return search_soup, search_url