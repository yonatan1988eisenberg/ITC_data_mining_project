import pymysql
from configparser import ConfigParser
import re
from integrate_api import integrate_api
from init_mysql_conn import sql_query


def insert_row_to_table(data, table, unique_col, unique_val, sql_conn):
    """
    This function checks if a row exists in a table. if it does it updates it, if not it creates it
    :param data: a dictionary containing the columns (keys) and values for the row
    :param table: the table we want to insert into
    :param unique_col: the column by which we will verify the row doesn't have duplicates
    :param unique_val: the value to search for in unique_col - must be string!
    :param sql_conn: to the mysql local server
    :return: the id of the row (new or existing)
    """

    query_res = sql_query(sql_conn, f"SELECT * From {table} WHERE {unique_col} LIKE '{unique_val}'")

    if query_res:
        data_string = "".join([f'{col} = {val},' for col, val in data.items()])[-1]
        sql_query(sql_conn, f"UPDATE {table} SET {data_string} WHERE {unique_col} LIKE '{unique_val}'")
    else:
        for col, val in data.items():
            col_string = "".join(f' {col},')[:-1]
            val_string = "".join(f' {val},')[:-1]
        sql_query(sql_conn, f'INSERT INTO {table} ({col_string}) VALUES ({val_string})')

    row_id = sql_conn.cursor.lastrowid

    return row_id
