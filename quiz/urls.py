from django.urls import path
from . import views

app_name = 'quiz'


urlpatterns = [
    path('', views.StageOne, name='stageone'),
    path('answer/', views.Stage1Answer, name="answer"),
    path('hint/', views.Stage1Hint, name="hint")
    # path('audio/<int:qid>', views.audio, name='audio'),
    # path('stat/finished', views.statend, name='statend'),
    # path('audio/finished', views.audend, name='audend'),

]
