https://github.com/localstack/awscli-local

# Build
`sam build --template-file template.yaml`

# Run Local API
`sam local start-api`

# Invoke Lambda
`sam local invoke SQSEventConsumer -e events/sqs_event.json`

# Start Lambda
```
sam local start-lambda
```
```
aws sqs create-queue --queue-name MyLearningQueue
```
```
aws sqs get-queue-url --queue-name MyLearningQueue
```

```
aws lambda create-event-source-mapping \ 
  --function-name SQSEventConsumer \ 
  --batch-size 1 \ 
  --event-source-arn arn:aws:sqs:us-east-1:YOUR-AWS-ACCOUNT:MyLearningQueue \ 
  --endpoint-url http://127.0.0.1:3001
```

```
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/YOUR-AWS-ACCOUNT/MyLearningQueue \
  --message-body "Hello from SQS"
```


# Create DynamoDB Local
```
aws dynamodb create-table \
  --table-name MyMessages \
  --attribute-definitions AttributeName=MessageId,AttributeType=S \
  --key-schema AttributeName=MessageId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --endpoint-url http://localhost:8000
```

## Check Tables
```
aws dynamodb list-tables --endpoint-url http://localhost:8000

```

# Verify DynamoDB Item
```
aws dynamodb scan \
  --table-name MyMessages \
  --endpoint-url http://localhost:8000 \
  --output json
```