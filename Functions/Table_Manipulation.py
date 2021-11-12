import boto3

def CreateTable():

    '''
    Creates DynamoDb Table and deletes the existing one
    '''

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'UserName',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'UserName',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='users')

def deleteTable():

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')

    try:
        table.delete()
        print('Table Deleted')
    except Exception as e:
        print('Table Not Deleted: Try Again')

# deleteTable()
# CreateTable()