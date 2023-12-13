import json
import boto3
import sys
import datetime

# Function to take in the file and tag the resources

def taggonator(resource_id, tags):
    
    #
    client = boto3.client('resourcegroupstaggingapi')
    response = client.tag_resources(
        ResourceARNList=[resource_id],
        Tags=tags
        
    )
    print(f"Tags added to {resource_id}: {response['ResponseMedadata']['HTTPSStatusCode']}")

def main():
    
    #Where is the input file
    file_path = sys.argv[1]

    #Read in the resource IDs from the file
    with open(file_path, 'r') as file:
        resource_ids = [line.strip() for line in file.readlines()]

    #Define the tags to be added
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    tags = [
        {'Key': 'RLEPodName', 'Value': 'Voltron'},
        {'Key': 'RLEProjectName', 'Value': 'RedLion'},
        {'Key': 'RLETPOC', 'Value': 'Dave Marshalonis'},
        {'Key': 'RLETPOCemail', 'Value': 'awsmarsh@amazon.com'},
        {'Key': 'RLEGPOC', 'Value': 'GPOC Marshalonis'},
        {'Key': 'RLEGPOCemail', 'Value': 'awsmarsh+voltron@amazon.com'},
        ]

    # Loop through resources and add tags
    for resource_id in resource_ids:
        taggonator(resource_id, tags)
    
    if __name__ == "__main__":
        main()

