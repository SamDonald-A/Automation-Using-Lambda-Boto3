Thanks for Checking this out!  I am still working on this Document, It will be availabe soon...

# Monitor and Alert AWS Billing Using AWS Lambda, Boto3, and SNS
Objective: To create an automated alerting mechanism for when AWS billing exceeds a given threshold

Boto3 GitHub Link: https://github.com/SamDonald-A/Automation-Using-Lambda-Boto3/blob/main/billing_alert.py

<img width="466" height="552" alt="image" src="https://github.com/user-attachments/assets/25cb53a0-2d2b-4097-94a5-53aa9712c636" />

# My Current Billing Cost is $0.19

<img width="1573" height="740" alt="image" src="https://github.com/user-attachments/assets/e09373f3-fced-4bae-8453-c06861094a39" />


**Step 1: Create SNS Topic**

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/7d16a7da-3833-4da1-9ab8-58b9de2faf83" />

•	Select Standard and Give a Name for the Topic

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/718d974b-c6dd-476e-9669-e37c9c35df7a" />

•	Click Create Topic

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/73240d90-4a08-460f-b213-9b4aa881a9bb" />

•	After creating the topic click create subscription

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/43522c78-608e-4e7a-b857-b67b457a0a2a" />

•	Select Email Under Protocol and then add your mail id in the endpoint then click create subscription

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/369401c8-8bd4-4723-ab4e-6bb8ebe85ed4" />

•	It’s sent a subscription link to your mail

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/e38220a1-edcd-4297-b8cb-54f94372c09a" />

•	Check in the inbox and open and click Confirm subscribe

<img width="976" height="167" alt="image" src="https://github.com/user-attachments/assets/b76749d7-6fa7-499c-a3ed-72f8ee5dbc64" />
<img width="974" height="350" alt="image" src="https://github.com/user-attachments/assets/b65508fd-29ea-4ee0-9c57-65e5de10933a" />

•	Now it confirmed your subscription

<img width="976" height="498" alt="image" src="https://github.com/user-attachments/assets/4c06a4d1-bf6b-476c-afb5-bb3fa9827baf" />

•	We can see the subscription details here in the topic

<img width="976" height="453" alt="image" src="https://github.com/user-attachments/assets/7f4ecb44-d01f-41c4-aca5-4ad9e435c33c" />

**Step 2: Create New Lambda Function**

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/6218386f-1e90-4338-95a6-4679c044e472" />

•	Give a name and select runtime

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/90b987fd-83cd-416b-a032-281001675b14" />

•	Let’s create new role for this lambda

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/f6fb630d-1d48-4dfd-8081-488a8a0056a2" />

•	Go to IAM and click role in the left menu

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/ac898a4b-2668-4b30-bbd8-4930eea4c851" />

•	Then select lambda under use case

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/981241c0-625c-40fe-acd5-9cee0af4d7db" />

•	Add permissions for SNS and CloudWatch Matrices

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/6d12c168-05b6-4467-841f-980d56af6942" />

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/703c16b1-510e-4cf8-941a-b7061b496f8f" />

•	Now Give a Name for your Role

<img width="976" height="457" alt="image" src="https://github.com/user-attachments/assets/625d5eff-f71c-48ac-9736-1e2b1e9f79f3" />

•	Then click create role

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/33cafc6a-9e63-4c9c-87b9-66fda9ba31d7" />

<img width="976" height="180" alt="image" src="https://github.com/user-attachments/assets/ba945ac8-6dfb-4aba-ae2b-23c19f44cb3c" />

•	Now let’s go to Lambda and select role that we created

<img width="976" height="454" alt="image" src="https://github.com/user-attachments/assets/c2c32c59-5cd2-467b-a573-42bb9d6108fa" />

•	Then Go to Configuration tab from the new lambda dashboard

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/4a5ccae4-9d88-4e22-8385-e162ebe3d4df" />

•	Then click edit and change the timeout to 1 minute, then click save

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/3d054c09-9a67-4bb4-bbbd-a26e5e11167a" />

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/a7ec5b38-cb1c-4c44-9e69-ed431692235b" />

**Step 3: We need an Access key and secret key from AWS security credentials so that boto3 can access securely to our AWS accounts, to create the credentials go to AWS Security Credentials from the Main Menu top right corner options.**

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/57de75f9-4242-4f71-8d4d-b78ad2a07770" />

•	Then scroll to Access Key

<img width="976" height="460" alt="image" src="https://github.com/user-attachments/assets/c697be8d-444d-4fa8-8341-f33fabd8d79d" />

