# Audit S3 Bucket Permissions and Notify for Public Buckets Using AWS Lambda and Boto3
Objective: Automatically audit S3 bucket permissions and send notifications if any buckets have public read or write permissions.

Boto3 GitHub Links: https://github.com/SamDonald-A/Automation-Using-Lambda-Boto3/blob/main/auditS3Buckets.py 

# Step 1: Create SNS Topic

<img width="976" height="481" alt="image" src="https://github.com/user-attachments/assets/68254a99-2a68-4050-88f1-cb3d3a0b5b7d" />

•	Select standard and give a name to create topic

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/0eb296d2-1cb3-4632-9753-604f1f7a7881" />

<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/f0485bce-0606-4a53-96b5-b9361e24c17c" />

•	Then create subscription

<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/94c870ae-63cd-46f5-a9ef-18a1c658b152" />

•	Select email and in endpoint give your email id to be subscribed

<img width="976" height="470" alt="image" src="https://github.com/user-attachments/assets/db06886a-554a-4a19-b85d-36aa737eb781" />

•	Once subscription is created you will receive a Confirmation mail for the subscription

<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/ebe016ef-fe53-4dfa-842f-fb731ecbe40f" />

•	Click confirm subscription to receive mails from SNS

<img width="976" height="183" alt="image" src="https://github.com/user-attachments/assets/bb913e5d-4137-425d-9e76-b62699b4bdc8" />

<img width="972" height="312" alt="image" src="https://github.com/user-attachments/assets/faed7718-3327-4170-b02a-7745e592e619" />

<img width="976" height="498" alt="image" src="https://github.com/user-attachments/assets/2598d1b1-0423-4d79-b688-e2d143b0b938" />

# Step 2: Create Lambda Function

•	Click create function and give name and select your runtime
<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/4615014b-6b78-492d-b4e7-2bf655dd4047" />

<img width="976" height="470" alt="image" src="https://github.com/user-attachments/assets/6976e7a7-840b-4757-9205-22fddac6299d" />

•	Then Select role, make sure you have S3 permission in the IAM role that you are selecting for this Lambda

<img width="976" height="461" alt="image" src="https://github.com/user-attachments/assets/3212455e-7a04-4525-b2e0-aa93f2b2f171" />

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/19fd571a-c3d6-48e2-ab91-a9c3104aa464" />

•	Then Click create Function

<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/1074226a-0f44-4fd8-8320-199d9840d3b0" />

•	Go to Configuration tab and click edit

<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/124c4d68-da0d-44a8-ab1b-2669a6906a6e" />

•	Give 1 Min in the Timeout

<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/ab5a0fa0-1f51-4023-bff7-8d44ca71c96f" />

•	 type the code in the code editor under code tab

<img width="976" height="470" alt="image" src="https://github.com/user-attachments/assets/dca4ad31-b4bc-455c-91f3-a789d87a50d9" />

•	We also need to add an environment variable in lambda for the security purpose
•	Click add environment variables in left bottom of the code editor

<img width="974" height="410" alt="image" src="https://github.com/user-attachments/assets/c3dccc5e-20c7-4180-9d9b-26d1fb2a1982" />

•	Add environment variables – My case I am adding only one variable but it’s suggested to create Environment variables for all of your credentials

<img width="976" height="487" alt="image" src="https://github.com/user-attachments/assets/f5bc8210-b628-48d0-a495-6bdc23f73089" />

•	We see the added environment variable here, then Click deploy to deploy the code

<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/c21db085-88b4-4616-a525-3dacb0314da7" />

•	Now go to the test tab to create, save and test the lambda
•	Give a name and save the test

<img width="976" height="478" alt="image" src="https://github.com/user-attachments/assets/055fec49-a0b8-47ef-8ba4-40100016f706" />

•	Click the test button to run the lambda, and we see that the test can executed lambda and its running for 40 sec already.

<img width="976" height="478" alt="image" src="https://github.com/user-attachments/assets/f5ca3467-0080-45b1-a2df-9a94a73742f8" />

•	We have error here, lets read the error logs

