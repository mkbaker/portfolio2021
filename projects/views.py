from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.


def home(request):
    return render(request, "home.html")


def projects(request):
    projects = Project.objects.filter(is_visible=True).order_by("-rank", "title")
    return render(request, "projects_list.html", {"projects": projects})


def project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "project.html", {"project": project})


def contact(request):
    return render(request, "contact.html")
