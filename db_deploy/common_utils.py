import os
import json
import constants


def get_file_path(relative_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, relative_path)


def read_json(relative_path):
    file_path = get_file_path(relative_path)
    with open(file_path) as json_file:
        dict_obj = json.load(json_file)
    return dict_obj


def get_databases(env):
    db_map = read_json(constants.DB_MAP_FILE)
    databases = read_json(constants.CONFIGS_PREFIX % db_map.get(env))
    return databases.get(constants.DATABASES)


def get_cluster_endpoint(env, cluster):
    conn_details = read_json(constants.CON_DETAILS_FILE)
    return conn_details.get(env).get(cluster)


def get_cluster_data(env):
    conn_details = read_json(constants.CON_DETAILS_FILE)
    return conn_details.get(env)


def get_custom_query():
    file_path = get_file_path(constants.CUSTOM_QUERY_PATH)
    with open(file_path, 'r') as file_handle:
        file_content = file_handle.read()
        return file_content