<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/d25e71d3-1023-4710-9bd0-06415ce21eed" />

<img width="976" height="313" alt="image" src="https://github.com/user-attachments/assets/15615424-fab1-4331-b1e6-f1222b10da61" />

•	We can see the error logs in CloudWatch also
•	Select your lambda and see the latest logs to study them

<img width="976" height="468" alt="image" src="https://github.com/user-attachments/assets/0f040be5-ecde-473d-a2d6-2d165df539c5" />

<img width="976" height="485" alt="image" src="https://github.com/user-attachments/assets/56fc4a08-5be0-4fdd-bab1-29b9fc190d73" />

<img width="976" height="465" alt="image" src="https://github.com/user-attachments/assets/6ca42bbf-3b00-4528-bac7-49aa99b3755e" />

•	We see that the Time out error in the logs, we need to increase the Timeout in the configuration tab in lambda
•	Because there are 200+ buckets are available and its takes more than a one minute to audit them

<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/05859bbb-7f57-4a9d-91f0-75ff6f744dd1" />

•	Increase the timeout to 2:30 minutes and click save, and run a test again

<img width="976" height="468" alt="image" src="https://github.com/user-attachments/assets/59512b7d-e48b-4b4c-8532-162a827f47ed" />

<img width="976" height="479" alt="image" src="https://github.com/user-attachments/assets/5219bf31-d62b-4c51-b6fd-3ba47cd85719" />

•	Received mail from SNS and detected all the buckets that are public

<img width="976" height="207" alt="image" src="https://github.com/user-attachments/assets/2660ec9d-5397-4343-ab69-38eb07610e22" />

<img width="937" height="520" alt="image" src="https://github.com/user-attachments/assets/2a6a6397-4c71-4938-9dc6-c97a63f70b7a" />

# Step 3: Setup EvenBridge to trigger lambda every day or Hourly

•	Click Create rule in AWS EvenBridge under rules

<img width="976" height="476" alt="image" src="https://github.com/user-attachments/assets/f36c6314-5d42-42a2-8b49-eea50d2b9f3a" />

•	Give a name and select Schedule 

<img width="976" height="458" alt="image" src="https://github.com/user-attachments/assets/cb93fa02-d654-40e8-b4ea-60299150f507" />

•	And continue with scheduler, Here schedule your time for triggering lambda
•	My case I am giving 10 Minutes to check the triggering, It should trigger lambda every 10 minutes

<img width="976" height="507" alt="image" src="https://github.com/user-attachments/assets/aa53d50e-1b9f-494b-95cd-6e40051833f4" />

•	And Click Next and click Update rule, Check the time for reference

<img width="976" height="516" alt="image" src="https://github.com/user-attachments/assets/dcbf4419-fa18-4825-a284-7964a9d14e07" />

<img width="1347" height="715" alt="image" src="https://github.com/user-attachments/assets/72f114ec-860b-43ba-9aa5-f87af38cbd15" />

•	While updating is done the time is 8:41 and received 2 mails in next 20 Minutes

<img width="976" height="175" alt="image" src="https://github.com/user-attachments/assets/ba039504-ba7b-4044-8f83-8db842be60bb" />

<img width="1347" height="748" alt="image" src="https://github.com/user-attachments/assets/6249c53b-0c7c-41e2-998f-738052d3cba9" />

•	We can check the logs in the CloudWatch as well

<img width="976" height="491" alt="image" src="https://github.com/user-attachments/assets/484c48a0-5139-4cf7-9057-b436ce70dfa5" />

<img width="976" height="495" alt="image" src="https://github.com/user-attachments/assets/428652a0-8093-41b5-92b1-ad56327ead1f" />

Likewise, we can audit S3 buckets everyday through Amazon EventBridge, Schedule to 1 day and will receive alert every 24 hours once.

<img width="975" height="276" alt="image" src="https://github.com/user-attachments/assets/4da2e480-2c81-4116-a086-a42bae2aa5c6" />


Documentation by: Sam Donald A

Email: samdonaldand@gmail.com

GitHub: https://github.com/SamDonald-A

Website: www.samdonald.in

