from django.contrib import admin
from .models import StaticQuestions, AudioQuestions
# Register your models here.

admin.site.register(StaticQuestions)
admin.site.register(AudioQuestions)
