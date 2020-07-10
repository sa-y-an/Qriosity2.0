from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Stage_1, StageTwo
from django.contrib.auth.decorators import login_required
from user.models import Player, Solved
from .forms import UserAnswer
import datetime
# Create your views here.

value = False


def Algo(request):
    question = Stage_1.objects.all()
    return render(request, 'quiz/algorithm.html', {"questions": question})


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
        player = get_object_or_404(Player, user=request.user)
        if (player.count2 < StageTwo.objects.count()):
            return render(request, 'quiz/index.html', {"q": q, "player": player})
        else:
            return render(request, 'quiz/finish.html', {"player": player})


@login_required(login_url='/login', redirect_field_name=None)
def Stage1Hint(request):
    player = get_object_or_404(Player, user=request.user)
    player.score -= 1
    player.save()
    question_level = player.question_level
    question = get_object_or_404(Stage_1, level=int(question_level))
    return render(request, 'quiz/hints.html', {"question": question})


@login_required(login_url='/login', redirect_field_name=None)
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
                    formp = UserAnswer
                    return render(request, 'quiz/Stage1.html', {"question": question, "form": formp, "value": value})
            else:
                formp = UserAnswer
                value = True
                return render(request, 'quiz/Stage1.html', {"question": question, "form": formp, "value": value})
        else:
            return HttpResponse('<h2> Form data not valid</h2>')

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required(login_url='/login', redirect_field_name=None)
def Index(request):
    q = StageTwo.objects.all()
    player = get_object_or_404(Player, user=request.user)
    if (player.count2 < StageTwo.objects.count()):
        return render(request, 'quiz/index.html', {"q": q, "player": player})
    else:
        return render(request, 'quiz/finish.html', {"player": player})


@login_required(login_url='/login', redirect_field_name=None)
def hint2(request, hint2):
    if request.method == "POST":
        player = get_object_or_404(Player, user=request.user)
        # qid = int(player.level2)
        player.score -= 1
        player.save()
        question = get_object_or_404(StageTwo, level=hint2)
        # print(question.title)
        return render(request, 'quiz/hint2.html', {"question": question})
    if request.method == "GET":
        return render(request, 'quiz/smart.html')


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


# individual questions of stage 2
@login_required(login_url='/login', redirect_field_name=None)
def Individual(request, qid):
    value = False  # this marks if the question is solved (and shows the popup)
    player = get_object_or_404(Player, user=request.user)
    s = player.solved_set.all()     # solved class has 2 objects 1. level_on 2. solved
    question = get_object_or_404(StageTwo, level=qid)
    p = get_object_or_404(Player, user=request.user)
    p.level2 = int(qid)
    p.save()            # sets the current level of the user to the visiting question

    flag = False        # player solved it or not
    for i in s:         # checks if player have already visited the question
        if (i.level_on == qid):
            if (i.solved == True):  # checks if player have solved the question
                flag = True
                # then returns the solved page
                return render(request, 'quiz/solved.html')
            else:
                flag = True
                if request.method == "GET":     # if the player comes for the question
                    my_form = UserAnswer
                    return render(request, 'quiz/individual.html', {"question": question, "form": my_form, "value": value})
                if request.method == "POST":    # if the player submits the question
                    my_form = UserAnswer(request.POST)

                    if my_form.is_valid():
                        ans = my_form.cleaned_data.get("answer")
                        organs = get_object_or_404(StageTwo, level=qid).answer

                        # correct answer
                        if (str(organs) == str(ans)):   # if the answer is correct
                            player.score += 5
                            player.count2 += 1          # count of solved questions
                            i.solved = True         # the question is set to solved corrosponding to that level
                            i.save()
                            player.save()
                            return render(request, 'quiz/solved.html')

                        # incorrect answer
                        else:   # returns the same question
                            value = True
                            return render(request, 'quiz/individual.html', {"question": question, "form": my_form, "value": value})
                    else:
                        return HttpResponse('<h2> Your Form data was Invalid </h2>')
                        # invalid form data submitted by tampering with developer console

    if (flag == False):  # the player didnot visited the question before
        # creates a Solved object with level_on = question level and solved set to False
        player.solved_set.create(level_on=qid, solved=False)

        if request.method == "GET":
            my_form = UserAnswer
            return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
        if request.method == "POST":
            my_form = UserAnswer(request.POST)
            if my_form.is_valid():
                ans = my_form.cleaned_data.get("answer")
                organs = get_object_or_404(StageTwo, level=qid).answer
                if (str(organs) == str(ans)):  # if the player succesfully solves the question
                    player.score += 5
                    player.count2 += 1          # count of solved questions
                    i = player.solved_set.get(level_on=qid)
                    i.solved = True  # sets the solved to true
                    i.save()
                    player.save()
                    return render(request, 'quiz/solved.html')
                else:   # returns the same question
                    value = False
                    return render(request, 'quiz/individual.html', {"question": question, "form": my_form})
            else:
                return HttpResponse('<h2> Your Form data was Invalid </h2>')
