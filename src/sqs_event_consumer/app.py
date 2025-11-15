import json
import os
import boto3

TABLE_NAME = os.getenv("TABLE_NAME")
ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")
dynamodb = boto3.resource("dynamodb",  endpoint_url = ENDPOINT, region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    print(f"Using DynamoDB endpoint: {ENDPOINT}")
    print(f'Table Name: {TABLE_NAME}')

    for record in event["Records"]:
        message_id = record["messageId"]
        body = record["body"]

        item = {
            "MessageId": message_id,
            "Body": body
        }

        print(f"Writing to DynamoDB: {item}")
        table.put_item(Item=item)

    return {"status": "ok"}
