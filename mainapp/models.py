from django.db import models

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(verbose_name='Название поста', max_length=110)
    text = models.TextField(verbose_name='Текст поста', max_length=400)
    date_created = models.DateTimeField(verbose_name='Дата публикиции', default=timezone.now())

    def __str__(self) -> str:
        return self.title
