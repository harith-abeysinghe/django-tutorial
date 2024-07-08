from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# django uses MVT (Model-View-Template architecture).


# The view is responsible for processing the request and returning the response. 
# The view is a Python function that takes a web request and returns a web response.
# The view function receives web requests and returns web responses
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)