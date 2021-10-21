from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=240)
    url = models.URLField()
    repository_url = models.URLField()
    description = models.TextField()
    rank = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    featured_image = models.ImageField(blank=True)
