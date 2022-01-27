import random

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


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list_departments'))
    print(reverse_lazy('department_details', kwargs={
        'id': 1
    }))

    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for i in range(8)]
    }
    return render(request, 'index.html', context, content_type='text/html')


def department_details(request, id):
    print(type(id))
    return HttpResponse(f'This is department {id} view, type: {type(id)} ')


def list_departments(request):
    return HttpResponse('This is list view')


def not_found(request):
    return Http404()


def go_to_home(request):
    return redirect('index')
    # return redirect(to='/')
    # return HttpResponseRedirect(request)
