PARAMETER_STORE = {
    "dev": {
        "01": {
            "USERNAME": "/CP/DEV/DATABASE/REF_PRICE/USERNAME",
            "PASSWORD": "/CP/DEV/DATABASE/REF_PRICE/PASSWORD"
        }
    },
    "exe": {
        "01": {
            "USERNAME": "/CP/EXE/DATABASE/REF_PRICE/USERNAME",
            "PASSWORD": "/CP/EXE/DATABASE/REF_PRICE/PASSWORD"
        }
    },
    "prod": {
        "01": {
            "USERNAME": "/CP/PROD/DATABASE/REF_PRICE/USERNAME",
            "PASSWORD": "/CP/PROD/DATABASE/REF_PRICE/PASSWORD"
        }
    }
}

VALID_ENV = ['local', 'dev', 'exe', 'prod']

LOCAL_USERNAME = 'root'
LOCAL_PASSWORD = 'gvt123'

ENV_LOCAL = 'local'
CLUSTER = 'cluster'
DB_NAME = 'name'
DATABASES = 'databases'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
ENV = 'ENV'
INIT_ALL_DB = 'INIT_ALL_DB'
CUSTOM_QUERY = 'CUSTOM_QUERY'

DB_MAP_FILE = 'configs/database_map.json'
CONFIGS_PREFIX = 'configs/%s'
CON_DETAILS_FILE = 'configs/connection_details.json'
RUN_CONFIGURATIONS = 'run_configs.json'
CUSTOM_QUERY_PATH = 'custom_query/custom_query.sql'

AVOID_SCRIPTS = ['DROP', 'TRUNCATE', 'DELETE', 'PURGE', 'SELECT']

LOG_GROUP = 'cp-ref-price-db-deploy'
LOG_STREAM = 'cp-ref-db-deploy-log-stream'
