from kafka import KafkaConsumer
import json
import boto3
from botocore.exceptions import ClientError

# DynamoDB config
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserItemInteractions')

# Kafka Consumer config
consumer = KafkaConsumer(
    'ott-view-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='ott-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Consumer started. Listening for events...")

# Consume messages
for message in consumer:
    event = message.value
    print(f"✅ Received event: {event}")

    # Auto-increment watchCount
    try:
        response = table.update_item(
            Key={
                'userId': event['userId'],
                'itemId': event['itemId']
            },
            UpdateExpression="ADD watchCount :inc SET lastWatchedTimestamp = :ts",
            ExpressionAttributeValues={
                ':inc': 1,
                ':ts': event['timestamp']
            },
            ReturnValues="UPDATED_NEW"
        )
        print(f"✅ Updated DynamoDB: userId={event['userId']}, itemId={event['itemId']}, watchCount={response['Attributes']['watchCount']}")
    except ClientError as e:
        print(f"❌ Error updating DynamoDB: {e.response['Error']['Message']}")
