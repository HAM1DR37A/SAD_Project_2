from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
class TopGenre(models.Model):
    name = models.CharField(max_length=200)
    amountOfBuyer = models.IntegerField()

    def __str__(self):
        return self.name


class BookForTarjome(models.Model):
    name = models.CharField(max_length=200)
    lang = models.CharField(max_length=2,default='FA')
    # adding_date = models.DateTimeField('date added', default=timezone.now())
    adding_date = models.DateTimeField('date added')

    def __str__(self):
        return self.name

# TODO in kelas bas eslah beshe
class motarjem(models.Model):
    name = models.CharField(max_length=200)
    desiredLang = models.CharField(max_length=2)
    notification = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name
