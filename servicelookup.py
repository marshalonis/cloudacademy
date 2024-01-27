import json
import sys

# JSON data
data = '''
[
    {
        "serviceName": "Amazon EC2",
        "arnFormat": "arn:aws:ec2:region:account-id:ec2/resource-id"
    },
    {
        "serviceName": "Amazon S3",
        "arnFormat": "arn:aws:s3:::bucket-name/resource-id"
    },
    {
        "serviceName": "Amazon:DynamoDB",
        "arnFormat": "arn:aws:dynamodb:region:account:table/resource-id"
    }
]
'''



def find_arn_format(service_name):
    # Convert JSON string into Python object
    service_region = "us-east-1"
    service_account = "1111111111"
    services = json.loads(data)

    # Search for the service
    for service in services:
        if service['serviceName'] == service_name:
            return service['arnFormat']

    return "Service name not found"

# Example usage
service_name_to_search = sys.argv[1]
resource_name = sys.argv[2]
service_region = "us-east-1"
service_account = "1111111111"
arn_format = find_arn_format(service_name_to_search)
account_arn = arn_format.replace("account", service_account)
region_arn = account_arn.replace("region", service_region)
resource_arn = region_arn.replace("resource-id", resource_name)
#print(region_arn)
print(f"ARN Format for {service_name_to_search}: {resource_arn}")
#print(service_account)
