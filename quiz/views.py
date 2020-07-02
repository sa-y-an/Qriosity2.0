from django.shortcuts import render, get_object_or_404
from .models import Stage_1
from django.contrib.auth.decorators import login_required
from user.models import Player
from .forms import UserAnswer
import datetime
# Create your views here.


def StageOne(request):
    player = get_object_or_404(Player, user=request.user)
    question_level = player.question_level
    question = get_object_or_404(Stage_1, level=int(question_level))
    return render(request, 'quiz/Stage1.html', {"question": question})
