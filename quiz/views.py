from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Stage_1, Stage_2
from django.contrib.auth.decorators import login_required
from user.models import Player
from .forms import UserAnswer
import datetime
# Create your views here.

value = False


def StageOne(request):

    player = get_object_or_404(Player, user=request.user)
    question_level = player.question_level
    player.save()

    if player.question_level > Stage_1.objects.count():

        return render(request, 'quiz/end.html')
    question = get_object_or_404(Stage_1, level=int(question_level))
    my_form = UserAnswer
    return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form, "value": value})


def Stage1Hint(request):
    player = get_object_or_404(Player, user=request.user)
    player.score -= 1
    player.save()
    question_level = player.question_level
    question = get_object_or_404(Stage_1, level=int(question_level))
    return render(request, 'quiz/hints.html', {"question": question})


def Stage1Answer(request):

    if request.method == "POST":
        player = get_object_or_404(Player, user=request.user)
        question_level = player.question_level

        try:
            question = Stage_1.objects.get(level=int(question_level))
        except Stage_1.DoesNotExist:
            return render(request, 'quiz/end.html')

        my_form = UserAnswer(request.POST)
        if my_form.is_valid():

            ans = my_form.cleaned_data.get("answer")

            if (str(ans) == str(question.answer)):
                value = False
                player.score += 3
                player.question_level += 1

                player.save()
                question_level = player.question_level
                try:
                    question = Stage_1.objects.get(
                        level=int(question_level))
                except Stage_1.DoesNotExist:
                    return render(request, 'quiz/end.html')

                if player.question_level > Stage_1.objects.count():
                    return render(request, 'quiz/end.html')
                else:
                    return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form, "value": value})
            else:
                value = True
                return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form, "value": value})
        else:
            return HttpResponse('<h2> Form data not valid</h2>')

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


# make a new player model and include level2
def Index(request):
    questions = Stage_2.objects.all()
    return render(request, 'quiz/index.html', {"questions": questions})


def Individual(request, qid):
    p = get_object_or_404(Player, user=request.user)
    p.level2 = int(qid)
    p.save()
    question = get_object_or_404(Stage_2, pk=qid)
    my_form = UserAnswer
    if request.method == "GET":
        return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
    if request.method == "POST":
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            player = Player(user=request.user)
            ans = my_form.cleaned_data.get("answer")
            organs = get_object_or_404(Stage_2, pk=qid).answer
            if (str(organs) == str(ans)):
                player.score += 5
                player.save()
                return render(request, 'quiz/solved.html')
            else:
                return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
        else:
            return HttpResponse('<h2> Your Form data was Invalid </h2>')


def hint2(request):
    if request.method == "POST":
        player = Player(user=request.user)
        qid = int(player.level2)
        player.score -= 1
        player.save()
        question = Stage_2(pk=qid)
        return render(request, 'quiz/hint2.html', {"question": question})
