Microsoft Windows [Version 10.0.22631.3155]
(c) Microsoft Corporation. All rights reserved.

M:\DjangoProjects01>python -m venv my_venv

M:\DjangoProjects01>my_venv\Scripts\activate

(my_venv) M:\DjangoProjects01>pip install django
Collecting django
  Using cached Django-5.0.3-py3-none-any.whl (8.2 MB)
Collecting asgiref<4,>=3.7.0
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata
  Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Collecting typing-extensions>=4
  Downloading typing_extensions-4.10.0-py3-none-any.whl (33 kB)
Installing collected packages: tzdata, typing-extensions, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-5.0.3 sqlparse-0.4.4 typing-extensions-4.10.0 tzdata-2024.1

[notice] A new release of pip is available: 23.0.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip

 

(my_venv) M:\DjangoProjects01>django-admin version
5.0.3

(my_venv) M:\DjangoProjects01>django-admin startproject firstproject

 
(my_venv) M:\DjangoProjects01>cd firstproject

(my_venv) M:\DjangoProjects01\firstproject>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 09, 2024 - 12:14:01
Django version 5.0.3, using settings 'firstproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[09/Mar/2024 12:14:28] "GET / HTTP/1.1" 200 10629
Not Found: /favicon.ico
[09/Mar/2024 12:14:29] "GET /favicon.ico HTTP/1.1" 404 2116


------------------------------------------------------------------------------------------------------









```
function test() {
  console.log("This code will have a copy button to the right of it");
}
```












































