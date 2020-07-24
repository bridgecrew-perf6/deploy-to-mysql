import boto3
import constants


def get_credentials(env, cluster):
    ssm = boto3.client('ssm')
    username = ssm.get_parameter(Name=constants.PARAMETER_STORE.get(env).get(cluster).get(constants.USERNAME),
                                 WithDecryption=True)
    password = ssm.get_parameter(Name=constants.PARAMETER_STORE.get(env).get(cluster).get(constants.PASSWORD),
                                 WithDecryption=True)
    return username, password
