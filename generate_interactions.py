import csv
import random
import time
from datetime import datetime, timedelta

# Parameters
num_users = 100   # number of unique users
num_items = 50    # number of unique movies/items
num_interactions = 2000  # total number of interactions

# Possible event types
event_types = ["watch", "like", "share"]

# Prepare data
user_ids = [f"user{u}" for u in range(1, num_users + 1)]
item_ids = [f"movie{m}" for m in range(1, num_items + 1)]

# Starting timestamp (e.g., now - 30 days)
start_time = datetime.now() - timedelta(days=30)

# Generate interactions
rows = []
for _ in range(num_interactions):
    user_id = random.choice(user_ids)
    item_id = random.choice(item_ids)
    event_type = random.choice(event_types)
    # Random timestamp in last 30 days
    random_seconds = random.randint(0, 30 * 24 * 60 * 60)
    event_time = start_time + timedelta(seconds=random_seconds)
    timestamp = int(event_time.timestamp())
    
    rows.append([user_id, item_id, event_type, timestamp])

# Write CSV
output_file = "personalize-interactions.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Header
    writer.writerow(["user_id", "item_id", "event_type", "timestamp"])
    # Data
    writer.writerows(rows)

print(f"✅ Generated {num_interactions} interactions → {output_file}")
