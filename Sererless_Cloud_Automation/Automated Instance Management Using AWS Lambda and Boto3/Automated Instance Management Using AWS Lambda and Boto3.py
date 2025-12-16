import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client("ec2")
    ec2_instance = ec2_client.describe_instances()
    Auto_Start = []
    Auto_Stop = []
    for reservation in ec2_instance['Reservations']:
        for instance in reservation['Instances']:
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            
            if tags.get('Action') == 'Auto-Stop':
                Auto_Stop.append(instance['InstanceId'])
            if tags.get('Action') == 'Auto-Start':
                Auto_Start.append(instance['InstanceId'])
    print(f"\nAll Auto-Stop instances: {Auto_Stop}")
    print(f"All Auto-Start instances: {Auto_Start}")

    if Auto_Start:
        for start in Auto_Start:
            ec2_start = ec2_client.start_instances(InstanceIds=[start])
            print (f"Started instance : {start}")
    else:
        print("There is no **instance** with tag Auto-Start")
    if Auto_Stop:
        for stop in Auto_Stop:
            ec2_stop = ec2_client.stop_instances(InstanceIds=[stop])
            print(f"Stopped instance : {stop}")
    else:
        print("There is no **instance** with tag Auto-Stop")
    return {
        'statusCode': 200,
        'body': f'Started {len(Auto_Start)} instances, Stopped {len(Auto_Stop)} instances'
    }
