from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User

# Create your views here.


@login_required
def dashboard(request):
    # social = User.social_auth.get(provider='facebook')
    # userid = social.uid
    # first_name = social.extra_data['first_name']
    # last_name = social.extra_data['last_name']
    return render(request, 'user/user.html')
