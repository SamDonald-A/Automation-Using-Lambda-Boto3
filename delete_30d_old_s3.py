import boto3
from datetime import datetime, timezone, timedelta

# AWS Credentials
access_Key = 'your-accesskey-from-AWS-security-credentials'
secret_access_key = 'your-secret-from-AWS-security-credentials'
aws_region='eu-west-2'

# Passing the credetials in client
s3 = boto3.resource('s3',aws_access_key_id=access_Key,aws_secret_access_key=secret_access_key,region_name=aws_region)

# passing the bucket name and saving it in a variable
bucket_name = "samcloudfrontbuc"
bucket = s3.Bucket(bucket_name)

# compare dates
delete_date = datetime.now(timezone.utc) - timedelta(days=30)

# variable to store deleted objects
deleted_count = 0
#deleting by finding the right bucket and its objects
for obj in bucket.objects.all():
    try:
        if obj.last_modified < delete_date:
            obj.delete()
            deleted_count += 1
            print(f"Deleted: {obj.key} (Last Modified: {obj.last_modified})")
    except s3.meta.client.exceptions.NoSuchKey: # error handeling
        print(f"Object not found: {obj.key}, skipping.")
    except Exception as e:
        print(f"Failed to delete {obj.key}: {e}")
# deleted objects
print(f"Total objects deleted from {bucket_name}: {deleted_count}")
