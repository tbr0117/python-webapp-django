from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def index(request):
    return HttpResponse('Hello World, this is my world ')

def detail(request, QuestionId):
    return HttpResponse("You're looking at question %s" % QuestionId)

def result(request, QuestionId):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % QuestionId)

def vote(request, QuestionId):
    return HttpResponse("You're voting on question %s." % QuestionId)
    

