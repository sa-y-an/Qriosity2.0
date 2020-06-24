from django.shortcuts import render, get_object_or_404
from .models import StaticQuestions, AudioQuestions
from django.contrib.auth.decorators import login_required
from user.models import Player
from .forms import UserAnswer
import datetime
# Create your views here.

@login_required(login_url='/')
def quiz(request):

    squestions = StaticQuestions.objects.all()
    aquestions = AudioQuestions.objects.all()

    return render(request, 'quiz/quiz.html', {'squestions': squestions,
                                              'aquestions': aquestions})

@login_required(login_url='/')
def stat(request, qid):

    if qid == 1:
        my_form = UserAnswer()
        ans = 4
        question = get_object_or_404(StaticQuestions, pk=qid)
        if (int(qid)+1 <= StaticQuestions.objects.count()):
            question2 = get_object_or_404(StaticQuestions, pk=int(qid)+1)
        else:
            question2 = -1

        return render(request, 'quiz/stat.html', {"question": question, "my_form": my_form, "question2": question2})
    else:
        if request.method == 'GET':
            return render(request, 'quiz/smart.html')
        elif request.method == 'POST':
            my_form = UserAnswer()
            if request.method == 'POST':
                my_form = UserAnswer(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data.get("answer"))
                ans = my_form.cleaned_data.get("answer")
            else:
                ans = 'error'

            question = get_object_or_404(StaticQuestions, pk=qid)
            if (int(qid)+1 <= StaticQuestions.objects.count()):
                question2 = get_object_or_404(StaticQuestions, pk=int(qid)+1)
            else:
                question2 = -1

            return render(request, 'quiz/stat.html', {"question": question, "my_form": my_form, "ans": ans, "question2": question2})

@login_required(login_url='/')
def audio(request, qid):

    if qid == 1:
        my_form = UserAnswer()
        ans = 4
        question = get_object_or_404(AudioQuestions, pk=qid)
        if (int(qid)+1 <= AudioQuestions.objects.count()):
            question2 = get_object_or_404(AudioQuestions, pk=int(qid)+1)
        else:
            question2 = -1

        return render(request, 'quiz/audio.html', {"question": question, "my_form": my_form, "question2": question2})
    else:
        if request.method == 'GET':
            return render(request, 'quiz/smart.html')
        elif request.method == 'POST':
            my_form = UserAnswer()
            if request.method == 'POST':
                my_form = UserAnswer(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data.get("answer"))
                ans = my_form.cleaned_data.get("answer")
            else:
                ans = 'error'

            question = get_object_or_404(AudioQuestions, pk=qid)
            if (int(qid)+1 <= AudioQuestions.objects.count()):
                question2 = get_object_or_404(AudioQuestions, pk=int(qid)+1)
            else:
                question2 = -1

            return render(request, 'quiz/audio.html', {"question": question, "my_form": my_form, "ans": ans, "question2": question2})

@login_required(login_url='/')
def statend(request):
    if (request.method == "POST"):
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data.get("answer"))
            ans = my_form.cleaned_data.get("answer")
    return render(request, 'quiz/statend.html')

@login_required(login_url='/')
def audend(request):
    if (request.method == "POST"):
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data.get("answer"))
            ans = my_form.cleaned_data.get("answer")
    return render(request, 'quiz/audend.html')

# https://gist.github.com/kissgyorgy/6110380
# while integrating with postgress
