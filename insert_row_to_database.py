from configparser import ConfigParser
from insert_row_to_table import insert_row_to_table
from insert_row_game_to_x_table import insert_row_game_to_x_table

# todo: arrange nicley, split into functions


def insert_row_to_database(data_dict, sql_conn):
    config_object = ConfigParser()
    config_object.read("config.ini")
    pub_id, ar_id, fr_id, ge_id, pp_id = None, None, None, None, None
    if 'release_date' not in data_dict.keys():
        data_dict['release_date'] = None
    if 'num_players' not in data_dict.keys():
        data_dict['num_players'] = None
    #
    # Insert into publisher
    if 'publisher' in data_dict.keys():
        pub_id = insert_row_to_table(data_dict={'name': data_dict['publisher']}, table='publishers', unique_col='name',
                                     unique_val=data_dict['publisher'], sql_conn=sql_conn)

    # Insert into age_rating
    if 'age_rating' in data_dict.keys():
        ar_id = insert_row_to_table(data_dict={'name': data_dict['age_rating']}, table='age_ratings', unique_col='name',
                                    unique_val=data_dict['age_rating'], sql_conn=sql_conn)
    # Insert into franchise
    if 'franchises' in data_dict.keys():
        fr_id = insert_row_to_table(data_dict={'name': data_dict['franchises']}, table='franchises', unique_col='name',
                                    unique_val=data_dict['franchises'], sql_conn=sql_conn)
    # Insert into game_engine
    if 'game_engines' in data_dict.keys():
        ge_id = insert_row_to_table(data_dict={'name': data_dict['game_engines']}, table='game_engines',
                                    unique_col='name', unique_val=data_dict['game_engines'], sql_conn=sql_conn)
    # Insert into player perspective
    if 'player_perspectives' in data_dict.keys():
        pp_id = insert_row_to_table(data_dict={'name': data_dict['player_perspectives']}, table='player_perspectives',
                                    unique_col='name', unique_val=data_dict['player_perspectives'], sql_conn=sql_conn)

    # insert into games
    game_id = insert_row_to_table(data_dict={'name': data_dict['name_of_game'],
                                             'publisher_id': pub_id,
                                             'age_rating_id': ar_id,
                                             'franchise_id': fr_id,
                                             'game_engine_id': ge_id,
                                             'perspective_id': pp_id,
                                             'num_players': data_dict['num_players'],
                                             'release_date': data_dict['release_date']},
                                  table='games', unique_col='name', unique_val=data_dict['name_of_game'],
                                  sql_conn=sql_conn)

    #
    # else:
    #     for perspectives in data_dict['player_perspectives']:
    #         pp_id = insert_row_to_table(data_dict={'name': perspectives}, table='player_perspectives',
    #                                     unique_col='name', unique_val=perspectives, sql_conn=sql_conn)
    #
    #         insert_row_game_to_x_table(ids_dict={'game_id': game_id,
    #                                              'perspective_id': pp_id},
    #                                    table='game_to_perspective', sql_conn=sql_conn)

    # Insert values into consoles
    if 'consoles' in data_dict.keys():
        for console, data in data_dict['consoles'].items():
            # check which scores are missing
            missing_scores = list(set(['metascore', 'user_score', 'number_of_metascore_reviewers',
                                       'number_of_user_reviews', 'user_review_positive', 'user_review_mixed',
                                       'user_review_negative', 'critic_review_positive', 'critic_review_mixed',
                                       'critic_review_negative', 'developer']) - set(data.keys()))
            for col in missing_scores:
                data[col] = None
            console_id = insert_row_to_table(data_dict={'name': console}, table='consoles',
                                             unique_col='name', unique_val=console, sql_conn=sql_conn)

            insert_row_game_to_x_table(ids_dict={'game_id': game_id,
                                                 'console_id': console_id},
                                       table='game_to_console', sql_conn=sql_conn)
            # insert scores values
            insert_row_game_to_x_table(data_dict={'game_id': game_id,
                                                  'console_id': console_id,
                                                  'metascore': data['metascore'],
                                                  'userscore': data['user_score'],
                                                  'num_metascore': data['number_of_metascore_reviewers'],
                                                  'num_userscore': data['number_of_user_reviews']},
                                       ids_dict={'game_id': game_id, 'console_id': console_id},
                                       table='main_scores', sql_conn=sql_conn)

            pmn_us_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
                                                              'console_id': console_id,
                                                              'num_positive': data['user_review_positive'],
                                                              'num_mixed': data['user_review_mixed'],
                                                              'num_negative': data['user_review_negative']},
                                                   table='PMN_user_scores', ids_dict={'game_id': game_id,
                                                                                      'console_id': console_id},
                                                   sql_conn=sql_conn)

            # Insert Values into PMN_critic_scores
            pmn_cs_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
                                                              'console_id': console_id,
                                                              'num_positive': data['critic_review_positive'],
                                                              'num_mixed': data['critic_review_mixed'],
                                                              'num_negative': data['critic_review_negative']},
                                                   table='PMN_critic_scores', ids_dict={'game_id': game_id,
                                                                                        'console_id': console_id},
                                                   sql_conn=sql_conn)
            # Insert Values into main_scores
            # ms_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
            #                                               'console_id': console_id,
            #                                               'metascore': data['metascore'],
            #                                               'userscore': data['user_score'],
            #                                               'num_metascore': data['number_of_metascore_reviewers'],
            #                                               'num_userscore': data['number_of_user_reviews']},
            #                                    ids_dict={'game_id': game_id, 'console_id': console_id},
            #                                    table='main_scores', sql_conn=sql_conn)

            # insert into developers
            dev_id = insert_row_game_to_x_table(ids_dict={'name': data['developer']}, table='developers',
                                                sql_conn=sql_conn)

            res = insert_row_game_to_x_table(ids_dict={'game_id': game_id, 'developer_id': dev_id,
                                                       'console_id': console_id}, table='game_to_developer',
                                             sql_conn=sql_conn)

    # # Insert Value into genres
    if 'genres' in data_dict.keys():
        for genre in data_dict['genres']:
            genre_id = insert_row_to_table(data_dict={'name': genre}, table='genres', unique_col='name',
                                           unique_val=genre, sql_conn=sql_conn)
            insert_row_game_to_x_table(ids_dict={'game_id': game_id,
                                                 'genre_id': genre_id},
                                       table='game_to_genre', sql_conn=sql_conn)



    return 1
    # todo implement logger messages in all the desired functions

    # # Insert into developer
    # dev_id = insert_row_to_table(data_dict={'name': data_dict['developer']}, table='developers', unique_col='name',
    #                              unique_val=data_dict['developer'], sql_conn=sql_conn)

    #
    # mc_id = insert_row_to_table(data_dict={'name': data_dict['main_platform']}, table='consoles', unique_col='name',
    #                             unique_val=data_dict['main_platform'], sql_conn=sql_conn)
    # insert_row_game_to_x_table(ids_dict={'game_id': game_id, 'console_id': mc_id}, table='game_to_console',
    #                            sql_conn=sql_conn)
    #
    # # Insert Values into PMN_user_scores
    # pmn_us_id = insert_row_game_to_x_table(ids_dict={'game_id': game_id, 'console_id': mc_id},
    #                                        table='PMN_user_scores', sql_conn=sql_conn,
    #                                        data_dict={'game_id': game_id,
    #                                                   'console_id': mc_id,
    #                                                   'num_positive': data_dict['user_review_positive'],
    #                                                   'num_mixed': data_dict['user_review_mixed'],
    #                                                   'num_negative': data_dict['user_review_negative']})
    #
    # # Insert Values into PMN_critic_scores
    # pmn_cs_id = insert_row_game_to_x_table(ids_dict={'game_id': game_id, 'console_id': mc_id},
    #                                        table='PMN_critic_scores', sql_conn=sql_conn,
    #                                        data_dict={'game_id': game_id,
    #                                                   'console_id': mc_id,
    #                                                   'num_positive': data_dict['critic_review_positive'],
    #                                                   'num_mixed': data_dict['critic_review_mixed'],
    #                                                   'num_negative': data_dict['critic_review_negative']})
    # # Insert Values into main_scores
    # ms_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
    #                                               'console_id': mc_id,
    #                                               'metascore': data_dict['metascore'],
    #                                               'userscore': data_dict['user_score'],
    #                                               'num_metascore': data_dict['number_of_metascore_reviewers'],
    #                                               'num_userscore': data_dict['number_of_user_reviews']},
    #                                    ids_dict={'game_id': game_id, 'console_id': mc_id},
    #                                    table='main_scores', sql_conn=sql_conn)
    #
    # if data_dict['other_consoles']:
    #     for index, console in enumerate(data_dict['other_consoles']):
    #         console_id = insert_row_to_table(data_dict={'name': console}, table='consoles',
    #                                          unique_col='name', unique_val=console, sql_conn=sql_conn)
    #
    #         insert_row_game_to_x_table(ids_dict={'game_id': game_id,
    #                                              'console_id': console_id},
    #                                    table='game_to_console', sql_conn=sql_conn)
    #         # insert scores values
    #         console_scores_dict = data_dict['other_consoles_scores'][index]
    #         insert_row_game_to_x_table(data_dict={'game_id': game_id,
    #                                               'console_id': console_id,
    #                                               'metascore': console_scores_dict['metascore'],
    #                                               'userscore': console_scores_dict['user_score'],
    #                                               'num_metascore': console_scores_dict['number_of_metascore_reviewers'],
    #                                               'num_userscore': console_scores_dict['number_of_user_reviews']},
    #                                    ids_dict={'game_id': game_id, 'console_id': console_id},
    #                                    table='main_scores', sql_conn=sql_conn)
    #
    #         pmn_us_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
    #                                                           'console_id': console_id,
    #                                                           'num_positive': console_scores_dict['user_review_positive'],
    #                                                           'num_mixed': console_scores_dict['user_review_mixed'],
    #                                                           'num_negative': console_scores_dict['user_review_negative']},
    #                                                table='PMN_user_scores', ids_dict={'game_id': game_id,
    #                                                                                   'console_id': console_id},
    #                                                sql_conn=sql_conn)
    #
    #         # Insert Values into PMN_critic_scores
    #         pmn_cs_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
    #                                                           'console_id': console_id,
    #                                                           'num_positive': console_scores_dict['critic_review_positive'],
    #                                                           'num_mixed': console_scores_dict['critic_review_mixed'],
    #                                                           'num_negative': console_scores_dict['critic_review_negative']},
    #                                                table='PMN_critic_scores', ids_dict={'game_id': game_id,
    #                                                                                     'console_id': console_id},
    #                                                sql_conn=sql_conn)
    #         # Insert Values into main_scores
    #         ms_id = insert_row_game_to_x_table(data_dict={'game_id': game_id,
    #                                                       'console_id': console_id,
    #                                                       'metascore': console_scores_dict['metascore'],
    #                                                       'userscore': console_scores_dict['user_score'],
    #                                                       'num_metascore': console_scores_dict['number_of_metascore_reviewers'],
    #                                                       'num_userscore': console_scores_dict['number_of_user_reviews']},
    #                                            ids_dict={'game_id': game_id, 'console_id': console_id},
    #                                            table='main_scores', sql_conn=sql_conn)

    # full_list_of_consoles = []
    # full_list_of_consoles.append(list_of_data[int(config_object['LIST_OF_DATA']['main platform'])])
    # full_list_of_consoles += list_of_data[int(config_object['LIST_OF_DATA']['Other Consoles'])]
    # for i in range(len(full_list_of_consoles)):
    #
    #     cursor.execute('SELECT Console_id FROM consoles WHERE Console_name LIKE %s',
    #                    (full_list_of_consoles[i],))
    #     Console_id_fetch = cursor.fetchone()
    #     if Console_id_fetch == None:
    #         cursor.execute('INSERT INTO consoles (Console_name) VALUE (%s)',
    #                        (full_list_of_consoles[i],))
    #     else:
    #         pass

    # Insert Value into Genre


    # # insert into game_to_developer
    # insert_row_game_to_x_table(ids_dict={'game_id': game_id,
    #                                      'developer_id': dev_id},
    #                            table='game_to_developer', sql_conn=sql_conn)

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
