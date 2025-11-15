import json

def lambda_handler(event, context):
    """Sample Lambda function that returns a greeting."""
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from your mock SAM application!"}),
        "headers": {
            "Content-Type": "application/json"
        }
    }