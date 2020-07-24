import boto3
import constants
import time


def get_credentials(env, cluster):
    ssm = boto3.client('ssm')
    username = ssm.get_parameter(Name=constants.PARAMETER_STORE.get(env).get(cluster).get(constants.USERNAME),
                                 WithDecryption=True)['Parameter']['Value']
    password = ssm.get_parameter(Name=constants.PARAMETER_STORE.get(env).get(cluster).get(constants.PASSWORD),
                                 WithDecryption=True)['Parameter']['Value']
    return username, password


def publish_event_cloudwatch(env, host, is_custom_query, is_all_init, queries):
    user_details = boto3.client('sts').get_caller_identity()
    client = boto3.client('logs')
    message = 'user_id- %s, env- %s, host- %s, custom_query- %s, init_all_db- %s, queries- %s' % (
        user_details.get('UserId'), env, host, is_custom_query, is_all_init, queries)
    timestamp = int(round(time.time() * 1000))

    event_log = {'logGroupName': constants.LOG_GROUP,
                 'logStreamName': constants.LOG_STREAM,
                 'logEvents': [
                     {
                         'timestamp': timestamp,
                         'message': message
                     },
                 ]}
    try:
        client.put_log_events(**event_log)
    except Exception as exception:
        if 'InvalidSequenceTokenException' in str(exception):
            next_token = exception.response.get('expectedSequenceToken')
            event_log.update({'sequenceToken': next_token})
            client.put_log_events(**event_log)
