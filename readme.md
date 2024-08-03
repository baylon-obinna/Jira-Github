########

AUTOMATING JIRA TICKET CREATION FOR GITHUB ISSUES USING JIRA API

########

STEPS TO IMPLEMENT

- JIRA ACCOUNT(IF NOT CREATED ALREADY)


- CREATE API TOKEN FROM ACCOUNT SETTINGS/PROFILE/SECURITY

![alt text](<Screenshot (173).png>)


- CLONE REPOSITORY OR USE ANY OTHER IDE FOR THE CODE LOGIC


- .ENV CONFIGURATION WITH NECESSARY KEY VARIABLES

- SERVER TO HOST API (FOR THIS I USED EC2 UBUNTU/24.04 ENVIRONMENT)

- INSTALL PACKAGES ( PYTHON3,FLASK, DOTENV)
  - {sudo apt install python3}
  - {sudo apt install python3-flask}
  - {sudo apt install python3-dotenv}


- RUN PYTHON PROGRAM 
  -{ python Auto_ticket_Jira.py } 


- GITHUB REPOSITORY WITH ISSUES TO BE HANDLED


- CREATE A WEBHOOK FOR THE REPOSITORY SPECIFYING THE PAYLOAD URL, FOR EXAMPLE (http://ec2-54-224-8-156.compute-1.amazonaws.com:5000/createJira)

![alt text](<Screenshot (168).png>)


- FOR THIS USE CASE SELECT (issue command) AS THE INDIVIDUAL EVENT AND SAVE WEBHOOK


- MAKE A COMMENT ON THE REPOSITORY ISSUES (validate the ping delivery works)

![alt text](<Screenshot (176).png>)

- ENSURE THE LOGIC WORKS (make /Jira comment and /* comments)

![alt text](<Screenshot (175).png>)