pip freeze -->What are the running python libraries 
Following the below command executed one by one in terminal/cmd
python -m venv myenv
myenv\Scripts\activate
myenv\Scripts\activate
pip install django
django-admin --version
django-admin startproject myproject
cd myproject
python manage.py runserver
http://127.0.0.1:8000/

------------Creating Individual apps inside of project--------------
step1: python manage.py startapp home
step2: Open the settings.py file , INSTALLED_APPS under insert the 'home'
INSTALLED_APPS = [
    ...
    'home',
]
step3: Create View file inside home app home/views.py
from django.http import HttpResponse

def home(request):
return HttpResponse("Hello, this is my first Django page 🚀")

step4: Create urls.py inside home app home/urls.py
from django.url import path
from .views import home

urlpatterns = [
    path('',home)
]

step5: Connect to Project urls.py refernce path myproject/urls.py
from django.contrib import admin
from django.urls import path, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),   # 👈 THIS FIXES IT
]

step6 :python manage.py runserver

=========Setup Admin Panel================
step1: python manage.py startapp employees
step2: python manage.py migrate
step3: python manage.py createsuperuser
step4: pip install Pillow
step5: python.exe -m pip install --upgrade pip
                (or)
        python -m pip install --upgrade pip  
step6: python manage.py makemigrations  
                (or)
       python manage.py makemigrations employees
step7: python manage.py migrate  
                          