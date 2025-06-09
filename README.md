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

Example Output

Recommendations for user1:
ItemId: movie23
ItemId: movie17
ItemId: movie45
