
from print_submenu import print_submenu
from http_to_soup import http_to_soup

DOMAIN_URL = "https://www.metacritic.com"


def dropdown_event(soup, search_url, html_class):
    """
    This function gets a soup and search parameters to print the user options to choose from.
    :param soup: current soup working on
    :param search_url: current url searching in
    :param html_class: of the dropdown/sort menu
    :return: updated soup and search_url
    """
    module = soup.find('div', class_=html_class)
    submodule = module.find('ul', class_='dropdown')
    dropdown_list = submodule.find_all('li')
    # either option.a.text or option.span.text holds names
    user_dropdown = dropdown_list[print_submenu([option.a.text.strip() if option.a is not None else
                                                 option.span.text.strip() for option in dropdown_list])]
    # updating search url and soup if needed:
    # if different than the default option was chosen
    # .span.a holds link for default option
    if user_dropdown.a is not None:
        search_url = DOMAIN_URL + user_dropdown.a.get('href')
        soup = http_to_soup(search_url)

    return soup, search_url
