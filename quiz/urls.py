from django.urls import path
from . import views

app_name = 'quiz'


urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('stat/<int:qid>', views.stat, name='stat'),
    path('audio/<int:qid>', views.audio, name='audio'),

]
