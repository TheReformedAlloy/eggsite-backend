from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length=15)

class Content(models.Model):

    class Meta():
        abstract = True
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Keyword)
    created_time = models.DateTimeField(auto_now_add=True)
    modfied_time = models.DateTimeField(auto_now=True)
    content = None

class Comment(models.Model):
    parent_post = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    post_id = models.PositiveIntegerField()
    post_object = GenericForeignKey('parent_post', 'post_id')

    parent_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modfied_time = models.DateTimeField(auto_now=True)
