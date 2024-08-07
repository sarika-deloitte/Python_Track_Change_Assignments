from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import CustomUser, Project, Sprint
from .forms import CustomUserForm, ProjectForm, SprintForm
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

# User views
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'object': user})

# Project views
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()  # Save the form instance
            # Handle many-to-many relationships manually
            users = form.cleaned_data.get('users')
            project.users.set(users)  # Update the many-to-many relationship
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()  # Save the form instance
            # Handle many-to-many relationships manually
            users = form.cleaned_data.get('users')
            project.users.set(users)  # Update the many-to-many relationship
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_update.html', {'form': form})
 

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'object': project})

# Sprint views
def sprint_list(request):
    sprints = Sprint.objects.all()
    return render(request, 'sprint_list.html', {'sprints': sprints})

def sprint_create(request):
    if request.method == 'POST':
        form = SprintForm(request.POST)
        
        if form.is_valid():
            sprint = form.save()  # Save the form instance
            # Handle many-to-many relationships manually
            users = form.cleaned_data.get('users')
            sprint.users.set(users)  # Update the many-to-many relationship
            return redirect('sprint_list')
    else:
        form = SprintForm()
    return render(request, 'sprint_form.html', {'form': form})

def sprint_update(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    if request.method == 'POST':
        form = SprintForm(request.POST, instance=sprint)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')  # Redirect after saving
    else:
        form = SprintForm(instance=sprint)
    
    return render(request, 'sprint_update.html', {'form': form})

def sprint_delete(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    if request.method == 'POST':
        sprint.delete()
        return redirect('sprint_list')
    return render(request, 'sprint_confirm_delete.html', {'object': sprint})


# views.py

def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'user_detail.html', {'user': user})
def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    return render(request, 'sprint_detail.html', {'sprint': sprint})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})
