# Generated by Django 4.0 on 2021-12-17 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110, verbose_name='Название поста')),
                ('text', models.TextField(max_length=400, verbose_name='Текст поста')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 12, 17, 8, 41, 57, 224363, tzinfo=utc), verbose_name='Дата публикиции')),
            ],
        ),
    ]