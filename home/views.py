from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def not_logged_in(user):
    return not user.is_authenticated


def base(request):
    return render(request, 'home/base.html')


def home(request):
    return render(request, 'home/home.html')


def hello(request):
    return render(request, 'home/hello.html')


@user_passes_test(not_logged_in, login_url='/user/dashboard', redirect_field_name=None)
def login(request):
    return render(request, 'home/login.html')


def rules(request):
    return render(request, 'home/rule.html')
