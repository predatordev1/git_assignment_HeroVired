import boto3  
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    bucket_name = 'your-bucket-name-cleanup-demo'
    days_threshold = 30 
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)
    deleted_files = [] 
    kept_files = []  
    
    try:
        # Paginator handles large buckets by fetching results in chunks
        # This prevents memory issues when buckets have thousands of files
        paginator = s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name)
        for page in pages:
            if 'Contents' not in page:
                print(f"No objects found in bucket {bucket_name}")
                return {
                    'statusCode': 200,
                    'body': 'No objects to process'
                }
            
            for obj in page['Contents']:
                object_key = obj['Key']
                last_modified = obj['LastModified']
                if last_modified < cutoff_date:
                    print(f"Deleting: {object_key} (Last Modified: {last_modified})")
                    s3_client.delete_object(Bucket=bucket_name, Key=object_key)
                    deleted_files.append(object_key)
                else:
                    print(f"Keeping: {object_key} (Last Modified: {last_modified})")
                    kept_files.append(object_key)
        return {
            'statusCode': 200,  # HTTP status code for success
            'body': {
                'message': f'Cleanup completed for bucket: {bucket_name}',
                'deleted_count': len(deleted_files),
                'kept_count': len(kept_files),  
                'deleted_files': deleted_files   
            }
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,  # HTTP status code for server error
            'body': f'Error: {str(e)}'  # Error message details
        }