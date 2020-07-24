import mysql.connector
import scripts


def get_mysql_connection(uname, psswd, host, database=None):
    config = {
        'user': uname,
        'password': psswd,
        'host': host,
        'raise_on_warnings': False,
        'database': database
    }
    db_conn = mysql.connector.connect(**config)
    return db_conn


def create_db(connection, db):
    # Create DB If not exists
    create_db_query = scripts.create_db % db
    print(create_db_query)
    cursor = connection.cursor()
    cursor.execute(create_db_query)
    connection.commit()
    cursor.close()


def create_tables(connection):
    # Create Tables
    for table_query in scripts.tables:
        cursor = connection.cursor()
        cursor.execute(table_query)
        connection.commit()
        cursor.close()


def execute_many(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
