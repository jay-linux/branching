import json
import dev2
def lambda_handler(event, context):
    clinet = boto3.client('ec2', region_name='ap-south-1')
    response = ec2.run_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        MinCount=1,
        MaxCount=1
    )
  
