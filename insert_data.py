import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
from insert_row_to_table import insert_row_to_table


def create_database(row_dict, sql_conn):
    config_object = ConfigParser()
    config_object.read("config.ini")

    # Get API data
    franchise_num_d, game_eng_num_d, plr_prspctv_num_d, franchises_name_d, game_engines_name_d, player_perspectives_name_d \
        = integrate_api(row_dict['name_of_game'])

    console_id_list = [config_object['LIST_OF_DATA']['main platform']]
    #
    # Insert Publisher
    insert_row_to_table(data={'name': row_dict['publisher']}, table='publishers', unique_col='name',
                        unique_val=row_dict['publisher'], sql_conn=sql_conn)

    # Insert Developer
    insert_row_to_table(data={'name': row_dict['developer']}, table='developers', unique_col='name',
                        unique_val=row_dict['developer'], sql_conn=sql_conn)

    # Insert Age_Rating
    insert_row_to_table(data={'name': row_dict['age_rating']}, table='age_rating', unique_col='name',
                        unique_val=row_dict['age_rating'], sql_conn=sql_conn)

    # Insert Franchise
    # Insert Game_Engine
    # Insert player_perspective
    # todo: insert all of them

    # Insert values into Consoles

    full_list_of_consoles = []
    full_list_of_consoles.append(list_of_data[int(config_object['LIST_OF_DATA']['main platform'])])
    full_list_of_consoles += list_of_data[int(config_object['LIST_OF_DATA']['Other Consoles'])]
    for i in range(len(full_list_of_consoles)):

        cursor.execute('SELECT Console_id FROM consoles WHERE Console_name LIKE %s',
                       (full_list_of_consoles[i],))
        Console_id_fetch = cursor.fetchone()
        if Console_id_fetch == None:
            cursor.execute('INSERT INTO consoles (Console_name) VALUE (%s)',
                           (full_list_of_consoles[i],))
        else:
            pass

    # Insert Value into Genre
    """
    if list_of_data[int(config_object['LIST_OF_DATA']['publisher'])] == None:
        pub_id = None
        pass
    else:
        cursor.execute('SELECT Publisher_id FROM publisher WHERE Publisher_name LIKE %s',
                       (list_of_data[int(config_object['LIST_OF_DATA']['publisher'])],))
        publisher_id_fetch = cursor.fetchone()
        if publisher_id_fetch == None:
            cursor.execute('INSERT INTO Publisher (Publisher_name) VALUE (%s)',
                           (list_of_data[int(config_object['LIST_OF_DATA']['publisher'])],))
            pub_id = cursor.lastrowid

        else:
            pub_id = publisher_id_fetch['Publisher_id']
            pass

    # Insert Developer
    if list_of_data[int(config_object['LIST_OF_DATA']['developer'])] == None:
        dev_id = None
        pass
    else:
        cursor.execute('SELECT Developer_id FROM developer WHERE Developer_name LIKE %s',
                       (list_of_data[int(config_object['LIST_OF_DATA']['developer'])],))
        developer_id_fetch = cursor.fetchone()
        if developer_id_fetch == None:
            cursor.execute('INSERT INTO Developer (Developer_name) VALUE (%s)',
                           (list_of_data[int(config_object['LIST_OF_DATA']['developer'])],))
            dev_id = cursor.lastrowid

        else:
            dev_id = developer_id_fetch['Developer_id']
            pass

    # Insert Age_Rating
    if list_of_data[int(config_object['LIST_OF_DATA']['age rating'])] == None:
        age_id = None
        pass
    else:

        cursor.execute('SELECT Age_Rating_id FROM age_rating WHERE Age_Rating_name LIKE %s',
                       (list_of_data[int(config_object['LIST_OF_DATA']['age rating'])],))
        Age_id_fetch = cursor.fetchone()
        if Age_id_fetch == None:
            cursor.execute('INSERT INTO Age_rating (Age_Rating_name) VALUE (%s)',
                           (list_of_data[int(config_object['LIST_OF_DATA']['age rating'])],))
            age_id = cursor.lastrowid
        else:
            age_id = Age_id_fetch['Age_Rating_id']
            pass

    # Insert Franchise
    if franchise_num_d == None or franchises_name_d == None:
        pass
    else:
        cursor.execute('SELECT Franchise_id FROM franchise WHERE Franchise_name LIKE %s',
                       (franchises_name_d,))
        Franchise_id_fetch = cursor.fetchone()
        if Franchise_id_fetch == None:
            cursor.execute('INSERT INTO Franchise (Franchise_id,Franchise_name) VALUE (%s,%s)',
                           (franchise_num_d, franchises_name_d))
        else:
            pass

    # Insert Game_Engine
    if game_eng_num_d == None or game_engines_name_d == None:
        pass
    else:
        cursor.execute('SELECT Game_engines_id FROM game_engine WHERE game_engines_name LIKE %s',
                       (game_engines_name_d,))
        Engine_id_fetch = cursor.fetchone()
        if Engine_id_fetch == None:
            cursor.execute('INSERT INTO Game_engine (Game_engines_id,game_engines_name) VALUE (%s,%s)',
                           (game_eng_num_d, game_engines_name_d))
        else:
            pass

    # Insert player_perspective

    if plr_prspctv_num_d == None or player_perspectives_name_d == None:
        pass
    else:
        for i in range(len(plr_prspctv_num_d)):
            cursor.execute(
                'SELECT player_perspectives_id FROM player_perspectives WHERE player_perspectives_name LIKE %s',
                (player_perspectives_name_d[i],))
            Perspective_id_fetch = cursor.fetchone()
            if Perspective_id_fetch == None:
                cursor.execute(
                    'INSERT INTO Player_perspectives (player_perspectives_id,player_perspectives_name) VALUE (%s,%s)',
                    (plr_prspctv_num_d[i], player_perspectives_name_d[i]))
            else:
                pass

    # Insert values into Consoles

    full_list_of_consoles = []
    full_list_of_consoles.append(list_of_data[int(config_object['LIST_OF_DATA']['main platform'])])
    full_list_of_consoles += list_of_data[int(config_object['LIST_OF_DATA']['Other Consoles'])]
    for i in range(len(full_list_of_consoles)):

        cursor.execute('SELECT Console_id FROM consoles WHERE Console_name LIKE %s',
                       (full_list_of_consoles[i],))
        Console_id_fetch = cursor.fetchone()
        if Console_id_fetch == None:
            cursor.execute('INSERT INTO consoles (Console_name) VALUE (%s)',
                           (full_list_of_consoles[i],))
        else:
            pass

    # Insert Value into Genre

    for i in range(len(list_of_data[int(config_object['LIST_OF_DATA']['Genres'])])):

        cursor.execute('SELECT Genre_id FROM genre WHERE Genre_name LIKE %s',
                       (list_of_data[int(config_object['LIST_OF_DATA']['Genres'])][i],))
        Genre_id_fetch = cursor.fetchone()
        if Genre_id_fetch == None:
            cursor.execute('INSERT INTO genre (Genre_name) VALUE (%s)',
                           (list_of_data[int(config_object['LIST_OF_DATA']['Genres'])][i],))
        else:
            pass

    # Edit Num of Players Colum ---> FIX THE AUG/SEP issue
    if list_of_data[int(config_object['LIST_OF_DATA']['num players'])] == 'No Online Multiplayer' or \
            list_of_data[int(config_object['LIST_OF_DATA']['num players'])] == 'Online Multiplayer':
        num_players = 1
    elif list_of_data[int(config_object['LIST_OF_DATA']['num players'])] == '' or \
            list_of_data[int(config_object['LIST_OF_DATA']['num players'])] == None:
        num_players = 'NaN'
    elif list_of_data[int(config_object['LIST_OF_DATA']['num players'])] == 'Massively Multiplayer':
        num_players = 'inf'
    else:
        num_players = re.findall(r'\d+', list_of_data[int(config_object['LIST_OF_DATA']['num players'])])[0]

    # Insert into Game
    cursor.execute('SELECT Game_id FROM game WHERE Game_name LIKE %s',
                   (list_of_data[int(config_object['LIST_OF_DATA']['name of game'])],))
    Game_id_fetch = cursor.fetchone()
    if Game_id_fetch == None:
        cursor.execute('INSERT INTO Game (Game_name, Publisher_id, Developer_id, Age_rating_id, Franchise_id, '
                       'Game_engine_id, num_players, Release_date) VALUE (%s, %s, %s, '
                       '%s, %s, %s, %s, %s)', (
                           list_of_data[0],
                           pub_id,
                           dev_id,
                           age_id,
                           franchise_num_d,
                           game_eng_num_d,
                           num_players,
                           list_of_data[3]))
        g_id = cursor.lastrowid

        # Insert into game_to Genre
        list_of_genres = []
        for i in list_of_data[int(config_object['LIST_OF_DATA']['Genres'])]:
            if i not in list_of_genres:
                list_of_genres.append(i)

                cursor.execute('SELECT Genre_id FROM genre WHERE Genre_name LIKE %s', i)
                g_g_id_fetch = cursor.fetchone()

                cursor.execute("INSERT INTO game_to_genre VALUES (%s,%s)", (g_id, g_g_id_fetch['Genre_id']))

        # Insert into game_to_console
        for i in full_list_of_consoles:
            cursor.execute('SELECT Console_id FROM consoles WHERE Console_name LIKE %s', i)
            Console_id_fetch = cursor.fetchone()

            cursor.execute('INSERT INTO game_to_console VALUES (%s,%s)', (g_id, Console_id_fetch['Console_id']))

        #Insert into game_to_perspective
        if plr_prspctv_num_d == None:
            pass
        else:
            for i in plr_prspctv_num_d:
                cursor.execute("INSERT INTO game_to_perspective VALUES (%s,%s)", (g_id, i))

        # Insert Values into main_scores
        cursor.execute('SELECT Console_id FROM consoles WHERE Console_name LIKE %s',
                       list_of_data[int(config_object['LIST_OF_DATA']['main platform'])])
        game_id_fetch = cursor.fetchone()
        cursor.execute('INSERT INTO main_scores VALUES (%s,%s,%s,%s,%s,%s)', (
            g_id, game_id_fetch['Console_id'],
            list_of_data[int(config_object['LIST_OF_DATA']['metascore'])],
            list_of_data[int(config_object['LIST_OF_DATA']['user score'])],
            list_of_data[int(config_object['LIST_OF_DATA']['number of metascore reviewers'])],
            list_of_data[int(config_object['LIST_OF_DATA']['number of user reviews'])]
        ))

        # Insert Values into PMN_user_table
        cursor.execute('INSERT INTO PMN_user_scores VALUES (%s,%s,%s,%s)', (
            g_id,
            list_of_data[int(config_object['LIST_OF_DATA']['user review positive'])],
            list_of_data[int(config_object['LIST_OF_DATA']["user review mixed"])],
            list_of_data[int(config_object['LIST_OF_DATA']["user review negative"])]))

        # Insert values into PMN_critic_table
        cursor.execute('INSERT INTO PMN_critic_scores VALUES (%s,%s,%s,%s)', (
            g_id,
            list_of_data[int(config_object['LIST_OF_DATA']["critic review_positive"])],
            list_of_data[int(config_object['LIST_OF_DATA']["critic review mixed"])],
            list_of_data[int(config_object['LIST_OF_DATA']["critic review negative"])]))

    else:
        pass

    conn.commit()
    """