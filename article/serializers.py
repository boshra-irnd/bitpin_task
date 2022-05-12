from rest_framework import serializers
from django.db.models import Avg
from .models import Article, Score


class ArticleSerializer(serializers.ModelSerializer):
    users_scored = serializers.SerializerMethodField(read_only=True)
    average_scores = serializers.SerializerMethodField(read_only=True)
    your_score = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'created', 'updated', 'users_scored', 'average_scores', 'your_score']
    
    def get_users_scored(self, article):
        user_count = article.article_score.all().count()
        return user_count
    
    def get_average_scores(self, article):
        average = article.article_score.all().aggregate(Avg('score')).get('score__avg')
        if average is None:
            return 0
        return average
    
    def get_your_score(self,article:Article()):
        user_id = self.context['request'].user.id
        article_id = article.id
        scored = Score.objects.filter(user_id=user_id,article_id=article_id).count()
        if scored == 1:
            return article.article_score.values('score').filter(user_id=user_id)
        return None
    

    
class ScoreSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    article_id = serializers.ReadOnlyField(source='article.id')

    
    class Meta:
        model = Score
        fields = [ 'article_id', 'user_id', 'score', 'created', 'updated']
        
