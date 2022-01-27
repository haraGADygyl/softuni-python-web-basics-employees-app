from django.urls import path

from softuni_python_web_basics_employees_app.employees.views import department_details, list_departments, \
    not_found

urlpatterns = [
    path('<int:id>/', department_details, name='department_details'),
    path('', list_departments, name='list_departments'),
    path('not-found/', not_found)
]
