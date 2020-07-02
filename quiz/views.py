from django.http import HttpResponse, HttpResponseNotFound
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
    my_form = UserAnswer
    return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form})


def Stage1Hint(request):
    player = get_object_or_404(Player, user=request.user)
    player.score -= 1
    question_level = player.question_level
    question = get_object_or_404(Stage_1, level=int(question_level))
    return render(request, 'quiz/Stage1.html', {"question": question})


def Stage1Answer(request):
    if request.method == "POST":
        player = get_object_or_404(Player, user=request.user)
        question_level = player.question_level
        question = get_object_or_404(Stage_1, level=int(question_level))

        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            ans = my_form.cleaned_data.get("answer")
            if (str(ans) == str(question.answer)):
                player.score += 3
                player.question_level += 1
                question_level = player.question_level
                question = get_object_or_404(
                    Stage_1, level=int(question_level))
                return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form})
            else:
                return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form})
        else:
            return HttpResponse('<h2> Form data not valid</h2>')

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
