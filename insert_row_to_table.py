from init_mysql_conn import sql_query
from get_exists_query_string import get_exists_query_string
from get_insert_query_string import get_insert_query_string


def insert_row_to_table(ids_dict, table, sql_conn, data_dict=None):
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

    query_string, values = get_exists_query_string(ids_dict)
    query_res = sql_query(sql_conn, f"SELECT * From {table} WHERE " + query_string, values)

    if query_res:
        if 'id' in query_res[0].keys():
            row_id = query_res[0]['id']
        elif 'game_id' in query_res[0].keys():
            row_id = query_res[0]['game_id']
        # todo: add an update query

    else:
        col_string, vals, ph = get_insert_query_string(data_dict)
        sql_query(sql_conn, f"INSERT INTO {table} ({col_string}) VALUES ({ph})", vals)
        row_id = sql_query(sql_conn, 'SELECT LAST_INSERT_ID()')[0]['LAST_INSERT_ID()']
    sql_conn.commit()

    return row_id


