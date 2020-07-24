import common_utils
import executor
import constants
import aws_utils

configs = common_utils.read_json(constants.RUN_CONFIGURATIONS)
env = configs.get(constants.ENV)

if env not in constants.VALID_ENV:
    print('Environment - %s is not valid' % env)
else:
    cluster_info = common_utils.get_cluster_data(env)
    print('Environment - %s' % env)
    print('Host - %s' % cluster_info)
    print('Configurations -%s' % common_utils.read_json(constants.RUN_CONFIGURATIONS))
    user_env = input("Do you want to proceed? If yes, type the ENV\n")

    if user_env == env:
        is_all_init = configs.get(constants.INIT_ALL_DB)
        is_custom_query = configs.get(constants.CUSTOM_QUERY)
        if env is not constants.ENV_LOCAL:
            aws_utils.publish_event_cloudwatch(env, cluster_info, is_custom_query, is_all_init,
                                               common_utils.get_custom_query())
        if is_all_init:
            executor.init_all_dbs(env)
        if is_custom_query:
            executor.execute_custom_queries(env)
    else:
        print('Environment mismatch, exiting..')
