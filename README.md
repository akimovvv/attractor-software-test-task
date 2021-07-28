# attractor-software-test-task
I'm a beginner python developer, and I'm just learning to write documentation, don't judge strictly :)
In this repository there is a project written according to the terms of reference of the Attractor Software.

### Test task solution

Basic entities and their fields:<br><br>
>Category<br>
- ID
- name
- Parent ID
>Article<br>
- ID
- Category ID
- User ID
- name
- Description
- image
>User<br>
- ID
- User name
- password

No part of the application can be viewed by an unauthorized user.
>Each entity (including users) needs to be able to:<br>
- Add
- View the list
- Edit
- Delete
  
  ---

<b>All steps to run project.</b>

- First step:
  - Please clone project<br>
  
    ```
    $ git clone https://github.com/akimovvv/attractor-software-test-task.git
    ```
    
- Second step:
  - Please install requirements.txt<br>
    for Linux:
    
      ```
      $ pip3 install -r requirements.txt
      ```
    for Windows:
    
      ```
      $ pip install -r requirements.txt
      ```
      
- Third step:
  - Please create new <b>.env</b> file<br>
    And write variables that are below:
    
    ```
    Django_Secret_Key=Your Django Project Secret Key
    PG_HOST = Your Database (PostgreSQL) Host
    PG_USER = Your Database (PostgreSQL) User
    PG_DATABASE_NAME = Your Database (PostgreSQL) Data Base Name
    PG_PASSWORD = Your Database (PostgreSQL) Password
    ```
  - Please create directory <b>media</b> in the main folder of the project (attractor-software-test-task).<br>This is very important for downloading media files.
  
    ```
    $ mkdir media
    ```
  
- Fourth step:
  - Create <b>Super User</b>
    ```
    $ py manage.py createsuperuser
    ```
    then fill out these fields.
- Fifth step:
  - Now we should to do migrations to create <b>DB Tables</b>
    - First <b>makemigrations</b>
    
      ```
      $ py manage.py makemigrations
      ```
    - Second <b>migrate</b>
    
      ```
      $ py manage.py migrate
      ```
- Sixth step:
  - Congratulation
  
    ```
    $ py manage.py runserver 8000
    ```
    You <b>run server</b>
    
---

You can login in django admin-panel (**http://127.0.0.1:8000/admin/**) and create new datas etc. 

---

<b>API</b>

- User (Registration, Authentication etc.)
  - User info **http://127.0.0.1:8000/auth/users/me/**
  - Registration **http://127.0.0.1:8000/auth/users/**
  - Login **http://127.0.0.1:8000/auth/token/login/**
  - Logout **http://127.0.0.1:8000/auth/token/logout/**
  - Edit user username **http://127.0.0.1:8000/auth/users/reset_username/**
  - Edit user password **http://127.0.0.1:8000/auth/users/set_password/**

- Category (Create, Update etc.)
  - All category:  **http://127.0.0.1:8000/api/get-all-category/**
  - Create category:  **http://127.0.0.1:8000/api/create-category/**
  - Update category:  **http://127.0.0.1:8000/api/update-category/category-primery-key/**
  - Delete (destroy):  **http://127.0.0.1:8000/api/delete-category/category-primery-key/**

- Article (Create, Update etc.)
  - All article:  **http://127.0.0.1:8000/api/get-all-article/**
  - Create article:  **http://127.0.0.1:8000/api/create-article/**
  - Update article:  **http://127.0.0.1:8000/api/update-article/article-primery-key/**
  - Delete (article):  **http://127.0.0.1:8000/api/delete-article/article-primery-key/**
