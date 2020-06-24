from django.db import models

# Create your models here.

# static questions containing only text and images


class StaticQuestions(models.Model):
    title = models.CharField(blank=True, max_length=200)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True, default='hello')
    image = models.ImageField(blank=True, upload_to='StaticQuestions/images')
    answer = models.CharField(blank=True, max_length=200)
    hint = models.TextField(blank=True, default='hint')
    # intans = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

# Audio questions


class AudioQuestions(models.Model):
    title = models.CharField(blank=True, max_length=200)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True, default='hello')
    file = models.FileField(upload_to='AudioQuestions/music')
    image = models.ImageField(blank=True, upload_to='AudioQuestions/images')
    answer = models.CharField(blank=True, max_length=200)
    hint = models.TextField(blank=True, default='hint')
    # intans = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

# add this in template to play it
# <audio src="{{ song.file.url }}" controls></audio>
