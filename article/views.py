from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Score
from .serializers import ArticleSerializer, ScoreSerializer
 
 
class ArticleList(ListAPIView):
    queryset = Article.objects \
        .prefetch_related('article_score') \
        .all() 
    serializer_class = ArticleSerializer
    

class ScoreCreate(CreateAPIView):
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        article = Article.objects.get(pk=self.kwargs['pk'])
        return Score.objects.filter(user=user, article=article) 
    
    def create(self, request, *args, **kwargs):
        try:
            user = self.request.user
            article = Article.objects.get(pk=self.kwargs['pk'])
            instance = Score.objects.filter(user=user, article=article)
            data = request.data
            if instance.exists():
                new_score = Score.objects.get(user=user, article=article)
                new_score.user_id = self.request.user.id
                new_score.article = Article.objects.get(pk=self.kwargs['pk'])
                new_score.score = data['score']
            else:
                new_score = Score.objects.create(user_id=self.request.user.id,
                                                 article=Article.objects.get(pk=self.kwargs['pk']),
                                                 score=request.data['score'])
            new_score.save()
            serializer = ScoreSerializer(new_score)
            return Response(serializer.data)
        except:
            return Response({'Error':'This article does not exist'},status=status.HTTP_404_NOT_FOUND)