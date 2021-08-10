from init_mysql_conn import sql_query


# todo: uncomment once player perspectives is handled the same way as genres
def create_tables(sql_conn):
    """
    This function creates the database tables by running a series of queries
    """

    tables_creation_queries = [
        'CREATE TABLE publishers (\
        id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE developers (\
        id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE age_ratings (\
        id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE franchises (\
        id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE game_engines (\
        id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE player_perspectives (\
        id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE games(\
        id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) UNIQUE, \
        publisher_id int, \
        age_rating_id int, \
        franchise_id int, \
        game_engine_id int, \
        num_players varchar(250), \
        release_date varchar(250), \
        perspective_id int, \
        FOREIGN KEY(publisher_id) REFERENCES publishers(id), \
        FOREIGN KEY(perspective_id) REFERENCES player_perspectives(id), \
        FOREIGN KEY(franchise_id) REFERENCES franchises(id), \
        FOREIGN KEY(game_engine_id) REFERENCES game_engines(id), \
        FOREIGN KEY(age_rating_id) REFERENCES age_ratings(id))',
        # developer_id int, \
        # FOREIGN KEY(developer_id) REFERENCES developers(id), \
        # FOREIGN KEY(game_engine_id) REFERENCES game_engines(id), \
        # FOREIGN KEY(franchise_id) REFERENCES franchises(id), \
        # franchise_id int, \
        # game_engine_id int, \
 


        'CREATE TABLE consoles (\
        id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE genres (\
        id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) NOT NULL, \
        UNIQUE (name))',

        'CREATE TABLE game_to_console( \
        game_id INT NOT NULL references games(id), \
        console_id INT NOT NULL references consoles(id), \
        PRIMARY KEY(game_id, console_id))',

        # 'CREATE TABLE game_to_perspective (\
        # game_id INT NOT NULL references games(id), \
        # perspective_id INT NOT NULL references player_perspectives(id), \
        # PRIMARY KEY(game_id, perspective_id))',

        'CREATE TABLE game_to_genre( \
        game_id INT NOT NULL references games(id), \
        genre_id INT NOT NULL references genres(id), \
        PRIMARY KEY(game_id, genre_id))',

        'CREATE TABLE game_to_developer( \
        game_id INT NOT NULL references games(id), \
        developer_id INT NOT NULL references developers(id), \
        console_id INT NOT NULL references consoles(id), \
        PRIMARY KEY(game_id, developer_id, console_id))',

        'CREATE TABLE main_scores( \
        game_id int, \
        console_id int, \
        metascore varchar(250), \
        userscore varchar(250), \
        num_metascore varchar(250), \
        num_userscore varchar(250), \
        FOREIGN KEY(game_id) REFERENCES games(id), \
        FOREIGN KEY(console_id) REFERENCES consoles(id))',

        'CREATE TABLE user_scores( \
        game_id int, \
        console_id int, \
        num_positive varchar(250), \
        num_mixed varchar(250), \
        num_negative varchar(250), \
        FOREIGN KEY(game_id) REFERENCES games(id))',

        'CREATE TABLE critic_scores( \
        game_id int, \
        console_id int, \
        num_positive varchar(250), \
        num_mixed varchar(250), \
        num_negative varchar(250), \
        FOREIGN KEY(game_id) REFERENCES games(id))'
    ]

    for query in tables_creation_queries:
        sql_query(sql_conn, query)
