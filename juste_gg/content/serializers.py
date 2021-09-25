from rest_framework import serializers

from content.serializers import ContentSerializer

from .models import Keyword, Content, Comment

class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('pk', 'title', 'title_dir', 'tags', 'timestamp')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'headline', 'title', 'subtitle', 'author', 'tags', 'created_time', 'modified_time')