•	Now click create access key
•	If you are a Root user you might see this page, it’s not a common practice in creating access key as a root user because considering the security it’s suggested to create IAM user and use the Access Key, but for this project I am creating from the root user, later I will delete this access key. Now, let’s Click Create Access Key

<img width="976" height="459" alt="image" src="https://github.com/user-attachments/assets/cef8d084-6096-4474-96a7-261629382692" />

•	Now the credentials are very important, copy and save this or we can download it in the CSV file also.

<img width="976" height="490" alt="image" src="https://github.com/user-attachments/assets/493f4ef8-70fd-4935-973b-b57b6dc71421" />

•	Now we need to create a python code that can fetch the details from AWS CloudWatch matrices and gives us a result by comparing with our threshold budget
•	Before directly typing it in the lambda function, I would like to test it locally using VS Code Editor

<img width="976" height="522" alt="image" src="https://github.com/user-attachments/assets/d9cb51da-3774-4367-9510-df54725546e3" />

•	Now we see here the amount is Fixed value which is for the testing purpose where we’ll test the code that execute SNS, and Its works as it expects, Mail also received

<img width="1425" height="759" alt="image" src="https://github.com/user-attachments/assets/eec457bd-9594-4d38-893c-dff6d27db24b" />

<img width="976" height="184" alt="image" src="https://github.com/user-attachments/assets/50dbea03-c66b-4060-8993-7d44ab4b2f61" />

<img width="974" height="438" alt="image" src="https://github.com/user-attachments/assets/4510943c-4dbd-4b6b-aea4-f68aafd9a06a" />

•	Now let’s try to fetch the actual current cost from the CloudWatch Matrices and pass that value to the amount variable
•	But we see there is no update received since the Realtime data is not updated by the CloudWatch

<img width="1423" height="759" alt="image" src="https://github.com/user-attachments/assets/540957ff-01cd-4981-a6b7-db31d7af8037" />

<img width="1419" height="413" alt="image" src="https://github.com/user-attachments/assets/206e951e-63a8-4449-a26e-71b024889d0e" />

•	Let’s change our approach, instead of using CloudWatch let’s use Cost Explorer for the real time data
•	And as we expected, we get the amount from the AWS cost explorer and compared with our threshold and returns result for us

<img width="974" height="540" alt="image" src="https://github.com/user-attachments/assets/88d4cfe7-5fba-4532-8fe6-85de102f6b6f" />

•	Mail also received successfully	

<img width="976" height="209" alt="image" src="https://github.com/user-attachments/assets/79a038a6-a075-4680-b770-b028887158a5" />


<img width="976" height="359" alt="image" src="https://github.com/user-attachments/assets/c6be721e-b26d-41c2-b33a-557bf5abf4c5" />

•	Let’s work on the Lambda under the Code tab


<img width="976" height="454" alt="image" src="https://github.com/user-attachments/assets/0b931ac3-7922-4b9a-be37-0ba7dd6d53ba" />

•	Now we need to create an Environment variable for the credentials, But here I am only creating for my variables since this is a demo project, In Realtime it’s a good practice to create an Environment variables for all of the credentials and confidential information
•	To create Environment variables, click create Environment variables in the left bottom of the left side in the editor

<img width="976" height="455" alt="image" src="https://github.com/user-attachments/assets/e7e2b558-0401-4337-acfe-fd0e329dc4bb" />

•	Now add Environment variables

<img width="976" height="453" alt="image" src="https://github.com/user-attachments/assets/a1f6fd67-2f37-4a81-bedd-671b44d56134" />

•	Here we need the ARN of the topic that we created in the SNS, because we are going to trigger SNS in the lambda using boto3
•	Copy the ARN and add in the Environment variables

<img width="975" height="456" alt="image" src="https://github.com/user-attachments/assets/10286457-4a8b-4c3a-93a8-bc844770fd45" />

•	Copy the ARN and add in the Environment variables

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/d0a00f1e-e2ee-446a-bc36-bcb78ed140fd" />

•	Add other Environment variables too

<img width="975" height="453" alt="image" src="https://github.com/user-attachments/assets/7b7d19e1-2a7b-420d-a4aa-152a8db95078" />

•	Now we can see the variables added here

<img width="1423" height="657" alt="image" src="https://github.com/user-attachments/assets/4c1c484d-a1ee-4f78-bf05-32d4e9df5dd9" />

•	Rest of the code

