from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from claims import models
from django.db import transaction

def index(request):
    return render(request, 'start.html')

def about(request):
    return render(request, 'about.html')

def project_discover(request):
    return render(request, 'projects/discover.html', {'project_list': models.Project.objects.all()}) #TODO filter by is_visible

#this should be moved elsewhere, probably
class CreateProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'external_uri', 'description', 'game_begin_date', 'game_end_date']

@transaction.atomic        
def save_project_to_db(instance):
    instance.author = models.User.objects.first() # TODO[Dair] Как сохранять здесь правильного пользователя?
    instance.status = models.ProjectStatus.objects.filter(is_default_status=True).first()
    instance.save() #Сохраняем
    root_acl = models.ProjectAcl.create_author_fullcontrol(instance)
    root_acl.save() #grant author fullcontrol rights
    root_object = models.Object()
    root_object.project = instance
    root_object.name = 'Вся игра'
    root_object.author = instance.author
    root_object.save()
    return instance.id
    
def project_create(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            instance = form.save (commit=False) # Не сохраняем пока в базу данных
            return redirect('project_start', project_id = save_project_to_db(instance))
    else:
        form = CreateProjectForm()
    return render(request, 'projects/create.html', {'form': form})

def project_start(request, project_id):
    return render(request, 'projects/start.html', {'project': models.Project.objects.get(id=project_id)}) 
