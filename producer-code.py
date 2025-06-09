from confluent_kafka import Producer
import json
import random
import time
from datetime import datetime

# Kafka configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Example data
user_ids = [f"user{num}" for num in range(1, 11)]           # 10 users
movie_ids = [f"movie{num}" for num in range(101, 121)]      # 20 movies
event_types = ["watch"]

# Function to generate a random event
def generate_event():
    event = {
        "userId": random.choice(user_ids),
        "itemId": random.choice(movie_ids),
        "eventType": random.choice(event_types),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    return event

# Produce N events
N = 100
for i in range(N):
    event = generate_event()
    producer.produce('ott-view-events', json.dumps(event).encode('utf-8'))
    producer.flush()
    print(f"[{i+1}/{N}] Sent event: {event}")

    # Optional: slight delay to simulate real-time stream
    time.sleep(0.1)

print("✅ All events sent to ott-view-events topic!")

