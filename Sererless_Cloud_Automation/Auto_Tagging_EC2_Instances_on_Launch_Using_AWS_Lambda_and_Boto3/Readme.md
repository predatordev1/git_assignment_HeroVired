# Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3
## Objective: <h3>Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.</h3>
## Task: <h3>Automatically tag any newly launched EC2 instance with the current date and a custom tag.</h3>
## Step 1: Creation of EC2 instances without any Tag.
<img width="1900" height="313" alt="image" src="https://github.com/user-attachments/assets/24b5bec8-e372-4429-9caa-ee2e262f3ea1" />
<img width="1891" height="667" alt="image" src="https://github.com/user-attachments/assets/bb463d2e-47b5-4584-9068-30e225058b17" />

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
#### Using Boto3 in the Lambda function. To Detect all EC2 instances with Tag as Start Date and User Named.If both or anyone of them is missing tag for Instance we will tag them user defined tag and start Date.
<img width="1907" height="916" alt="image" src="https://github.com/user-attachments/assets/c10ecabe-9fe7-4196-8be7-239f7e0cd436" />

## Step 4:Assigning of Role to the Lambda function:
### Search for Lambda and click on it.
<img width="1055" height="675" alt="image" src="https://github.com/user-attachments/assets/a3cc3131-f735-482b-b81c-24384ea7ad0b" />

### Click on create function and create a lambda function as per below.
### Assign Lambda function name and use runtime as python 3.*.
### Assign Created Role for Lambda function by selecting Change default execution role and Select Use an existing role.
<img width="1378" height="833" alt="image" src="https://github.com/user-attachments/assets/378d9fd6-b703-4cd0-b494-f6296323a150" />

### After assigning created Role to lambda fuction click on create function.
<img width="1632" height="820" alt="image" src="https://github.com/user-attachments/assets/79b67895-0a2b-4a61-af3d-5a92fea0c193" />

## Step 5: Configuration of Lambda function with created python prgoram to test or trigger manually of function:
### Check and click on "_Code_" option and paste python code in Lambda function and deploy your code.
<img width="1587" height="857" alt="image" src="https://github.com/user-attachments/assets/071978cc-1308-44fc-8106-7b502a2e236a" />
<img width="1592" height="781" alt="image" src="https://github.com/user-attachments/assets/3dfff073-9a13-4027-ba90-22f43323a853" />

## Step 6: Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
### Search for Amazone Eventbridge.
<img width="1730" height="835" alt="image" src="https://github.com/user-attachments/assets/aebf79b3-fdf3-45cb-89e0-e118297abf54" />

### Click on Create event and goto in Configure tab and Enter your event name.
<img width="1883" height="803" alt="image" src="https://github.com/user-attachments/assets/b4f4a39e-7330-4827-9823-8040478f73b7" />
<img width="1882" height="837" alt="image" src="https://github.com/user-attachments/assets/dfce16be-80ed-4dcd-8e6f-225a473aa366" />

### Now Goto in Build tab and Enter your event pattern.
<img width="1870" height="813" alt="image" src="https://github.com/user-attachments/assets/52793f8c-196b-4d2b-90e5-555d379276c7" />

### After giving Event pattern target after click on target drag and drop for Lambda Function.
<img width="1582" height="486" alt="image" src="https://github.com/user-attachments/assets/47e26c03-1e5d-4f75-bab3-5c570c4fdb92" />

### Once you drag and drop Target as Lambda then more options will auto enable to configure lambda function and execution role.
<img width="1875" height="836" alt="image" src="https://github.com/user-attachments/assets/fd6d806a-9cd0-4d34-831a-d1e688cf4874" />
<img width="1882" height="792" alt="image" src="https://github.com/user-attachments/assets/6e09a530-20bf-40db-84fc-fed6e4a97e93" />

### Now we are done with event configuration for particular lambda function and Role, Click on create Button and create Event.
<img width="1893" height="772" alt="image" src="https://github.com/user-attachments/assets/4b0142f7-a4c9-4b46-9f28-25081759615b" />

## Step 7: Now we are done with all configuration and setup its time to Test.
## Case 1: 
### After hitting Test button you will be able to see Executing function: succeeded message along with "_log_" link. If Test event suceeded then Verify Logs will show assigned tags for running Intances along with Message.
### For Verification Open Log and Verify also check Start Date and User_defined name of ec2 Instances, EC2 instance which having "_Key=Date_" and "_Value=Today_Date_" and "_Key=User_tag_" and "_Value=Userdefined_Tag_".
<img width="1877" height="711" alt="image" src="https://github.com/user-attachments/assets/968bfa6f-3537-482c-9e8b-bb2c23e0f9d9" />

### As per above test event with manual testing Lambda function is adding missing tags.

## Case2 : Now will create a new EC2 instance and will monitor logs and tag status.
<img width="1920" height="337" alt="image" src="https://github.com/user-attachments/assets/3bbe6b8d-043f-43c4-8aa1-cc7e03ad0afe" />
<img width="1903" height="837" alt="image" src="https://github.com/user-attachments/assets/e599dd6e-0e4d-4135-9e3c-e557e9c438e2" />

### Assigned lambda function Is auto assigning Tags immediately once you click on create EC2 innstance.
<img width="1900" height="597" alt="image" src="https://github.com/user-attachments/assets/b65a5437-28e1-4cc7-8d6e-baee22507800" />
<img width="1913" height="627" alt="image" src="https://github.com/user-attachments/assets/65b5ce9a-02e5-4fcf-a989-f43c23f8b5c1" />
<img width="1902" height="640" alt="image" src="https://github.com/user-attachments/assets/d4e9ca40-ac0c-4d5a-a3a7-2305dfe99f7b" />

<h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>
