import boto3
import os
import json
# Import Thread Pool to control the repeated executor in loop
from concurrent.futures import ThreadPoolExecutor, as_completed


def lambda_handler(event, context):
    # Aws Credentials
    access_Key = 'your-accesskey-from-security-credentials' # Setup an Enviroinment variable in lambda
    secret_access_key = 'your-secret-accesskey-from-security-credentials' # Setup an Enviroinment variable in lambda
    aws_region='eu-west-2'
    SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN") # Setup an Enviroinment variable in lambda

    # Create S3 and SNS clients
    s3 = boto3.client('s3', aws_access_key_id=access_Key, aws_secret_access_key=secret_access_key,region_name=aws_region)
    sns = boto3.client('sns', aws_access_key_id=access_Key, aws_secret_access_key=secret_access_key, region_name=aws_region)

    # Function to check if a bucket is public via its policy
    def is_public(bucket_name):
        try:
            policy = s3.get_bucket_policy(Bucket=bucket_name)
            policy_json = json.loads(policy['Policy'])
            for stmt in policy_json.get('Statement', []):
                if stmt.get('Effect') == 'Allow' and stmt.get('Principal') in ('*', {'AWS': '*'}):
                    return bucket_name
        except s3.exceptions.ClientError:
            return None

    # Get all buckets
    buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
    public_buckets = []

    # Use threads to check 10 buckets each time since we have more than 200 buckets and can audit faster
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(is_public, name): name for name in buckets}
        for future in as_completed(futures):
            result = future.result()
            if result:
                public_buckets.append(result)

    # Sending SNS alert if buckets are detected
    if public_buckets:
        message = "Hi Sam Donald, Public S3 Buckets Detected:\n" + "\n".join(public_buckets)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='Public S3 Bucket Alert',
            Message=message
        )
        print("Alert sent:", public_buckets)
        
    # If no bucket found
    else:
        print("No public buckets found.")

    return {
        'statusCode': 200,
        'public_buckets': public_buckets
    }
