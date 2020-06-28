from django.urls import path
from .import views

app_name = 'user'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('privacypolicy', views.privacy_policy_fb, name="privacypolicy"),
    path('details/', views.UserData, name="details"),
]
