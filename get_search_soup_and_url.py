from platforms_event import platforms_event
from genre_event import genre_event
from time_frame_event import time_frame_event


def get_search_soup_and_url(search_code, user_menu, logger):
    """
    This fucntion prompt the user for the ssearch parameters (manual mode) and sends the search code (CLI mode)
    :param search_code: the input search code (=None if manual mode)
    :param user_menu: the chosen menu option (manual mode)
    :param logger: a handle to the program's logger
    :return: the search soup and url
    """

    logger.info('fetching search soup and url')

    if user_menu == 0:
        search_soup, search_url = platforms_event(search_code)

    elif user_menu == 1:
        search_soup, search_url = genre_event(search_code)

    elif user_menu == 2:
        search_soup, search_url = time_frame_event(search_code)

    logger.info('fetched search soup and url')

    return search_soup, search_url
