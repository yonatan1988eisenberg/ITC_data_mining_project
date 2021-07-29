import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
from init_mysql_conn import sql_query

config_object = ConfigParser()
config_object.read("config.ini")


def create_tables(connection):

    tables_creation_queries = [
        'CREATE TABLE publishers (id int AUTO_INCREMENT PRIMARY KEY,\
                 name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Developer (Developer_id int AUTO_INCREMENT PRIMARY KEY, \
        Developer_name varchar(250) NOT NULL, UNIQUE (Developer_name))',

        'CREATE TABLE Age_Rating (Age_Rating_id int AUTO_INCREMENT PRIMARY KEY,\
        Age_Rating_name varchar(250) NOT NULL, UNIQUE (Age_Rating_name))',

        'CREATE TABLE Franchise (Franchise_id int PRIMARY KEY,\
        Franchise_name varchar(250) NOT NULL, UNIQUE (Franchise_name))',

        'CREATE TABLE Game_engine (Game_engines_id int PRIMARY KEY,\
        game_engines_name varchar(250) NOT NULL, UNIQUE (game_engines_name))',

        'CREATE TABLE Player_perspectives (player_perspectives_id int PRIMARY KEY,\
        player_perspectives_name varchar(250) NOT NULL, UNIQUE (player_perspectives_name))',

        'CREATE TABLE Consoles (Console_id int AUTO_INCREMENT PRIMARY KEY, \
        Console_name varchar(250) NOT NULL, UNIQUE (Console_name))',

        'CREATE TABLE Genre (Genre_id int AUTO_INCREMENT PRIMARY KEY,\
         Genre_name varchar(250) NOT NULL, UNIQUE (Genre_name))',

        'CREATE TABLE Game(Game_id int AUTO_INCREMENT PRIMARY KEY, Game_name varchar(250) UNIQUE, \
        Publisher_id int, \
        Developer_id int, Age_rating_id int,Franchise_id int,Game_engine_id int, \
        num_players varchar(250), Release_date varchar(250), \
        FOREIGN KEY(Publisher_id) REFERENCES Publisher(Publisher_id),  \
        FOREIGN KEY(Developer_id) REFERENCES Developer(Developer_id), \
        FOREIGN KEY(Age_rating_id) REFERENCES Age_Rating(Age_Rating_id), \
        FOREIGN KEY(Franchise_id) REFERENCES Franchise(Franchise_id), \
        FOREIGN KEY(Game_engine_id) REFERENCES Game_engine(Game_engines_id))',

        ' CREATE TABLE game_to_console \
        ( Game_id INT NOT NULL references Console(Console_id), Console_id INT NOT NULL references Game(Game_id), \
        PRIMARY KEY(Game_id, Console_id))',

        ' CREATE TABLE game_to_perspective (Game_id INT NOT NULL references Game(Game_id), \
         perspective_id INT NOT NULL references player_perspectives(player_perspectives_id), \
                PRIMARY KEY(Game_id, perspective_id))',

        ' CREATE TABLE game_to_genre (Game_id INT NOT NULL references Game(Game_id), \
         Genre_id INT NOT NULL references Genre(Genre_id), \
                PRIMARY KEY(Game_id, Genre_id))',

        ' CREATE TABLE Main_Scores( \
        Game_id int, Console_id int, Metascore varchar(250), Userscore varchar(250), Num_Metascore varchar(250), num_Userscore varchar(250), \
         FOREIGN KEY(Game_id) REFERENCES Game(Game_id), \
        FOREIGN KEY(Console_id) REFERENCES Consoles(Console_id))',

        ' CREATE TABLE PMN_user_scores( \
        Game_id int, Num_positive varchar(250), Num_mixed varchar(250), Num_negative varchar(250), FOREIGN KEY(Game_id) REFERENCES Game(Game_id))',

        ' CREATE TABLE PMN_critic_scores( \
        Game_id int, Num_positive varchar(250), Num_mixed varchar(250), Num_negative varchar(250),FOREIGN KEY(Game_id) REFERENCES Game(Game_id))'
    ]

    for query in tables_creation_queries:
        sql_query(connection, query)
