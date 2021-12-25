from django import template
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

from django.template import loader

# Create your views here.
def index(request):
    print(request)
    latest_questions = Question.objects.order_by("-PostedOn")[:10]
    output = ', '.join([q.QuestionText for q in latest_questions])
    print(output)
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render({latest_questions:latest_questions}, request))
    return render(request, "polls/index.html", {'latest_questions':latest_questions})


class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name = "latest_questions"
    def get_queryset(self):
        return Question.objects.filter(
            PostedOn__lte=timezone.now()
        ).order_by("-PostedOn")[:10]


def detail(request, QuestionId):
    print(request)
    try:
        question = Question.objects.get(QuestionId=QuestionId)
    except Question.DoesNotExist:
        raise Http404("Hey dude, No poll here; go back ur work😎😎😎")
    
    return render(request, "polls/details.html", {"Question": question})


def results(request, QuestionId):
    question = get_object_or_404(Question, QuestionId=QuestionId)
    response = "You're looking at the result of question %s"
    # return HttpResponse(response % ', '.join([f"{c.ChoiceText}: {c.Votes}" for c in question.choice_set.all()]))
    return render(request, "polls/results.html", {'Question':question})

def vote(request, QuestionId):
    question = get_object_or_404(Question, QuestionId=QuestionId)
    try: 
        selected_choice  = question.choice_set.get(ChoiceId=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            "question": question,
            "error_message": "You didn't select a choice"
        })
    else:
        selected_choice.Votes += 1
        selected_choice.save()
        # return response.HttpResponse("Hey Total polls matched with ur choice %s", selected_choice.ChoiceId)   
        return HttpResponseRedirect(reverse('polls:results', args=(QuestionId,)))
    # return HttpResponse("You're voting on question %s." % QuestionId)
    

