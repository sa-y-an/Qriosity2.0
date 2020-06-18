from django.shortcuts import render, get_object_or_404
from .models import StaticQuestions, AudioQuestions
from .forms import UserAnswer
# Create your views here.


def quiz(request):

    squestions = StaticQuestions.objects.all()
    aquestions = AudioQuestions.objects.all()
    return render(request, 'quiz/quiz.html', {'squestions': squestions,
                                              'aquestions': aquestions})


def stat(request, qid):
    my_form = UserAnswer()
    if request.method == 'POST':
        my_form = UserAnswer(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data.get("answer"))
            ans = my_form.cleaned_data.get("answer")
    else:
        ans = 'error'

    question = get_object_or_404(StaticQuestions, pk=qid)
    return render(request, 'quiz/stat.html', {"question": question, "my_form": my_form, "ans": ans})


def audio(request, qid):
    question = get_object_or_404(AudioQuestions, pk=qid)
    return render(request, 'quiz/audio.html', {"question": question})
