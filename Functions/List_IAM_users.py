import boto3


def List_Users():
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')

    response = table.scan()
    return response['Items']