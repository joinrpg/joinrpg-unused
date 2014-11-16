from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'start.html')

def about(request):
    return render(request, 'about.html')

def project_discover(request):
    return render(request, 'projects/discover.html')

def project_start(request, project_id):
    return render(request, 'projects/start.html', {'project': {'name':'Ведьмак:Большая Игра'}})
