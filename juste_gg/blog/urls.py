from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^api/blogs/$', views.blogs_list),
    re_path(r'^api/blogs/([0-9])$', views.blogs_detail),
]