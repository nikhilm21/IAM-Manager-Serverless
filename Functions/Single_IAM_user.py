import boto3
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('username',help='Write the IAM you want to search')
args = parser.parse_args()


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

try:
    response = table.get_item(
        Key = {
            'UserName': args.username
        }
    )
    print(response['Item'])
    
except Exception as e:
    print('User Not Found: Try Again')