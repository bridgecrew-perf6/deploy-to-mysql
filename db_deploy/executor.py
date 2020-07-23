import mysql.connector
import json
import scripts
import utils

# TODO: Get password from AWS Parameter store
username = 'root'
password = 'gvt123'


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


def init_all_dbs(env):
    for db in utils.get_databases(env):
        cluster = db.get('cluster')
        host = utils.get_cluster_endpoint(env, cluster)
        db_name = db.get('name')
        print('DB - %s, ENV - %s, HOST - %s' % (db_name, env, host))
        db_con = get_mysql_connection(username, password, host)
        create_db(db_con, db_name)
        db_con.close()

        table_con = get_mysql_connection(username, password, host, database=db_name)
        create_tables(table_con)
        table_con.close()
