from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug>", views.blog, name="blog"),
]
