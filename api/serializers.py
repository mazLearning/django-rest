from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['author', 'title', 'slug', 'description', 'image', 'publish', 'status']
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
