from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=240)
    text = HTMLField()
    rank = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    featured_image = models.ImageField(blank=True)
    slug = models.SlugField(blank=True)
