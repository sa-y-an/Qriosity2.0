from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
import user
import home

urlpatterns = [
    path('harrypotter/', admin.site.urls),
    path('user/', include('user.urls')),
    path('quiz/', include('quiz.urls')),
    path('', include('home.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
