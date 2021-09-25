from django.db import models
from django.contrib.auth.models import User

from content.models import Keyword, Content

def get_series_path(instance, filename):
    return '{0}/{1}'.format(instance.parent_series.title_dir, filename)

# Create your models here.

class Series(models.Model):
    title = models.CharField(max_length=100)
    title_dir = models.CharField(max_length=20)
    tags = models.ManyToManyField(Keyword)
    created_time = models.DateTimeField(auto_now_add=True)

class Comic(Content):
    parent_series = models.ForeignKey(Series, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_series_path, null=True)
    content = models.CharField(max_length=500)
