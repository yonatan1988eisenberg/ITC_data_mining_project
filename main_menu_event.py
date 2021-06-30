

from print_submenu import print_submenu
from http_to_soup import http_to_soup


DOMAIN_URL = "https://www.metacritic.com"
EXCLUDE_LEGACY = -1


def main_menu_event(soup, search_url, header, options_class, case):
    """
    This function gets a soup and search parameters to print the user options to choose from.
    :param soup: the html soup object we're looking at
    :param search_url: the soup's url
    :param header: the object type we're looking for
    :param options_class: the object class we're looking for
    :param case: a flag allowing the function to deal with both platforms and genre main menu choices
    :return: updated soup and url
    """
    module = soup.find(header, class_=options_class)
    options_list = module.find_all('li')
    if case == 'platform':
        options_names = [option.div.span.a.text if option.div.span.a is not None
                         else option.a.text for option in options_list[:EXCLUDE_LEGACY]]
    elif case == 'genre':
        options_names = [option.a.text for option in options_list]

    user_option = options_list[print_submenu(options_names)]
    # updating url and soup
    # either user_option.a or user_option.span.a holds the url
    if user_option.a is not None:
        search_url = DOMAIN_URL + user_option.a.get('href')
    else:
        search_url = DOMAIN_URL + user_option.span.a.get('href')

    soup = http_to_soup(search_url)

    return soup, search_url
