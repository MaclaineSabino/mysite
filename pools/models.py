from django.db import models

# Create your models here.

#class Question(object):
    #def __init__(self,question_text='',pub_date=''):
        #self.question_text=question_text
        #self.pub_date=pub_date


class Question(models.Model):
    question_text=models.CharField(max_length=255)
    closed=models.BooleanField(default=False)
    pub_date=models.DateField(max_length=50)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,null=True)

    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):

        return self.choice_text
