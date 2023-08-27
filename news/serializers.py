from rest_framework import serializers
from .models import News, ForUsers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'image', 'created_at', 'content', ]


class ForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForUsers
        fields = ['id', 'name', 'content', 'image']



