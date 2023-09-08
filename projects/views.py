from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserCreationForm


@login_required(login_url='login')
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


@login_required(login_url='login')
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',
                  {'project': projectObj})


@login_required(login_url="login")
def createProject(request):

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)


    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if request.user == project.owner:
            if form.is_valid():
                form.save()
                return redirect('projects')

        else:
            messages.error(request, "not valid")



    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.user == project.owner:
        project.delete()
        return redirect('projects')
    else:
        messages.error(request, "not valid")

    context={'object': project}
    return render(request, 'projects/delete_object.html',context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    return render(request, 'projects/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account is created')

            login(request, user)
            return redirect('projects')
        else:
            messages.success(
                request, 'an error has occured during registration'
            )

    context = {'page': page, 'form': form}
    return render(request, 'projects/login_register.html', context)
