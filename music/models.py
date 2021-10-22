from django.db import models

# Create your models here.
class MusicPost(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    featured_image = models.ImageField(blank=True)
    rank = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    embed = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True)
