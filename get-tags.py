import boto3
import csv
import os

os.environ['AWS_PROFILE'] = "awsmarsh+RLE-gsproto-deploy-Admin"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

# Initialize AWS client
session = boto3.Session()
client = session.client('resourcegroupstaggingapi')
boto3.set_stream_logger('botocore', level='DEBUG')

# Define AWS service types you want to include
#resource_types = ['ec2', 's3', 'rds']
resource_types = []
# Initialize an empty list to store resource data
resource_data = []

# Loop through each resource type
#for resource_type in resource_types:
    # Get resources with tags for the specified resource type
response = client.get_resources(
        ResourceTypeFilters=[],
        TagFilters=[],
        #ResourcesPerPage=0
    )

for resource in response['ResourceTagMappingList']:
        resource_arn = resource['ResourceARN']
        resource_tags = resource.get('Tags', [])
        resource_data.append((resource_arn, resource_tags))

# Define the CSV file name
csv_file_name = 'isengard-aws_resources_tags.csv'

# Write resource data to a CSV file
with open(csv_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write CSV header
    csv_writer.writerow(['Resource ARN', 'Tags'])
    # Write resource data
    for resource_arn, resource_tags in resource_data:
        csv_writer.writerow([resource_arn, ', '.join([f"{tag['Key']}:{tag['Value']}" for tag in resource_tags])])

print(f"CSV report saved as {csv_file_name}")