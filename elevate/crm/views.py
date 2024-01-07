from django.shortcuts import render

from django.http import HttpResponse

from .models import Task


def homepage(request):

    client_list = [
        {
            "id" : "1",
            "name" : "Peter",
            "occupation" : "Software developer"
        },
        {
            "id" : "2",
            "name" : "Zuzi",
            "occupation" : "Lawyer"
        }

    ]
    context = {"main_client_list" : client_list}


    return render(request, 'crm/index.html', context)


def task(request):

    query_data_all = Task.objects.all()
    query_data_single = Task.objects.get(id=3)

    context = {"all_tasks" : query_data_all,
               "single_task": query_data_single}

    return render(request,'crm/task.html', context)


def register(request):

    return render(request,'crm/register.html')

