# SDLC Assignment on Testing, Linux and Servers

### Task 1: System Monitoring Setup

1. Install htop on machine.
<img width="873" height="140" alt="image" src="https://github.com/user-attachments/assets/eca3ec2b-da8a-40f0-aff8-9a672c535028" />

2. Create a script to automate monitoring of performance of syatem using htop.
<img width="809" height="548" alt="image" src="https://github.com/user-attachments/assets/98d6273b-1809-49e4-bf50-ce82090bb650" />

3. System Monitoring script loaded into Github "https://github.com/predatordev1/my-hero-git/tree/main/Assignment_SDLC_testing_Linux-server"
<img width="1880" height="560" alt="image" src="https://github.com/user-attachments/assets/74d69fa1-b09a-459f-82e9-235a754a5447" />

4. Testing of script.
<img width="1468" height="840" alt="image" src="https://github.com/user-attachments/assets/24f1de0b-6f7d-4b2a-b0d5-bb9cc8125b6c" />
<img width="960" height="518" alt="image" src="https://github.com/user-attachments/assets/5931d263-92b0-45c5-9c51-27c74e769585" />

5. Scheduling System Monitoring for every hour in cronetab.
<img width="604" height="283" alt="image" src="https://github.com/user-attachments/assets/1451ed41-2788-488b-b34b-2fae246e3672" />


### Task 2 : User Management and Access Control

1. We are creating two new users named Sarah and Mike with their own workspace.
<img width="1020" height="607" alt="image" src="https://github.com/user-attachments/assets/dc01e12b-28c5-4699-8422-950efd1c9a29" />

2. Assigning password for both Accounts.
<img width="737" height="361" alt="image" src="https://github.com/user-attachments/assets/63d40dbb-dbb0-43b6-977d-493705e55bf2" />

3. Adding permission for both user with their specific workspace.
<img width="542" height="478" alt="image" src="https://github.com/user-attachments/assets/d9f6417a-b5d2-46d4-a372-e9b38a2d2c55" />
<img width="505" height="142" alt="image" src="https://github.com/user-attachments/assets/45f7b300-cc3d-4f62-bc78-4750dee38404" />

4. To Check Access for dedicated directries with other users.
<img width="464" height="124" alt="image" src="https://github.com/user-attachments/assets/731f0fef-9832-41cd-8d97-68b21098a4f6" />
<img width="457" height="222" alt="image" src="https://github.com/user-attachments/assets/5420b122-88bb-4b8e-b364-377bb5bcb290" />

5. To set Password expiry and warnings using change commond for Exiting Mike and Sarah users.
<img width="812" height="272" alt="image" src="https://github.com/user-attachments/assets/4287bdef-bbcd-4d44-8de3-b285b5e54a56" />
<img width="733" height="342" alt="image" src="https://github.com/user-attachments/assets/375c0d65-100d-4bf7-8013-a93b3e5ff730" />

6. Password complexity added using nano /etc/pam.d/system-auth.
<img width="1906" height="471" alt="image" src="https://github.com/user-attachments/assets/b56e1b3e-19bf-4be7-ae50-5f52d99b7165" />

### Task 3 : Backup Configuration for Web Servers

1. Createing a backup script for Sarah's Apache Server backup as named Sarah_apache_backup.sh and storing backup in /backups
<img width="1065" height="190" alt="image" src="https://github.com/user-attachments/assets/07377ad1-c45c-484a-aff1-0be4d4723396" />
<img width="989" height="505" alt="image" src="https://github.com/user-attachments/assets/3f141c7f-ff70-451c-85f6-aa8f5e07184d" />

2. Creating a backup script for Mike's Nginx Server backup as named Mike_nginx_backup.sh and storing backup in /backups
<img width="969" height="486" alt="image" src="https://github.com/user-attachments/assets/b90ce48c-3d82-4580-94ea-0f6742c93a5e" />

3. Backup uploaded into Github repo "https://github.com/predatordev1/my-hero-git/tree/main/Assignment_SDLC_testing_Linux-server"
<img width="597" height="65" alt="image" src="https://github.com/user-attachments/assets/8a88ec29-6692-4e75-a082-4eccee6e55b7" />
<img width="1888" height="494" alt="image" src="https://github.com/user-attachments/assets/2b4303ba-2f84-4563-b52f-490bf11379ab" />

4. Scheduling Backup in cronetab for every Tuesday 12:00 AM.
<img width="529" height="218" alt="image" src="https://github.com/user-attachments/assets/eaee10cb-d50f-4b6f-8172-9f8f3eb20f24" />

5. Testing of backup scripts
<img width="853" height="114" alt="image" src="https://github.com/user-attachments/assets/cd2d73d1-cb4c-4044-a811-e86c80341d63" />





