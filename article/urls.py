from django.urls import path
from .views import ArticleList
 
urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
]