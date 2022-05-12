from django.contrib import admin
from .models import Article, Score

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created', 'updated']
    
@admin.register(Score)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article', 'user', 'score','created', 'updated']

