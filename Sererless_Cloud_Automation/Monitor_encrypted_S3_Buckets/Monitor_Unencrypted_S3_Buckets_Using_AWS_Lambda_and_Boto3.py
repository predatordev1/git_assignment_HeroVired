import boto3

def lambda_handler(event, context):
    s3_client = boto3.client("s3")
    response = s3_client.list_buckets()
    sse_s3_buckets = []
    sse_kms_buckets = []
    dsse_kms_buckets = []

    for bucket in response['Buckets']:
        try:
            bucket_name = bucket['Name']
            encryption_check = s3_client.get_bucket_encryption(Bucket=bucket_name)
            sseAlgorithm = encryption_check['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            if sseAlgorithm == 'AES256':
                sse_s3_buckets.append(bucket_name)
            elif sseAlgorithm == 'aws:kms':
                sse_kms_buckets.append(bucket_name)
            else:
                dsse_kms_buckets.append(bucket_name)
            
        except s3_client.exceptions.ServerSideEncryptionConfigurationNotFoundError:
            print(f"✗ {bucket_name}: NO ENCRYPTION (rare)")
        except Exception as e:
            print(f"⚠ {bucket_name}: Error - {e}")

    print(f"\n{'*'*50}")
    print(f"\nSSE-S3 buckets: {sse_s3_buckets}")
    print(f"\nSSE-KMS buckets: {sse_kms_buckets}")
    print(f"\nDSSE-KMS buckets: {dsse_kms_buckets}\n")
    print(f"\n{'*'*50}")
    return{
        'statusCode': 200,
        'body': f'{len(sse_s3_buckets)} buckets are with SSE-S3 encryption named {sse_s3_buckets}. {len(sse_kms_buckets)} buckets are with SSE-KMS encryption named {sse_kms_buckets}.{len(dsse_kms_buckets)} buckets are with DSSE-KMS encryption named {dsse_kms_buckets}'

        }
