from insert_row_to_table import insert_row_to_table


def insert_consoles_to_database(data_dict, game_id, sql_conn):
    if 'consoles' in data_dict.keys():
        for console, data in data_dict['consoles'].items():
            # check which scores are missing
            missing_scores = list({'metascore', 'user_score', 'number_of_metascore_reviewers', 'number_of_user_reviews',
                                   'user_review_positive', 'user_review_mixed', 'user_review_negative',
                                   'critic_review_positive', 'critic_review_mixed', 'critic_review_negative',
                                   'developer'} - set(data.keys()))
            for col in missing_scores:
                data[col] = None
            console_id = insert_row_to_table(ids_dict={'name': console}, table='consoles',
                                             sql_conn=sql_conn)

            insert_row_to_table(ids_dict={'game_id': game_id,
                                          'console_id': console_id},
                                table='game_to_console', sql_conn=sql_conn)
            # insert scores values
            insert_row_to_table(data_dict={'game_id': game_id,
                                           'console_id': console_id,
                                           'metascore': data['metascore'],
                                           'userscore': data['user_score'],
                                           'num_metascore': data['number_of_metascore_reviewers'],
                                           'num_userscore': data['number_of_user_reviews']},
                                ids_dict={'game_id': game_id, 'console_id': console_id},
                                table='main_scores', sql_conn=sql_conn)

            pmn_us_id = insert_row_to_table(data_dict={'game_id': game_id,
                                                       'console_id': console_id,
                                                       'num_positive': data['user_review_positive'],
                                                       'num_mixed': data['user_review_mixed'],
                                                       'num_negative': data['user_review_negative']},
                                            table='user_scores', ids_dict={'game_id': game_id,
                                                                           'console_id': console_id},
                                            sql_conn=sql_conn)

            # Insert Values into PMN_critic_scores
            pmn_cs_id = insert_row_to_table(data_dict={'game_id': game_id,
                                                       'console_id': console_id,
                                                       'num_positive': data['critic_review_positive'],
                                                       'num_mixed': data['critic_review_mixed'],
                                                       'num_negative': data['critic_review_negative']},
                                            table='critic_scores', ids_dict={'game_id': game_id,
                                                                             'console_id': console_id},
                                            sql_conn=sql_conn)

            dev_id = insert_row_to_table(ids_dict={'name': data['developer']}, table='developers',
                                         sql_conn=sql_conn)

            res = insert_row_to_table(ids_dict={'game_id': game_id, 'developer_id': dev_id,
                                                'console_id': console_id}, table='game_to_developer',
                                      sql_conn=sql_conn)
