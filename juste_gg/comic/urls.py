from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^api/comics/$', views.comics_list),
    re_path(r'^api/comics/([0-9])$', views.comics_detail),
]