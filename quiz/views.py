from django.shortcuts import render, get_object_or_404
from .models import StaticQuestions, AudioQuestions
# Create your views here.


def quiz(request):

    squestions = StaticQuestions.objects.all()
    aquestions = AudioQuestions.objects.all()
    return render(request, 'quiz/quiz.html', {'squestions': squestions,
                                              'aquestions': aquestions})


# def details(request):
#     squestions = get_object_or_404(StaticQuestions,  pk=staticquestions_id)
#     return render(request, 'quiz/squestions.html', {'squestions': squestions})
