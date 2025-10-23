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
      
