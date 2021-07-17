from configparser import ConfigParser

# Get the configparser object
config_object = ConfigParser()

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

config_object['CREATE_DATABASE'] = {
    "LIST_OF_TABLES":
        'CREATE TABLE IF NOT EXISTS Publisher (Publisher_id int AUTO_INCREMENT PRIMARY KEY,\
         Publisher_name varchar(250), UNIQUE (Publisher_name))' '&&'

        'CREATE TABLE IF NOT EXISTS Developer (Developer_id int AUTO_INCREMENT PRIMARY KEY, \
        Developer_name varchar(250), UNIQUE (Developer_name))' '&&'

        'CREATE TABLE IF NOT EXISTS Age_Rating (Age_Rating_id int AUTO_INCREMENT PRIMARY KEY,\
        Age_Rating_name varchar(250), UNIQUE (Age_Rating_name))' '&&'

        'CREATE TABLE IF NOT EXISTS Consoles (Console_id int AUTO_INCREMENT PRIMARY KEY, \
        Console_name varchar(250), UNIQUE (Console_name))' '&&'

        'CREATE TABLE IF NOT EXISTS Genre (Genre_id int AUTO_INCREMENT PRIMARY KEY,\
         Genre_name varchar(250), UNIQUE (Genre_name))' '&&'

        'CREATE TABLE IF NOT EXISTS Game(Game_id int AUTO_INCREMENT PRIMARY KEY, Game_name varchar(250) UNIQUE, \
        Publisher_id int, \
        Developer_id int, Age_rating_id int, num_players varchar(250), Release_date varchar(250), \
        FOREIGN KEY(Publisher_id) REFERENCES Publisher(Publisher_id),  \
        FOREIGN KEY(Developer_id) REFERENCES Developer(Developer_id), FOREIGN KEY(Age_rating_id) \
        REFERENCES Age_Rating(Age_Rating_id)) ' '&&'

        ' CREATE TABLE IF NOT EXISTS game_to_console \
        ( Game_id INT NOT NULL references Console(Console_id), Console_id INT NOT NULL references Game(Game_id), \
        PRIMARY KEY(Game_id, Console_id))' '&&'

        ' CREATE TABLE IF NOT EXISTS Main_Scores( \
        Game_id int, Console_id int, Metascore int, Userscore float, Num_Metascore int, num_Userscore int, \
         FOREIGN KEY(Game_id) REFERENCES Game(Game_id), \
        FOREIGN KEY(Console_id) REFERENCES Consoles(Console_id))' '&&'

        ' CREATE TABLE IF NOT EXISTS PMN_user_scores( \
        Game_id int, Num_positive int, Num_mixed int, Num_negative int, FOREIGN KEY(Game_id) REFERENCES Game(Game_id))' '&&'

        ' CREATE TABLE IF NOT EXISTS PMN_critic_scores( \
        Game_id int, Num_positive int, Num_mixed int, Num_negative int,FOREIGN KEY(Game_id) REFERENCES Game(Game_id))',

    "LIST_OF_INSERTS":
        'INSERT INTO Publisher (Publisher_name) VALUE (%%s)' '&&'
        'INSERT INTO Developer (Developer_name) VALUE (%%s)' '&&'
        'INSERT INTO Age_rating (Age_Rating_name) VALUE (%%s)' '&&'
        'INSERT INTO Consoles (Console_name) VALUE (%%s)' '&&'
        'INSERT INTO Genre (Genre_name) VALUE (%%s)' '&&'
        'SELECT Publisher_id FROM Publisher WHERE Publisher_name = %%s' '&&'
        'SELECT Developer_id FROM Developer WHERE Developer_name = %%s' '&&'
        'SELECT Age_Rating_id FROM Age_rating WHERE Age_Rating_name = %%s' '&&'
        'INSERT INTO Game (Game_name, Publisher_id, Developer_id, Age_rating_id, num_players, '
        'Release_date) VALUE (%%s,%%s, %%s,%%s, %%s, %%s)' '&&'
        'SELECT Console_id From Consoles WHERE Console_name = %%s' '&&'
        'INSERT INTO game_to_console (Game_id, Console_id) Value (%%s,%%s)' '&&'
        'INSERT INTO main_scores (Game_id, Console_id, Metascore, Userscore, Num_Metascore, num_Userscore) '
        'VALUE (%%s,%%s,%%s,%%s,%%s,%%s)' '&&'
        'INSERT INTO PMN_user_scores (Game_id, Num_positive, Num_mixed, Num_negative) VALUES (%%s,%%s,%%s,%%s)' '&&'
        'INSERT INTO PMN_critic_scores (Game_id, Num_positive, Num_mixed, Num_negative) VALUES (%%s,%%s,%%s,%%s)',

    "CREATE_TRIAL": 'CREATE DATABASE IF NOT EXISTS trial_1',
    "USE_TRIAL": 'USE trial_1',
    "INSERT_GAME": 'INSERT INTO Game (Game_name, Publisher_id, Developer_id, Age_rating_id, num_players, '
                   'Release_date) ' 'VALUE (%%s,%%s, %%s,%%s, %%s, %%s)',
    "INSERT_MAIN": 'SELECT Console_id From Consoles WHERE Console_name = %%s',
    "PUBLISHER": 'publisher',
    "DEVELOPER": 'developer',
    "AGE_RATING": 'age rating',
    "MAIN_PLATFROM": 'main platform',
    "OTHER_CONSOLES": 'Other Consoles',
    "GENRES": 'Genres',
    "NAME_OF_GAME": 'name of game',
    "PUB_ID": 'Publisher_id',
    "DEV_ID": 'Developer_id',
    "AGE_ID": 'Age_Rating_id',
    "NUM_PLAYERS": 'num players',
    "REL_DATE": 'release date',
    "CONSOLE_ID": 'Console_id',
    "METASCORE": 'metascore',
    "USER_SCORE": 'user score',
    "NUM_MET_REV": 'number of metascore reviewers',
    "NUM_USER_REV": 'number of user reviews',
    "USER_POS": 'user review positive',
    "USER_MIX": 'user review mixed',
    "USER_NEG": 'user review negative',
    "CRITIC_POS": 'critic review_positive',
    "CRITIC_MIX": 'critic review mixed',
    "CRITIC_NEG": 'critic review negative'
}

with open('config.ini', 'w') as conf:
    config_object.write(conf)
