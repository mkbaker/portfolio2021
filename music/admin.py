from django.contrib import admin
from .models import MusicPost

# Register your models here.
class MusicPostAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(MusicPost, MusicPostAdmin)
