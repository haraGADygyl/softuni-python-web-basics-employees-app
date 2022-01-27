from django.contrib import admin
from django.urls import path

from softuni_python_web_basics_employees_app.employees.views import home, department_details, list_departments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('departments/1', department_details),
    path('departments/', list_departments)
]
