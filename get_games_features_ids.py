from insert_row_to_table import insert_row_to_table


def get_games_features_ids(data_dict, sql_conn):
    """
    This function gets a data dictionary and sql connection. It checks for the id of the features in games table.
    """

    pub_id, ar_id, fr_id, ge_id, pp_id = None, None, None, None, None

    # Insert into publisher
    if 'publisher' in data_dict.keys():
        pub_id = insert_row_to_table(ids_dict={'name': data_dict['publisher']}, table='publishers',
                                     sql_conn=sql_conn)

    # Insert into age_rating
    if 'age_rating' in data_dict.keys():
        ar_id = insert_row_to_table(ids_dict={'name': data_dict['age_rating']}, table='age_ratings',
                                    sql_conn=sql_conn)
    # Insert into franchise
    if 'franchises' in data_dict.keys():
        fr_id = insert_row_to_table(ids_dict={'name': data_dict['franchises']}, table='franchises',
                                    sql_conn=sql_conn)
    # Insert into game_engine
    if 'game_engines' in data_dict.keys():
        ge_id = insert_row_to_table(ids_dict={'name': data_dict['game_engines']}, table='game_engines',
                                    sql_conn=sql_conn)
    # Insert into player perspective
    if 'player_perspectives' in data_dict.keys():
        pp_id = insert_row_to_table(ids_dict={'name': data_dict['player_perspectives']},
                                    table='player_perspectives', sql_conn=sql_conn)

    return pub_id, ar_id, fr_id, ge_id, pp_id
