# Task1: Jenkins CI CD pipeline for flask application

## Objective:
#### Set up a Jenkins pipeline that automates the testing and deployment of a simple Python web application

### Step: 1. Setup:
   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.

     <img width="1581" height="671" alt="image" src="https://github.com/user-attachments/assets/d3e02f09-e5fd-4145-9d1f-ebcc6a4bc26f" />

   - Configure Jenkins with Python and any necessary libraries.
     
     <img width="545" height="103" alt="image" src="https://github.com/user-attachments/assets/03b55fed-732c-450a-9ad1-f1f1f0465b83" />
     
### Step:2. Source Code:
  -  Write a python code and push to Github Repo.
  - 
    <img width="796" height="552" alt="image" src="https://github.com/user-attachments/assets/a67682aa-1262-4368-b715-1a1bb082d2cd" />
    <img width="746" height="463" alt="image" src="https://github.com/user-attachments/assets/c5602953-99da-41dd-85c4-86ebcb1d2c2a" />

  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).
    <img width="440" height="432" alt="image" src="https://github.com/user-attachments/assets/98b35ea1-c568-493a-baff-71461bba94ab" />

  - Clone the forked repository into your Jenkins server.
   <img width="1115" height="898" alt="image" src="https://github.com/user-attachments/assets/2408a257-34d9-4b01-8ccd-41402780ed40" />

### Step:3. Jenkins Pipeline:
   - Create a Jenkinsfile in the root of your Python application repository.
     <img width="1862" height="512" alt="image" src="https://github.com/user-attachments/assets/f3d99ec1-bf4c-4383-a788-c99900409ed3" />
   
   - Define a pipeline with the following stages:
   - Build: Install dependencies using pip.
   - Test: Run unit tests using a testing framework like pytest.
   - Deploy: If tests pass, deploy the application to a staging environment.
   <img width="955" height="1010" alt="image" src="https://github.com/user-attachments/assets/bc2196da-b3aa-473d-b1bc-044d704376b2" />
### Step:4. Triggers:
   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.
   <img width="1698" height="722" alt="image" src="https://github.com/user-attachments/assets/afb2eaf8-26a6-4944-ae36-edffc9034428" />

### Step:5. Notifications:
   - Set up a notification system to alert via email when the build process fails or succeeds.
  <img width="1052" height="506" alt="image" src="https://github.com/user-attachments/assets/9526a97e-4bcf-46ef-8786-68bcee5ca409" />

### Step: Verification of pipeline 

   - Pipeline succeed check on jenkins status.
  <img width="1197" height="532" alt="image" src="https://github.com/user-attachments/assets/aad7ddd3-ec87-41ba-8bf2-adc3438e333c" />
  <img width="1718" height="782" alt="image" src="https://github.com/user-attachments/assets/bedaf69c-9f86-485b-9df9-18e2eee8af1c" />
  <img width="1902" height="437" alt="image" src="https://github.com/user-attachments/assets/734a94eb-e500-4256-a2b9-36a1ff33777e" />

  - As per post Action python code must be in <b><i>/var/jenkins/agent/devendra/workspace/ci_cd_flask_app/git_assignment_HeroVired/CI-CD_Pipeline/cicd_logs<b><i>
 <img width="1153" height="426" alt="image" src="https://github.com/user-attachments/assets/9041daa7-281a-4bde-948c-e1f795e7c482" />

<h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>


