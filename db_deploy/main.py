import utils
import executor

configs = utils.read_json('run_configs.json')
env = configs.get('ENV')

print('Environment - %s' % env)
# TODO: Get user confirmation

if configs.get('INIT_ALL_DB'):
    executor.init_all_dbs(env)

# TODO: Execute Custom query in all DBs
