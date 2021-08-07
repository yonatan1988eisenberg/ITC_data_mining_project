from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")


def time_frame_event(search_code):
    """
    This function prints to the user the available time frames to search for and allows the user to choose one.
    It then prompt available years, platforms and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    """
    # (search page)
    search_url = config_object['USER_QUESTIONS']['DOMAIN_URL'] + config_object['TIMEFRAME']['TIME_FRAME_URL']
    search_soup = http_to_soup(search_url)
    if search_code is None:
        search_code = [None, None, None, None, None]
    else:
        if len(search_code) == 4 and search_code[1] != 2:
            temp_sc = [search_code[0], search_code[1], None, search_code[2], search_code[3]]
            search_code = temp_sc

    # a. get available data frames and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['TIMEFRAME'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 filter',
                                             search_code=search_code[1])

    # if year was chosen choose a year as well
    if "year" in search_url:
        if search_code[0] is None:
            print(config_object['USER_QUESTIONS']['YEARS'])
        search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 year',
                                                 search_code=search_code[2])

    # b. get available platforms and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['PLATFORMS'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 platform',
                                             search_code=search_code[3])

    # c. get available sort options and input from user
    if search_code[0] is None:
        print(config_object['USER_QUESTIONS']['SORT'])
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort',
                                             search_code=search_code[4])

    return search_soup, search_url
