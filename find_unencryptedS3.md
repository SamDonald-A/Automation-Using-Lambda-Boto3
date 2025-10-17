# Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
Objective: Identify the buckets that are without server-side encryption.

Boto3 GitHub Links: https://github.com/SamDonald-A/Automation-Using-Lambda-Boto3/blob/main/find_unencryptedS3.py

Step 1: Create New Lambda Function

<img width="880" height="436" alt="image" src="https://github.com/user-attachments/assets/f4f4a598-0517-42be-9864-574b8e94916b" />

•	Give a name and select runtime

<img width="875" height="430" alt="image" src="https://github.com/user-attachments/assets/b8ae92fd-39f8-4be7-a1f6-b57dc47c8c6d" />

•	Make sure you are selecting your role and create function

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/d708b87c-50c7-4adc-807f-42423f8d2268" />

•	Make sure you have S3 permission in the role

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/85cc0885-873a-460c-a7fa-5470e985e156" />

•	Go to Configuration tab and click edit

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/13b4bdf3-3682-4c84-8cb3-f1e85559f2f5" />

•	Give 1 Min in the Timeout

<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/1209d6b3-f3dd-4738-827f-c638ef71667e" />

Step 2: type the code in the code editor under code tab

<img width="976" height="481" alt="image" src="https://github.com/user-attachments/assets/c1ad355e-ccac-49ab-9e7f-b11cbfa182cf" />

   
    import boto3
    from botocore.exceptions import ClientError
    from botocore.config import Config


    def lambda_handler(event, context):
    # Credentials for AWS
    access_Key = 'your-accesskey-from-security-credentials'
    secret_access_key = 'your-secret-from-security-credentials'
    aws_region='eu-west-2' 
    
   
    # Timeout for infinite execution
    config = Config(connect_timeout=5, read_timeout=5)
    # Create S3 resource and client
    s3 = boto3.resource('s3', aws_access_key_id=access_Key,
    aws_secret_access_key=secret_access_key,
    region_name=aws_region,config=config)
    client = s3.meta.client

    unencrypted_buckets = []
   
    # Check all buckets
    for bucket in s3.buckets.all():
          bucket_name = bucket.name
    # Check each bucket's encryptions
       try:
           print(f"Checking bucket: {bucket_name}")
            client.get_bucket_encryption(Bucket=bucket_name)
       except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                unencrypted_buckets.append(bucket_name)
            elif error_code == 'AccessDenied':
                print(f"Skipping {bucket_name} — Access Denied")
            else:
                print(f"Unexpected error on {bucket_name}: {error_code}")

        # Check each bucket's encryptions
        if unencrypted_buckets:
        print("Buckets without default encryption:")
        for b in unencrypted_buckets:
            print(f" - {b}")
        else:
        print(" All buckets have default encryption enabled.")

        return {
        "unencrypted_buckets": unencrypted_buckets,
        "count": len(unencrypted_buckets)
        }

•	Deploy code by clicking Deploy Button

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/e9cfad0e-1739-4294-975d-3d6fe48f2f8d" />

Step 3: Setup Test to trigger lambda and save

•	Under test create new test by giving event name, save and click test

<img width="976" height="477" alt="image" src="https://github.com/user-attachments/assets/4dd9e965-1521-4977-a9e7-4b899ede040e" />

•	After saving the Test, Click the test button to trigger the Lambda manually

<img width="976" height="482" alt="image" src="https://github.com/user-attachments/assets/12a8c6a7-e89c-4b0b-8dde-b484221b388c" />

Step 4: Check the CloudWatch for the logs

•	Go to CloudWatch under logs we see the log group and select your function

<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/f11462b2-b7b1-435c-a303-0d4a83f4b168" />

•	Click the latest log to study

<img width="976" height="483" alt="image" src="https://github.com/user-attachments/assets/cdeea0bb-7e2c-4dde-8a11-a668f1857a4e" />

•	We see in the logs, buckets are being checked its encryption

<img width="976" height="478" alt="image" src="https://github.com/user-attachments/assets/afdeb57b-c26c-42e6-9c8a-af3576c6ac60" />

•	But between error accrued as timeout, we need to fix the timeout minutes

<img width="972" height="84" alt="image" src="https://github.com/user-attachments/assets/f469cd12-1bbb-493b-8f4e-b5ca07c4cf74" />

•	The error also showing in the lambda

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/ee3acde9-81ae-4768-92f3-bd98cccea257" />

•	Go to Configuration tab and change the timeout between 5 to 10 min depends on the speed of the network and response, my case I give 7 min and click save

<img width="976" height="477" alt="image" src="https://github.com/user-attachments/assets/f48b2973-da4f-4cb1-81fd-5602f991ef8f" />

•	Now run the test again

<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/a10b0ebe-1c09-48e4-afb8-36100427b9d0" />

•	Check the Log stream again

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/d97acffc-3ed6-4549-8905-712275f8e445" />

•	Now we see that the code able to run successfully and showing result

<img width="1794" height="731" alt="image" src="https://github.com/user-attachments/assets/e9c2c883-2209-42a6-aa4a-85b9a071664e" />

•	The result also showing in the lambda

<img width="975" height="226" alt="image" src="https://github.com/user-attachments/assets/1d6b64e9-31b9-40e1-9a80-c2c65836bf6b" />

•	We see that the result is no unencrypted buckets are found 

<img width="1792" height="423" alt="image" src="https://github.com/user-attachments/assets/57c163af-e370-40a4-9c0c-92dbcd6b1d4d" />

# Default Encryption by AWS

**According to AWS:** after January 2023, the default encryption is enabled for bucket objects, so no more control on server-side encryption for us to enable, and that is why we in the result also not found any Unencrypted buckets.

**Read the Official Articles:**
1.	https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html
2.	https://aws.amazon.com/about-aws/whats-new/2023/01/amazon-s3-automatically-encrypts-new-objects/


Documentation by: Sam Donald A

Email: samdonaldand@gmail.com

GitHub: https://github.com/SamDonald-A

Website: www.samdonald.in


