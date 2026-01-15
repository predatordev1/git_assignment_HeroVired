# Task: GitHub Actions CI/CD Pipeline Flask App

## Objective:
Implement a CI/CD workflow using GitHub Actions for a Python application.

### Step 1: Setup:
- Ensure the repository has a main branch and a staging branch.
  
  <img width="471" height="781" alt="image" src="https://github.com/user-attachments/assets/8f4f988a-8492-4910-9dd3-0d659de17407" />
- Use a provided Python application repository on GitHub

  https://github.com/predatordev1/git_assignment_HeroVired/blob/main/CI-CD_Pipeline/Github_Actions/ci_cd_app.py

### Step 2: GitHub Actions Workflow
 - Create a .github/workflows directory in your repository.
 - Inside the directory, create a YAML file to define the workflow.
 <img width="1187" height="790" alt="image" src="https://github.com/user-attachments/assets/51c7e5d9-b689-4a3f-b9a4-c3d8e9a9924f" />

### Step 3: Define a workflow that performs the following jobs:
  https://github.com/predatordev1/git_assignment_HeroVired/blob/main/CI-CD_Pipeline/Github_Actions/github-actions.yml
  - Install Dependencies: Install all necessary dependencies for the Python application using pip.
  - Run Tests: Execute the test suite using a framework like pytest.
  - Build: If tests pass, prepare the application for deployment.
  - Deploy to Staging: Deploy the application to a staging environment when changes are pushed to the staging
  
  <img width="1633" height="397" alt="image" src="https://github.com/user-attachments/assets/dfc07299-29f3-484e-9d23-435bcf2aebfd" />
  <img width="1202" height="891" alt="image" src="https://github.com/user-attachments/assets/1f775857-2614-4b3e-ab6b-c26d6d8e4cea" />

### Step 4: Testing 
- Once code pushed to main branch CICD will auto start.

 <img width="1871" height="832" alt="image" src="https://github.com/user-attachments/assets/d5524811-1c24-41c6-9771-572a281c03c5" />
 <img width="1715" height="902" alt="image" src="https://github.com/user-attachments/assets/ae4f9d17-fc8e-44ad-83e2-b4cf88ba9695" />
 <img width="1605" height="566" alt="image" src="https://github.com/user-attachments/assets/b3aa9f33-bad4-4932-924e-aa8803ac85c4" />
 <img width="1202" height="620" alt="image" src="https://github.com/user-attachments/assets/a47f273d-8d58-426d-ad71-27b7ed29218a" />
 <img width="1176" height="722" alt="image" src="https://github.com/user-attachments/assets/2da8daa6-4488-4e20-81a6-2ea9f49e5d04" />

 <h4> 🙏 Thank You & Feedback <br>
Thank you for checking out this project.<br>
I appreciate your time and interest.<br>
This project is actively improving, and I welcome feedback, suggestions, and contributions. If you have ideas to enhance it or notice any issues, please feel free to open an issue or submit a pull request.<br>
Your feedback is valuable and helps make this project better.<br>
Thank you for your support! </h4>


