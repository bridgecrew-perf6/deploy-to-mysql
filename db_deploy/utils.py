import os
import json


def get_file_path(relative_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, relative_path)


def read_json(relative_path):
    file_path = get_file_path(relative_path)
    with open(file_path) as json_file:
        dict_obj = json.load(json_file)

    return dict_obj


def get_databases(env):
    db_map = read_json('configs/database_map.json')
    databases = read_json('configs/%s' % db_map.get(env))
    return databases.get('databases')


def get_cluster_endpoint(env, cluster):
    conn_details = read_json('configs/connection_details.json')
    return conn_details.get(env).get(cluster)
