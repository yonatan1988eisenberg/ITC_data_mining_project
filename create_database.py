import csv
import pymysql
from configparser import ConfigParser


config_object = ConfigParser()
config_object.read("config.ini")

# Make Connection
conn = pymysql.connect(host='localhost', user='root',
                       password='Weasil123', cursorclass=pymysql.cursors.DictCursor)  # give ur username, password

# Make Cursos
cursor = conn.cursor()

# Create Database
cursor.execute(config_object['CREATE_DATABASE']['CREATE_TRIAL'])

# Use Database
cursor.execute(config_object['CREATE_DATABASE']['USE_TRIAL'])


# Create Tables
for i in config_object['CREATE_DATABASE']['LIST_OF_TABLES'].split("&&"):
    cursor.execute(f'{i}')


# Insert Values
with open('db.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    # Insert Value into Publisher,Developer and Age_rating tables
    for row in reader:
        list_of_paramaters = [(row[config_object['CREATE_DATABASE']['PUBLISHER']],),
                              (row[config_object['CREATE_DATABASE']['DEVELOPER']],),
                              (row[config_object['CREATE_DATABASE']['AGE_RATING']],),
                              (row[config_object['CREATE_DATABASE']['MAIN_PLATFROM']],)]
        console_id_list = [row[config_object['CREATE_DATABASE']['MAIN_PLATFROM']]]
        for i in range(4):
            try:
                cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[i],
                               list_of_paramaters[i])
            except pymysql.err.IntegrityError:
                pass

        # Insert values into Consoles and Genres
        list_of_paramaters_two = [row[config_object['CREATE_DATABASE']['OTHER_CONSOLES']],
                                  row[config_object['CREATE_DATABASE']['GENRES']]]
        for j in range(3, 5):
            for k in list_of_paramaters_two[j - 3].split(','):
                console_id_list.append(k.strip("']['"))
                try:
                    cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[j],
                                   (k.strip("'][' '"),))
                except pymysql.err.IntegrityError:
                    pass

        # Fetch id of Publisher,Developer and Age_rating
        save_fetch = []
        for i in range(3):
            cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[i + 5],
                           list_of_paramaters[i])
            save_fetch.append(cursor.fetchone())

        # Insert into Game
        try:
            cursor.execute(
                config_object['CREATE_DATABASE']['INSERT_GAME'],
                (
                    row[config_object['CREATE_DATABASE']['NAME_OF_GAME']],
                    save_fetch[0][config_object['CREATE_DATABASE']['PUB_ID']],
                    save_fetch[1][config_object['CREATE_DATABASE']['DEV_ID']],
                    save_fetch[2][config_object['CREATE_DATABASE']['AGE_ID']],
                    row[config_object['CREATE_DATABASE']['REL_DATE']],
                    row[config_object['CREATE_DATABASE']['REL_DATE']]))
            g_id = cursor.lastrowid
        except pymysql.err.IntegrityError:
            pass

        # Insert into game_to_Console table
        try:
            for i in console_id_list:
                cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[9], i)
                Console_id_fetch = cursor.fetchone()
                cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[10],
                               (g_id, Console_id_fetch[config_object['CREATE_DATABASE']['CONSOLE_ID']])
                               )
        except NameError:
            pass

        except TypeError:
            pass
        except pymysql.err.IntegrityError:
            pass

        # Insert Values into main_scores
        try:
            cursor.execute(config_object['CREATE_DATABASE']['INSERT_MAIN'], row['main platform'])
            Console_id_fetch = cursor.fetchone()
            cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[11],
                           (g_id, Console_id_fetch[config_object['CREATE_DATABASE']['CONSOLE_ID']],
                            row[config_object['CREATE_DATABASE']['METASCORE']],
                            row[config_object['CREATE_DATABASE']['USER_SCORE']],
                            row[config_object['CREATE_DATABASE']['NUM_MET_REV']],
                            row[config_object['CREATE_DATABASE']['NUM_USER_REV']]))
        except NameError:
            pass

        # Insert Values into PMN_user_table
        try:
            cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[12],
                           (g_id,
                            row[config_object['CREATE_DATABASE']['USER_POS']],
                            row[config_object['CREATE_DATABASE']['USER_MIX']],
                            row[config_object['CREATE_DATABASE']['USER_NEG']]))
        except NameError:
            pass
        except pymysql.err.DataError:
            pass

        # Insert values into PMN_critic_table
        try:
            cursor.execute(config_object['CREATE_DATABASE']['LIST_OF_INSERTS'].split("&&")[13], (
                g_id, row[config_object['CREATE_DATABASE']['CRITIC_POS']],
                row[config_object['CREATE_DATABASE']['CRITIC_MIX']],
                row[config_object['CREATE_DATABASE']['CRITIC_NEG']]))
        except NameError:
            pass

    conn.commit()
