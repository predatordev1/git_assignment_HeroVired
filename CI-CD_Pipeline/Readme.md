# Task1: Jenkins CI CD pipeline for flask application

## Objective:
#### Set up a Jenkins pipeline that automates the testing and deployment of a simple Python web application

### Step: 1. Setup:
   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.
   - Configure Jenkins with Python and any necessary libraries.

### Step:2. Source Code:
  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).
  - Clone the forked repository into your Jenkins server.

### Step:3. Jenkins Pipeline:
   - Create a Jenkinsfile in the root of your Python application repository.
   - Define a pipeline with the following stages:
   - Build: Install dependencies using pip.
   - Test: Run unit tests using a testing framework like pytest.
   - Deploy: If tests pass, deploy the application to a staging environment.

### Step:4. Triggers:
   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.

### Step:5. Notifications:
   - Set up a notification system to alert via email when the build process fails or succeeds.
