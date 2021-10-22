from django.shortcuts import render
from django.http import HttpResponse

from .models import MusicPost

# Create your views here.


def music_list(request):
    music_list = MusicPost.objects.filter(is_visible=True).order_by("-rank", "title")
    return render(request, "music_list.html", {"music_list": music_list})
