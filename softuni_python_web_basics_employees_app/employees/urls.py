from django.urls import path

from softuni_python_web_basics_employees_app.employees.views import create_employee

urlpatterns = [
    path('create/', create_employee, name='create employee')
]
