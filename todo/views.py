from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

from .models import Task

def index(request, *args, **kwargs):
    tasks = Task.objects.all()
    tasks = [
        {
            "name": task.name,
            "is_completed": task.is_completed,
            "date_created": task.date_created,
            "date_updated": task.date_updated,
        } for task in tasks
    ]
    # data = {
    #     "name": "Mr. Joshua",
    #     "age": 14
    # }
    # name = "PG"
    data = ...
    return JsonResponse(data=tasks, safe=False)