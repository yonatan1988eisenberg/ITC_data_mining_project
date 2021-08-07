from http_to_soup import http_to_soup
from get_scores_and_dev_from_soup import get_scores_and_dev_from_soup
from configparser import ConfigParser


def get_consoles_and_scores(soup):
    """
    This function gets a game's soup and returns a dictionary of dictionaries containing the consoles and scores.
    The dictionary format is {'console1': {score1: x, score2: y}, 'console2': {score1: w, score2: z}..}
    """

    config_object = ConfigParser()
    config_object.read("config.ini")

    data_dict = {'consoles': {}}

    # handle the main console and scores
    main_console = soup.find('span', class_='platform')
    if main_console:
        main_console = main_console.text.strip()
        data_dict['consoles'][main_console] = get_scores_and_dev_from_soup(soup)

    # handle other consoles
    other_consoles = soup.find('li', class_='summary_detail product_platforms')
    if other_consoles:
        other_consoles = other_consoles.find_all('a', class_='hover_none')
        for console in other_consoles:
            name = console.text
            url = console.get('href')
            data_dict['consoles'][name] = get_scores_and_dev_from_soup(http_to_soup(
                config_object['USER_QUESTIONS']['DOMAIN_URL'] + url))

    return data_dict


