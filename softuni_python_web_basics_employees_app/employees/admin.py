from django.contrib import admin

# Register your models here.
from softuni_python_web_basics_employees_app.employees.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title', 'company')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
