from django.shortcuts import render
from django.conf import settings
from .models import Project, Experience, Education, Skill

def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()  # Fetch experiences
    education = Education.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects': projects, 
        'experiences': experiences, 
        'education': education, 
        'skills': skills,
        'MEDIA_URL': settings.MEDIA_URL,
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

