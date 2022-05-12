from django.urls import path
from .views import ArticleList, ScoreCreate
 
urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<int:pk>/score/', ScoreCreate.as_view(), name='article-score')
]