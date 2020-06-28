from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .import models
import datetime
from .forms import UserDetails
#from django.contrib.auth.models import User

# Create your views here.

current_leaderboard = None


def dashboard(request):
    if request.method == "POST":
        my_form = UserDetails(request.POST)
        if my_form.is_valid():
            # my form is valid
            print(my_form.cleaned_data)
            models.PlayerDetails.objects.create(**my_form.cleaned_data)

            if request.user:
                if request.user.is_authenticated:
                    player = models.Player.objects.get(user=request.user)
                    return render(request, 'user/dashboard.html', {'user': player})
                else:
                    return redirect('home:home')
            else:
                return redirect('home:home')

        else:
            print(my_form.errors)

    if request.method == "GET":
        if request.user:
            if request.user.is_authenticated:
                player = models.Player.objects.get(user=request.user)
                return render(request, 'user/dashboard.html', {'user': player})
            else:
                return redirect('home:home')
        else:
            return redirect('home:home')


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        profile = user
        try:
            player = models.Player.objects.get(user=profile)
        except:
            player = models.Player(user=profile)
            player.last_submit = datetime.datetime.now()
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
            player.name = response.get(
                'first_name')+" "+response.get('last_name')
            player.email = response.get('email')
            player.image = "http://graph.facebook.com/%s/picture?type=large" \
                % response["id"]
            player.last_submit = datetime.datetime.now()
            player.save()


@login_required(login_url='/')
def leaderboard(request):
    global current_leaderboard
    current_leaderboard = models.Player.objects.order_by(
        '-score', '-last_submit')
    return render(request, 'user/leaderboard.html', {'leaderboard': current_leaderboard})


def privacy_policy_fb(request):
    return render(request, "user/privacypolicy.html")


def UserData(request):
    my_form = UserDetails()
    context = {
        "form": my_form
    }
    return render(request, "user/details.html", context)
