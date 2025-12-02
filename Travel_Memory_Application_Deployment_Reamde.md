# Project : Travel Memory Application Deployment

## GOAL : Deployment of any Site with Full BackEnd ,FrontEnd and Database using MERN(MongoDB, Express.js, React, Node.js)
- Set up the backend running on Node.js.
- Configure the front end designed with React.
- Ensure efficient communication between the front end and back end.
- Deploy the full application on an EC2 instance.
- Facilitate load balancing by creating multiple instances of the application.
- Connect a custom domain through Cloudflare.

## Tasks 1: Backend Configuration:
### Creation of EC2 instance with Ubuntu and default VPC and allow SSH connection using Port 22.
<img width="1896" height="780" alt="image" src="https://github.com/user-attachments/assets/9de198ec-8a94-494a-bc62-54c1425486c7" />
<img width="1242" height="622" alt="image" src="https://github.com/user-attachments/assets/9e81a0c6-45cd-4231-87ae-65964c5c3029" />
<img width="1852" height="577" alt="image" src="https://github.com/user-attachments/assets/7c78ab5b-9bec-419d-99d6-25d246d45a16" />

### Access the Instance and Clone the repository and navigate to the backend directory.
<img width="1148" height="846" alt="image" src="https://github.com/user-attachments/assets/407fe237-7177-41d9-b2cf-1f34e8d9f132" />
<img width="933" height="771" alt="image" src="https://github.com/user-attachments/assets/81a411d6-846e-47b4-a194-7ecb2d59af79" />

###  Install Node.js 22 and npm "curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -"
<img width="1227" height="978" alt="image" src="https://github.com/user-attachments/assets/901d1949-6d7f-4092-a7b1-624a04650d1a" />
<img width="1197" height="692" alt="image" src="https://github.com/user-attachments/assets/3d1e669b-0618-471f-a066-311d95632cc3" />

### The backend runs on port 3001. Set up a reverse proxy using nginx to ensure smooth deployment on EC2.
<img width="908" height="288" alt="image" src="https://github.com/user-attachments/assets/a6981c5d-6009-4a33-ad1e-6b6078996198" />
<img width="872" height="328" alt="image" src="https://github.com/user-attachments/assets/d06d2472-adaf-4a62-8d5e-e533b6e97bfb" />

### Port 3001 removed from AWS security group and reverse proxy is working through nginx.
<img width="1643" height="661" alt="image" src="https://github.com/user-attachments/assets/7194460b-7598-45c3-b45e-a2cccad82d37" />
<img width="1037" height="847" alt="image" src="https://github.com/user-attachments/assets/b2a2a4ed-2c87-4a0d-b00f-65ca2e24328d" />
<img width="827" height="275" alt="image" src="https://github.com/user-attachments/assets/c39da272-28de-483b-bd0a-d6fdc0aa1c3e" />

### Update the .env file to incorporate database connection details and port information.
<img width="1407" height="245" alt="image" src="https://github.com/user-attachments/assets/a63a7ff2-d3c9-4fe6-9f51-b7dbb4f9f16e" />

### Installation of backend packages using npm install and start backend of application at Port 3001. 
<img width="747" height="448" alt="image" src="https://github.com/user-attachments/assets/6475f087-1294-49c5-a384-5350e1bd0818" />
<img width="736" height="62" alt="image" src="https://github.com/user-attachments/assets/e8882d29-80fb-4ffe-b28c-8f0298054b6d" />

## Tasks 2: Frontend Configuration:
### Login to EC2 Instance on another window:
<img width="807" height="587" alt="image" src="https://github.com/user-attachments/assets/9dbf67f7-463b-4d45-9d7d-500c690d3cf1" />

### Navigate to Your Frontend Directory:
<img width="1163" height="523" alt="image" src="https://github.com/user-attachments/assets/f7f18740-201d-44fb-98e4-e27e2e6e909c" />

### Create the .env File using echo "REACT_APP_BACKEND_URL=http://EC2_PUBLIC_IP:3001" > .env
<img width="1163" height="523" alt="image" src="https://github.com/user-attachments/assets/d89ec121-476a-45da-989e-c183daf1fb77" />

### Install Required Packages using npm install
<img width="1258" height="486" alt="image" src="https://github.com/user-attachments/assets/9e726f7b-edbe-45f9-b439-717f9e5dad6a" />

### Start Frontend and test
<img width="845" height="355" alt="image" src="https://github.com/user-attachments/assets/3a4a5858-c848-47a1-bdd2-6dc434611474" />
<img width="1062" height="598" alt="image" src="https://github.com/user-attachments/assets/a2c256f3-061a-438c-8f80-7fa308147385" />
<img width="1407" height="952" alt="image" src="https://github.com/user-attachments/assets/6922d841-7aa5-4015-9a5a-59806a87ae82" />



