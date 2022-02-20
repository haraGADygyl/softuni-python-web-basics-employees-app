import random

from django import forms
from django.http import HttpResponse, Http404
# Create your views here.
from django.shortcuts import redirect, render
# def home(request):
#     if request.method == 'GET':
#         return HttpResponse(
#             f'<h1>{request.method}: This is home</h1>',
#             status=201,
#             content_type='text/html',
#             headers={
#                 'x-tisho-header': 'Tisho header'
#             }
#         )
#
#     return HttpResponse(f'{request.method}: This is home view')
from django.urls import reverse_lazy

from softuni_python_web_basics_employees_app.employees.models import Department, Employee


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=30
    )

    last_name = forms.CharField(
        max_length=40
    )

    age = forms.IntegerField()


def create_employee(request):
    employee_form = EmployeeForm(request.POST)
    if employee_form.is_valid():
        print('Valid')
    print('Invalid')


def home(request):
    context = {
        'employee_form': EmployeeForm(),
    }
    return render(request, 'index.html', context)


def department_details(request, id):
    print(type(id))
    return HttpResponse(f'This is department {id} view, type: {type(id)} ')


def list_departments(request):
    department = Department(
        name=f'Department {random.randint(1, 1024)}',
    )
    department.save()

    Department.objects.create(
        name=f'Department {random.randint(1, 1024)}',
    )

    context = {
        # 'departments': Department.objects.filter(name__contains='app'),
        'departments': Department.objects
            .prefetch_related('employee_set')
            .all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def not_found(request):
    return Http404()


def go_to_home(request):
    return redirect('index')
    # return redirect(to='/')
    # return HttpResponseRedirect(request)
