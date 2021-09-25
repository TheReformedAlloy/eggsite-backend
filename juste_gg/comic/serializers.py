from rest_framework import serializers

from .models import Series, Comic

class SeriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Series
        fields = ('pk', 'title', 'title_dir', 'tags', 'created_time')

class ComicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comic
        fields = ('pk', 'parent_series', 'image', 'title', 'subtitle', 'author', 'tags', 'created_time', 'modified_time', 'content')
