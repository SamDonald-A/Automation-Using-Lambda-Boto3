- Automated Instance Management Using AWS Lambda and Boto3
Objective: Create a Lambda function that will automatically manage EC2 instances based on their tags.

Boto3 Git Links: https://github.com/SamDonald-A/Frontend-TravelMemory/tree/master 



- Step 1: Create 2 New Instances – One of them has a tag name “Sam-Auto-Stop” and another one has “Sam-Auto-Start”

•	One of the Instance which has to be Stopped by Lambda should be running
•	Another one which has be started by Lambda should not be running


<img width="976" height="471" alt="image" src="https://github.com/user-attachments/assets/89c5cadc-c7a1-4cce-a3de-a6e51619faf1" />



- Step 2: Create & configure Lambda

While Creating the Lambda function 

•	make sure you are selecting Runtime 


<img width="976" height="478" alt="image" src="https://github.com/user-attachments/assets/13fb3de2-f4a0-4ab6-9824-dc58cd369ce2" />


•	Select Role for the Permission

 
<img width="976" height="309" alt="image" src="https://github.com/user-attachments/assets/fedd32fa-c363-4cf6-b513-1a43a1830034" />

•	If role is not created – Create role under IAM role and Allow permission as EC2 Full Access then select your role in lambda function

<img width="976" height="481" alt="image" src="https://github.com/user-attachments/assets/e15835f2-d10b-43ef-8b11-9529d3de2198" />

- Step 3: Add your code In Lambda Function under Code Tab

<img width="976" height="479" alt="image" src="https://github.com/user-attachments/assets/f10463fa-ecb1-486d-bf47-3c107c7d47f6" />



    import boto3

    #Credentials for AWS
    access_Key = 'your-accesskey-from-aws-security-credentials'
    secret_access_key = 'your-secret-from-aws-security-credentials'
    aws_region='eu-west-2'
    
    #Passing the credentials in client
    response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': ['Sam-Auto-Stop']},
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
    )
 
    #To find the Instance that has Tag as Sam-Auto-Start
    response_2 = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': ['Sam-Auto-Start']},
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
    )

    #Creating the variable
    sam_auto_stop = None
    #To get the exact Instance's ID
    for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance.get('Tags'))
         #Storing the instance ID in the variable
        sam_auto_stop = instance['InstanceId']
        print(f"Sam-Auto-Stop ID: {sam_auto_stop}")
        print(f"Current State: {instance['State']['Name']}")
         #Stopping the exact Instance
        response_stop = ec2.stop_instances(
            InstanceIds=[sam_auto_stop]
        )



    #Creating the variable
    sam_auto_start = None
    #To get the exact Instance's ID
    for reservation in response_2['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance.get('Tags'))
         #Storing the instance ID in the variable
        sam_auto_stop = instance['InstanceId']
        print(f"Sam-Auto-Start ID: {sam_auto_start}")
        print(f"Current State: {instance['State']['Name']}")
         #Stopping the exact Instance
        response_start = ec2.start_instances(
            InstanceIds=[sam_auto_start]
        )



•	Deploy code by clicking Deploy Button


 <img width="976" height="477" alt="image" src="https://github.com/user-attachments/assets/9bae95bf-8b38-4533-8458-1b7e8cfa2545" />
 

- Step 4: Configure Timeout & Setup Test to trigger lambda and save

•	Update Timeout to 1 Minute 3 sec by clicking edit Button Under Configuration


 <img width="975" height="475" alt="image" src="https://github.com/user-attachments/assets/71edd255-8c10-419f-8d33-66dd0bcd1945" />


•	Under test create new test by giving event name, save and test the code

 <img width="975" height="476" alt="image" src="https://github.com/user-attachments/assets/0bca699d-b13f-48d8-a647-e66ce125ce59" />






•	After saving the Test, Click the test button to trigger the Lambda manually
<img width="976" height="475" alt="image" src="https://github.com/user-attachments/assets/3b4d3142-9937-41d9-848a-d2f426402ec6" />

 

- Step 5: Check the Instance state is changing after Lambda triggered

•	We can see the state is changing in the EC2 console
<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/d4b1e40d-7f9e-4f87-9dcb-23cd2398d6e9" />


•	Now the instance that supposed to stopped has been stopped and another one supposed to start has started


<img width="976" height="474" alt="image" src="https://github.com/user-attachments/assets/6e2690e5-1d83-4ca5-83a0-52ebcd846cf6" />


















Documentation by: Sam Donald A

Email: samdonaldand@gmail.com

GitHub: https://github.com/SamDonald-A

Website: www.samdonald.in
