import boto3
from datetime import datetime, timezone
import json

def lambda_handler(event, context):
    try:
        print(f"Received event: {json.dumps(event)}")
        
        # Check if this is an EventBridge event
        if 'detail' not in event:
            return {
                'statusCode': 400,
                'body': 'Invalid event format. Expected EventBridge event with "detail" key.'
            }
        
        # Extract instance ID from EventBridge event
        if 'instance-id' not in event['detail']:
            return {
                'statusCode': 400,
                'body': 'Missing instance-id in event detail'
            }
        
        instance_id = event['detail']['instance-id']
        instance_state = event['detail'].get('state', 'unknown')
        
        print(f"Processing instance {instance_id} with state: {instance_state}")
        
        ec2_client = boto3.client("ec2")
        
        # Get details of the specific instance
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        
        if not response['Reservations']:
            return {
                'statusCode': 404,
                'body': f'Instance {instance_id} not found'
            }
        
        instance = response['Reservations'][0]['Instances'][0]
        
        # Check existing tags
        existing_tags = {}
        has_date_tag = False
        has_name_tag = False
        
        if 'Tags' in instance:
            for tag in instance['Tags']:
                existing_tags[tag['Key']] = tag['Value']
                if tag['Key'] == 'Date':
                    has_date_tag = True
                if tag['Key'] == 'Name':
                    has_name_tag = True
        
        print(f"Existing tags: {existing_tags}")
        
        # Prepare tags to add
        tags_to_add = []
        messages = []
        
        # Add Date tag if missing
        if not has_date_tag:
            current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            tags_to_add.append({
                'Key': 'Date',
                'Value': current_date
            })
            messages.append(f"Adding Date tag: {current_date}")
        else:
            messages.append(f"Date tag already exists: {existing_tags.get('Date')}")
        
        # Add Name tag if missing (with auto-generated name)
        if not has_name_tag:
            auto_name = f"EC2-{instance_id}-{datetime.now(timezone.utc).strftime('%Y%m%d')}"
            tags_to_add.append({
                'Key': 'Name',
                'Value': auto_name
            })
            messages.append(f"Adding Name tag: {auto_name}")
        else:
            messages.append(f"Name tag already exists: {existing_tags.get('Name')}")
        
        # Apply tags if there are any to add
        if tags_to_add:
            ec2_client.create_tags(
                Resources=[instance_id],
                Tags=tags_to_add
            )
            print(f"Successfully added {len(tags_to_add)} tag(s) to {instance_id}")
            for tag in tags_to_add:
                print(f"  - {tag['Key']}: {tag['Value']}")
        else:
            print(f"Instance {instance_id} already has both Date and Name tags")
        
        # Get updated tags
        updated_response = ec2_client.describe_instances(InstanceIds=[instance_id])
        updated_instance = updated_response['Reservations'][0]['Instances'][0]
        final_tags = {}
        if 'Tags' in updated_instance:
            final_tags = {tag['Key']: tag['Value'] for tag in updated_instance['Tags']}
        
        print(f"Final tags: {final_tags}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Successfully processed instance {instance_id}',
                'instance_id': instance_id,
                'state': instance_state,
                'actions': messages,
                'final_tags': final_tags
            })
        }
        
    except KeyError as e:
        error_msg = f"Missing required key in event: {str(e)}"
        print(f"KeyError: {error_msg}")
        print(f"Event structure: {json.dumps(event)}")
        return