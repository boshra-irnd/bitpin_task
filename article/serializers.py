
from rest_framework import serializers
from .models import Article, Score


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['user', 'title', 'body', 'created', 'updated']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = [ 'article', 'user', 'score', 'created', 'updated']
