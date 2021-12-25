import datetime
from django.test import TestCase
from django.utils import timezone
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
