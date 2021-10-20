from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def music_list(request):
    return render(request, "music_list.html")
