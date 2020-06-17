from django.urls import path, include
from . import views
import user
import quiz

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', include(user.urls), name='user'),
    path('quiz/', include(quiz.urls), name='quiz'),
]
