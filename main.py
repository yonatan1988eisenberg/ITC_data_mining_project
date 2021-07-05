from print_submenu import print_submenu
from get_num_of_articles_from_soup import get_num_of_articles_from_soup
from scrape_search_page import scrape_search_page
from check_input import check_input
from platforms_event import platforms_event
from genre_event import genre_event
from time_frame_event import time_frame_event
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")



def main():
    """
    The main function will
    1. gets input from the user
    2. call the functions to scrape the data
    3. print the data to the console
    :return:
    """

    print(config_object["MAIN"]["WELCOME"])
    user_menu = print_submenu(config_object["MAIN"]["MAIN_MENU_LIST"])

    # ask the user for additional input, get to the relevant search page and obtain it's html
    if user_menu == 0:
        search_soup, search_url = platforms_event()

    elif user_menu == 1:
        search_soup, search_url = genre_event()

    elif user_menu == 2:
        search_soup, search_url = time_frame_event()

    # check for the number of available games and ask the user how many he would like to fetch
    num_of_articles_found = get_num_of_articles_from_soup(search_soup)
    if num_of_articles_found == 0:
        print(config_object['MAIN']['FAREWELL'])
        exit()

    print(f"{num_of_articles_found}", config_object['MAIN']['NUM_FETCH'])
    num_of_articles_to_fetch = check_input(num_of_articles_found)
    # fetch the articles
    scrape_search_page(search_soup, search_url, int(num_of_articles_to_fetch))


if __name__ == "__main__":
    main()
