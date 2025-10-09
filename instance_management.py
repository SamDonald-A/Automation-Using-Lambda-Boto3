import boto3

# Credentials for AWS
access_Key = 'your-access-key-from-aws-security-credentials'
secret_access_key = 'your-secret-key-from-aws-security-credentials'
aws_region='eu-west-2'

# Passing the credetials in client
ec2 = boto3.client('ec2',aws_access_key_id=access_Key,aws_secret_access_key=secret_access_key,region_name=aws_region,)

# To find the Instance that has Tag as Sam-Auto-Stop
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': ['Sam-Auto-Stop']},
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
)

# To find the Instance that has Tag as Sam-Auto-Start
response_2 = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': ['Sam-Auto-Start']},
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
)

# Creating the variable
sam_auto_stop = None
# To get the exact Instance's ID
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance.get('Tags'))
        # Storing the instance ID in the variable
        sam_auto_stop = instance['InstanceId']
        print(f"Sam-Auto-Stop ID: {sam_auto_stop}")
        print(f"Current State: {instance['State']['Name']}")
        # Stopping the exact Instance
        response_stop = ec2.stop_instances(
            InstanceIds=[sam_auto_stop]
        )


# Creating the variable
sam_auto_start = None
# To get the exact Instance's ID
for reservation in response_2['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance.get('Tags'))
        # Storing the instance ID in the variable
        sam_auto_start = instance['InstanceId']
        print(f"Sam-Auto-Start ID: {sam_auto_start}")
        print(f"Current State: {instance['State']['Name']}")
        # Starting the exact Instance
        response_start = ec2.start_instances(
            InstanceIds=[sam_auto_start]
        )
