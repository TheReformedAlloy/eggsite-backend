from django.db import models

from content.models import Content

# Create your models here.

class Blog(Content):
    headline = models.CharField(max_length=100)
    content = models.FileField(null=True)