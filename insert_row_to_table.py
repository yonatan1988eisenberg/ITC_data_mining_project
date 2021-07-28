import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
def insert_row_to_table(row, table, unique, connection, list_of_data):
    """
    This function gets a row to be inserted to a table. If the row exists the data will be overwritten
    :param row:
    :param table:
    :param unique:
    :return:
    """
    config_object = ConfigParser()
    config_object.read("config.ini")
    # Get API data
    franchise_num_d, game_eng_num_d, plr_prspctv_num_d, franchises_name_d, game_engines_name_d, player_perspectives_name_d \
        = integrate_api(list_of_data[0])
    console_id_list = [config_object['LIST_OF_DATA']['main platform']]

    # Insert Publisher
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