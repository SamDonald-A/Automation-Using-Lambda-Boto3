import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

def lambda_handler(event, context):
    # Credentials
    access_Key = 'Your AWS Access Key from Your Security Credentials'
    secret_access_key = 'Your AWS Secret Access Key from Your Security Credentials'
    aws_region='eu-west-2'
    # timeout for infinite excecution
    config = Config(connect_timeout=5, read_timeout=5)
    
    # Create S3 resource and client
    s3 = boto3.resource('s3', aws_access_key_id=access_Key, aws_secret_access_key=secret_access_key,region_name=aws_region,config=config)
    client = s3.meta.client

    unencrypted_buckets = []

    # check all buckets
    for bucket in s3.buckets.all():
        bucket_name = bucket.name

        # Check each bucket's encriptions
        try:
            print(f"Checking bucket: {bucket_name}")
            client.get_bucket_encryption(Bucket=bucket_name)
            # Error Handeling
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                unencrypted_buckets.append(bucket_name)
            elif error_code == 'AccessDenied':
                print(f"Skipping {bucket_name} — Access Denied")
            else:
                print(f"Unexpected error on {bucket_name}: {error_code}")

    # Getting all unencripted and encripted buckets
    if unencrypted_buckets:
        print("Buckets without default encryption:")
        for b in unencrypted_buckets:
            print(f" - {b}")
    else:
        print(" All buckets have default encryption enabled.")
    # Result
    return {
        "unencrypted_buckets": unencrypted_buckets,
        "count": len(unencrypted_buckets)
    }

