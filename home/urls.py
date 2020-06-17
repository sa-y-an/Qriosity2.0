from django.urls import path
from . import views
import user
import quiz

urlpatterns=[
    path('',views.home,name='home'),
    path('user',user.views.user,name='user'),
    path('quiz',quiz.views.quiz,name='quiz')
]