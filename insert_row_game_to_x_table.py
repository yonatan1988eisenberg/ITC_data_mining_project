

import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
from init_mysql_conn import sql_query


def insert_row_game_to_x_table(ids_dict, table, sql_conn, data_dict=None):
    """
    This function checks if a row exists in a table. if not it inserts it
    :param ids_dict: a dictionary containing the columns (game_id, console_id, etc.) and their values.
    :param data_dict: a dictionary with the columns and values to insert
    :param table: the table we want to insert into
    :param sql_conn: to the mysql local server
    :return: the result of the last sql query and the id of the row (new or existing). 'Null' if data is empty
    """
    if None in ids_dict.values():
        return None
    if data_dict is None:
        data_dict = ids_dict
    col_string = ""
    vals = []
    for col, val in ids_dict.items():
        col_string = col_string + "".join(f"CAST({col} as CHAR) LIKE %s AND ")
        vals.append(val)
    col_string = col_string[:-5]
    query_res = sql_query(sql_conn, f"SELECT * From {table} WHERE " + col_string, vals)
    # CAST({unique_col} as CHAR) LIKE %s", unique_val)

    if query_res:
        row_id = {}
        for key, val in query_res:
            row_id[key] = val
    else:
        col_string = ""
        vals = []
        for col, val in data_dict.items():
            col_string = col_string + "".join(f"{col}, ")
            vals.append(val)
        col_string = col_string[:-2]
        ph = ('%s, ' * len(vals))[:-2]
        sql_query(sql_conn, f"INSERT INTO {table} ({col_string}) VALUES ({ph})", vals)
        row_id = sql_query(sql_conn, 'SELECT LAST_INSERT_ID()')[0]['LAST_INSERT_ID()']
    sql_conn.commit()
    return row_id


