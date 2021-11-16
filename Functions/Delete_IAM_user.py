import boto3
import argparse
from Dependencies import Sync_IAM

def Delete_User():

    '''
    Delets IAM User with parser passing the username
    '''


    parser = argparse.ArgumentParser()
    parser.add_argument('username',help='Write the IAM user you want to delete')
    args = parser.parse_args()

    try:
        client = boto3.client('iam')
        client.delete_user(UserName = args.username)
        Sync_IAM()
        return 'User Deleted'
        
        
    except Exception as e:
        return 'User Not Deleted: Try Again'

