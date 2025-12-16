# Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

## Step 1: Creation of EC2 instances as Key = Action and  value = Auto-start and Auto-stop.
### Creation of EC2 instance with Key = Action and  value = Auto-Start.
<img width="1212" height="507" alt="image" src="https://github.com/user-attachments/assets/c80b45f7-77fd-45a6-a17c-4e2f500b494b" />

### Creation of EC2 instance with Key = Action and  value = Auto-Stop.
<img width="1182" height="505" alt="image" src="https://github.com/user-attachments/assets/a2150750-09b5-411a-8bda-a5a4adf63456" />
<img width="1888" height="293" alt="image" src="https://github.com/user-attachments/assets/1e79da07-d44f-4ee3-8c4b-968e679f5a49" />

## Step 2: Creation IAM Role to execute Lamda function with assigning permission of EC2 for Lambda Execution.
<img width="995" height="702" alt="image" src="https://github.com/user-attachments/assets/31584c4f-98be-4c45-98b9-58198b07734c" />

### Select Role option and click on create Role.
<img width="1857" height="486" alt="image" src="https://github.com/user-attachments/assets/b953e42b-d91f-43e0-a039-90364229bcfd" />

### Choose Trusted entity type = AWS Service and Use case = Lambda.
<img width="1475" height="717" alt="image" src="https://github.com/user-attachments/assets/beddd37d-5444-4dcd-b183-a5896d46163f" />

### Assign permission for Role by selecting AmazonEC2FullAccess & AWSLambdaBasicExecutionRole.
<img width="1597" height="226" alt="image" src="https://github.com/user-attachments/assets/022e0f4b-717a-4285-9ad0-e91ac08e1065" />

### Give name for Role and click on create Role.
<img width="1550" height="450" alt="image" src="https://github.com/user-attachments/assets/2f963399-7cbe-4e2e-8665-895e9404f8dd" />

### Now again click on Role and search for your Role.
<img width="1917" height="518" alt="image" src="https://github.com/user-attachments/assets/d574b7f1-ca1e-4625-86f6-dffafbf1995d" />

## Step 3:Coding: https://github.com/predatordev1/git_assignment_HeroVired/blob/main/Sererless_Cloud_Automation/Automated%20Instance%20Management%20Using%20AWS%20Lambda%20and%20Boto3/Automated%20Instance%20Management%20Using%20AWS%20Lambda%20and%20Boto3.py
#### - Using Boto3 in the Lambda function. To Detect all EC2 instances with the `Auto-Stop` tag and stop them and Detect all EC2 instances with the `Auto-Start` tag and start them.
<img width="1062" height="754" alt="image" src="https://github.com/user-attachments/assets/ab7aebcd-8ee5-427d-8193-02d5dce89f3b" />

### Improved Code with Empty list handaling.
<img width="1142" height="827" alt="image" src="https://github.com/user-attachments/assets/48ac5ca5-4be2-479d-9479-d3dc1b2b20d5" />

## Step 4:Assigning of Role to the Lambda function:
### Search for Lambda and click on it.
<img width="1055" height="675" alt="image" src="https://github.com/user-attachments/assets/a3cc3131-f735-482b-b81c-24384ea7ad0b" />

### Click on create function and create a lambda function as per below.
<img width="1627" height="514" alt="image" src="https://github.com/user-attachments/assets/7bfa5038-4bd3-4d0c-b5d5-e7e8f141946a" />

### Assign Lambda function name and use runtime as python 3.*.
<img width="1843" height="837" alt="image" src="https://github.com/user-attachments/assets/0954de4c-d2b0-474f-b55f-32af69f64716" />

### Assign Created Role for Lambda function by selecting Change default execution role and Select Use an existing role.
<img width="1598" height="783" alt="image" src="https://github.com/user-attachments/assets/42ae24ed-c360-4d19-b43d-cbd8a7ea68de" />

### After assigning created Role to lambda fuction click on create function.
<img width="1600" height="797" alt="image" src="https://github.com/user-attachments/assets/4f88a45f-74ba-4491-b2e7-29fbe6da2e0b" />

## Step 5: Configuration of Lambda function with created python prgoram to test or trigger manually of function:
### Check and click on "_Code_" option and paste python code in Lambda function and deploy your code.
<img width="1537" height="739" alt="image" src="https://github.com/user-attachments/assets/7e9cdabd-c9ce-4d36-a3fc-96ec678ee487" />
<img width="1267" height="796" alt="image" src="https://github.com/user-attachments/assets/67db0a30-cddc-4f7c-a9ab-056f91d34c10" />

## Step 6: Now we are done with configuration. Its time to test the function.
### Find Test option and create new event and assign test event and hit Test button.
<img width="1571" height="834" alt="image" src="https://github.com/user-attachments/assets/0d4dd9ab-857b-45ac-ba9d-c5a22681b2b5" />

## Case 1: 
### After hitting Test button you will be able to see Executing function: succeeded message along with "_log_" link. If Test event suceeded then Verify Logs will show "_InstanceID_" for Auto-start and Auto-Stop Intances along with Message.
### For Verification Open Log and Verify also check Current Status of ec2 Instances, EC2 instance which having "_Key=Action_" and "_Value=Auto-Stop_" will be In stopped stage.
<img width="1513" height="342" alt="image" src="https://github.com/user-attachments/assets/d5976f77-2094-43d4-878c-800c658672b2" />
<img width="1517" height="342" alt="image" src="https://github.com/user-attachments/assets/9d65a49f-71dc-439a-9474-03ac13791560" />

### First open execution logs for Lambda function.
<img width="1925" height="817" alt="image" src="https://github.com/user-attachments/assets/510491ad-a6db-4081-b0a4-b518be121a95" />
<img width="1890" height="714" alt="image" src="https://github.com/user-attachments/assets/d05d4827-2140-4c4c-bacf-c49943b0dda1" />

### As per above test logs we have timeout during Test case execution so Countinue to "_Case 2_".

## Case 2: If you are getting Error during Triggring of test event ot timeout during test event test Suceeded then follow below steps to correct.
### Select option Configuration and click on edit.
### Increese Timeout to 2 Mins and save it.
<img width="1548" height="487" alt="image" src="https://github.com/user-attachments/assets/9034c6bb-0459-44af-bba4-c9bfcdbd7d85" />
<img width="1219" height="778" alt="image" src="https://github.com/user-attachments/assets/215b3bd8-cd25-464f-8667-b97654a0e9c6" />

### Now again try to test , At this time issues should be cleared and will be executed without any issue.
<img width="1583" height="762" alt="image" src="https://github.com/user-attachments/assets/e9bcce16-2b62-405a-b99c-5d47ed4e5d9c" />
<img width="1913" height="784" alt="image" src="https://github.com/user-attachments/assets/09e8fc18-f691-41cb-a56f-3a3b6a979aa6" />

### Now again Verify logs and EC2 Instances.
### First open execution logs for Lambda function. Logs are clean without error.
<img width="1913" height="784" alt="image" src="https://github.com/user-attachments/assets/09e8fc18-f691-41cb-a56f-3a3b6a979aa6" />
<img width="1895" height="648" alt="image" src="https://github.com/user-attachments/assets/ada44dfd-75dc-4b6c-9200-f2fe92bfccc1" />

### Verify EC2 Instances state,EC2 instance which having "_Key=Action_" and "_Value=Auto-Stop_" will be In stopped stage.
<img width="1917" height="293" alt="image" src="https://github.com/user-attachments/assets/f38f1e6a-e50e-4b54-83c3-88b0273990af" />



<h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>









