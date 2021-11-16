import boto3

def Sync_IAM():

    '''
    Syncs over IAM users and updates them on delete
    '''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'UserName': each['UserName']
                }
            )

    client = boto3.client('iam')
    response = client.list_users()

    for i in response['Users']:
        i.pop('CreateDate')  
        table.put_item(Item=i)

    #TODO: Return Type?

    print('DB Sync Completed')



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

Sync_IAM()