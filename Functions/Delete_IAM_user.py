import boto3
import argparse
from Dependencies import Sync_IAM

parser = argparse.ArgumentParser()
parser.add_argument('username',help='Write the IAM user you want to delete')
args = parser.parse_args()

try:
    client = boto3.client('iam')
    client.delete_user(UserName = args.username)
    print('User Deleted')
    Sync_IAM()
    
except Exception as e:
    print('User Not Deleted: Try Again')



# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('users')


# try:
#     response = table.delete_item(
#         Key = {
#             'UserName': args.username
#         }
#     )
#     print('User Deleted')
    
# except Exception as e:
#     print('User Not Found: Try Again')