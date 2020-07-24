import mysql_connector
import common_utils
import aws_utils
import constants


def init_all_dbs(env):
    for db in common_utils.get_databases(env):
        cluster = db.get(constants.CLUSTER)
        host = common_utils.get_cluster_endpoint(env, cluster)
        db_name = db.get(constants.DB_NAME)
        print('DB - %s, ENV - %s, HOST - %s' % (db_name, env, host))
        if env == constants.ENV_LOCAL:
            uname, psswd = constants.LOCAL_USERNAME, constants.LOCAL_PASSWORD
        else:
            uname, psswd = aws_utils.get_credentials(env, cluster)
            print(uname, psswd)
        db_con = mysql_connector.get_mysql_connection(uname, psswd, host)
        mysql_connector.create_db(db_con, db_name)
        db_con.close()

        table_con = mysql_connector.get_mysql_connection(uname, psswd, host, database=db_name)
        mysql_connector.create_tables(table_con)
        table_con.close()


def execute_custom_queries(env):
    queries = common_utils.get_custom_query()
    print('Custom queries: %s' % queries)
    for keyword in constants.AVOID_SCRIPTS:
        if keyword in queries:
            print('Unexpected keyword found in custom query, exiting..')
            return

    for db in common_utils.get_databases(env):
        cluster = db.get(constants.CLUSTER)
        host = common_utils.get_cluster_endpoint(env, cluster)
        db_name = db.get(constants.DB_NAME)
        print('DB - %s, ENV - %s, HOST - %s' % (db_name, env, host))
        if env == constants.ENV_LOCAL:
            uname, psswd = constants.LOCAL_USERNAME, constants.LOCAL_PASSWORD
        else:
            uname, psswd = aws_utils.get_credentials(env, cluster)

        db_con = mysql_connector.get_mysql_connection(uname, psswd, host, database=db_name)
        mysql_connector.execute_many(db_con, queries)
        db_con.close()
