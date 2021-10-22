from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Project, ProjectAdmin)
