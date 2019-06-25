# INSTAGRAM CLONE

#### By **Canssidle** 

## Description

Instagram clone is an application that is similary to Instagram app.A usure can register and log in to the application and create an account where he or she can post photos and follow friends and see their photos.The user acn like and coment on the photos on their timeline.
## Behaviour Driven Development

| Behavior our program should handle | Input description |  Output description
| --- | --- | --- |
| `Register/Sign up` | Fill in the required details | The user will recieve an activation email
| `Login` |Enter the reqired details |  The user will be redirected to the homepage
| `Profile` | The user can edit their profile by clicking on the edit.This is where the user can upload their profile photo | Shows the profile with the changes
| `Comment/Like`| The user can click on the like or the comment section to like the photo or comment| The comment will be appended on the comment section of the photo 





### prerequisites
First clone the project to your camputer. 
* git clone https://github.com/canssidle/Instagram-clone.git
Ensure python3 is installed.
Install virtual environment by running 
* pip3 install virtualenv
Create a virtualenvironment by running  
* virtualenv <name of environment>on the terminal and once its activated by running  *source <name of environment>/bin/activate then install all the packages by running 
* pip3 install -r requirements.txt

Create .env file and paste the following.
* SECRET_KEY = '<Secret_key>'
* DBNAME = 'name-of-app-database'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True

* EMAIL_USE_TLS = True
* EMAIL_HOST = 'smtp.gmail.com'
* EMAIL_PORT = 587
* EMAIL_HOST_USER = '<your-email>'
Then start the server by running 
* python3 manage.py runserver.
Copy the link and paste in any browser 
* http://localhost:8000





## Technology and Tools Used

 Python3.6 - Programming language
 Django - Django framework
 Git - Version control
 Visual Studio - Code editor
 Postgresql
 Heroku
 Bootstrap4

 

## Further help
+ To get Further help you can read the Django Documentation.

## Licence
MIT (c) 2019 canssidle (https://github.com/canssidle)