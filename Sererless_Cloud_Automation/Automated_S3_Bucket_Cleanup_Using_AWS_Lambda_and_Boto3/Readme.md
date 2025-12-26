<h1>Assignment : Automated S3 Bucket Cleanup Using AWS Lambda and Boto3</h1>
<h2>Objective:</h2><h3>To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.</h3><br>
<h2>Task:</h2> <h3></h3>Automate the deletion of files older than 30 days in a specific S3 bucket.</h3>
<h2>Step 1: Setup S3</h2>
<h3>Navigate to the S3 dashboard and create a new bucket.</h3>
<img width="1447" height="737" alt="image" src="https://github.com/user-attachments/assets/8bcfe48c-2a89-433d-b5ac-df8003a9d899" />
<img width="1822" height="456" alt="image" src="https://github.com/user-attachments/assets/523f2abe-c206-41b2-b56f-3d8b39fa244e" />

<h3>Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).</h3>
<img width="1655" height="707" alt="image" src="https://github.com/user-attachments/assets/1096bd5a-7c42-4e62-9d27-509eb7dd5fe4" />
<img width="1785" height="611" alt="image" src="https://github.com/user-attachments/assets/9be6592f-23f3-4893-86bf-b3e24429866e" />

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
<img width="1586" height="490" alt="image" src="https://github.com/user-attachments/assets/5517855f-0ab2-469b-897e-60f17c7e60db" />

<h3> Complete pthon code for S3 celanup more than 30 days and deploy into lambda function.</h3>
For python code checkout : https://github.com/predatordev1/git_assignment_HeroVired/blob/main/Sererless_Cloud_Automation/Automated_S3_Bucket_Cleanup_Using_AWS_Lambda_and_Boto3/Automated%20_S3_Object_DeletionUsing_AWS_Lambda_and_Boto3.py


<img width="1531" height="716" alt="image" src="https://github.com/user-attachments/assets/3e307996-fa0f-4440-86ab-f93b7dbbc883" />
<img width="1626" height="866" alt="image" src="https://github.com/user-attachments/assets/89a41b71-88fc-4a00-996d-be042dcb5e02" />

<h3>Assign created IAM role and timeout values more than or equl to 2 mins. </h3>
<img width="1515" height="667" alt="image" src="https://github.com/user-attachments/assets/10cfd70c-b3c9-4b36-91bc-9fc7ec173d50" />
<img width="1472" height="786" alt="image" src="https://github.com/user-attachments/assets/720a251d-ab9b-4379-8bf1-72a6943144a9" />

<h2> Now Lambda function is ready for testing. </h2>
<h2> Step 4: Now we will test the code and lambda function.</h2>
<h3>Create a Test event and hit Test button.</h3>
<img width="1617" height="787" alt="image" src="https://github.com/user-attachments/assets/db0f3f0e-cd56-47f7-a765-792ab2557344" />

<h3> Once Test get Success check for details and execution logs. </h3>
<h4>In Execution details will show the return output of code and in Cloudwatch will show print statement output.</h4>
<img width="1540" height="761" alt="image" src="https://github.com/user-attachments/assets/783e2998-f60a-4533-ac81-6b2526c93339" />
<img width="1743" height="718" alt="image" src="https://github.com/user-attachments/assets/a4aba63c-ab1c-43ca-9cf0-a46403c0be95" />

<h3> In above test funtion in keeping all files since Sytem date and S3 bucket time both are same hence all files of S3 bucket are kept in.</h3>
<img width="1468" height="461" alt="image" src="https://github.com/user-attachments/assets/ea83ed62-7048-424c-a3d7-9f69c61ef6db" />
<img width="1566" height="501" alt="image" src="https://github.com/user-attachments/assets/8557aba2-4e84-419c-b9b9-d9b2711006cc" />
<img width="1871" height="587" alt="image" src="https://github.com/user-attachments/assets/91281530-b3e5-423b-9a61-6bce58a65e9c" />


<h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>


