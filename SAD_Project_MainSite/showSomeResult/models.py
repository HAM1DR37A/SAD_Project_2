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



########################################################################
#############These lines are added by hamid#############################

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.fields.related import ForeignKey


class BookReaderUser(models.Model):
    django_user = models.OneToOneField(User, null=False)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)


class OrganizationFinancialAccount(models.Model):
    account_id = models.IntegerField(primary_key=True)


class ShoppingCart(models.Model):
    shopping_cart_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(BookReaderUser)


class Language(models.Model):
    language_name = models.CharField(max_length= 10)


class Admin(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    admin_id = models.IntegerField(primary_key=True, auto_created=True)


class Book(models.Model):
    title = models.CharField(max_length=40, null=False)
    book_id = models.CharField(max_length=10, primary_key=True, auto_created=True)
    first_publish_year = models.IntegerField(null=False)
    isbn = models.CharField(max_length=20, null=False, unique=True)
    number_of_pages = models.IntegerField()
    summary = models.TextField()
    cover_image_addr = models.ImageField(null=False, default='Book.png')
    author_name = models.CharField(null=False, max_length=20, default='author')
    translator_name = models.CharField(null=True, max_length=20)
    publisher_name = models.CharField(null=True, max_length=20)
    adding_date = models.DateTimeField(default=timezone.now())

class Genre(models.Model):
    genre_type = models.CharField(max_length=20,null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=False)

    class Meta:
        unique_together = ('genre_type', 'book_id')


class BookSeller(models.Model):
    book_seller_id = models.CharField(max_length=15, auto_created=True, primary_key=True)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)


class SellBy(models.Model):
    price = models.FloatField(null= False)
    number_of_copies = models.IntegerField(null= False)
    book_seller_id = models.ForeignKey(BookSeller, on_delete=models.CASCADE, null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('book_id', 'book_seller_id')


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
    verifier_id = models.ForeignKey(Admin)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)


class FinancialAccount(models.Model):
    # ****book_seller_id and book_maker_id can't be null at the same time****
    account_no = models.CharField(max_length=20)
    book_seller_id = models.ForeignKey(BookSeller, on_delete=models.CASCADE)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)


class BookMakerLanguage(models.Model):
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
    language_name = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book_maker_id', 'language_name')


class Write(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book_id', 'book_maker_id')


class Order(models.Model):
    delivery_date = models.DateField()
    order_date = models.DateField()
    order_id = models.IntegerField(primary_key=True, auto_created=True)
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)


class BookShoppingCart(models.Model):
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)


class PreOrder(models.Model):
    #author can be retrieved by access to Write table
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    user_name = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)


class BookRating(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BookReaderUser, on_delete= models.CASCADE)
    Score = models.IntegerField(null= False)

    class Meta:
        unique_together = ('book_id', 'user_id')


class BookMakerRating(models.Model):
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
    date = models.DateField()
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    Score = models.IntegerField()

    class Meta:
        unique_together = ('book_maker_id', 'user_id')


class TranslationRequest(models.Model):
    book_file = models.FileField()
    translation_request_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.PROTECT, null=True)
    register_date = models.DateField()
    response_date = models.DateField()
    finish_date = models.DateField()


class Income(models.Model):
    income_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT, null=True)
    amount = models.FloatField()
    date = models.DateField()
    source_financial_account_no = models.IntegerField(null=False)
    organization_financial_account = models.ForeignKey(OrganizationFinancialAccount, on_delete=models.PROTECT)


class Expense(models.Model):
    expense_id = models.IntegerField(primary_key=True, auto_created=True)
    destination = models.ForeignKey(FinancialAccount)
    organization_financial_account = models.ForeignKey(OrganizationFinancialAccount, on_delete=models.PROTECT)
    amount = models.FloatField()
    date = models.DateField()


class BookPackage(models.Model):
    package_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()
    price = models.FloatField()


class BookAndBookPackage(models.Model):
    book_package_id = models.ForeignKey(BookPackage)
    book_id = models.ForeignKey(Book)

    class Meta:
        unique_together = ('book_package_id', 'book_id')


class BookComment(models.Model):
    book_comment_id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    user_id = models.ForeignKey(BookReaderUser)
    book_id = models.ForeignKey(Book)
    date = models.DateField()


class CommentReply(models.Model):
    reply_comment_id = models.IntegerField(primary_key=True, auto_created=True)
    book_comment_id = models.ForeignKey(BookComment)
    user_id = models.ForeignKey(BookReaderUser) #id of the person who wrote reply
    content = models.TextField()


class Notification(models.Model):
    notif_id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    notif_date_created = models.DateField(null=False)
    BookMaker_id = models.ForeignKey(BookReaderUser)

