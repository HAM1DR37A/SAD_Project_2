from __future__ import unicode_literals

from django.db import models


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



########################################################################
#############These lines are added by hamid#############################

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.fields.related import ForeignKey


class BookReaderUser(models.Model):
    django_user = models.OneToOneField(User, null=False)
    # avatar = models.ImageField(null=False, default='user.png')
    # telephone_no = models.CharField(max_length=15)
    # address = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.django_user


class Language(models.Model):
    language_name = models.CharField(max_length= 10)

    def __str__(self):
        return self.language_name


class Book(models.Model):
    title = models.CharField(max_length=40, null=False)
    book_id = models.CharField(max_length=10, primary_key=True, auto_created=True)
    # first_publish_year = models.IntegerField(null=False)
    # isbn = models.CharField(max_length=20, null=False, unique=True)
    # number_of_pages = models.IntegerField()
    # summary = models.TextField()
    # cover_image_addr = models.ImageField(null=False, default='Book.png')
    # author_name = models.CharField(null=False, max_length=20, default='author')
    # translator_name = models.CharField(null=True, max_length=20)
    # publisher_name = models.CharField(null=True, max_length=20)
    # adding_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

class Genre(models.Model):
    genre_type = models.CharField(max_length=20,null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=False)

    class Meta:
        unique_together = ('genre_type', 'book_id')

    def __str__(self):
        return self.genre_type


# TODO in chera name nadare?
class BookSeller(models.Model):
    book_seller_id = models.CharField(max_length=15, auto_created=True, primary_key=True)
    # avatar = models.ImageField(null=False, default='user.png')
    # telephone_no = models.CharField(max_length=15)
    # address = models.CharField(max_length=150, null=False)


#BookMaker
class BookMaker(models.Model):
    male = 'ML'
    female = 'FM'
    translator = 'TR'
    author = 'AUT'
    both = 'Both'
    gender_choices = (
        (male, 'Male'),
        (female, 'Female')
    )
    type_choices = (
        (translator, "Translator"),
        (author, "Author"),
        (both, "Both")
    )
    name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    book_maker_id = models.CharField(max_length=10, auto_created=True, primary_key=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=2, choices=gender_choices)
    book_maker_type = models.CharField(max_length=4, choices=type_choices)
    # verifier_id = models.ForeignKey(Admin)
    # avatar = models.ImageField(null=False, default='user.png')
    # telephone_no = models.CharField(max_length=15)
    # address = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name+" "+self.last_name


# class BookMakerLanguage(models.Model):
#     book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
#     language_name = models.ForeignKey(Language, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('book_maker_id', 'language_name')

class TranslationRequest(models.Model):
    # book_file = models.FileField()
    source_lang = models.ForeignKey(Language,null=False)
    translation_request_id = models.IntegerField(primary_key=True, auto_created=True)
    # user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)
    # book_maker_id = models.ForeignKey(BookMaker, on_delete=models.PROTECT, null=True)
    # register_date = models.DateField()
    # response_date = models.DateField()
    # finish_date = models.DateField()
#     TODO added byME
    BookName = models.CharField(max_length=200)

    def __str__(self):
        return self.BookName


class Notification(models.Model):
    notif_id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    notif_date_created = models.DateField(null=False)
    # TODO in khat e paiini eslah shod
    BookMaker_id = models.ForeignKey(BookMaker)

    def __str__(self):
        return self.content

