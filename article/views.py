from rest_framework.generics import ListAPIView
from .models import Article, Score
from .serializers import ArticleSerializer, ScoreSerializer
 
 
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer