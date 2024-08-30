from django.db import models
from django.conf import settings


class ArticleStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Article(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.ForeignKey(ArticleStatus, on_delete=models.PROTECT)
    published_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleStatistics(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='statistics')
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Statistics for {self.article.title}"
