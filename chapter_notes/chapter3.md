# CHAPTER 3: Django Basics
## 3.1: Testing Your Setup
- Check that you have the right versions of Python and Django in the virtual environment
- Check that django can be imported by quickly testing it in the Python interpreter
'
python 
>>>
>>> import django
>>> django.get_version()
\'3.7.7\'
>>> exit()
'
## 3.2: Creating Your Django Project
- To create a new Django project, go to the workspace directory and enter:
    'django-admin.py startproject tango_with_djang_project'
- Running this command creates a new project directory with two items:
    1. a nested directory with the same name as the main project
    2. A python script manage.py
- The subdirectory (for the sake of this tutorial) the *project configuration directory*
    - This directory has four scripts:
        1. '__init__.py': an empty script that indicates to Python that the directory is a Python package
        2. 'settings.py': stores all of the project's settings
        3. 'urls.py': stores all URL patterns for the project
        4. 'wsgi.py': helps run a development server and deploy the project to a production envrionment
- 'manage.py' is a script that provides a series of commands to help maintain the project
    - The script can allow you to run a built-in development server, test the application, and run database commands
    - We'll use this script for virtually every Django command we want to run
    - Running 'python manage.py runserver' will result in the development server being hosted at the outputted local server
    - 
