from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=200,blank=True)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    last_submit = models.DateTimeField(default=datetime.now)
    question_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
