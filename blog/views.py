from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog_list(request):
    return render(request, "blog_list.html")
