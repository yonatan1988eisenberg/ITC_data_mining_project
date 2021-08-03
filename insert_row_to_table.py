import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
from init_mysql_conn import sql_query


def insert_row_to_table(data_dict, table, unique_col, unique_val, sql_conn):
    """
    This function checks if a row exists in a table. if it does it updates it, if not it creates it
    :param data_dict: a dictionary containing the columns (keys) and values for the row
    :param table: the table we want to insert into
    :param unique_col: the column by which we will verify the row doesn't have duplicates
    :param unique_val: the value to search for in unique_col - must be string!
    :param sql_conn: to the mysql local server
    :return: the result of the last sql query and the id of the row (new or existing). 'Null' if data is empty
    """

    if unique_val is None:
        return None
    if isinstance(unique_col, list):

        query_where = "".join([f'CAST({col} as CHAR) LIKE %s AND ' for col in unique_col ])[:-5]# if col is not None
    else:
        query_where = f'CAST({unique_col} as CHAR) LIKE %s'

    query_res = sql_query(sql_conn, f"SELECT * From {table} WHERE " + query_where, unique_val)
    # CAST({unique_col} as CHAR) LIKE %s", unique_val)
    if query_res:
        if 'id' in query_res[0].keys():
            row_id = query_res[0]['id']
        elif 'game_id' in query_res[0].keys():
            row_id = query_res[0]['game_id']
        # data_string = "".join([f"{col} = '{val}', " for col, val in data_dict.items()])[:-2]
        # sql_query(sql_conn, f"UPDATE {table} SET {data_string} WHERE {unique_col} LIKE %s", unique_val)
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

