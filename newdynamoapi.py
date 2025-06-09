import boto3
import csv
from datetime import datetime
import time

# Config
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserItemInteractions')

# Output CSV file
csv_file_name = 'personalize-interactions.csv'

# CSV header
csv_header = ['user_id', 'item_id', 'event_type', 'timestamp']

# Start scan
print("✅ Starting DynamoDB scan...")
response = table.scan()
items = response['Items']
total_items = len(items)

# Pagination handling
while 'LastEvaluatedKey' in response:
    print(f"✅ Scanned {total_items} items so far... fetching more...")
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response['Items'])
    total_items = len(items)

print(f"✅ Total items scanned: {total_items}")

# Write to CSV
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)

    for item in items:
        user_id = item['userId']
        item_id = item['itemId']
        event_type = 'watch'  # or change if you add more event types

        # Convert ISO timestamp to UNIX timestamp
        timestamp_dt = datetime.strptime(item['lastWatchedTimestamp'], "%Y-%m-%dT%H:%M:%SZ")
        timestamp_unix = int(time.mktime(timestamp_dt.timetuple()))

        writer.writerow([user_id, item_id, event_type, timestamp_unix])

print(f"✅ CSV file '{csv_file_name}' created successfully with {total_items} records!")
