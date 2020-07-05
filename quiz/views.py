from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Stage_1, StageTwo
from django.contrib.auth.decorators import login_required
from user.models import Player
from .forms import UserAnswer
import datetime
# Create your views here.

value = False


@login_required(login_url='/login', redirect_field_name=None)
def StageOne(request):
    player = get_object_or_404(Player, user=request.user)
    # print(player.level2)

    if player.level2 < 0:
        player = get_object_or_404(Player, user=request.user)
        question_level = player.question_level
        player.save()

        if player.question_level > Stage_1.objects.count():
            formp = UserAnswer
            check = False
            return render(request, 'quiz/end.html', {"form": formp, "check": check})

        question = get_object_or_404(Stage_1, level=int(question_level))
        my_form = UserAnswer
        return render(request, 'quiz/Stage1.html', {"question": question, "form": my_form, "value": value})
    if player.level2 > -1:
        q = StageTwo.objects.all()
        return render(request, 'quiz/index.html', {"player": player, "q": q})


@login_required(login_url='/login', redirect_field_name=None)
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
            formp = UserAnswer
            check = False
            return render(request, 'quiz/end.html', {"form": formp, "check": check})

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
                    formp = UserAnswer
                    check = False
                    return render(request, 'quiz/end.html', {"form": formp, "check": check})

                if player.question_level > Stage_1.objects.count():
                    formp = UserAnswer
                    check = False
                    return render(request, 'quiz/end.html', {"form": formp, "check": check})
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
@login_required(login_url='/login', redirect_field_name=None)
def Index(request):
    q = StageTwo.objects.all()
    player = get_object_or_404(Player, user=request.user)
    return render(request, 'quiz/index.html', {"q": q, "player": player})


@login_required(login_url='/login', redirect_field_name=None)
def Individual(request, qid):
    p = get_object_or_404(Player, user=request.user)
    p.level2 = int(qid)
    p.save()
    question = get_object_or_404(StageTwo, pk=qid)
    my_form = UserAnswer
    if request.method == "GET":
        return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
    if request.method == "POST":
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            player = get_object_or_404(Player, user=request.user)
            ans = my_form.cleaned_data.get("answer")
            organs = get_object_or_404(StageTwo, pk=qid).answer
            if (str(organs) == str(ans)):
                player.score += 5
                player.save()
                return render(request, 'quiz/solved.html')
            else:
                return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
        else:
            return HttpResponse('<h2> Your Form data was Invalid </h2>')


@login_required(login_url='/login', redirect_field_name=None)
def hint2(request):
    if request.method == "POST":
        player = get_object_or_404(Player, user=request.user)
        qid = int(player.level2)
        player.score -= 1
        player.save()
        question = StageTwo(pk=qid)
        return render(request, 'quiz/hint2.html', {"question": question})


@login_required(login_url='/login', redirect_field_name=None)
def Passcode(request):
    code = "ENIGMACODE"
    if request.method == "POST":
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            # print(my_form.cleaned_data)
            ans = my_form.cleaned_data.get("answer")

            if (str(ans) == str(code)):
                player = get_object_or_404(Player, user=request.user)
                player.level2 = 0
                player.save()
                # print(player.level2)
                q = StageTwo.objects.all()
                player = get_object_or_404(Player, user=request.user)
                return render(request, "quiz/index.html", {"q": q, "player": player})
            else:
                check = True
                formp = UserAnswer
                return render(request, "quiz/end.html", {"check": check, "form": formp})
        else:
            return HttpResponse("<h1>form data invalid </h1>")
