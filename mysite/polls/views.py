from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"your looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"your looking at results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"your voting on question {question_id}")
