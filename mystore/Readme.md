# Book Store


## Setup

- Preq: Python 37.9
- Install libraries in requirements.txt
- Database used: MySQL

## Install requirements

- pip install requirements.txt

# setup datbase
- create datbase on the name 'test' in MySql
Run 
-     python manage.py makimigrations
-     python manage.py migrate
  Create super user with below command
-     python manage.py createsuper
  provide necessary data for the above command

## Admin access

    127.0.0.1:8000/admin
create a new user from users table

# Run App
- python manage.py runserver & visit 127.0.0.1:8000
- Tests: python manage.py test from root folder

## Access Application

- 127.0.0.1:8000 shows list of api's

## JWT token 

- use 127.0.0.1:8000/token/ and provide username password to acquire access_token
- use this access_token for all the operations

