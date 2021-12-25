import datetime
from django.http import response
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose PostedOn
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(PostedOn=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose PostedOn
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(PostedOn=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(QuestionId, QuestionText, days):
    """
    Create a question with the given `QuestionText` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(QuestionId=QuestionId, QuestionText=QuestionText, PostedOn=time)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "There are no polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])


    def test_past_question(self):
        """
        Questions with a PostedOn in the past are displayed on the
        index page.
        """
        question = create_question(QuestionId=2, QuestionText="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            [question],
        )
    

    def test_future_question(self):
        """
        Questions with a PostedOn in the futrue are not displayed on the
        index page
        """
        create_question(QuestionId=3, QuestionText="Future question ?", days=+30)
        response = self.client.get(reverse("polls:index"))
        # self.assertContains(response, "There are no polls are available.")
        self.assertQuerysetEqual(response.context["latest_questions"], [])
    

    def test_future_and_past_question(self):
        """
        Questions with a PostedOn in the futrue are not displayed on the
        index page
        """
        question1 = create_question(QuestionId=4, QuestionText="Past Quetion ?", days=-30)
        question2 = create_question(QuestionId=5, QuestionText="Future question ?", days=+30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_questions"], [question1])


    def test_two_past_question(self):
        """
        Questions with a PostedOn in the past are displayed on the
        index page
        """
        question1 = create_question(QuestionId=6, QuestionText="Past -30 Quetion ?", days=-30)
        question2 = create_question(QuestionId=7, QuestionText="Past -5 question ?", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_questions"], [question2, question1])

    


