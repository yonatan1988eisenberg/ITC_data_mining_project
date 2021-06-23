from http_to_soup import http_to_soup
from dropdown_event import dropdown_event
from main_menu_event import main_menu_event
from print_submenu import print_submenu
from get_num_of_articles_from_soup import get_num_of_articles_from_soup
from scrape_search_page import scrape_search_page
DOMAIN_URL = "https://www.metacritic.com"
GAMES_URL = "/game"
TIME_FRAMES_URL = "/browse/games/score/metascore/all/all/filtered"



def main():
    """
    The main function will
    1. gets input from the user
    2. call the functions to scrape the data
    3. print the data to the console
    :return:
    """
    main_menu_list = ['Games by platform', 'Games by genre', 'Games by time frame']
    # 1:
    print("Welcome user!\n")
          # "Data can be searched in a few methods:\n"
          # "0. Games by platform\n"
          # "1. Games by genre\n"
          # "2. Games by time frame\n")
    # user_menu = int(input("Please enter your choice:"))
    user_menu = print_submenu(main_menu_list)
    if user_menu == 0:
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

        print(search_url)

    elif user_menu == 1:
        search_url = DOMAIN_URL + GAMES_URL
        search_soup = http_to_soup(search_url)

        # a. get available genres and input from user
        search_soup, search_url = main_menu_event(search_soup, search_url, 'ul', 'genre_nav', case='genre')

        # b. get available platforms and input from user
        print("The available platforms to search are:")
        search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style2 platform')

        # c. get available sort options and input from user
        print("The available sort options are available:")
        search_soup, search_url = dropdown_event(search_soup, search_url, 'mcmenu dropdown style1 sort')

        print(search_url)

    elif user_menu == 2:
        search_url = DOMAIN_URL + TIME_FRAMES_URL   # (search page)
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

        print(search_url)

    # num_of_articles_to_fetch = input(f"There are {get_num_of_articles_from_soup(search_soup)} results\n"
    #                                  f"How many would you like to fetch?")
    #
    # scrape_search_page(search_soup, search_url, num_of_articles_to_fetch)

if __name__ == "__main__":
    main()
