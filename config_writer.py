from configparser import ConfigParser

# Get the configparser object
config_object = ConfigParser()
# todo: arrange to config writer according to type of data (urls, constants..) and not according to function
config_object['USER_QUESTIONS'] = {
    "DOMAIN_URL": "https://www.metacritic.com",
    "GAMES_URL": "/game",
    "PLATFORMS": "The available platforms are",
    "TIMEFRAME": "The available time frames to search are:",
    "SORT": "The available sort options are available:",
    "YEARS": "The available years to search are:"
}

config_object['MAIN'] = {
    'MAIN_MENU_LIST': ['Games by platform', 'Games by genre', 'Games by time frame'],
    'WELCOME': 'Welcome user!',
    'FAREWELL': 'no results found, goodbye!',
    'NUM_FETCH': 'total results found. How many would you like to fetch?"'
}

config_object['TIMEFRAME'] = {
    "TIME_FRAME_URL": "/browse/games/score/metascore/all/all/filtered"
}

config_object['SCRAPE_SEARCH_PAGE'] = {
    "FILE_NAME": "db.csv"
}

config_object['CHECK_INPUT'] = {
    "CHOICE": "Please enter your choice:",
    "INVALID": "Invalid integer was given"
}

config_object["MAIN_EVENT"] = {
    "EXCLUDE_LEGACY": '-1'
}

config_object['SCRAPE_PLATFORM'] = {
    'PLATFORMS_TABLE_FILENAME': 'platforms.csv',
    'PLATFORM_ID': '0',
    'PLATFORM_NAME': '1',
    'PLATFORM_URL': '2',
    'ARTICLES_TABLE_HEADERS': ["id", "Title", "url"],
    'DATA_FOLDER': "./data/",
    'URL_LOCATION': '3',
    'ARTICLE_URL_HEAD': "https://www.metacritic.com"
}

config_object['SCRAPE_CATEGORY'] = {
    'GAMES_URL': "https://www.metacritic.com/game",
    'PLATFORM_URL_HEAD': "https://www.metacritic.com/browse/games/release-date/new-releases/",
    'SORTING_OPTIONS': ["/date", "/metascore"],
    'SORT_BY_DATE': '0',
    'SORT_BY_METASCORE': '1',
    'PLATFORMS_TABLE_FILENAME': "platforms.csv",
    'PLATFORMS_TABLE_HEADERS': ["id", "Name", "url"],
    'GET_HEADERS': {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"},
    'URL_LOCATION': -2
}

config_object['FINAL_DATA_SCRAPE'] = {
    'HEADER_LIST': ['name of game', 'main platform', 'publisher', 'release date', 'Other Consoles',
                    'metascore', 'number of metascore reviewers', 'user score', 'number of user reviews',
                    'developer', 'num players', 'Genres', 'age rating', 'critic review_positive',
                    'critic review mixed', 'critic review negative', 'user review positive',
                    'user review mixed', 'user review negative']
}

config_object['LIST_OF_DATA'] = {
        "name of game": '0',
        "main platform": '1',
        "publisher": '2',
        "release date": '3',
        "Other Consoles": '4',
        "metascore": '5',
        "number of metascore reviewers": '6',
        "user score": '7',
        "number of user reviews": '8',
        "developer": '9',
        "num players": '10',
        "Genres": '11',
        "age rating": '12',
        "critic review_positive": '13',
        "critic review mixed": '14',
        "critic review negative": '15',
        "user review positive": '16',
        "user review mixed": '17',
        "user review negative": '18'

}

with open('config.ini', 'w') as conf:
    config_object.write(conf)