<img width="975" height="452" alt="image" src="https://github.com/user-attachments/assets/d5391aef-c37f-4cb0-a6b5-3b3e857bcbf8" />

    import boto3
    import os
    from datetime import datetime, timedelta, timezone

    access_Key = 'Your Access Key from AWS Security Credentials'
    secret_access_key = 'Your Secret Access Key from AWS Security Credentials'
    aws_region='us-east-1'

    # Create Enviroinment Veriables and store the credentials in the Lambda function 
    SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN") 
    THRESHOLD_USD = float(os.environ.get("THRESHOLD_USD"))
    CURRENCY = os.environ.get("CURRENCY")

    ce = boto3.client('ce', aws_access_key_id=access_Key, aws_secret_access_key=secret_access_key, region_name=aws_region)
    sns = boto3.client('sns', aws_access_key_id=access_Key, aws_secret_access_key=secret_access_key, region_name=aws_region)


    # Getting the Cost from the Cost Explorer
    def get_cost():
    today = datetime.now(timezone.utc)
    start_of_month = today.replace(day=1)

    # To get the recent update from last 24 hours
    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start_of_month.strftime("%Y-%m-%d"),
            "End": today.strftime("%Y-%m-%d")
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )
    # amount variable for fetched result
    amount = float(response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"])
    print("Cost Explorer response:", response)
    return amount
 
    def lambda_handler(event=None, context=None):

    # Conforming we are getting the right data
    try:
        amount = get_cost()
    except Exception as e:
        print("Error fetching cost:", e)
        return {"status": "error", "message": str(e)}

    print(f"Current cost: ${amount:.2f} {CURRENCY} | Threshold: ${THRESHOLD_USD:.2f}")

    # Compare the recived amount to the threshold
    if amount >= THRESHOLD_USD:
        subject = "AWS Billing Alert — Threshold Exceeded"
        message = (
            f"Your estimated AWS charges have exceeded the threshold.\n\n"
            f"Current Charges: ${amount:.2f} {CURRENCY}\n"
            f"Threshold: ${THRESHOLD_USD:.2f}\n\n"
            "This is an automated notification from Your Lambda."
        )
        # If amount is greater than or equel to threshold the message will send as an email via SNS
        try:
            sns.publish(TopicArn=SNS_TOPIC_ARN, Subject=subject, Message=message)
            print("SNS alert published.")
        except Exception as e:
            print("SNS publish failed:", e)
        return {"status": "alert_sent", "amount": amount}
    # If the amount is not greater than or equel to threshold the below code will excecute
    else:
        print("Billing is within threshold.")
        return {"status": "ok", "amount": amount}

•	Deploy the code by clicking the deploy button in the left side of the editor

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/d76298df-7ede-44da-8e45-9a30e4921164" />

•	Now go to the test tab and create the test by giving name and empty Json object and save the test

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/344eb730-747d-4c8e-bb5f-becc8e5513d6" />

•	Click the test button to manually test the lambda function
•	We see that the lambda successfully ran and return the result

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/7694c2cd-ec0b-4080-b031-b60cbcb21090" />

<img width="975" height="335" alt="image" src="https://github.com/user-attachments/assets/579483b8-e881-4e82-9f1e-4b33e6f54de4" />

•	We can see that in the Cloud watch logGroup to study the logs

<img width="975" height="456" alt="image" src="https://github.com/user-attachments/assets/3c6700f9-6483-4245-a0ab-b6afa1f36663" />

<img width="975" height="452" alt="image" src="https://github.com/user-attachments/assets/95999103-d874-4e6e-b55e-12ea43ea3607" />

•	Mail also received

<img width="975" height="222" alt="image" src="https://github.com/user-attachments/assets/73e660f1-0770-4510-bf8d-6efdb7515d4d" />

<img width="973" height="420" alt="image" src="https://github.com/user-attachments/assets/ba6696c4-a180-4267-bb10-548d490441ce" />

**Step 4: Now let’s setup the EvenBridge amazon service to trigger the lambda daily or hourly**

•	Go to EvenBridge service and click rules under Buses from the left menu
•	Click create rule

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/d101112c-0ad9-43db-a8de-00f5cc5655e3" />

•	Give a name and select Schedule option and click continue to create rule

<img width="975" height="454" alt="image" src="https://github.com/user-attachments/assets/32436f26-f458-4bf9-9225-0d99206506e0" />

•	This is to define how many minutes (Or Hour or day) once your lambda has to be triggered
•	For the testing purpose I will give 12 minutes

<img width="975" height="454" alt="image" src="https://github.com/user-attachments/assets/b9199809-5c25-4d7b-859e-671a5a678a3d" />

•	Then Under target select lambda and under function select your lambda function

<img width="975" height="457" alt="image" src="https://github.com/user-attachments/assets/bbe300ea-3184-4ad6-974b-d48d1586e24d" />

•	Leave the default option and click Next

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/d6c95df5-d138-4142-b3d7-17a5a69f8ca3" />

•	Click Next here as well

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/91c61028-234b-4098-bbaa-ed661b111772" />

•	Review and click create rule

<img width="975" height="453" alt="image" src="https://github.com/user-attachments/assets/753d9a25-7a74-46da-b859-598e28f83ff7" />

<img width="975" height="457" alt="image" src="https://github.com/user-attachments/assets/360e5339-3f51-4d50-9a62-90f78264a5b8" />

•	Note the time when the rule is created

<img width="1421" height="705" alt="image" src="https://github.com/user-attachments/assets/1f1cc8f1-280b-4648-82ad-2f5db49ed86e" />

•	After saving the rule we must receive mail within 12 minutes
•	As expected, Mail also received within 12 minutes

<img width="975" height="237" alt="image" src="https://github.com/user-attachments/assets/1869d8c9-d4ee-426d-a529-25be3173b957" />

<img width="1420" height="781" alt="image" src="https://github.com/user-attachments/assets/a4a4693a-4668-4071-9ea1-feb256e8a009" />

•	We can see the logs in the CloudWatch logGroups 

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/8cd4c074-520e-4483-a1e8-31505bd3bdc0" />

<img width="1420" height="661" alt="image" src="https://github.com/user-attachments/assets/34f39743-784c-4364-bacd-98ad54e0cf23" />

•	To confirm let’s increase the Schedule time 15 Hours and check the mail inbox after 15 hours

<img width="975" height="456" alt="image" src="https://github.com/user-attachments/assets/15393b81-9f39-454b-82bd-4be87ae6129e" />

•	Leave the default value and click Next

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/e41e82ee-58e9-41b1-8b0d-d1e294a8f5e2" />

<img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/df2e3b81-c3be-4ed9-924a-d4296737c61c" />

•	So, this rule should trigger the Lambda after 15 Hours, Let’s wait and see

<img width="975" height="484" alt="image" src="https://github.com/user-attachments/assets/d8de6470-86d9-48b5-b285-b8e7f8d19b60" />

•	Note the time when you are saving your changes to the Scheduled Hours

<img width="1423" height="702" alt="image" src="https://github.com/user-attachments/assets/cd0e06a2-e78f-449e-9147-a2313c1f8255" />

•	As we expected the mail is received, Logs also register in CloudWatch

<img width="1423" height="720" alt="image" src="https://github.com/user-attachments/assets/de09f690-f82d-45a6-b598-840a592a6d10" />

•	We see the same price as last night we seen, lets cross check from the AWS console

<img width="1417" height="784" alt="image" src="https://github.com/user-attachments/assets/f7b151bc-a76f-4926-baa9-3e617d32058b" />

•	We see the same price in the AWS console as well

<img width="1421" height="702" alt="image" src="https://github.com/user-attachments/assets/08c02eb2-0976-47b9-8b70-fac85e3135c2" />

<img width="975" height="483" alt="image" src="https://github.com/user-attachments/assets/4b7d2c07-d04a-4e0d-bf3e-9aa7daf695a3" />

<img width="975" height="486" alt="image" src="https://github.com/user-attachments/assets/d99546d6-2fd2-4e07-bf49-d2fc21a004ea" />

•	Lately, I saw Bill was Increased by evening, So I decided to change scheduler to just 15 minutes to confirm it fetching the updated cost by triggering lambda and get it from the AWS Cost Explorer

<img width="1422" height="704" alt="image" src="https://github.com/user-attachments/assets/4fa4b991-9e83-4f20-8f48-36260d865ed1" />

<img width="1423" height="706" alt="image" src="https://github.com/user-attachments/assets/4086681b-6514-420c-b481-6bc0c0ed45a2" />

•	After 30 Minutes I got 2 mails, and successfully got the updated Cost

<img width="1423" height="722" alt="image" src="https://github.com/user-attachments/assets/a0517331-4b15-4c25-a4ac-6bac0eae8315" />

<img width="1346" height="743" alt="image" src="https://github.com/user-attachments/assets/ad22f5a7-6aba-4139-90f6-d2f7ed747b2b" />




Documentation by: Sam Donald A

Email: samdonaldand@gmail.com

GitHub: https://github.com/SamDonald-A

Website: www.samdonald.in

