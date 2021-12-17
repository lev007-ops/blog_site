from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(verbose_name='Название поста', max_length=110)
    text = models.TextField(verbose_name='Текст поста', max_length=400)
    cre_date = models.DateTimeField(verbose_name='Дата публикиции', default=timezone.now())

    def __str__(self) -> str:
        return self.title

    @admin.display(
        boolean=True,
        ordering='cre_date',
        description='Опубликовано недавно?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.cre_date <= now
