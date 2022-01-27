from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse('This is home view')


def department_details(request):
    return HttpResponse('This is department 1 view')


def list_departments(request):
    return HttpResponse('This is list view')
