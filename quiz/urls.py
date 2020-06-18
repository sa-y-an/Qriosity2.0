from django.urls import path
from . import views
urlpatterns = [
    path('', views.quiz, name='quiz'),
    # path('<str:staticquestions_id>/', views.details, name='details')
]
