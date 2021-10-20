from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.


def home(request):
    return render(request, "home.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects_list.html", {"projects": projects})


def contact(request):
    return render(request, "contact.html")
