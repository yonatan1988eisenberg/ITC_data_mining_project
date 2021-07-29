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

    query_res = sql_query(sql_conn, f"SELECT * From {table} WHERE {unique_col} LIKE %s", (f'%{unique_val}',))

    if query_res:
        data_string = [f'{col} = "{val}"' for col, val in data.items()][0]
        sql_query(sql_conn, f"UPDATE {table} SET {data_string} WHERE {unique_col} LIKE %s", (f'%{unique_val}',))
    else:
        if len(data) == 1:
            for col, val in data.items():
                col_string = "".join(f' {col},')[:-1]
                val_string = "".join(f' {val},')[:-1]
            sql_query(sql_conn, f'INSERT INTO {table} ({col_string}) VALUES %s', ({val_string},))
        else:
            num_s = ('%s, ' * len(data)).strip(" , ")
            my_lst_1 = []
            my_lst_2 = []
            for i in data.keys():
                my_lst_1.append(i)
            for i in data.values():
                my_lst_2.append(str(i))


            sql_query(sql_conn, f'INSERT INTO {table} (%s,%s) VALUES (%s,%s)',((my_lst_1)[0],(my_lst_1)[1],(my_lst_2)[0],{(my_lst_2)[1]}))

    # row_id = sql_conn.cursor.lastrowid
    #
    # return row_id
