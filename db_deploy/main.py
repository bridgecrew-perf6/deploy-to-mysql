import common_utils
import executor
import constants

configs = common_utils.read_json(constants.RUN_CONFIGURATIONS)
env = configs.get(constants.ENV)

if env not in constants.VALID_ENV:
    print('Environment - %s is not valid' % env)
else:
    print('Environment - %s' % env)
    print('Host - %s' % common_utils.get_cluster_data(env))
    print('Configurations -%s' % common_utils.read_json(constants.RUN_CONFIGURATIONS))
    user_env = input("Do you want to proceed? If yes, type the ENV\n")

    if user_env == env:
        if configs.get(constants.INIT_ALL_DB):
            executor.init_all_dbs(env)
        if configs.get(constants.CUSTOM_QUERY):
            executor.execute_custom_queries(env)
    else:
        print('Environment mismatch, exiting..')
