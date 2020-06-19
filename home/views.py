from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def rules(request):
    return render(request, 'home/rules.html')
