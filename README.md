
# Transit Tracker
A serverless alexa skill to know the position of public transit in Logan, Utah using flask-ask

## Software Needed
- Python Version 2.7
- Zappa only works for python 2.7

## Installation

### Step 1:
- Download the files or clone the repository.

- If your system has  version of python 3, Use virtualenv to install python 2.7 into the folder which has these files


- In commnad prompt, naviagte to the folder containg the files, and run the following command where the first argument is the installation path for python 2.7 and the second argument is the destination folder. Here the destination folder is itself.

- virtualenv -p C:\newPython27\python.exe   .\

- You can check for python version using the command "python --version" where the result should contain number 2.7


### Step 2: Installing requirements/dependencies
- In windows, navigate to Script folder and run activate.bat

- Then run the following command to install the requirements

- pip install flask flask-ask zappa awscli googlemaps

- once successfully installed, you need to edit the directions.py file

### Step 3: Requesting API keys
- you need the request and obtain the following API keys

 - 1) CVTD api key
     you can request this key here: https://www.cvtdbus.org/MIWorkWithCvtd/developer.php

- 2) google maps APi key
### Step 4: Get the latitude and longitude of your place

- you can use your mobile phone or any other means to get the latitude and longitude of your place.

### Step 5: Editing the directions.py file
- edit the variables CVTD_KEY, DIRECTION_API_KEY, MYlOCATION_LATITUDE, MYlOCATION_LONGITUDE 

### Step 6: Run the flask ask app/skill
- from the command prompt, run the app using the command: "python cvtd.py"

- To check running of the app, open browser and navigate to the URL: http://localhost:5000/

- You will be able to see the message "Welcome to CVTD Tracker" if your app is running properly

### Step 7: Deploying it to AWS lambda using Zappa
- This step is quite interesting and you can learn about some interesting stuff about AWS, once you are able to finish this step
- The following link provides detailed instruction on how to deploy our flask-ask app using zappa into AWS lambda services.
- https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa

 Happy coding 

 Please feel free to contact [me](https://www.linkedin.com/in/santhoshboggarapu/) for any info / help to install the app. 




