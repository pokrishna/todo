# todo
Create a TO-DO list app.
Tech Stack to be used : Python, Django, & Bootstrap. (Use latest versions)
Requirements:
1. The app should have following fields:
•	Title
•	Description
•	Date & time of the Todo task.
•	Status (In progress, completed, pending)
•	Created at & Modified at
2. Login & Authentication is not required.
3. App should handle all the CRUD operations. No fancy things required in frontend. Basic form/list view is sufficient.
4. Create Django admin interface for this so that an admin user can login and add the entries. The entry deleted from non-admin interface should be still visible for the Admin. 
5. Admin view should have list display with all the fields from point 1 above. Provide search and filtering with required fields in the admin interface.
6. Admin should be able to download the bulk entries of todo list in csv format from Django Admin Interface.
7. Create an API to list all the to do items as well as individual item without using any API Framework.

Features of todo app:

1.CRUD Operations
2.Admin interface
3.Admin should be able to download the bulk entires of todo list in CSV format from Django Admin Interface

Prerequisites

A Terminal (preferred) or a CMD
Python 3.4 or above installed. (Windows users might need to add it to path.)
Django framework 1.8 or above installed and working.

Installation
1. Open a Terminal, and clone the current repository.

git clone https://github.com/pokrishna/todo.git


2.Enter the root directory.

cd todo_list

3. Now start the setup by entering the following command.

python manage.py runserver

4. project execution link.

http://http://127.0.0.1:8000/

5.Admin interface 

http://127.0.0.1:8000/admin/

username = krishna
password = india@123


6.API testing

create a file name test.py
----------------------------
import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resource(id=None):
    data={'id':id,}
    r=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.json())
    print(r.status_code)


get_resource()   # list all todo items
get_resource(31) # individual items
get_resource(39) # individual items

-------------------------------


Thank you!!!








