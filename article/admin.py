from django.contrib import admin
from .models import Article, Score

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created', 'updated']

