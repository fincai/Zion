# Zion


##Requirements

- [Python 2.6+](https://www.python.org/downloads/) 
- [Django 1.5+](https://www.djangoproject.com/download/) 
- [MySQLdb](http://sourceforge.net/projects/mysql-python/) If you use Django with MySQL, you'll also need to install the MySQLdb package
- [PIL](http://www.pythonware.com/products/pil/)
- [widget_tweaks](https://pypi.python.org/pypi/django-widget-tweaks)
- [django_ajax](https://github.com/yceruto/django-ajax)

## Database Migration
1. Create a new database named "zion".
2. Modify the settings.py file, replace the "USER" and "PASSWORD" 
   in DATABASES setting by your own database's user and password.
   
3. Enter the project directory, run the following on the command line (or cmd.exe on Windows):

$ python manage.py migrate

## Test The Project On development Server
1. Enter the project directory, run the following on the command line (or cmd.exe on Windows):

$ python manage.py runserver

2. Open your browser and access 127.0.0.1:8000