import pymysql


def init_mysql_conn(user='root', password=None, db=None):
    """
    This functions initialized a connection to the local mysql server
    :param user: local mysql server username, default is 'root'
    :param password: local mysql server password, default is None
    :param db: The database to use
    :return: A connection object
    """
    connection = pymysql.connect(host='localhost',
                                 user=user,
                                 password=password,
                                 database=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def sql_query(connection, query, holders=None):
    """
    This function executes sql queries
    :param connection: an initialized mysql local connection
    :param query: the sql query
    :param holders: placeholders values, default is None
    :return: the query return value and last row id
    """

    with connection.cursor() as cursor:
        cursor.execute(query, holders)
        res = cursor.fetchall()
        return res
