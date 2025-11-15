#!/bin/sh
# Wait for DynamoDB Local to start
sleep 2

echo "Creating DynamoDB table MyMessages..."

export AWS_ACCESS_KEY_ID=dummy
export AWS_SECRET_ACCESS_KEY=dummy
export AWS_REGION=us-east-1

aws dynamodb create-table \
  --table-name MyMessages \
  --attribute-definitions AttributeName=MessageId,AttributeType=S \
  --key-schema AttributeName=MessageId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --endpoint-url http://dynamodb-local:8000 \
  --region us-east-1

aws dynamodb list-tables --endpoint-url http://dynamodb-local:8000 --region us-east-1

echo "Table creation complete."
