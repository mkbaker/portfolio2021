from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=240)
    text = models.TextField()
    rank = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    featured_image = models.ImageField(blank=True)
