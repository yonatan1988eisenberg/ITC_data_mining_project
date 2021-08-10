from configparser import ConfigParser
from insert_row_to_table import insert_row_to_table
from get_games_features_ids import get_games_features_ids
from insert_consoles_to_database import insert_consoles_to_database


def insert_row_to_database(data_dict, sql_conn):
    config_object = ConfigParser()
    config_object.read("config.ini")

    if 'release_date' not in data_dict.keys():
        data_dict['release_date'] = None
    if 'num_players' not in data_dict.keys():
        data_dict['num_players'] = None

    # get ids for the features in games table
    pub_id, ar_id, fr_id, ge_id, pp_id = get_games_features_ids(data_dict, sql_conn)

    # insert into games table and get id
    game_id = insert_row_to_table(ids_dict={'name': data_dict['name_of_game']},
                                  data_dict={'name': data_dict['name_of_game'],
                                             'publisher_id': pub_id,
                                             'age_rating_id': ar_id,
                                             'franchise_id': fr_id,
                                             'game_engine_id': ge_id,
                                             'perspective_id': pp_id,
                                             'num_players': data_dict['num_players'],
                                             'release_date': data_dict['release_date']},
                                  table='games', sql_conn=sql_conn)

    # insert consoles data
    insert_consoles_to_database(data_dict, game_id, sql_conn)

    # # Insert Value into genres
    if 'genres' in data_dict.keys():
        for genre in data_dict['genres']:
            genre_id = insert_row_to_table(ids_dict={'name': genre}, table='genres',
                                           sql_conn=sql_conn)
            insert_row_to_table(ids_dict={'game_id': game_id,
                                          'genre_id': genre_id},
                                table='game_to_genre', sql_conn=sql_conn)

    return 1

    # todo implement logger messages in all the desired functions
