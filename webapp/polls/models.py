from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    QuestionId = models.IntegerField(unique=True, db_index=True)
    QuestionText = models.CharField(max_length=255)
    Department = models.CharField(max_length=20)
    Topic = models.CharField(max_length=20)
    Tags = models.CharField(max_length=200)
    PostedOn = models.DateTimeField('date published')
    
    def __str__(self):
        return self.QuestionText
    
    def was_published_recently(self):
        return self.PostedOn >= timezone.now() - datetime.timedelta(days=1)

    
    def __iter__(self):
        for key in self.__dict__:
            if not key == "__state":
              yield key, getattr(self, key)

class Choice(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    ChoiceId = models.IntegerField()
    ChoiceText = models.CharField(max_length=100)
    Votes = models.IntegerField(max_length=10)

    def __str__(self):
        return self.ChoiceText