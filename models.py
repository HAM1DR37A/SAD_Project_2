from django.db import models
from django.contrib.auth.models import User as myUser
from django.db.models.fields.related import ForeignKey


class User(myUser):
    user_name = models.CharField(max_length=30, primary_key=True)
    user_avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)


class OrganizationFinancialAccount(models.Model):
    account_id = models.IntegerField(primary_key=True)


class ShoppingCart(models.Model):
    shopping_cart_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User)


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


class Genre(models.Model):
    genre_type = models.CharField(max_length=20,null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=False)

    class Meta:
        unique_together = ('genre_type', 'book_id')


class BookSeller(models.Model):
    name = models.CharField(max_length=20, null=False)
    book_seller_id = models.CharField(max_length=15, auto_created=True, primary_key=True)


class SellBy(models.Model):
    price = models.FloatField(null= False)
    number_of_copeis = models.IntegerField(null= False)
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
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    book_maker_id = models.CharField(max_length=10, auto_created=True, primary_key=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=2, choices=gender_choices)
    book_maker_type = models.CharField(max_length=4, choices=type_choices)
    verifier_id = models.ForeignKey(Admin)


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
    user_name = models.ForeignKey(User, on_delete=models.PROTECT)


class BookRating(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    Score = models.IntegerField(null= False)

    class Meta:
        unique_together = ('book_id', 'user_id')


class BookMakerRating(models.Model):
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    Score = models.IntegerField()

    class Meta:
        unique_together = ('book_maker_id', 'user_id')


class TranslationRequest(models.Model):
    book_file = models.FileField()
    translation_request_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.PROTECT, null=True)
    register_date = models.DateField()
    response_date = models.DateField()
    finish_date = models.DateField()


class Income(models.Model):
    income_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL)
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
    user_id = models.ForeignKey(User)
    book_id = models.ForeignKey(Book)
    date = models.DateField()


class CommentReply(models.Model):
    reply_comment_id = models.IntegerField(primary_key=True, auto_created=True)
    book_comment_id = models.ForeignKey(BookComment)
    user_id = models.ForeignKey(User) #id of the person who wrote reply
    content = models.TextField()
















