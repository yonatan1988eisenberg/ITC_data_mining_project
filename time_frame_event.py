from http_to_soup import http_to_soup
from dropdown_event import dropdown_event

DOMAIN_URL = "https://www.metacritic.com"
TIME_FRAMES_URL = "/browse/games/score/metascore/all/all/filtered"


def time_frame_event():
    """
    This function prints to the user the available time frames to search for and allows the user to choose one.
    It then prompt available years, platforms and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    :return:
    """
    search_url = DOMAIN_URL + TIME_FRAMES_URL  # (search page)
    search_soup = http_to_soup(search_url)

    # a. get available data frames and input from user
    print("The available time frames to search are:")
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 filter')
    # if year was chosen choose a year as well
    if "Year" in search_url:
        print("The available years to search are:")
        search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 year')

    # b. get available platforms and input from user
    print("The available platforms to search are:")
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 platform')

    # c. get available sort options and input from user
    print("The available sort options are available:")
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort')

    return search_soup, search_url
