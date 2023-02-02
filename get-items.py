# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('HelloWorldDatabase')

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    response = table.scan()

    return {
        'statusCode': 200,
        'body': response["Items"]
    }