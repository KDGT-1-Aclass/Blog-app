from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='タイトル')
    content = models.TextField(verbose_name='本文')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='著者')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    published = models.BooleanField(default=True, verbose_name='公開')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '投稿'
        verbose_name_plural = '投稿'

    def __str__(self):
        return self.title