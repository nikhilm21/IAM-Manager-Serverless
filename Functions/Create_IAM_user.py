import boto3
import argparse
from Dependencies import Sync_IAM

def Create_User():
    
    '''
    Creates a New user with passing the argument
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('username',help='Write the IAM username you want to add')
    args = parser.parse_args()

    try:
        client = boto3.client('iam')
        client.create_user(UserName = args.username)
        print('User Created')
        Sync_IAM()

    except Exception as e:
        print('User Not Created: Try Again')

