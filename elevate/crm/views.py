from django.shortcuts import render

from django.http import HttpResponse

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


def register(request):

    return render(request,'crm/register.html')

