import boto3

# Setup client for Personalize runtime
personalize_runtime = boto3.client('personalize-runtime', region_name='us-east-1')

# Your Campaign ARN → you will get this when Campaign becomes ACTIVE
campaign_arn = 'arn:aws:personalize:us-east-1:129317715590:campaign/OTT-Recommendation-Campaign'

# UserId you want recommendations for → must be from your training data!
user_id = 'user5'

# Number of recommendations to retrieve
num_results = 5

# Call Personalize runtime API
response = personalize_runtime.get_recommendations(
    campaignArn=campaign_arn,
    userId=user_id,
    numResults=num_results
)

# Print recommended items
print(f"Recommendations for User: {user_id}")
for item in response['itemList']:
    print(f"ItemId: {item['itemId']} → Score: {item.get('score', 'N/A')}")
