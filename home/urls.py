from django.urls import path, include
from . import views
import user
import quiz

urlpatterns = [
    path('', views.home, name='home'),

]
