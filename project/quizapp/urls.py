from django.urls import path
from django.views.generic.base import TemplateView
from . import views

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="base.html"), name="base"),
    path('quiz/<int:quiz_id>', views.QuizView.as_view(), name="quiz"),
    path('quiz/<int:quiz_id>/results', views.QuizView.as_view(), name="results")
]