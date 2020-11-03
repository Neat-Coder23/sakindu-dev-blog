from django.shortcuts import render,redirect
from .models import Projects
from .forms import ProjectForm

# Create your views here.
def projects_list(request):
    projects = Projects.objects.all()
    return render(request,'projects_list.html',{'projects':projects})

def project_detail(request,pk):
    project = Projects.objects.get(pk=pk)
    return render(request,'projects_detail.html',{'project':project})

def new_project(request):
    if request.method == 'POST':
        pjform = ProjectForm(request.POST)
        if pjform.is_valid():
            project = pjform.save(commit=False)
            project.save()
            return redirect('project_detail',pk=project.pk)
    else:
        pjform = ProjectForm()
    return render(request, 'project_new.html',{'form':pjform})

