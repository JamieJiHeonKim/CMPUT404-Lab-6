from django.db import models

# Create your models here.

class Question(models.Model):
    question text = models.CharField(max length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on delete=models.CASCADE)
    choice text = models.CharField(max length=200)
    votes = models.IntegerField(default=0)
