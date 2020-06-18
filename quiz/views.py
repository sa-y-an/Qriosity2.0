from django.shortcuts import render, get_object_or_404
from .models import StaticQuestions, AudioQuestions
# Create your views here.


def quiz(request):

    squestions = StaticQuestions.objects.all()
    aquestions = AudioQuestions.objects.all()
    return render(request, 'quiz/quiz.html', {'squestions': squestions,
                                              'aquestions': aquestions})


def stat(request, qid):
    question = get_object_or_404(StaticQuestions, pk=qid)
    return render(request, 'quiz/stat.html', {"question": question})


def audio(request, qid):
    question = get_object_or_404(AudioQuestions, pk=qid)
    return render(request, 'quiz/audio.html', {"question": question})
