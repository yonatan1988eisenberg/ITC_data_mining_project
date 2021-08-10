from get_game_api_data import get_game_api_data
from get_consoles_and_scores import get_consoles_and_scores
from get_soup_general_data import get_soup_general_data


def scrape_game_page(soup, api_header):
    """
    This function gets a game's page soup and scrape it for the details. it returns a dictionary where every key
    is the column. The function also scrapes data from IGNB API using the provided header.
    """

    data = get_soup_general_data(soup)
    data.update(get_consoles_and_scores(soup))
    data.update(get_game_api_data(data['name_of_game'], api_header))

    # todo: handle player perspectives the same way as genres

    return data


