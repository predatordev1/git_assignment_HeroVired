# Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
# _Note_:
### Since January 2023, AWS automatically applies SSE-S3 encryption to all S3 buckets as the default behavior. Even when you delete the encryption configuration, AWS may re-apply it automatically. So we can't create/delete encryption for buckets  so we will Monitor are diffrent types of encryptions for buckets.

## Objective: 
### To enhance your AWS security posture by setting up a Lambda function to check server-side enabled encryption type for S3 Buckets.

## Task: 
### Automate the detection of S3 buckets to check server-side enabled encryption type.

<h2>Step 1: Setup S3</h2>
<h3>Navigate to the S3 dashboard and create a new buckets with different - different encryption type.</h3>
<img width="1447" height="737" alt="image" src="https://github.com/user-attachments/assets/8bcfe48c-2a89-433d-b5ac-df8003a9d899" />
<img width="1822" height="456" alt="image" src="https://github.com/user-attachments/assets/523f2abe-c206-41b2-b56f-3d8b39fa244e" />
<img width="1748" height="483" alt="image" src="https://github.com/user-attachments/assets/99bec797-79f2-4dd8-8834-9c57ca671c17" />

<h2>Step 2: Setup IAM Role for S3 buckect with full Access</h2>
<h3> Sesrch for IAM and create a New IAM role.</h3>
<img width="1030" height="187" alt="image" src="https://github.com/user-attachments/assets/919d34b6-4a7f-438b-b7e9-ecd5bf81f13c" />
<img width="1928" height="536" alt="image" src="https://github.com/user-attachments/assets/435c6f09-1d46-4f84-a446-a4a20b4663cb" />
<img width="1891" height="795" alt="image" src="https://github.com/user-attachments/assets/f1f43d5c-2e5a-4c7a-9619-b8c4ea0f3ce0" />
<img width="1612" height="608" alt="image" src="https://github.com/user-attachments/assets/7cd83503-f252-4e97-b910-3950eebf8ecd" />
<img width="1363" height="281" alt="image" src="https://github.com/user-attachments/assets/82ec5da6-c6ae-466c-b581-22fd95225328" />

<h2>Step 3: Setup Lambda function using Python3.* and assign IAM Role.</h2>
<h3> Sesrch for Lambda and create a New Lambda function.</h3>
<img width="1032" height="172" alt="image" src="https://github.com/user-attachments/assets/7d215f49-cfa4-475a-aef9-00de9277b120" />
<img width="1618" height="467" alt="image" src="https://github.com/user-attachments/assets/9c881900-a207-403c-aa28-b7743a54cb02" />
<img width="1393" height="830" alt="image" src="https://github.com/user-attachments/assets/cad9c451-9cb3-48ce-b89c-5f32a4b90994" />

<h3> Complete pthon code for S3 celanup more than 30 days and deploy into lambda function.</h3>
For python code checkout : https://github.com/predatordev1/git_assignment_HeroVired/blob/main/Sererless_Cloud_Automation/Monitor_encrypted_S3_Buckets/Monitor_Unencrypted_S3_Buckets_Using_AWS_Lambda_and_Boto3.py

<img width="1827" height="936" alt="image" src="https://github.com/user-attachments/assets/603f0b49-c09b-4f73-af11-71db0cb989d8" />
<img width="1806" height="801" alt="image" src="https://github.com/user-attachments/assets/192af57b-1b17-417e-9523-8de093b0ce7c" />

<h3>Assign created IAM role and timeout values more than or equl to 2 mins. </h3>
<img width="1515" height="667" alt="image" src="https://github.com/user-attachments/assets/10cfd70c-b3c9-4b36-91bc-9fc7ec173d50" />
<img width="1538" height="787" alt="image" src="https://github.com/user-attachments/assets/bc9592ef-d790-4dfc-ae01-76c3c2a51b4e" />

<h2> Now Lambda function is ready for testing. </h2>
<h2> Step 4: Now we will test the code and lambda function.</h2>
<h3>Create a Test event and hit Test button.</h3>
<img width="1567" height="782" alt="image" src="https://github.com/user-attachments/assets/43730761-061f-4b59-9110-983ba8145748" />

<h3> Once Test get Success check for details and execution logs. </h3>
<h4>In Execution details will show the return output of code and in Cloudwatch will show print statement output.</h4>
<img width="1562" height="792" alt="image" src="https://github.com/user-attachments/assets/001a3549-50fd-4daa-8537-e58c6bcea02a" />
<img width="1857" height="671" alt="image" src="https://github.com/user-attachments/assets/263ac539-2bf6-43a9-a055-fd3a3197daf6" />

<h3> In above test funtion we created 6(_Six_) S3 buckets with different - different encryption types.</h3>
<h3>3 Buckets with SEE-S3 ,2 with SSE-KMS and 1 with DSEE-KMS encryption and same is showing in Lambda function output.</h3>
<img width="1282" height="602" alt="image" src="https://github.com/user-attachments/assets/68c206e8-6fe2-4126-b6f7-cf8c5471ed15" />
<img width="1567" height="703" alt="image" src="https://github.com/user-attachments/assets/b5b9f985-202a-4b4b-a05a-ac77a84a5c73" />
<img width="1506" height="352" alt="image" src="https://github.com/user-attachments/assets/11488e75-fce0-48b1-ad09-ad5a74fcbd4f" />

<h1>                                        THE END                                                                </h1>


<h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>

