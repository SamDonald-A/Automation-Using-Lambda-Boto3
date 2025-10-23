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

