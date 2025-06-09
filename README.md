# OTT-Recommendation-System
🚀 Built a Netflix-style Personalized Content Recommendation Engine using:

✅ Real-time user event ingestion → Kafka

 ✅ User-item interaction store → DynamoDB
 
 ✅ Model training pipeline → CSV → S3 → Amazon Personalize
 
 ✅ Trained model deployed as live API → serving recommendations
 
 ✅ Tested with Python → API returns top movie recommendations for each user.

Include the architecture diagram we created:

Kafka → DynamoDB → S3 → Personalize → Model → Campaign → API → React

Skills demonstrated:
✅ AWS Personalize
 ✅ Kafka Streaming
 ✅ Data Engineering Pipeline → DynamoDB → S3 → Personalize
 ✅ Real-world RecSys architecture
 ✅ Model training → API deployment → testing

Components
Kafka Producer
Simulate ott-view-events (userId, itemId, eventType, timestamp)

Kafka Consumer
Store interactions into DynamoDB table UserItemInteractions

DynamoDB → CSV Export
Export interactions → CSV → ready for Personalize import

## 🚀 Steps — OTT Content Recommendation System Demo

**Step 1 — Kafka Topic:** `ott-view-events` → ✅ *(created Kafka topic to capture user view events)*

**Step 2 — Kafka Producer:** `producer-code.py` → ✅ *(simulated user watch events → sent to Kafka topic `ott-view-events`)*

**Step 3 — Kafka Consumer:** `consumer-dynamodb.py` → ✅ *(listened on topic → processed events → stored user-item interactions in DynamoDB table `UserItemInteractions`)*

**Step 4 — DynamoDB Table:** `UserItemInteractions` → ✅ *(created table with `userId`, `itemId`, `eventType`, `watchCount`, `lastWatchedTimestamp`)*

**Step 5 — DynamoDB Export to CSV:** `newdynamoapi.py` or `personalize-interactions.py` → ✅ *(exported DynamoDB interactions → CSV `personalize-interactions.csv` → required format for Personalize)*

**Step 6 — Upload CSV to S3:** → ✅ *(uploaded CSV to `s3://ott-demo-bucketjune7/personalize/interactions/`)*

**Step 7 — Personalize Dataset Group:** `OTT-Recommendation-Group` → ✅ *(created Dataset Group in Amazon Personalize)*

**Step 8 — Personalize Dataset:** `OTT-Interactions` → ✅ *(created Interactions Dataset with required schema → `user_id`, `item_id`, `event_type`, `timestamp`)*

**Step 9 — Dataset Import Job:** → ✅ *(imported CSV from S3 → Personalize Dataset → Import job completed successfully)*

**Step 10 — Solution:** `solution-OTT-June9` → ✅ *(created Solution using `aws-user-personalization` recipe)*

**Step 11 — Solution Version:** → ✅ *(created Solution Version → triggered model training → Solution Version ACTIVE)*

**Step 12 — Campaign:** `OTT-Recommendation-Campaign` → ✅ *(deployed Campaign → live API endpoint created → ACTIVE)*

**Step 13 — Python API Test:** `personalize_get_recommendations.py` → ✅ *(tested Personalize API → retrieved personalized movie recommendations for userId → working successfully)*



Amazon Personalize

✅ Dataset Group → OTT-Recommendation-Group
✅ Interactions Dataset → user_id, item_id, event_type, timestamp
✅ Solution → aws-user-personalization recipe
✅ Solution Version → trained model
✅ Campaign → live recommendations API

Python API Testing
Use Personalize get_recommendations(userId) API → test recommendations

🛠️ Setup Steps

1️⃣ Simulate Kafka → ingest events

2️⃣ Store interactions in DynamoDB

3️⃣ Export CSV → S3

4️⃣ Import dataset into Personalize

5️⃣ Train Solution → Create Solution Version

6️⃣ Deploy Campaign → API ready

7️⃣ Test recommendations using Python

File	Purpose
producer-code.py	Generate real-time user view events → Kafka

consumer-dynamodb.py	Store events in DynamoDB → UserItemInteractions

newdynamoapi.py	Export DynamoDB → CSV → Personalize format

generate_interactions.py	Generate synthetic interactions for Personalize

personalize_get_recommendations.py	Test API → Get movie recommendations

Example Output

Recommendations for user1:
ItemId: movie23
ItemId: movie17
ItemId: movie45
