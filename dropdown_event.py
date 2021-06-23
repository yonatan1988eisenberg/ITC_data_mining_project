from get_dropdown_options_names import get_dropdown_options_names
from print_submenu import print_submenu
from http_to_soup import http_to_soup

DOMAIN_URL = "https://www.metacritic.com"


def dropdown_event(soup, search_url, html_class, case_sort=False):
    """
    This function gets a soup and search parameters to print the user options to choose from.
    :param soup: current soup working on
    :param search_url: current url searching in
    :param html_class: of the dropdown/sort menu
    :param case_sort: a flag to be risen in the case of a sort menu
    :return: updated soup and search_url
    """
    dropdown_list = get_dropdown_options_names(soup, html_class)
    user_dropdown = dropdown_list[print_submenu([option.a.text.strip() if option.a is not None else
                                                 option.span.text.strip() for option in dropdown_list])]
    """
    ^^^ either option.a.text or option.span.text holds names
    """
    # updating search url if needed
    if user_dropdown.a is not None:
        """
        if a different than the default option was chosen.
        .span.a holds link for default option
        """
        search_url = DOMAIN_URL + user_dropdown.a.get('href')
        if not case_sort:
            soup = http_to_soup(search_url)

    return soup, search_url
