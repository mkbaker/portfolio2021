from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.


def blog_list(request):
    blog_list = Blog.objects.filter(is_visible=True).order_by("-rank", "title")
    return render(request, "blog_list.html", {"blog_list": blog_list})


def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog.html", {"blog": blog})
