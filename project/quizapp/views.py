from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views import View
from django.conf import settings

from . import models
# Create your views here.


def getGrade(n):
    if n < 0:
        return "F-"
    elif 0 < n <= 3.29:
        return "F"
    elif 3.29 < n <= 3.9:
        return "D"
    elif 3.99 < n <= 4.99:
        return "C"
    elif 4.99 < n <= 5.99:
        return "B"
    elif 5.99 < n <= 6.99:
        return "A-"
    elif 6.99 < n <= 7.99:
        return "A"
    elif n >= 8:
        return "A+"
    
    


class BaseView(TemplateView):
    template_name = 'base.html'

class QuizView(TemplateView):
    template_name = 'quiz.html'

    def get(self, request, quiz_id, *args, **kwargs):
        
        quiz = get_object_or_404(models.Quiz, pk=quiz_id)
        questions= models.Question.objects.filter(correspondingToQuiz=quiz_id)
        
        context = {
            'quiz': quiz,
            'questions': questions,
            'results': False,
            'results_info': {}
            }

        return render(
            request,
            self.template_name,
            context=context
            )

    def post(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(models.Quiz, pk=quiz_id)
        questions= models.Question.objects.filter(correspondingToQuiz=quiz_id)
        
        max_score = len(questions)
        score = 0
        bonus_score = 0
        bonus_questions = 0
        for i in range(len(request.POST)-1):
            question = questions[i]
            if settings.DEBUG:
                print(f"Question: {question}")
                print(f"Answer: {request.POST[str(question)]}")
                print(f"Right answer: {question.rightAnswer}")
            if request.POST[str(question)] == question.rightAnswer:
                if question.bonus:
                    bonus_score+=.5
                    bonus_questions+=1
                else:
                    score+=1

        divisor = len(questions) - bonus_questions
        total_score = score+bonus_score / divisor
        avg = total_score*10 / divisor
        percentage = (total_score / divisor) * 100

        context = {
            'quiz': quiz,
            'results': True,
            'results_info': {
                'divisor': divisor,
                'avg': avg,
                'score': score,
                'bonus': bonus_score,
                'percentage': float(f"{percentage: .3f}"),
                'grade': getGrade(avg),
                'total_score': total_score
            }
        }

        return render(request, self.template_name, context=context)

class ResultsView(TemplateView):
    template_name = 'results.html'
    def get(self, request, *args, **kwargs):
        pass