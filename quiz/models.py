from django.db import models

# Create your models here.

# static questions containing only text and images


class Stage_1(models.Model):
    title = models.CharField(blank=True, max_length=200)
    level = models.IntegerField()
    description = models.TextField(blank=True, default='hello')
    image_url = models.URLField(blank=True)
    hint = models.TextField(blank=True, default='hint')
    answer = models.CharField(blank=True, max_length=400)
    algo = models.TextField(blank=True)

    def __str__(self):
        return str(str(self.level)+str(" . ")+str(self.title))


class StageTwo(models.Model):
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True, default='hello')
    answer = models.CharField(blank=True, max_length=400)
    level = models.IntegerField()

    def __str__(self):
        return str(str(self.level)+str(" . ")+str(self.title))
