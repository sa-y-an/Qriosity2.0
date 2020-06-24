from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import models
import datetime
#from django.contrib.auth.models import User

# Create your views here.


def dashboard(request):
    if request.user:
        if request.user.is_authenticated:
            player=models.Player.objects.get(user=request.user)
            return render(request, 'user/user.html', {'user':player})
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')





def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        profile = user
        try :
            player = models.Player.objects.get(user=profile)
        except:
            player = models.Player(user=profile)
            player.timestamp = datetime.datetime.now()
            player.name = response.get('name')
            player.image = response.get('picture')
            player.email = response.get('email')
            player.save()
    elif backend.name == 'facebook':
        profile = user
        try:
            player = models.Player.objects.get(user=profile)
        except:
            player = models.Player(user=profile)
            player.name = response.get('first_name')+" "+response.get('last_name')
            player.email = response.get('email')
            player.image = "http://graph.facebook.com/%s/picture?type=large" \
                % response["id"]
            player.timestamp = datetime.datetime.now()
            player.save()
