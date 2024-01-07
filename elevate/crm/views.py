from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Task
from .forms import TaskForm


# Homepage

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


# CRUD - Create a task

def create_task(request):
    
    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')

    context = {'form' : form}

    return render(request, 'crm/create-task.html', context)

# CRUD - Read task

def tasks(request):

    query_data_all = Task.objects.all()
    #query_data_single = Task.objects.get(id=3)

    context = {"all_tasks" : query_data_all,}
               #"single_task": query_data_single}

    return render(request,'crm/view-task.html', context)

# CRUD - update task

def update_task(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
             
             form.save()

             return redirect('view-tasks')
    
    context = {'update_task' : form}

    return render(request,'crm/update-task.html',context)

# CRUD - Delete tasks

def delete_task(request,pk):
    
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('view-tasks')

    return render(request,'crm/delete-task.html')

# Registration page

def register(request):

    return render(request,'crm/register.html')


