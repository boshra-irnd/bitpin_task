from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # article_score
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

class Score(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_score')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_score')
    SCORE_CHOICES = [(num,num) for num in range(1,6)]
    score = models.IntegerField(choices=SCORE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ['created']
