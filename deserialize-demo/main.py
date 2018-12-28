import boto3
import json
import deserialize as ds

ec2Client = boto3.client('ec2')

def lambda_handler(event, context):
    response = ec2Client.describe_instances()
    return json.loads(json.dumps(response, default = ds.deserialize))