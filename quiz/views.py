from django.shortcuts import render, get_object_or_404
from .models import Stage_1
from django.contrib.auth.decorators import login_required
from user.models import Player
from .forms import UserAnswer
import datetime
# Create your views here.


def StageOne(request, qid):
    question = get_object_or_404(Stage_1, level=1)
    return render(request, 'quiz/Stage1.html', {"question": question})

    # @login_required(login_url='/login', redirect_field_name=None)
    # def StageOne(request, qid):

    #     if qid == 1:
    #         my_form = UserAnswer()
    #         ans = 4
    #         question = get_object_or_404(Stage1, pk=qid)
    #         if (int(qid)+1 <= Stage1.objects.count()):
    #             question2 = get_object_or_404(Stage1, pk=int(qid)+1)
    #         else:
    #             question2 = -1

    #         return render(request, 'quiz/stat.html', {"question": question, "my_form": my_form, "question2": question2})
    #     else:
    #         if request.method == 'GET':
    #             return render(request, 'quiz/smart.html')
    #         elif request.method == 'POST':
    #             my_form = UserAnswer()
    #             if request.method == 'POST':
    #                 my_form = UserAnswer(request.POST)
    #             if my_form.is_valid():
    #                 print(my_form.cleaned_data.get("answer"))
    #                 ans = my_form.cleaned_data.get("answer")
    #                 question = get_object_or_404(Stage1, pk=int(qid) - 1)
    #                 print(question.answer)

    #                 if (str(ans) == str(question.answer)):
    #                     player = Player.objects.get(user=request.user)
    #                     player.score += 1
    #                     player.last_submit = datetime.datetime.now()
    #                     player.save()

    #             else:
    #                 ans = 'error'

    #             question = get_object_or_404(Stage1, pk=qid)
    #             if (int(qid)+1 <= Stage1.objects.count()):
    #                 question2 = get_object_or_404(Stage1, pk=int(qid)+1)
    #             else:
    #                 question2 = -1

    #             return render(request, 'quiz/stat.html', {"question": question, "my_form": my_form, "ans": ans, "question2": question2})
