from django.db import models

# Create your models here.

# static questions containing only text and images


class Stage_1(models.Model):
    title = models.CharField(blank=True, max_length=200)
    level = models.IntegerField(unique=True)
    description = models.TextField(blank=True, default='hello')
    image = models.ImageField(blank=True, upload_to='StaticQuestions/images')
    image_url = models.URLField(blank=True)
    hint = models.TextField(blank=True, default='hint')
    answer = models.CharField(blank=True, max_length=400)

    def __int__(self):
        return self.level


class Stage_2(models.Model):
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True, default='hello')
    background = models.FileField(blank=True, upload_to='AudioQuestions/music')
    image = models.ImageField(blank=True, upload_to='StaticQuestions/images')
    image_url = models.URLField(blank=True)
    files = models.FileField(blank=True, upload_to='AudioQuestions/music')
    hint = models.TextField(blank=True, default='hint')
    answer = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.title
