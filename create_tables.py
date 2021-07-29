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

        'CREATE TABLE Developer (id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Age_Rating (id int AUTO_INCREMENT PRIMARY KEY,\
        name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Franchise (id int PRIMARY KEY,\
        name varchar(250), UNIQUE (name))',

        'CREATE TABLE Game_engine (id int PRIMARY KEY,\
        name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Player_perspectives (id int PRIMARY KEY,\
        name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Consoles (id int AUTO_INCREMENT PRIMARY KEY, \
        name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Genre (id int AUTO_INCREMENT PRIMARY KEY,\
         name varchar(250) NOT NULL, UNIQUE (name))',

        'CREATE TABLE Game(id int AUTO_INCREMENT PRIMARY KEY, Game_name varchar(250) UNIQUE, \
        Publisher_id int, \
        Developer_id int, Age_rating_id int,Franchise_id int,Game_engine_id int, \
        num_players varchar(250), Release_date varchar(250), \
        FOREIGN KEY(Publisher_id) REFERENCES publishers(id),  \
        FOREIGN KEY(Developer_id) REFERENCES Developer(id), \
        FOREIGN KEY(Age_rating_id) REFERENCES Age_Rating(id), \
        FOREIGN KEY(Franchise_id) REFERENCES Franchise(id), \
        FOREIGN KEY(Game_engine_id) REFERENCES Game_engine(id))',

        ' CREATE TABLE game_to_console \
        ( Game_id INT NOT NULL references Console(id), Console_id INT NOT NULL references Game(id), \
        PRIMARY KEY(Game_id, Console_id))',

        ' CREATE TABLE game_to_perspective (Game_id INT NOT NULL references Game(id), \
         perspective_id INT NOT NULL references player_perspectives(id), \
                PRIMARY KEY(Game_id, perspective_id))',

        ' CREATE TABLE game_to_genre (Game_id INT NOT NULL references Game(id), \
         Genre_id INT NOT NULL references Genre(id), \
                PRIMARY KEY(Game_id, Genre_id))',

        ' CREATE TABLE Main_Scores( \
        Game_id int, Console_id int, Metascore varchar(250), Userscore varchar(250), Num_Metascore varchar(250), num_Userscore varchar(250), \
         FOREIGN KEY(Game_id) REFERENCES Game(id), \
        FOREIGN KEY(Console_id) REFERENCES Consoles(id))',

        ' CREATE TABLE PMN_user_scores( \
        Game_id int, Num_positive varchar(250), Num_mixed varchar(250), Num_negative varchar(250), FOREIGN KEY(Game_id) REFERENCES Game(id))',

        ' CREATE TABLE PMN_critic_scores( \
        Game_id int, Num_positive varchar(250), Num_mixed varchar(250), Num_negative varchar(250),FOREIGN KEY(Game_id) REFERENCES Game(id))'
    ]

    for query in tables_creation_queries:
        sql_query(connection, query)
