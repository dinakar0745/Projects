import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'ap-southeast-2'

# Gmail SMTP configuration
GMAIL_USERNAME = 'dinakara.pathakota@gmail.com'
GMAIL_PASSWORD = 'lqus scgq ipzr kekt'

def send_email(subject, body):
    try:
        # Set up the SMTP server
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        # Create message
        message = MIMEMultipart()
        message['From'] = GMAIL_USERNAME
        message['To'] = 'dinakar.pathakota@gmail.com'
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send email
        smtp_server.send_message(message)
        smtp_server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email: ", str(e))

def lambda_handler(event, context):
    #Create an EC2 client
    ec2_client = boto3.client('ec2', region_name=AWS_REGION)
    try:
        # Describe all EC2 instances
        response = ec2_client.describe_instances()

        # Extract information about the instances and their status
        instance_data = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                instance_data.append({'InstanceId': instance_id, 'State': instance_state})

        # Prepare email subject and body
        email_subject = "EC2 Instance Status Report"
        email_body = "EC2 Instance Status:\n"
        for instance in instance_data:
            email_body += f"Instance ID: {instance['InstanceId']}, State: {instance['State']}\n"

        # Send email
        send_email(email_subject, email_body)

    except Exception as e:
        # Handle any errors
        print("Error:", str(e))
        # You can also send an email here to notify about the error

        
    return {
        'statusCode': 200,
        'body': 'Email sent successfully'
    }
