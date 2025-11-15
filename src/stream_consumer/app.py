# stream_consumer.py
import json

def handler(event, context):
    print("Received DynamoDB stream event:")
    print(json.dumps(event, indent=2))

    # Process each record
    for record in event["Records"]:
        print("Record:", record["eventID"], record["eventName"])
        if "NewImage" in record["dynamodb"]:
            print("New item:", record["dynamodb"]["NewImage"])
