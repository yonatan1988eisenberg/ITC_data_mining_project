from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from main_menu_event import main_menu_event

DOMAIN_URL = "https://www.metacritic.com"
GAMES_URL = "/game"


def platforms_event():
    """
    This function prints to the user the available platforms to search for and allows the user to choose one.
    It then prompt available time frames and sort options for the user to choose.
    :return: a soup object and its url pointing to the relevant search page on metacritic.com
    """
    search_url = DOMAIN_URL + GAMES_URL
    search_soup = http_to_soup(search_url)

    # a. get available platforms and input from user
    print("The available platforms are:")
    search_soup, search_url = main_menu_event(search_soup, search_url, 'div', 'platforms_wrap',
                                              case='platform')
    # updating url - go to "platform -> all the games" page (search page)
    search_url = DOMAIN_URL + search_soup.find('div', class_='foot_wrap').span.a.get('href')
    search_soup = http_to_soup(search_url)

    # b. get available time frames and input from user
    print("The available time frames to search are:")
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 filter')

    # c. get available sort options and input from user
    print("The available sort options are available:")
    search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort')

    return search_soup, search_url
