from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task

# Create your views here.

def tasks(request):
    Tasks = Task.objects.all().values()
    template = loader.get_template('taskpage.html')
    context = {
        'tasks': Tasks,
    }
    return HttpResponse(template.render(context, request))