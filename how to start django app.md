# How to start Django

- first dont use Vscode's terminal. Always use pc's CMD or mac's terminal although macs vscode have acces to zsh terminal wich is fine.

- Next navegate to the folder where you want create your app, so all the app files including env files will be there.

- open the cmd an type each command one at the time:

```shell
python -m venv [my_venv_name]

[my_venv_name]\Scripts\activate

pip install django

django-admin version
django-admin startproject [project-name]

cd [project-name]

python manage.py runserver
```
- Navigate to you browser localhost: http://127.0.0.1:8000/ or localhost:8000 

- If you want to change the port just specify which port you want to run:

```shell
python manage.py runserver 8080
``` 
- Deactivate:
    - to deactivate the venv type [my_venv_name]\Scripts\deactivate??????
    - $cd ~/python-venv/
    - $./bin/activate


## Creating the APP

```shell
python manage.py startapp [app_name]

cd [app_name]

mkdir templates

cd templates

echo index.html

cd ..
```
- inside templates create an index.html file with whatever you want inside

- navegate to the [project-name] folder and open the settings.py file

- import the os module

- find the code:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- inside 'DIRS' empty object write:  

```python
os.path.join(BASE_DIR, "[app_name]/templates")
```
- create a view inside the file views.py with this code inside:

```python
def home(req):
    return render(req, "index.html")
```

- create a urls.py file inside the [app_name] folder with this inside:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home)
]
```

- navegate to the [project_name] folder and find the urls.py file:
- replace the code inside with:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('[app_name].urls')),
    path('admin/', admin.site.urls),
]
```
- Navigate in the browser to: localhost:8000/home/

## Static files:

- create in [app_name] folder a folder called "static", inside create anothewr called "css" and inside css create a file style.css

- navegate to the settings.py inside [project_name] folder and scroll down until finding:

```python
STATIC_URL = 'static/'
```
- and right under it add this code:

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "[app_name]/static"),
]
```
- add this to your index.html under the DOC tag:

```html
<!DOCTYPE html>
{% load static %}
```

- add a link tag to css:

```html
<link rel="stylesheet" href="{% static '/css/style.css' %}">
```

- refresh the browser and the cache.
    -( ctrl + click on refresh-button )


## ENVIROMENT AND SECURITY:

- in console type:
```shell
pip install python-dotenv
```

- create a new file inside outter [project-name] called ".env"

- from settings.py (inside inner [project-name]) copy the whole line:

´´´python
 SECRET_KEY = 'django-insecure-z7y4h1!@fz*75w4=f(+765khds674v-n*0p)nl=#99v05'
´´´

- copy this line inside ".env" strip the text from quotation marks and make sure of of not leaving spaces in between as example:

```text
SECRET_KEY=django-insecure-z7y4h1!@fz*75w4=f(+765khds674v-n*0p)nl=#99v05
```

- next copy line inside settings.py DEBUG = True in the ".env" file stripping spaces as example:

```text
DEBUG=True
```

- return to settings.py and in the import section include load_dotenv and instanciate the load_dotenv:

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

- change the secret key and debug to read from .env:

```python
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
```


## APPs declarations:

- all apps created with the command ">python manage.py startapp [app_name]" need to be declared in the settings.py for example "account", "chat_server" and "VictorGrinan"

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'chat_server',
    'VictorGrinan'
]
```

## create model 

- after models are created then use the command "python manage.py makemigrations" and "python manage.py migrate"


## create super user (admin)

```shell
python manage.py createsuperuser
```

rest framework : https://www.django-rest-framework.org/#installation