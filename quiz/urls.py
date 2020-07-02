from django.urls import path
from . import views

app_name = 'quiz'


urlpatterns = [
    path('', views.StageOne, name='stat'),
    # path('audio/<int:qid>', views.audio, name='audio'),
    # path('stat/finished', views.statend, name='statend'),
    # path('audio/finished', views.audend, name='audend'),

]
