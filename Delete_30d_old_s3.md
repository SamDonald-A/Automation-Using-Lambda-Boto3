# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
Objective: Automate the deletion of files older than 30 days in a specific S3 bucket.

Boto3 GitHub Links: https://github.com/SamDonald-A/Automation-Using-Lambda-Boto3/blob/main/delete_30d_old_s3.py 

Step 1: Create New S3 Bucket

•	Go to S3 Bucket and Click Create Bucket

<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/164278b2-2ddf-437d-a79a-2f83cbaac483" />

•	Give a name and create bucket

<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/d73bc5ad-0eb4-4dd6-a22d-8a85712fd291" />

<img width="976" height="477" alt="image" src="https://github.com/user-attachments/assets/5ecff7b9-b957-4488-beb5-7e33facffe23" />

Step 2: Upload files in the bucket and change the system date & time or select any old bucket that are created 30 days before, Or wait for 30 days

•	Uploading files in the bucket

<img width="975" height="476" alt="image" src="https://github.com/user-attachments/assets/353c0992-00bb-49bd-8de0-265297c608ae" />

<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/4a8416d5-b23e-4f30-96a5-694e8bd5b026" />

•	For this project I am selecting a bucket that is created before 30 days

<img width="1493" height="731" alt="image" src="https://github.com/user-attachments/assets/07ee4f46-9a9d-4431-ae09-ce0709b92991" />

•	This bucket has file that are uploaded before 30 days and within the 30 days
•	My current date is 11-10-2025 and the files that are uploaded before and within the 30 days is available here


<img width="1427" height="735" alt="image" src="https://github.com/user-attachments/assets/c08c05a8-8ed4-40ce-835b-361926454a98" />

Step 3: Create & configure Lambda

•	Click create function 

<img width="975" height="480" alt="image" src="https://github.com/user-attachments/assets/760610c5-7dbd-4b00-98d5-dcc9cd4189ee" />

While Creating the Lambda function 

•	After giving a name, make sure you are selecting Runtime 

<img width="976" height="477" alt="image" src="https://github.com/user-attachments/assets/d8c64579-8d56-4446-b426-c316d720745f" />

•	Select Role for the Permission

<img width="976" height="479" alt="image" src="https://github.com/user-attachments/assets/3ec3eee9-a8cb-4142-84a9-04477dd7df29" />

•	If role is not created – Create role under IAM role and Allow permission as S3 Full Access then select your role in lambda function

<img width="976" height="481" alt="image" src="https://github.com/user-attachments/assets/e087fc17-db57-418c-b931-ce3bc45791dd" />

Step 4: Add your code In Lambda Function under Code Tab    

    import boto3
    from datetime import datetime, timezone, timedelta

    # AWS Credentials
    access_Key = 'your-access-key-from-aws-security-credentials'
    secret_access_key = 'your-secret-key-from-aws-security-credentials'
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


•	Deploy code by clicking Deploy Button

<img width="976" height="507" alt="image" src="https://github.com/user-attachments/assets/2398a981-5ede-4a54-835f-dc6ab9b63f49" />


Step 5: Configure Timeout & Setup Test to trigger lambda and save

•	Update Timeout to 1 Minute 3 sec by clicking edit Button Under Configuration

<img width="976" height="472" alt="image" src="https://github.com/user-attachments/assets/bc51c032-f386-40ae-861f-c7da13eff79a" />

•	Under test create new test by giving event name, save and test the code

<img width="976" height="479" alt="image" src="https://github.com/user-attachments/assets/f5a696fe-30f4-4198-b67a-035f3d96a3c7" />

•	After saving the Test, Click the test button to trigger the Lambda manually

<img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/f9635750-eeb3-47b9-8ecf-92fd20ce9de5" />

Step 6: Check the bucket and see if the objects are deleted that are 30 days old

•	We can see that only few old files are deleted, but still its not deleted all of them, before it was 7 files now 5 files, which means the code was not running fully. 

<img width="976" height="508" alt="image" src="https://github.com/user-attachments/assets/5c0b2dce-7db6-4ab6-83b7-fa6c1611e6a2" />

•	The error also showing in the lambda

<img width="976" height="507" alt="image" src="https://github.com/user-attachments/assets/38f8362f-5a4e-4989-bfc4-04c1bfa575cf" />

•	Let’s study the error log from CloudWatch and adjust the code in lambda
•	Go to cloud watch and select the correct lambda function under log group menu

<img width="976" height="483" alt="image" src="https://github.com/user-attachments/assets/68984208-3dd4-47a7-ab8e-5440de0747e0" />

•	Click the latest log streams and study the logs 

<img width="976" height="479" alt="image" src="https://github.com/user-attachments/assets/1976e91b-9ac1-4ae2-8c37-74fdacd6657f" />

<img width="976" height="483" alt="image" src="https://github.com/user-attachments/assets/991b0790-63e8-440f-a00b-574084e2d135" />

Step 7: Change the code accordingly and deploy again

<img width="976" height="510" alt="image" src="https://github.com/user-attachments/assets/ba0455cc-b014-4ef0-8f8f-46250be59594" />

•	Check the S3 bucket, now everything is deleted that are older than 30 days.
only one file is available that is uploaded within the 30 days.

<img width="976" height="511" alt="image" src="https://github.com/user-attachments/assets/8bbd0fd1-9418-47f5-aff1-b8df05386b99" />

•	Open log stream to study the logs if you need more information

<img width="976" height="483" alt="image" src="https://github.com/user-attachments/assets/056747af-b726-4dd7-b25f-1b14e84f80cb" />


Documentation by: Sam Donald A
Email: samdonaldand@gmail.com
GitHub: https://github.com/SamDonald-A
Website: www.samdonald.in



















