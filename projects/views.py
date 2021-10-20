from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html")


def projects(request):
    return render(request, "projects_list.html")


def contact(request):
    return render(request, "contact.html")
