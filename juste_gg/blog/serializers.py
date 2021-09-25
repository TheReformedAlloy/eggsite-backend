from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog 
        fields = ('pk', 'headline', 'title', 'subtitle', 'author', 'tags', 'created_time', 'modified_time', 'content')